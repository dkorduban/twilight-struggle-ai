# minimal_hybrid detailed rollout log

- seed: `20260540`
- winner: `USSR`
- final_vp: `14`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], NATO[21], US/Japan Mutual Defense Pact[27], Red Scare/Purge[31], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], CIA Created[26], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Nuclear Test Ban [34] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], NATO[21], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban COUP Iran | 82.35 | 4.00 | 78.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus |
| 2 | Nuclear Test Ban INFLUENCE West Germany, Japan, South Korea, Thailand | 78.87 | 5.00 | 75.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |
| 3 | Romanian Abdication COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | NATO COUP Iran | 58.35 | 4.00 | 78.95 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | US/Japan Mutual Defense Pact COUP Iran | 58.35 | 4.00 | 78.95 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+4/A+0`

## Step 4: T1 AR1 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], CIA Created[26], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Indonesia | 24.37 | 5.00 | 20.85 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:1.33 |
| 2 | De Gaulle Leads France INFLUENCE Indonesia, Philippines | 23.52 | 5.00 | 40.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 3 | Suez Crisis INFLUENCE Indonesia, Philippines | 23.52 | 5.00 | 40.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | De-Stalinization INFLUENCE Indonesia, Philippines | 23.52 | 5.00 | 40.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | CIA Created COUP Syria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], NATO[21], US/Japan Mutual Defense Pact[27], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, South Korea, Thailand | 56.20 | 5.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, South Korea, Thailand | 56.20 | 5.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 42.80 | 5.00 | 58.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 29.30 | 5.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | Romanian Abdication INFLUENCE Thailand | 27.30 | 5.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], De Gaulle Leads France[17], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Philippines | 23.05 | 5.00 | 40.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | Suez Crisis INFLUENCE West Germany, Philippines | 23.05 | 5.00 | 40.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | De-Stalinization INFLUENCE West Germany, Philippines | 23.05 | 5.00 | 40.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | De Gaulle Leads France COUP Syria | 13.60 | 4.00 | 30.05 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Suez Crisis COUP Syria | 13.60 | 4.00 | 30.05 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, Pakistan, Israel, Thailand | 56.15 | 5.00 | 75.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Five Year Plan INFLUENCE Pakistan, Israel, Thailand | 43.85 | 5.00 | 59.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Special Relationship INFLUENCE Pakistan, Thailand | 31.10 | 5.00 | 42.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Romanian Abdication INFLUENCE Thailand | 30.30 | 5.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 5 | Truman Doctrine INFLUENCE Thailand | 18.30 | 5.00 | 25.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Suez Crisis[28], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Turkey, North Korea | 17.55 | 5.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | De-Stalinization INFLUENCE Turkey, North Korea | 17.55 | 5.00 | 35.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Suez Crisis COUP Syria | 13.75 | 4.00 | 30.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | De-Stalinization COUP Syria | 13.75 | 4.00 | 30.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Syria | 12.40 | 4.00 | 24.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Truman Doctrine[19], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE North Korea, Pakistan, Thailand | 45.50 | 5.00 | 60.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE North Korea, Thailand | 29.70 | 5.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE North Korea | 25.40 | 5.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea |
| 4 | Truman Doctrine INFLUENCE North Korea | 13.40 | 5.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Decolonization[30], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France | 15.98 | 5.00 | 34.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | De-Stalinization COUP Syria | 14.00 | 4.00 | 30.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Decolonization COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, Thailand | 29.20 | 5.00 | 40.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Truman Doctrine INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Romanian Abdication COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U4/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Syria | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Syria | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Decolonization COUP Syria | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Vietnam Revolts SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Arab-Israeli War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 13: T1 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Truman Doctrine[19]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 25.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Truman Doctrine INFLUENCE Thailand | 13.30 | 5.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Romanian Abdication COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |
| 5 | Romanian Abdication EVENT | 2.35 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U4/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Decolonization COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Arab-Israeli War INFLUENCE Italy | 5.15 | 5.00 | 16.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-4/A-2`

## Step 15: T2 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], COMECON[14], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Korean War[11], Nasser[15], Independent Reds[22], Marshall Plan[23], Indo-Pakistani War[24], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Fidel EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `COMECON[14], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, India, Thailand | 59.33 | 5.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | Warsaw Pact Formed INFLUENCE Italy, India, Thailand | 59.33 | 5.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | COMECON COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | Warsaw Pact Formed COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games INFLUENCE Italy, Thailand | 41.93 | 5.00 | 39.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Korean War[11], Nasser[15], Independent Reds[22], Indo-Pakistani War[24], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Iraq, Panama | 50.53 | 5.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 2 | Independent Reds INFLUENCE Iraq, Panama | 34.53 | 5.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, access_touch:Iraq, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 3 | Indo-Pakistani War INFLUENCE Iraq, Panama | 34.53 | 5.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, access_touch:Iraq, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.67 |
| 4 | NORAD COUP Iraq | 33.10 | 4.00 | 29.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 5 | NORAD COUP Indonesia | 32.65 | 4.00 | 29.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Iraq, Philippines, Thailand | 57.55 | 5.00 | 56.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Warsaw Pact Formed COUP Philippines | 44.45 | 4.00 | 40.90 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games INFLUENCE Iraq, Thailand | 41.25 | 5.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 4 | The Cambridge Five INFLUENCE Iraq, Thailand | 41.25 | 5.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 5 | Olympic Games COUP Philippines | 39.10 | 4.00 | 35.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Korean War[11], Nasser[15], Independent Reds[22], Indo-Pakistani War[24]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Iran | 38.35 | 4.00 | 34.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 2 | Indo-Pakistani War COUP Iran | 38.35 | 4.00 | 34.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 3 | Independent Reds INFLUENCE Saudi Arabia, Philippines | 37.25 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.20 |
| 4 | Indo-Pakistani War INFLUENCE Saudi Arabia, Philippines | 37.25 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.20 |
| 5 | Independent Reds COUP Philippines | 32.10 | 4.00 | 28.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 21: T2 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Saudi Arabia, Thailand | 37.45 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | The Cambridge Five INFLUENCE Saudi Arabia, Thailand | 37.45 | 5.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | East European Unrest INFLUENCE Japan, Saudi Arabia, Thailand | 33.45 | 5.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Olympic Games COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |
| 5 | The Cambridge Five COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Blockade[10], Korean War[11], Nasser[15], Indo-Pakistani War[24]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Saudi Arabia, Philippines | 40.45 | 5.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines |
| 2 | Fidel INFLUENCE Saudi Arabia, Philippines | 24.45 | 5.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 3 | Korean War INFLUENCE Saudi Arabia, Philippines | 24.45 | 5.00 | 35.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 4 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 5 | Indo-Pakistani War COUP SE African States | 12.80 | 4.00 | 9.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Thailand | 35.97 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:5.33 |
| 2 | East European Unrest INFLUENCE Japan, Indonesia, Thailand | 31.67 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | The Cambridge Five COUP Syria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 4 | Captured Nazi Scientist COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist INFLUENCE Thailand | 19.97 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Blockade[10], Korean War[11], Nasser[15]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 2 | Korean War INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 3 | Blockade INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Nasser INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 5 | Fidel SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Egypt | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Syria | 25.30 | 4.00 | 21.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | East European Unrest INFLUENCE Japan, Indonesia, Thailand | 23.00 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | East European Unrest COUP Egypt | 19.50 | 4.00 | 35.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Israel | 19.25 | 4.00 | 15.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 26: T2 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Korean War[11], Nasser[15]`
- state: `VP 1, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 2 | Blockade INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Nasser INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Korean War COUP SE African States | -3.20 | 4.00 | 9.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `East European Unrest[29], Formosan Resolution[35]`
- state: `VP 1, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Egypt, Thailand | 28.85 | 5.00 | 55.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Formosan Resolution INFLUENCE Egypt, Thailand | 16.85 | 5.00 | 39.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | East European Unrest COUP Sudan | 2.15 | 4.00 | 18.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Sudan | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution SPACE | -2.30 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 1, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Nasser INFLUENCE Japan | 9.00 | 5.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 3 | Blockade COUP SE African States | -4.55 | 4.00 | 3.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Blockade COUP Sudan | -4.55 | 4.00 | 3.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP Zimbabwe | -4.55 | 4.00 | 3.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Vietnam Revolts [9] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Blockade[10], Truman Doctrine[19], Containment[25], US/Japan Mutual Defense Pact[27], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | US/Japan Mutual Defense Pact EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Red Scare/Purge[31], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Truman Doctrine[19], Containment[25], US/Japan Mutual Defense Pact[27], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Japan, Libya, Indonesia, Thailand | 44.55 | 5.00 | 68.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Duck and Cover INFLUENCE Japan, Indonesia, Thailand | 33.00 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Containment INFLUENCE Japan, Indonesia, Thailand | 33.00 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | NORAD INFLUENCE Japan, Indonesia, Thailand | 33.00 | 5.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Blockade COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Five Year Plan[5], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Iran, Indonesia | 51.25 | 5.00 | 50.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, influence:Indonesia:13.85, control_break:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Five Year Plan COUP Iran | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Five Year Plan COUP Libya | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Olympic Games INFLUENCE Japan, Indonesia | 35.70 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, non_coup_milops_penalty:4.00 |
| 5 | Indo-Pakistani War INFLUENCE Japan, Indonesia | 35.70 | 5.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Truman Doctrine[19], Containment[25], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Iran, Libya, Thailand | 37.60 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Libya:13.70, control_break:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Containment INFLUENCE Iran, Libya, Thailand | 37.60 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Libya:13.70, control_break:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | NORAD INFLUENCE Iran, Libya, Thailand | 37.60 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Libya:13.70, control_break:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Blockade COUP Syria | 24.10 | 4.00 | 20.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Syria | 24.10 | 4.00 | 20.25 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], Olympic Games[20], Indo-Pakistani War[24], CIA Created[26], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Pakistan | 33.00 | 5.00 | 33.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, non_coup_milops_penalty:4.80 |
| 2 | Indo-Pakistani War INFLUENCE Japan, Pakistan | 33.00 | 5.00 | 33.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, non_coup_milops_penalty:4.80 |
| 3 | Special Relationship INFLUENCE Japan, Pakistan | 33.00 | 5.00 | 33.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, non_coup_milops_penalty:4.80 |
| 4 | Olympic Games COUP Libya | 32.95 | 4.00 | 29.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Libya | 32.95 | 4.00 | 29.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Truman Doctrine[19], Containment[25], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Pakistan, Thailand | 35.10 | 5.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | NORAD INFLUENCE Japan, Pakistan, Thailand | 35.10 | 5.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Blockade COUP Syria | 24.55 | 4.00 | 20.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:0.5 |
| 4 | UN Intervention COUP Syria | 24.55 | 4.00 | 20.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:0.5 |
| 5 | Blockade COUP Egypt | 20.05 | 4.00 | 16.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:3`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], Indo-Pakistani War[24], CIA Created[26], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Libya | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Special Relationship COUP Libya | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Indo-Pakistani War INFLUENCE India, Japan | 32.40 | 5.00 | 33.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 4 | Special Relationship INFLUENCE India, Japan | 32.40 | 5.00 | 33.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 5 | Warsaw Pact Formed INFLUENCE India, Japan, Libya | 27.95 | 5.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 37: T3 AR4 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Truman Doctrine[19], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE UK, Japan, Thailand | 28.80 | 5.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Blockade INFLUENCE Thailand | 17.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 3 | UN Intervention INFLUENCE Thailand | 17.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 4 | Blockade COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], CIA Created[26], Special Relationship[37]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE India, Japan | 35.73 | 5.00 | 33.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, non_coup_milops_penalty:2.67 |
| 2 | Warsaw Pact Formed INFLUENCE India, Japan, Libya | 31.28 | 5.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Captured Nazi Scientist INFLUENCE India | 19.73 | 5.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, non_coup_milops_penalty:2.67 |
| 4 | CIA Created INFLUENCE India | 19.73 | 5.00 | 17.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, access_touch:India, non_coup_milops_penalty:2.67 |
| 5 | Special Relationship COUP SE African States | 14.80 | 4.00 | 11.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Sudan | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Sudan | 12.95 | 4.00 | 9.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade INFLUENCE Thailand | 4.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 4 | UN Intervention INFLUENCE Thailand | 4.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 5 | Blockade COUP Tunisia | 2.55 | 4.00 | -1.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 40: T3 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Warsaw Pact Formed[16], Captured Nazi Scientist[18], CIA Created[26]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Sudan | 31.95 | 4.00 | 28.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 2 | CIA Created COUP Sudan | 31.95 | 4.00 | 28.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 3 | Warsaw Pact Formed INFLUENCE West Germany, Japan, Libya | 25.05 | 5.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Warsaw Pact Formed COUP Sudan | 22.65 | 4.00 | 39.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Captured Nazi Scientist INFLUENCE Japan | 14.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Truman Doctrine[19], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Sudan | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Tunisia | 4.05 | 4.00 | 0.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:0.5 |
| 3 | UN Intervention INFLUENCE Thailand | 3.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:22.00 |
| 4 | Truman Doctrine COUP Sudan | 2.45 | 4.00 | 10.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Tunisia | -7.95 | 4.00 | 0.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:1`
- hand: `Warsaw Pact Formed[16], CIA Created[26]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Sudan | 33.45 | 4.00 | 29.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Warsaw Pact Formed COUP Sudan | 24.15 | 4.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Warsaw Pact Formed INFLUENCE West Germany, Japan, Libya | 21.05 | 5.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 4 | CIA Created COUP SE African States | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Zimbabwe | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 43: T4 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], Independent Reds[22], CIA Created[26], Red Scare/Purge[31], Bear Trap[47], We Will Bury You[53], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Bear Trap EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], NATO[21], Decolonization[30], De-Stalinization[33], Special Relationship[37], SALT Negotiations[46], Junta[50], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], Independent Reds[22], CIA Created[26], Bear Trap[47], We Will Bury You[53], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE West Germany, Mexico, Algeria, Morocco | 65.93 | 5.00 | 66.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 2 | We Will Bury You COUP Sudan | 53.96 | 4.00 | 50.56 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:5.5 |
| 3 | Warsaw Pact Formed INFLUENCE Mexico, Algeria, Morocco | 49.93 | 5.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.57 |
| 4 | Warsaw Pact Formed COUP Sudan | 47.61 | 4.00 | 44.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:4.5 |
| 5 | We Will Bury You COUP Syria | 42.56 | 4.00 | 39.16 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `SALT Negotiations [46] as COUP`
- flags: `milops_shortfall:4`
- hand: `Warsaw Pact Formed[16], Decolonization[30], De-Stalinization[33], Special Relationship[37], SALT Negotiations[46], Junta[50], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations COUP Mexico | 40.46 | 4.00 | 36.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | SALT Negotiations COUP Algeria | 39.71 | 4.00 | 36.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | SALT Negotiations COUP Libya | 38.71 | 4.00 | 35.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | SALT Negotiations INFLUENCE Mexico, Ethiopia | 37.53 | 5.00 | 37.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 5 | Special Relationship COUP Mexico | 34.11 | 4.00 | 30.41 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 47: T4 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], Independent Reds[22], CIA Created[26], Bear Trap[47], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Mexico, Algeria | 51.52 | 5.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 2 | Warsaw Pact Formed COUP Sudan | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 3 | Arab-Israeli War COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War INFLUENCE Mexico, Algeria | 35.52 | 5.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:5.33 |
| 5 | Bear Trap INFLUENCE West Germany, Mexico, Algeria | 31.52 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Warsaw Pact Formed[16], Decolonization[30], De-Stalinization[33], Special Relationship[37], Junta[50], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Ethiopia | 24.97 | 5.00 | 41.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 2 | De-Stalinization INFLUENCE West Germany, Ethiopia | 24.97 | 5.00 | 41.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 3 | Special Relationship INFLUENCE West Germany | 24.52 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:1.33 |
| 4 | Junta INFLUENCE West Germany | 24.52 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:1.33 |
| 5 | Special Relationship COUP Colombia | 17.05 | 4.00 | 13.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.17, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Independent Reds[22], CIA Created[26], Bear Trap[47], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Sudan | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War INFLUENCE West Germany, Mexico | 34.40 | 5.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:6.40 |
| 3 | Bear Trap INFLUENCE East Germany, West Germany, Mexico | 29.80 | 5.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Bear Trap COUP Sudan | 28.30 | 4.00 | 44.75 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Independent Reds COUP Sudan | 25.95 | 4.00 | 38.25 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 50: T4 AR3 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:1`
- hand: `Decolonization[30], De-Stalinization[33], Special Relationship[37], Junta[50], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5 |
| 3 | De-Stalinization COUP Sudan | 24.50 | 4.00 | 40.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Decolonization COUP Sudan | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Sudan | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], Bear Trap[47], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE West Germany, Mexico, Ethiopia | 32.25 | 5.00 | 51.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, influence:Ethiopia:13.60, access_touch:Ethiopia, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Independent Reds INFLUENCE West Germany, Mexico | 20.80 | 5.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Nixon Plays the China Card INFLUENCE West Germany, Mexico | 20.80 | 5.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | CIA Created INFLUENCE Mexico | 8.80 | 5.00 | 19.95 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Bear Trap COUP Saharan States | 4.40 | 4.00 | 20.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:1`
- hand: `Decolonization[30], De-Stalinization[33], Junta[50], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Sudan | 39.30 | 4.00 | 35.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:3.5 |
| 2 | De-Stalinization COUP Sudan | 24.65 | 4.00 | 41.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Junta INFLUENCE West Germany | 23.85 | 5.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:2.00 |
| 4 | Decolonization COUP Sudan | 23.30 | 4.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Sudan | 23.30 | 4.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Sudan | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Independent Reds INFLUENCE West Germany, Ethiopia | 18.12 | 5.00 | 34.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Ethiopia:13.60, control_break:Ethiopia, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Nixon Plays the China Card INFLUENCE West Germany, Ethiopia | 18.12 | 5.00 | 34.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Ethiopia:13.60, control_break:Ethiopia, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Decolonization[30], De-Stalinization[33], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Ethiopia | 21.63 | 5.00 | 39.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Ethiopia:13.60, control_break:Ethiopia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Decolonization INFLUENCE West Germany | 7.18 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany | 7.18 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Willy Brandt INFLUENCE West Germany | 7.18 | 5.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Decolonization SPACE | 5.03 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Sudan | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | CIA Created COUP Sudan | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 6.40 | 5.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Nixon Plays the China Card COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Guatemala | 3.30 | 4.00 | 15.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Decolonization[30], Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Sudan | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Portuguese Empire Crumbles COUP Sudan | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Sudan | 24.05 | 4.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Colombia | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP SE African States | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Sudan | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created COUP Saharan States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | CIA Created COUP Guatemala | 3.95 | 4.00 | 12.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Kenya | -5.20 | 4.00 | 2.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Kenya, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:0.5, offside_ops_penalty |
| 5 | CIA Created COUP Somalia | -5.20 | 4.00 | 2.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Somalia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Sudan | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Colombia | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP SE African States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Zimbabwe | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 59: T5 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Korean War[11], Nasser[15], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36], Cuban Missile Crisis[43], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Ussuri River Skirmish [77] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Blockade[10], Special Relationship[37], Quagmire[45], Kitchen Debates[51], Missile Envy[52], South African Unrest[56], Allende[57], Ussuri River Skirmish[77]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Quagmire EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Nasser[15], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Cuban Missile Crisis[43], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE West Germany, Argentina, Chile | 49.99 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:Chile:16.80, non_coup_milops_penalty:5.71 |
| 2 | Cuban Missile Crisis COUP Sudan | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | Cuban Missile Crisis COUP Ethiopia | 43.54 | 4.00 | 39.99 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Ethiopia, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:4.5 |
| 4 | Korean War COUP Sudan | 41.69 | 4.00 | 37.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Sudan | 41.69 | 4.00 | 37.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Blockade[10], Special Relationship[37], Quagmire[45], Kitchen Debates[51], Missile Envy[52], South African Unrest[56], Allende[57]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Ethiopia | 37.19 | 4.00 | 33.49 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ethiopia, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:3.5 |
| 2 | Missile Envy COUP Ethiopia | 37.19 | 4.00 | 33.49 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ethiopia, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:3.5 |
| 3 | Special Relationship INFLUENCE West Germany, Mexico | 37.09 | 5.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.71 |
| 4 | Missile Envy INFLUENCE West Germany, Mexico | 37.09 | 5.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.71 |
| 5 | Special Relationship COUP Mexico | 34.54 | 4.00 | 30.84 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 63: T5 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Korean War[11], Nasser[15], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Argentina, Brazil, Chile | 49.08 | 5.00 | 75.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, control_break:Argentina, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 2 | Korean War COUP Sudan | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | The Cambridge Five COUP Sudan | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | One Small Step COUP Sudan | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Sudan | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Blockade[10], Quagmire[45], Kitchen Debates[51], Missile Envy[52], South African Unrest[56], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U0/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE Mexico, South Africa | 34.45 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Quagmire INFLUENCE Israel, Mexico, South Africa | 30.70 | 5.00 | 50.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Missile Envy COUP Colombia | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Missile Envy COUP SE African States | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Missile Envy COUP Sudan | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Nasser[15], Truman Doctrine[19], The Cambridge Five[36], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Sudan | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | The Cambridge Five COUP Sudan | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | One Small Step COUP Sudan | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP Sudan | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Nasser COUP Sudan | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 66: T5 AR3 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Fidel[8], Blockade[10], Quagmire[45], Kitchen Debates[51], South African Unrest[56], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Sudan | 35.00 | 4.00 | 31.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 2 | Quagmire INFLUENCE Israel, Algeria, South Africa | 34.15 | 5.00 | 54.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Kitchen Debates COUP Guatemala | 33.75 | 4.00 | 29.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 4 | Quagmire COUP Sudan | 27.70 | 4.00 | 44.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Guatemala | 26.45 | 4.00 | 42.90 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], Truman Doctrine[19], The Cambridge Five[36], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Sudan | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Sudan | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Sudan | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 4 | The Cambridge Five INFLUENCE Mexico, Brazil | 37.85 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.00 |
| 5 | One Small Step INFLUENCE Mexico, Brazil | 37.85 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Quagmire[45], South African Unrest[56], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE Israel, Algeria, South Africa | 32.95 | 5.00 | 54.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Quagmire COUP Sudan | 28.15 | 4.00 | 44.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Guatemala | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Fidel COUP Sudan | 25.80 | 4.00 | 38.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Sudan | 25.80 | 4.00 | 38.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], Truman Doctrine[19], One Small Step[81], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Mexico, Brazil | 35.85 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:8.00 |
| 2 | Colonial Rear Guards INFLUENCE Mexico, Brazil | 35.85 | 5.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:8.00 |
| 3 | One Small Step COUP Colombia | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | One Small Step COUP Mozambique | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Blockade[10], South African Unrest[56], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Sudan | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | South African Unrest COUP Sudan | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Fidel COUP Guatemala | 25.30 | 4.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Guatemala | 25.30 | 4.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Blockade COUP Sudan | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], Truman Doctrine[19], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Colombia | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Colonial Rear Guards COUP Mozambique | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Saharan States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP SE African States | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Sudan | 22.05 | 4.00 | 18.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], South African Unrest[56], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Colombia | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | South African Unrest COUP Sudan | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | South African Unrest COUP Guatemala | 26.80 | 4.00 | 39.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Blockade COUP Colombia | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP Sudan | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:3`
- hand: `Nasser[15], Truman Doctrine[19]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Colombia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Truman Doctrine COUP Colombia | 30.20 | 4.00 | 38.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Nasser COUP Mozambique | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Nasser COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Sudan | 30.20 | 4.00 | 38.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Allende COUP Sudan | 30.20 | 4.00 | 38.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Blockade COUP Guatemala | 28.95 | 4.00 | 37.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Guatemala | 28.95 | 4.00 | 37.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP Colombia | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Blockade[10], De Gaulle Leads France[17], UN Intervention[32], Nuclear Test Ban[34], Brush War[39], Muslim Revolution[59], OPEC[64]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Sadat Expels Soviets [73] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Truman Doctrine[19], Camp David Accords[66], Grain Sales to Soviets[68], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Shuttle Diplomacy[74], Voice of America[75], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Blockade[10], De Gaulle Leads France[17], UN Intervention[32], Brush War[39], Muslim Revolution[59], OPEC[64]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE Argentina, Chile, Venezuela, Algeria | 65.94 | 5.00 | 68.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.86 |
| 2 | Muslim Revolution COUP Indonesia | 54.82 | 4.00 | 51.42 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:5.5 |
| 3 | Muslim Revolution COUP Egypt | 51.92 | 4.00 | 48.52 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 4 | De Gaulle Leads France INFLUENCE Argentina, Chile, Algeria | 49.89 | 5.00 | 52.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.86 |
| 5 | Brush War INFLUENCE Argentina, Chile, Algeria | 49.89 | 5.00 | 52.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Socialist Governments[7], Truman Doctrine[19], Camp David Accords[66], Grain Sales to Soviets[68], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Indonesia | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:4.5 |
| 2 | Shuttle Diplomacy INFLUENCE West Germany, Morocco, South Africa | 47.44 | 5.00 | 49.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | Shuttle Diplomacy COUP Guatemala | 47.22 | 4.00 | 43.67 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 4 | Shuttle Diplomacy COUP Libya | 45.57 | 4.00 | 42.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |
| 5 | Camp David Accords COUP Indonesia | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 79: T6 AR2 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Blockade[10], De Gaulle Leads France[17], UN Intervention[32], Brush War[39], OPEC[64]`
- state: `VP 0, DEFCON 4, MilOps U0/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Indonesia | 55.90 | 4.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Brush War COUP Indonesia | 55.90 | 4.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | OPEC COUP Indonesia | 55.90 | 4.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | De Gaulle Leads France INFLUENCE Argentina, Chile, Venezuela | 48.75 | 5.00 | 52.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 5 | Brush War INFLUENCE Argentina, Chile, Venezuela | 48.75 | 5.00 | 52.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 80: T6 AR2 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Truman Doctrine[19], Camp David Accords[66], Grain Sales to Soviets[68], John Paul II Elected Pope[69], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Guatemala | 39.80 | 4.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Guatemala | 39.80 | 4.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | John Paul II Elected Pope COUP Guatemala | 39.80 | 4.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Voice of America COUP Guatemala | 39.80 | 4.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 5 | Camp David Accords INFLUENCE Morocco, South Africa | 34.30 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Blockade[10], UN Intervention[32], Brush War[39], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE Argentina, Chile, Venezuela | 51.95 | 5.00 | 52.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:4.80 |
| 2 | OPEC INFLUENCE Argentina, Chile, Venezuela | 51.95 | 5.00 | 52.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:4.80 |
| 3 | Brush War COUP Egypt | 38.80 | 4.00 | 35.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | OPEC COUP Egypt | 38.80 | 4.00 | 35.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Brush War COUP Syria | 36.30 | 4.00 | 32.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Truman Doctrine[19], Grain Sales to Soviets[68], John Paul II Elected Pope[69], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE Morocco, South Africa | 33.50 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | John Paul II Elected Pope INFLUENCE Morocco, South Africa | 33.50 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | Voice of America INFLUENCE Morocco, South Africa | 33.50 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 4 | Grain Sales to Soviets COUP Libya | 32.45 | 4.00 | 28.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | John Paul II Elected Pope COUP Libya | 32.45 | 4.00 | 28.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Blockade[10], UN Intervention[32], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE West Germany, Argentina, Chile | 47.70 | 5.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 2 | OPEC COUP Egypt | 39.25 | 4.00 | 35.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | OPEC COUP Syria | 36.75 | 4.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 4 | OPEC COUP Mexico | 34.00 | 4.00 | 30.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:2.5 |
| 5 | OPEC COUP Algeria | 33.25 | 4.00 | 29.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Truman Doctrine[19], John Paul II Elected Pope[69], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Libya | 32.90 | 4.00 | 29.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Voice of America COUP Libya | 32.90 | 4.00 | 29.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 31.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Voice of America INFLUENCE West Germany, South Africa | 31.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | John Paul II Elected Pope COUP Mexico | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Argentina, Chile | 25.70 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Blockade COUP Colombia | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP Mozambique | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Blockade COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP SE African States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Truman Doctrine[19], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 25.05 | 5.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Voice of America COUP Colombia | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Voice of America COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Voice of America COUP SE African States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Colombia | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Mozambique | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | Blockade COUP SE African States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP Zimbabwe | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Truman Doctrine[19], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Panama Canal Returned COUP Colombia | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Socialist Governments COUP Colombia | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP SE African States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Colombia | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Mozambique | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Socialist Governments[7], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Colombia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Socialist Governments COUP Colombia | 34.90 | 4.00 | 51.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Sudan | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Cultural Revolution [61] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Olympic Games[20], Nuclear Subs[44], How I Learned to Stop Worrying[49], Cultural Revolution[61], Puppet Governments[67], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `COMECON[14], East European Unrest[29], ABM Treaty[60], U2 Incident[63], Lonely Hearts Club Band[65], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Olympic Games[20], Nuclear Subs[44], How I Learned to Stop Worrying[49], Puppet Governments[67], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Indonesia | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games COUP Colombia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 94: T7 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], East European Unrest[29], U2 Incident[63], Lonely Hearts Club Band[65], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Brazil, Venezuela, South Africa | 45.75 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Alliance for Progress INFLUENCE Brazil, Venezuela, South Africa | 45.75 | 5.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | East European Unrest COUP Brazil | 41.00 | 4.00 | 37.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | East European Unrest COUP Venezuela | 41.00 | 4.00 | 37.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Alliance for Progress COUP Brazil | 41.00 | 4.00 | 37.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:7, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Nuclear Subs[44], How I Learned to Stop Worrying[49], Puppet Governments[67], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying INFLUENCE Brazil, Venezuela | 36.43 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 4 | Latin American Death Squads INFLUENCE Brazil, Venezuela | 36.43 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 5 | Captured Nazi Scientist COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], U2 Incident[63], Lonely Hearts Club Band[65], OAS Founded[71], Alliance for Progress[79], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE West Germany, Argentina, South Africa | 46.37 | 5.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Alliance for Progress COUP Argentina | 43.50 | 4.00 | 39.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Alliance for Progress COUP Libya | 40.50 | 4.00 | 36.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Lonely Hearts Club Band COUP Argentina | 37.15 | 4.00 | 33.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Our Man in Tehran COUP Argentina | 37.15 | 4.00 | 33.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Nuclear Subs[44], Puppet Governments[67], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Colombia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Colombia | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Latin American Death Squads INFLUENCE Brazil, Venezuela | 35.10 | 5.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 4 | Latin American Death Squads COUP Egypt | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Five Year Plan INFLUENCE Brazil, Chile, Venezuela | 31.75 | 5.00 | 55.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], U2 Incident[63], Lonely Hearts Club Band[65], OAS Founded[71], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Colombia | 43.75 | 4.00 | 40.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP Colombia | 43.75 | 4.00 | 40.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 3 | OAS Founded COUP Colombia | 37.40 | 4.00 | 33.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:2.5 |
| 4 | Lonely Hearts Club Band COUP Libya | 34.85 | 4.00 | 31.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Our Man in Tehran COUP Libya | 34.85 | 4.00 | 31.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 99: T7 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Nuclear Subs[44], Puppet Governments[67], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Panama, Brazil, Venezuela | 29.90 | 5.00 | 55.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Panama, Brazil, Venezuela | 29.90 | 5.00 | 55.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Captured Nazi Scientist COUP Panama | 29.80 | 4.00 | 25.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Egypt | 28.05 | 4.00 | 24.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Syria | 25.55 | 4.00 | 21.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `milops_shortfall:5`
- hand: `COMECON[14], U2 Incident[63], OAS Founded[71], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Colombia | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | OAS Founded COUP Colombia | 36.95 | 4.00 | 33.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 3 | Our Man in Tehran COUP Libya | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Our Man in Tehran INFLUENCE Panama, Chile | 33.45 | 5.00 | 38.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:10.00 |
| 5 | Our Man in Tehran COUP Argentina | 30.40 | 4.00 | 26.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Nuclear Subs[44], Puppet Governments[67], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Egypt | 29.30 | 4.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Syria | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Argentina | 25.30 | 4.00 | 21.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Mexico | 24.05 | 4.00 | 20.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Panama | 24.05 | 4.00 | 20.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:5`
- hand: `COMECON[14], U2 Incident[63], OAS Founded[71], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 38.20 | 4.00 | 34.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 2 | COMECON COUP Colombia | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | U2 Incident COUP Colombia | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | COMECON INFLUENCE Panama, Chile, South Africa | 26.77 | 5.00 | 55.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | U2 Incident INFLUENCE Panama, Chile, South Africa | 26.77 | 5.00 | 55.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Nuclear Subs[44], Puppet Governments[67], Ask Not What Your Country Can Do For You[78]`
- state: `VP -1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Sudan | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Sudan | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Sudan | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Colombia | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP Mozambique | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 104: T7 AR6 US

- chosen: `COMECON [14] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `COMECON[14], U2 Incident[63], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Colombia | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | U2 Incident COUP Colombia | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Colombia | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | COMECON COUP Saharan States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP SE African States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 105: T7 AR7 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Nuclear Subs[44], Puppet Governments[67]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Colombia | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Sudan | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Colombia | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Puppet Governments COUP Sudan | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Mozambique | 13.55 | 4.00 | 25.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `U2 Incident [63] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `U2 Incident[63], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | U2 Incident COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | U2 Incident COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | U2 Incident COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | U2 Incident COUP Zimbabwe | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 107: T8 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Five Year Plan[5], Socialist Governments[7], Arab-Israeli War[13], East European Unrest[29], De-Stalinization[33], Junta[50], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], ABM Treaty[60], Lonely Hearts Club Band[65], Camp David Accords[66], Puppet Governments[67], Voice of America[75], Tear Down this Wall[99], Solidarity[104]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Tear Down this Wall EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Five Year Plan[5], Arab-Israeli War[13], East European Unrest[29], De-Stalinization[33], Junta[50], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Indonesia | 55.58 | 4.00 | 52.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 2 | De-Stalinization COUP Sudan | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 3 | Arab-Israeli War COUP Indonesia | 49.23 | 4.00 | 45.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 4 | Junta COUP Indonesia | 49.23 | 4.00 | 45.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 5 | De-Stalinization INFLUENCE West Germany, Egypt, Venezuela | 48.96 | 5.00 | 53.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 110: T8 AR1 US

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Camp David Accords[66], Puppet Governments[67], Voice of America[75], Tear Down this Wall[99], Solidarity[104]`
- state: `VP -2, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, West Germany, Panama | 52.06 | 5.00 | 56.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Panama:13.45, control_break:Panama, non_coup_milops_penalty:9.14 |
| 2 | Tear Down this Wall COUP Egypt | 40.18 | 4.00 | 36.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Tear Down this Wall COUP Libya | 40.18 | 4.00 | 36.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Lonely Hearts Club Band INFLUENCE West Germany, Panama | 35.91 | 5.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Panama:13.45, control_break:Panama, non_coup_milops_penalty:9.14 |
| 5 | Camp David Accords INFLUENCE West Germany, Panama | 35.91 | 5.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Panama:13.45, control_break:Panama, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Five Year Plan[5], Arab-Israeli War[13], East European Unrest[29], Junta[50], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Sudan | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Sudan | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Colombia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | Junta COUP Colombia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | Arab-Israeli War INFLUENCE East Germany, Venezuela | 38.03 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Camp David Accords[66], Puppet Governments[67], Voice of America[75], Solidarity[104]`
- state: `VP -2, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Sudan | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | Camp David Accords COUP Sudan | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | Puppet Governments COUP Sudan | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 4 | Voice of America COUP Sudan | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 5 | Solidarity COUP Sudan | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 113: T8 AR3 USSR

- chosen: `Junta [50] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Five Year Plan[5], East European Unrest[29], Junta[50], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Sudan | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Junta INFLUENCE East Germany, Venezuela | 36.70 | 5.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Venezuela:13.70, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 4 | Duck and Cover INFLUENCE East Germany, Egypt, Venezuela | 34.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Five Year Plan INFLUENCE East Germany, Egypt, Venezuela | 34.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:6`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], Camp David Accords[66], Puppet Governments[67], Voice of America[75], Solidarity[104]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Sudan | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | Puppet Governments COUP Sudan | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Voice of America COUP Sudan | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Solidarity COUP Sudan | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 5 | Camp David Accords COUP Egypt | 34.00 | 4.00 | 30.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Duck and Cover[4], Five Year Plan[5], East European Unrest[29], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, Egypt, Venezuela | 32.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Five Year Plan INFLUENCE East Germany, Egypt, Venezuela | 32.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | East European Unrest INFLUENCE East Germany, Egypt, Venezuela | 32.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | The Iron Lady INFLUENCE East Germany, Egypt, Venezuela | 32.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Egypt:12.95, control_break:Egypt, influence:Venezuela:13.70, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Duck and Cover COUP Sudan | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:6`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], Puppet Governments[67], Voice of America[75], Solidarity[104]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Egypt | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Puppet Governments COUP Libya | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Voice of America COUP Egypt | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Voice of America COUP Libya | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Solidarity COUP Egypt | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Five Year Plan [5] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Five Year Plan[5], East European Unrest[29], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan COUP Colombia | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | East European Unrest COUP Colombia | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | The Iron Lady COUP Colombia | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Colombia | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Five Year Plan INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:6`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], Voice of America[75], Solidarity[104]`
- state: `VP -2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Voice of America COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Voice of America COUP Sudan | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Voice of America COUP Zimbabwe | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Solidarity COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `East European Unrest [29] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `East European Unrest[29], The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Saharan States | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | The Iron Lady COUP Saharan States | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | East European Unrest COUP Colombia | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | The Iron Lady COUP Colombia | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Reagan Bombs Libya COUP Saharan States | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Solidarity [104] as COUP`
- flags: `milops_shortfall:6`
- hand: `Nasser[15], Portuguese Empire Crumbles[55], Solidarity[104]`
- state: `VP -2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Saharan States | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Solidarity COUP SE African States | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Solidarity COUP Sudan | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Solidarity COUP Zimbabwe | 26.55 | 4.00 | 22.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Solidarity COUP Colombia | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `The Iron Lady [86] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `The Iron Lady[86], Reagan Bombs Libya[87]`
- state: `VP -2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady COUP Saharan States | 40.90 | 4.00 | 57.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | The Iron Lady COUP Colombia | 40.40 | 4.00 | 56.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Reagan Bombs Libya COUP Saharan States | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Reagan Bombs Libya COUP Colombia | 38.05 | 4.00 | 50.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | The Iron Lady COUP Mozambique | 18.90 | 4.00 | 35.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Nasser[15], Portuguese Empire Crumbles[55]`
- state: `VP -2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Portuguese Empire Crumbles COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP Sudan | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Zimbabwe | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Colombia | 19.05 | 4.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 123: T9 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Korean War[11], De Gaulle Leads France[17], Captured Nazi Scientist[18], Nuclear Test Ban[34], Brush War[39], South African Unrest[56], Puppet Governments[67], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Soviets Shoot Down KAL 007 [92] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Korean War[11], COMECON[14], NORAD[38], Kitchen Debates[51], Missile Envy[52], OPEC[64], Soviets Shoot Down KAL 007[92], Ortega Elected in Nicaragua[94], Chernobyl[97]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (down)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Chernobyl EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `milops_shortfall:9`
- hand: `Korean War[11], De Gaulle Leads France[17], Captured Nazi Scientist[18], Brush War[39], South African Unrest[56], Puppet Governments[67], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Saharan States | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Brush War COUP Saharan States | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | De Gaulle Leads France COUP Colombia | 49.26 | 4.00 | 45.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | Brush War COUP Colombia | 49.26 | 4.00 | 45.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 5 | De Gaulle Leads France COUP Egypt | 46.61 | 4.00 | 43.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 126: T9 AR1 US

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Korean War[11], COMECON[14], NORAD[38], Kitchen Debates[51], Missile Envy[52], OPEC[64], Ortega Elected in Nicaragua[94], Chernobyl[97]`
- state: `VP -4, DEFCON 4, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 56.01 | 4.00 | 52.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Chernobyl COUP Indonesia | 56.01 | 4.00 | 52.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | NORAD COUP Saharan States | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | Chernobyl COUP Saharan States | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 5 | Missile Envy COUP Indonesia | 49.66 | 4.00 | 45.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], Captured Nazi Scientist[18], Brush War[39], South African Unrest[56], Puppet Governments[67], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE West Germany, Nigeria, Indonesia | 52.40 | 5.00 | 55.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:Indonesia:11.35, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 2 | Brush War COUP Colombia | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Korean War COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | South African Unrest COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], Kitchen Debates[51], Missile Envy[52], OPEC[64], Ortega Elected in Nicaragua[94], Chernobyl[97]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, West Germany, Egypt | 52.70 | 5.00 | 56.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:8.00 |
| 2 | Chernobyl COUP Saharan States | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Missile Envy COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Chernobyl COUP Libya | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Missile Envy INFLUENCE West Germany, Egypt | 36.55 | 5.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Egypt:12.95, control_break:Egypt, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:6`
- hand: `Korean War[11], Captured Nazi Scientist[18], South African Unrest[56], Puppet Governments[67], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 42.65 | 4.00 | 38.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | South African Unrest COUP Colombia | 42.65 | 4.00 | 38.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Colombia | 42.65 | 4.00 | 38.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Colombia | 36.30 | 4.00 | 32.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 5 | Korean War COUP Egypt | 34.00 | 4.00 | 30.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], Kitchen Debates[51], Missile Envy[52], OPEC[64], Ortega Elected in Nicaragua[94]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Saharan States | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | Missile Envy COUP Colombia | 42.65 | 4.00 | 38.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Kitchen Debates COUP Saharan States | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 4 | Kitchen Debates COUP Colombia | 36.30 | 4.00 | 32.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 5 | Missile Envy COUP Libya | 34.00 | 4.00 | 30.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `South African Unrest [56] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], South African Unrest[56], Puppet Governments[67], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Saharan States | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Colonial Rear Guards COUP Saharan States | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 4 | South African Unrest COUP Egypt | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Colonial Rear Guards COUP Egypt | 34.90 | 4.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], Kitchen Debates[51], OPEC[64], Ortega Elected in Nicaragua[94]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Kitchen Debates COUP Colombia | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | COMECON COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | OPEC COUP Saharan States | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP Colombia | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Puppet Governments[67], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Saharan States | 45.55 | 4.00 | 41.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 3 | Colonial Rear Guards COUP Egypt | 36.40 | 4.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Colonial Rear Guards COUP Syria | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:1.5 |
| 5 | Colonial Rear Guards COUP Algeria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `COMECON [14] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], COMECON[14], OPEC[64], Ortega Elected in Nicaragua[94]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Colombia | 31.40 | 4.00 | 47.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | OPEC COUP Colombia | 31.40 | 4.00 | 47.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Korean War COUP Colombia | 29.05 | 4.00 | 41.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Ortega Elected in Nicaragua COUP Colombia | 29.05 | 4.00 | 41.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | COMECON COUP Libya | 22.75 | 4.00 | 39.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 41.70 | 4.00 | 37.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Egypt | 33.05 | 4.00 | 29.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Puppet Governments COUP Colombia | 32.05 | 4.00 | 44.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Colombia | 32.05 | 4.00 | 44.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Syria | 30.55 | 4.00 | 26.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `OPEC [64] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], OPEC[64], Ortega Elected in Nicaragua[94]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Colombia | 34.40 | 4.00 | 50.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Korean War COUP Colombia | 32.05 | 4.00 | 44.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Ortega Elected in Nicaragua COUP Colombia | 32.05 | 4.00 | 44.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | OPEC COUP Libya | 25.75 | 4.00 | 42.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Korean War COUP Libya | 23.40 | 4.00 | 35.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Colombia | 41.05 | 4.00 | 53.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Colombia | 41.05 | 4.00 | 53.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Egypt | 32.40 | 4.00 | 44.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:6.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Egypt | 32.40 | 4.00 | 44.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:6.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Puppet Governments COUP Syria | 29.90 | 4.00 | 42.20 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], Ortega Elected in Nicaragua[94]`
- state: `VP -4, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 41.05 | 4.00 | 53.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Ortega Elected in Nicaragua COUP Colombia | 41.05 | 4.00 | 53.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP Libya | 32.40 | 4.00 | 44.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:6.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Ortega Elected in Nicaragua COUP Libya | 32.40 | 4.00 | 44.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:6.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Korean War COUP Algeria | 26.65 | 4.00 | 38.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:6.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 139: T10 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Truman Doctrine[19], Nuclear Test Ban[34], Quagmire[45], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Liberation Theology[76], Iranian Hostage Crisis[85], Pershing II Deployed[102], Colonial Rear Guards[110]`
- state: `VP -4, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Iranian Hostage Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Pershing II Deployed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Blockade[10], Indo-Pakistani War[24], CIA Created[26], UN Intervention[32], Arms Race[42], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:10`
- hand: `Truman Doctrine[19], Quagmire[45], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Liberation Theology[76], Iranian Hostage Crisis[85], Pershing II Deployed[102], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Colombia | 49.69 | 4.00 | 46.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Iranian Hostage Crisis COUP Colombia | 49.69 | 4.00 | 46.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | Pershing II Deployed COUP Colombia | 49.69 | 4.00 | 46.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 4 | Quagmire INFLUENCE East Germany, France, West Germany | 47.62 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 47.62 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Blockade[10], Indo-Pakistani War[24], CIA Created[26], UN Intervention[32], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -2, DEFCON 5, MilOps U3/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Indonesia | 56.44 | 4.00 | 52.89 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Indo-Pakistani War COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Camp David Accords COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Nixon Plays the China Card COUP Indonesia | 50.09 | 4.00 | 46.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 143: T10 AR2 USSR

- chosen: `Iranian Hostage Crisis [85] as COUP`
- flags: `milops_shortfall:7`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Liberation Theology[76], Iranian Hostage Crisis[85], Pershing II Deployed[102], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 4, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis COUP Indonesia | 55.65 | 4.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 2 | Pershing II Deployed COUP Indonesia | 55.65 | 4.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 49.72 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 4 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 49.72 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 5 | Liberation Theology COUP Indonesia | 49.30 | 4.00 | 45.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Indo-Pakistani War[24], CIA Created[26], UN Intervention[32], How I Learned to Stop Worrying[49], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -2, DEFCON 3, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Libya | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | How I Learned to Stop Worrying COUP Libya | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Camp David Accords COUP Libya | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Nixon Plays the China Card COUP Libya | 33.90 | 4.00 | 30.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 28.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Liberation Theology[76], Pershing II Deployed[102], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 47.85 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 4 | Pershing II Deployed COUP Cameroon | 28.10 | 4.00 | 24.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:4.5 |
| 5 | Pershing II Deployed COUP Mozambique | 28.10 | 4.00 | 24.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], CIA Created[26], UN Intervention[32], How I Learned to Stop Worrying[49], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 2 | Camp David Accords INFLUENCE East Germany, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 31.70 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 4 | How I Learned to Stop Worrying COUP Saharan States | 21.75 | 4.00 | 18.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |
| 5 | How I Learned to Stop Worrying COUP SE African States | 21.75 | 4.00 | 18.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.40, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Liberation Theology[76], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 28.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 28.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:14.00 |
| 3 | Liberation Theology COUP Cameroon | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Liberation Theology COUP Mozambique | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Liberation Theology COUP Saharan States | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], CIA Created[26], UN Intervention[32], Camp David Accords[66], Nixon Plays the China Card[72]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE East Germany, West Germany | 28.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:14.00 |
| 2 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 28.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:14.00 |
| 3 | Camp David Accords COUP Saharan States | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 4 | Camp David Accords COUP SE African States | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |
| 5 | Camp David Accords COUP Sudan | 22.80 | 4.00 | 19.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:1.75, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:7`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Grain Sales to Soviets[68], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Cameroon | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Colonial Rear Guards COUP Mozambique | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Colonial Rear Guards COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP SE African States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Zimbabwe | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], CIA Created[26], UN Intervention[32], Nixon Plays the China Card[72]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 2 | Nixon Plays the China Card COUP SE African States | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 3 | Nixon Plays the China Card COUP Sudan | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | Nixon Plays the China Card COUP Zimbabwe | 24.55 | 4.00 | 20.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | Nixon Plays the China Card COUP Colombia | 24.05 | 4.00 | 20.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Truman Doctrine[19], Lonely Hearts Club Band[65], Grain Sales to Soviets[68]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Grain Sales to Soviets COUP Saharan States | 34.05 | 4.00 | 46.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Saharan States | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Lonely Hearts Club Band COUP Cameroon | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Lonely Hearts Club Band COUP Mozambique | 12.05 | 4.00 | 24.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], CIA Created[26], UN Intervention[32]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 21.70 | 4.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | CIA Created COUP SE African States | 21.70 | 4.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | CIA Created COUP Sudan | 21.70 | 4.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | CIA Created COUP Zimbabwe | 21.70 | 4.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Saharan States | 21.70 | 4.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 44.55 | 4.00 | 56.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Cameroon | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP Mozambique | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP SE African States | 22.55 | 4.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], UN Intervention[32]`
- state: `VP -2, DEFCON 2, MilOps U3/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 54.20 | 4.00 | 50.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5 |
| 2 | Blockade COUP Saharan States | 42.20 | 4.00 | 50.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | UN Intervention COUP SE African States | 32.20 | 4.00 | 28.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Sudan | 32.20 | 4.00 | 28.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 32.20 | 4.00 | 28.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +16, DEFCON +1, MilOps U-3/A-3`
