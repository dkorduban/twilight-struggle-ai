# minimal_hybrid detailed rollout log

- seed: `20260532`
- winner: `US`
- final_vp: `-15`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Vietnam Revolts[9], COMECON[14], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Suez Crisis[28], East European Unrest[29], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Fidel[8], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32], Nuclear Test Ban[34], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Marshall Plan[23], US/Japan Mutual Defense Pact[27], Suez Crisis[28], East European Unrest[29], De-Stalinization[33]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | De-Stalinization COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 3 | Vietnam Revolts COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 62.47 | 6.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, Thailand | 62.47 | 6.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Fidel[8], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32], NORAD[38]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Olympic Games INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Independent Reds INFLUENCE Indonesia, Philippines | 44.67 | 6.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | Socialist Governments INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | NORAD COUP Syria | 33.50 | 4.00 | 29.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Marshall Plan[23], US/Japan Mutual Defense Pact[27], East European Unrest[29], De-Stalinization[33]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, North Korea, Thailand | 66.70 | 6.00 | 61.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 60.20 | 6.00 | 78.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, North Korea, Thailand | 60.20 | 6.00 | 78.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | De-Stalinization COUP Iran | 53.50 | 4.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:2.5, opening_iran_coup_bonus |
| 5 | Vietnam Revolts INFLUENCE North Korea, Thailand | 48.70 | 6.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Fidel[8], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, Turkey | 38.60 | 6.00 | 34.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:1.60 |
| 2 | Independent Reds INFLUENCE East Germany, Turkey | 38.60 | 6.00 | 34.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:1.60 |
| 3 | Socialist Governments INFLUENCE East Germany, France, Turkey | 35.50 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Olympic Games COUP Syria | 28.25 | 4.00 | 24.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |
| 5 | Independent Reds COUP Syria | 28.25 | 4.00 | 24.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Marshall Plan[23], US/Japan Mutual Defense Pact[27], East European Unrest[29]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, South Korea, Israel, Thailand | 58.95 | 6.00 | 77.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | US/Japan Mutual Defense Pact INFLUENCE West Germany, South Korea, Israel, Thailand | 58.95 | 6.00 | 77.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Vietnam Revolts INFLUENCE West Germany, Thailand | 48.80 | 6.00 | 43.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand |
| 4 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Duck and Cover INFLUENCE West Germany, South Korea, Thailand | 46.20 | 6.00 | 60.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Fidel[8], Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE France, West Germany | 41.40 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:2.00 |
| 2 | Socialist Governments INFLUENCE France, West Germany, Panama | 37.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Independent Reds COUP Syria | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:1.5 |
| 4 | Independent Reds COUP Indonesia | 26.05 | 4.00 | 22.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Fidel INFLUENCE France, West Germany | 25.40 | 6.00 | 37.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Vietnam Revolts[9], US/Japan Mutual Defense Pact[27], East European Unrest[29]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, Saudi Arabia, Philippines, Thailand | 51.05 | 6.00 | 69.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Vietnam Revolts INFLUENCE Italy, Thailand | 42.60 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |
| 4 | Duck and Cover INFLUENCE Italy, Philippines, Thailand | 38.90 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |
| 5 | East European Unrest INFLUENCE Italy, Philippines, Thailand | 38.90 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Italy, Panama, Philippines | 34.98 | 6.00 | 52.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Panama:11.20, control_break:Panama, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Captured Nazi Scientist COUP Philippines | 25.55 | 4.00 | 21.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:1, milops_urgency:0.33, expected_swing:0.5 |
| 3 | UN Intervention COUP Philippines | 25.55 | 4.00 | 21.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:1, milops_urgency:0.33, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Japan | 24.50 | 4.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.33 |
| 5 | UN Intervention COUP Japan | 24.50 | 4.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china`
- hand: `Duck and Cover[4], Vietnam Revolts[9], East European Unrest[29]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Vietnam Revolts COUP Indonesia | 46.30 | 4.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, coup_access_open, expected_swing:3.5 |
| 3 | Vietnam Revolts INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Duck and Cover INFLUENCE Japan, Indonesia, Thailand | 38.00 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty |
| 5 | East European Unrest INFLUENCE Japan, Indonesia, Thailand | 38.00 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP -3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |
| 4 | UN Intervention COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |
| 5 | Captured Nazi Scientist INFLUENCE Japan | 15.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], East European Unrest[29]`
- state: `VP -3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Pakistan, Thailand | 39.10 | 6.00 | 53.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | East European Unrest INFLUENCE Japan, Pakistan, Thailand | 39.10 | 6.00 | 53.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Duck and Cover SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | East European Unrest SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Duck and Cover COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], UN Intervention[32]`
- state: `VP -3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Fidel INFLUENCE Japan, Egypt | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 3 | UN Intervention COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Fidel COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Arab-Israeli War [13] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], Containment[25], CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], NATO[21], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], Containment[25], CIA Created[26], Decolonization[30], Formosan Resolution[35]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Indonesia | 49.30 | 4.00 | 45.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 2 | Decolonization INFLUENCE Pakistan, Thailand | 43.43 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Blockade COUP Indonesia | 42.95 | 4.00 | 39.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | Nasser COUP Indonesia | 42.95 | 4.00 | 39.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 5 | Containment INFLUENCE India, Pakistan, Thailand | 40.83 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 18: T2 AR1 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Japan, Indonesia | 35.03 | 6.00 | 32.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:2.67 |
| 2 | Special Relationship INFLUENCE Japan, Indonesia | 35.03 | 6.00 | 32.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:2.67 |
| 3 | Warsaw Pact Formed INFLUENCE Japan, Egypt, Indonesia | 30.58 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | De Gaulle Leads France INFLUENCE Japan, Egypt, Indonesia | 30.58 | 6.00 | 47.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Indo-Pakistani War COUP Syria | 29.65 | 4.00 | 25.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], Containment[25], CIA Created[26], Formosan Resolution[35]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE India, Pakistan, Thailand | 43.50 | 6.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Pakistan, Thailand | 30.10 | 6.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], The Cambridge Five[36], Special Relationship[37]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Egypt | 34.35 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.20 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, Japan, Egypt | 29.85 | 6.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Japan, Egypt | 29.85 | 6.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Special Relationship COUP Syria | 29.85 | 4.00 | 26.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Korean War INFLUENCE Japan, Egypt | 18.35 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china`
- hand: `Blockade[10], Nasser[15], Truman Doctrine[19], CIA Created[26], Formosan Resolution[35]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Egypt, Libya | 32.10 | 6.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France INFLUENCE Japan, Egypt, Libya | 32.10 | 6.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Korean War INFLUENCE Japan, Egypt | 20.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five INFLUENCE Japan, Egypt | 20.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Warsaw Pact Formed COUP Syria | 15.50 | 4.00 | 31.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Truman Doctrine[19], CIA Created[26], Formosan Resolution[35]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 5 | Nasser COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], De Gaulle Leads France[17], The Cambridge Five[36]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, Libya | 35.72 | 6.00 | 55.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | Korean War INFLUENCE Japan, Libya | 24.22 | 6.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | The Cambridge Five INFLUENCE Japan, Libya | 24.22 | 6.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | De Gaulle Leads France COUP Syria | 16.00 | 4.00 | 32.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Korean War COUP Syria | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26], Formosan Resolution[35]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Formosan Resolution COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Syria | 13.30 | 4.00 | 21.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Korean War INFLUENCE West Germany, Japan | 12.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | The Cambridge Five INFLUENCE West Germany, Japan | 12.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 27: T2 AR6 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 2 | CIA Created INFLUENCE Thailand | 14.30 | 6.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | Truman Doctrine COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine EVENT | -6.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, Japan | 26.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Japan | 15.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 3 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | The Cambridge Five COUP Lebanon | -0.95 | 4.00 | 11.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Lebanon | -2.30 | 4.00 | 5.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Marshall Plan[23], Containment[25], Red Scare/Purge[31], The Cambridge Five[36]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Socialist Governments[7], Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON -1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Marshall Plan[23], Containment[25], The Cambridge Five[36]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE UK, Japan, Egypt, Thailand | 45.35 | 6.00 | 67.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Fidel INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Vietnam Revolts INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 33.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Egypt | 25.65 | 4.00 | 21.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 2 | Special Relationship COUP Egypt | 25.65 | 4.00 | 21.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, expected_swing:1.5 |
| 3 | UN Intervention INFLUENCE Japan | 23.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |
| 4 | Formosan Resolution INFLUENCE Japan | 22.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |
| 5 | Special Relationship INFLUENCE Japan | 22.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 33: T3 AR2 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Fidel[8], Vietnam Revolts[9], Romanian Abdication[12], Containment[25], The Cambridge Five[36]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Vietnam Revolts INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | The Cambridge Five INFLUENCE Japan, Thailand | 37.50 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 33.05 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Containment INFLUENCE Japan, Egypt, Thailand | 33.05 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17], UN Intervention[32], Special Relationship[37]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE UK | 22.90 | 6.00 | 18.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:UK:13.65, control_break:UK, non_coup_milops_penalty:1.60 |
| 2 | Special Relationship INFLUENCE UK | 22.75 | 6.00 | 18.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:13.65, control_break:UK, non_coup_milops_penalty:1.60 |
| 3 | Socialist Governments INFLUENCE UK, Japan | 18.75 | 6.00 | 34.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | De Gaulle Leads France INFLUENCE UK, Japan | 18.75 | 6.00 | 34.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, control_break:UK, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Special Relationship COUP SE African States | 14.40 | 4.00 | 10.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Romanian Abdication[12], Containment[25], The Cambridge Five[36]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Japan, Thailand | 36.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 36.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 31.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Containment INFLUENCE Japan, Egypt, Thailand | 31.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Romanian Abdication INFLUENCE Thailand | 20.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17], Special Relationship[37]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan | 19.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan | 15.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Japan | 15.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Special Relationship COUP SE African States | 14.55 | 4.00 | 10.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Special Relationship COUP Sudan | 14.55 | 4.00 | 10.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Romanian Abdication[12], Containment[25], The Cambridge Five[36]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Thailand | 34.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 29.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Containment INFLUENCE Japan, Egypt, Thailand | 29.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Romanian Abdication INFLUENCE Thailand | 18.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 5 | Five Year Plan SPACE | 0.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan | 14.68 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | De Gaulle Leads France INFLUENCE West Germany, Japan | 14.68 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Nasser INFLUENCE Japan | 7.33 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Arab-Israeli War SPACE | 6.03 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Socialist Governments SPACE | 5.88 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Romanian Abdication[12], Containment[25]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 16.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | Containment INFLUENCE Japan, Egypt, Thailand | 16.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 3 | Romanian Abdication INFLUENCE Thailand | 5.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:21.00 |
| 4 | Five Year Plan SPACE | -12.45 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | Containment SPACE | -12.45 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], De Gaulle Leads France[17]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan | 10.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Nasser INFLUENCE Japan | 3.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Arab-Israeli War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | De Gaulle Leads France SPACE | 1.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | De Gaulle Leads France COUP SE African States | 0.65 | 4.00 | 17.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Containment[25]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Sudan | 17.45 | 4.00 | 13.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Containment COUP Sudan | 10.15 | 4.00 | 26.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Containment INFLUENCE Japan, Libya, Thailand | 4.85 | 6.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:33.00 |
| 4 | Romanian Abdication INFLUENCE Thailand | -6.70 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:33.00 |
| 5 | Containment SPACE | -24.45 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:33.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 42: T3 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15]`
- state: `VP -3, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Sudan | 22.80 | 4.00 | 35.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nasser COUP Sudan | 21.45 | 4.00 | 29.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP SE African States | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Zimbabwe | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Colombia | 0.30 | 4.00 | 12.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 43: T4 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Marshall Plan[23], Containment[25], Decolonization[30], Red Scare/Purge[31], Portuguese Empire Crumbles[55], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Marshall Plan[23], Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], ABM Treaty[60], Flower Power[62], Sadat Expels Soviets[73], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Marshall Plan[23], Containment[25], Decolonization[30], Portuguese Empire Crumbles[55], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, West Germany, Mexico, Algeria | 41.68 | 6.00 | 64.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Vietnam Revolts COUP Sudan | 41.26 | 4.00 | 37.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Sudan | 41.26 | 4.00 | 37.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |
| 4 | Decolonization COUP Sudan | 41.26 | 4.00 | 37.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |
| 5 | Portuguese Empire Crumbles COUP Sudan | 41.26 | 4.00 | 37.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], ABM Treaty[60], Flower Power[62], Sadat Expels Soviets[73], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE Italy, Mexico, Ethiopia | 58.33 | 6.00 | 57.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 2 | ABM Treaty COUP Mexico | 46.81 | 4.00 | 43.41 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | ABM Treaty COUP Algeria | 46.06 | 4.00 | 42.66 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 4 | Sadat Expels Soviets INFLUENCE Italy, Ethiopia | 41.53 | 6.00 | 40.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, non_coup_milops_penalty:4.57 |
| 5 | Sadat Expels Soviets COUP Mexico | 40.46 | 4.00 | 36.91 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], Containment[25], Decolonization[30], Portuguese Empire Crumbles[55], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 3 | Decolonization COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 4 | Portuguese Empire Crumbles COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 5 | Willy Brandt COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 48: T4 AR2 US

- chosen: `Sadat Expels Soviets [73] as COUP`
- flags: `milops_shortfall:4`
- hand: `Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Flower Power[62], Sadat Expels Soviets[73], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets COUP Sudan | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 2 | Nuclear Subs COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Sudan | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 4 | Sadat Expels Soviets COUP Algeria | 40.00 | 4.00 | 36.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Sadat Expels Soviets INFLUENCE Morocco, South Africa | 33.82 | 6.00 | 33.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 49: T4 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Arab-Israeli War[13], Containment[25], Decolonization[30], Portuguese Empire Crumbles[55], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Algeria, Morocco | 38.50 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.20 |
| 2 | Decolonization INFLUENCE Algeria, Morocco | 38.50 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.20 |
| 3 | Portuguese Empire Crumbles INFLUENCE Algeria, Morocco | 38.50 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.20 |
| 4 | Willy Brandt INFLUENCE Algeria, Morocco | 38.50 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.20 |
| 5 | Containment INFLUENCE West Germany, Algeria, Morocco | 34.50 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:1`
- hand: `Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Flower Power[62], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Sudan | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5 |
| 3 | Brezhnev Doctrine COUP Sudan | 24.50 | 4.00 | 40.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Flower Power COUP Sudan | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Liberation Theology COUP Sudan | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Containment[25], Decolonization[30], Portuguese Empire Crumbles[55], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Sudan | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Portuguese Empire Crumbles COUP Sudan | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | Willy Brandt COUP Sudan | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Decolonization INFLUENCE East Germany, West Germany | 33.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 33.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Flower Power[62], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE Morocco | 20.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:2.00 |
| 2 | How I Learned to Stop Worrying COUP Colombia | 17.30 | 4.00 | 13.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP SE African States | 17.30 | 4.00 | 13.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |
| 4 | How I Learned to Stop Worrying COUP Sudan | 17.30 | 4.00 | 13.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | How I Learned to Stop Worrying COUP Zimbabwe | 17.30 | 4.00 | 13.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Containment[25], Portuguese Empire Crumbles[55], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Willy Brandt COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 32.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 4 | Willy Brandt INFLUENCE East Germany, West Germany | 32.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.33 |
| 5 | Containment INFLUENCE East Germany, France, West Germany | 27.47 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Brezhnev Doctrine[54], Flower Power[62], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE Algeria, South Africa | 15.88 | 6.00 | 33.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Lone Gunman INFLUENCE South Africa | 7.98 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Flower Power SPACE | 5.03 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Liberation Theology SPACE | 5.03 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Brezhnev Doctrine SPACE | 4.88 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Containment[25], Willy Brandt[58], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE West Germany, Algeria | 27.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:14.00 |
| 2 | Containment INFLUENCE East Germany, West Germany, Algeria | 22.45 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Willy Brandt COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Willy Brandt COUP Sudan | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP Guatemala | 19.30 | 4.00 | 15.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Flower Power[62], Liberation Theology[76], Lone Gunman[109]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE South Africa | 8.65 | 6.00 | 21.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Flower Power INFLUENCE South Africa | 4.50 | 6.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Liberation Theology INFLUENCE South Africa | 4.50 | 6.00 | 21.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Flower Power COUP Colombia | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Saharan States | 2.05 | 4.00 | 14.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Containment[25], Nixon Plays the China Card[72]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 10.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 2 | Containment COUP Saharan States | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Containment COUP Sudan | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Containment COUP Guatemala | 7.65 | 4.00 | 24.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Flower Power [62] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Flower Power[62], Liberation Theology[76]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Colombia | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Flower Power COUP Saharan States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Flower Power COUP SE African States | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Flower Power COUP Sudan | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Flower Power COUP Zimbabwe | 3.55 | 4.00 | 15.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 59: T5 AR0 USSR

- chosen: `U2 Incident [63] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Olympic Games[20], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32], Special Relationship[37], U2 Incident[63], Latin American Death Squads[70]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Indo-Pakistani War[24], Formosan Resolution[35], NORAD[38], Brush War[39], Quagmire[45], SALT Negotiations[46], One Small Step[81]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Olympic Games[20], CIA Created[26], US/Japan Mutual Defense Pact[27], UN Intervention[32], Special Relationship[37], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Cuba | 38.49 | 6.00 | 62.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:5.71 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | 31.69 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 3 | Olympic Games INFLUENCE East Germany, West Germany | 31.69 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | Latin American Death Squads INFLUENCE East Germany, West Germany | 31.69 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 5 | Vietnam Revolts COUP Mexico | 27.54 | 4.00 | 23.84 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Indo-Pakistani War[24], Formosan Resolution[35], Brush War[39], Quagmire[45], SALT Negotiations[46], One Small Step[81]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE Brazil, Venezuela, South Africa | 49.04 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | SALT Negotiations COUP Libya | 39.14 | 4.00 | 35.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | SALT Negotiations COUP Mexico | 33.89 | 4.00 | 30.34 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 4 | SALT Negotiations COUP Algeria | 33.14 | 4.00 | 29.59 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 5 | Indo-Pakistani War INFLUENCE Brazil, South Africa | 32.99 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Olympic Games[20], CIA Created[26], UN Intervention[32], Special Relationship[37], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE France, West Germany | 35.73 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 2 | Olympic Games INFLUENCE France, West Germany | 35.73 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 3 | Latin American Death Squads INFLUENCE France, West Germany | 35.73 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.67 |
| 4 | Duck and Cover INFLUENCE East Germany, France, West Germany | 31.13 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Vietnam Revolts COUP Mexico | 27.90 | 4.00 | 24.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Indo-Pakistani War[24], Formosan Resolution[35], Brush War[39], Quagmire[45], One Small Step[81]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Brazil, Venezuela | 37.43 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 2 | Formosan Resolution INFLUENCE Brazil, Venezuela | 37.43 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 3 | One Small Step INFLUENCE Brazil, Venezuela | 37.43 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 4 | Brush War INFLUENCE Argentina, Brazil, Venezuela | 35.48 | 6.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 5 | Quagmire INFLUENCE Argentina, Brazil, Venezuela | 35.48 | 6.00 | 56.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Olympic Games[20], CIA Created[26], UN Intervention[32], Special Relationship[37], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Latin American Death Squads INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Olympic Games COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Latin American Death Squads COUP Mexico | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Olympic Games COUP Algeria | 27.65 | 4.00 | 23.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Formosan Resolution[35], Brush War[39], Quagmire[45], One Small Step[81]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Argentina | 37.05 | 6.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:8.00 |
| 2 | One Small Step INFLUENCE West Germany, Argentina | 37.05 | 6.00 | 39.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:8.00 |
| 3 | Brush War INFLUENCE West Germany, Argentina, South Africa | 33.70 | 6.00 | 56.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Quagmire INFLUENCE West Germany, Argentina, South Africa | 33.70 | 6.00 | 56.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, access_touch:Argentina, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Formosan Resolution COUP Libya | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], CIA Created[26], UN Intervention[32], Special Relationship[37], Latin American Death Squads[70]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Mexico | 29.15 | 4.00 | 25.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |
| 2 | Latin American Death Squads COUP Algeria | 28.40 | 4.00 | 24.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 27.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 4 | Latin American Death Squads COUP Egypt | 27.40 | 4.00 | 23.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |
| 5 | UN Intervention COUP Mexico | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 68: T5 AR4 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Blockade[10], Brush War[39], Quagmire[45], One Small Step[81]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Argentina, Chile | 35.70 | 6.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:10.00 |
| 2 | Brush War INFLUENCE Mexico, Argentina, Chile | 32.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Quagmire INFLUENCE Mexico, Argentina, Chile | 32.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | One Small Step COUP Colombia | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP Saharan States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Duck and Cover[4], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | UN Intervention COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention INFLUENCE West Germany | 14.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Special Relationship INFLUENCE East Germany, West Germany | 13.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Brush War[39], Quagmire[45]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE West Germany, Mexico, Chile | 27.12 | 6.00 | 54.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Quagmire INFLUENCE West Germany, Mexico, Chile | 27.12 | 6.00 | 54.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Brush War COUP Colombia | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Brush War COUP Saharan States | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Brush War COUP SE African States | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Sudan | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP Guatemala | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Haiti | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Special Relationship COUP Saharan States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Quagmire[45]`
- state: `VP -3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Saharan States | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Blockade COUP Saharan States | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Quagmire COUP Colombia | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP SE African States | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Sudan | 11.40 | 4.00 | 27.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 73: T5 AR7 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Special Relationship COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Special Relationship COUP Guatemala | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship COUP Haiti | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Haiti, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Saharan States | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10]`
- state: `VP -3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Blockade COUP Colombia | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Blockade COUP SE African States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Blockade COUP Sudan | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Blockade COUP Zimbabwe | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], The Cambridge Five[36], Arms Race[42], Allende[57], Muslim Revolution[59], Camp David Accords[66]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:6`
- hand: `De Gaulle Leads France[17], Nuclear Test Ban[34], South African Unrest[56], OPEC[64], Puppet Governments[67], Grain Sales to Soviets[68], OAS Founded[71], Che[83], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], The Cambridge Five[36], Arms Race[42], Allende[57], Camp David Accords[66]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE Egypt, Mexico, Nigeria | 57.44 | 6.00 | 58.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Egypt:13.20, control_break:Egypt, influence:Mexico:14.95, control_break:Mexico, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:6.86 |
| 2 | Arms Race COUP Indonesia | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:4.5 |
| 3 | Korean War COUP Indonesia | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Indonesia | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Indonesia | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:6`
- hand: `De Gaulle Leads France[17], South African Unrest[56], OPEC[64], Puppet Governments[67], Grain Sales to Soviets[68], OAS Founded[71], Che[83], Panama Canal Returned[111]`
- state: `VP -4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 2 | Puppet Governments COUP Indonesia | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP Saharan States | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Indonesia | 42.12 | 4.00 | 38.42 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:3.5 |
| 5 | Puppet Governments COUP Egypt | 39.22 | 4.00 | 35.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 79: T6 AR2 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], The Cambridge Five[36], Allende[57], Camp David Accords[66]`
- state: `VP -4, DEFCON 5, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Korean War COUP Indonesia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, expected_swing:3.5 |
| 3 | Arab-Israeli War COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Indonesia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 80: T6 AR2 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], South African Unrest[56], OPEC[64], Grain Sales to Soviets[68], OAS Founded[71], Che[83], Panama Canal Returned[111]`
- state: `VP -4, DEFCON 5, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Nigeria | 50.05 | 4.00 | 46.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | OAS Founded COUP Nigeria | 43.70 | 4.00 | 39.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Nigeria | 43.70 | 4.00 | 39.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 4 | Grain Sales to Soviets COUP Indonesia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, expected_swing:3.5 |
| 5 | Grain Sales to Soviets INFLUENCE Chile, South Africa | 38.97 | 6.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], The Cambridge Five[36], Allende[57], Camp David Accords[66]`
- state: `VP -4, DEFCON 4, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Indonesia | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, expected_swing:3.5 |
| 3 | The Cambridge Five COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Indonesia | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, expected_swing:3.5 |
| 5 | Nasser COUP Saharan States | 35.60 | 4.00 | 31.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], South African Unrest[56], OPEC[64], OAS Founded[71], Che[83], Panama Canal Returned[111]`
- state: `VP -4, DEFCON 4, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Saharan States | 35.60 | 4.00 | 31.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:2.5 |
| 2 | OAS Founded COUP Indonesia | 35.60 | 4.00 | 31.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Saharan States | 35.60 | 4.00 | 31.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Indonesia | 35.60 | 4.00 | 31.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, expected_swing:2.5 |
| 5 | De Gaulle Leads France INFLUENCE Argentina, Chile, South Africa | 33.95 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Truman Doctrine[19], The Cambridge Five[36], Allende[57], Camp David Accords[66]`
- state: `VP -4, DEFCON 4, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Nigeria | 51.05 | 4.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Nasser COUP Nigeria | 44.70 | 4.00 | 40.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Allende COUP Nigeria | 44.70 | 4.00 | 40.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | The Cambridge Five COUP Indonesia | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:1.00, expected_swing:3.5 |
| 5 | Nasser COUP Indonesia | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], South African Unrest[56], OPEC[64], Che[83], Panama Canal Returned[111]`
- state: `VP -4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | De Gaulle Leads France INFLUENCE Argentina, Chile, South Africa | 32.35 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | OPEC INFLUENCE Argentina, Chile, South Africa | 32.35 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Che INFLUENCE Argentina, Chile, South Africa | 32.35 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | De Gaulle Leads France COUP Saharan States | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Truman Doctrine[19], Allende[57], Camp David Accords[66]`
- state: `VP -4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 3 | Camp David Accords COUP Saharan States | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 25.20 | 4.00 | 33.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP Mexico | 23.05 | 4.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `De Gaulle Leads France[17], South African Unrest[56], OPEC[64], Che[83]`
- state: `VP -4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | OPEC COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Che COUP Saharan States | 29.90 | 4.00 | 46.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | De Gaulle Leads France INFLUENCE Argentina, Chile, South Africa | 29.68 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | OPEC INFLUENCE Argentina, Chile, South Africa | 29.68 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 87: T6 AR6 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], Allende[57], Camp David Accords[66]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Camp David Accords COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Mexico | 25.05 | 4.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Allende COUP Algeria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `South African Unrest[56], OPEC[64], Che[83]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE Chile, Nigeria, South Africa | 23.75 | 6.00 | 59.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | Che INFLUENCE Chile, Nigeria, South Africa | 23.75 | 6.00 | 59.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, control_break:Chile, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 3 | OPEC COUP Egypt | 21.50 | 4.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | OPEC COUP Libya | 21.50 | 4.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Che COUP Egypt | 21.50 | 4.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Camp David Accords[66]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Saharan States | 33.20 | 4.00 | 41.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Camp David Accords COUP Mexico | 21.40 | 4.00 | 33.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:4.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 4 | Camp David Accords COUP Algeria | 20.65 | 4.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:4.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Mexico | 19.05 | 4.00 | 27.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:4.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Che [83] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `South African Unrest[56], Che[83]`
- state: `VP -4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Egypt | 26.00 | 4.00 | 42.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Che COUP Libya | 26.00 | 4.00 | 42.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | South African Unrest COUP Egypt | 23.65 | 4.00 | 35.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | South African Unrest COUP Libya | 23.65 | 4.00 | 35.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Che COUP Mexico | 20.75 | 4.00 | 37.20 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U-2/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Socialist Governments[7], Romanian Abdication[12], De Gaulle Leads France[17], Containment[25], East European Unrest[29], The Cambridge Five[36], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], Cuban Missile Crisis[43], Junta[50], Cultural Revolution[61], Ask Not What Your Country Can Do For You[78]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Romanian Abdication[12], De Gaulle Leads France[17], Containment[25], East European Unrest[29], The Cambridge Five[36], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 44.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | The Cambridge Five INFLUENCE East Germany, West Germany | 29.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Duck and Cover INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Containment INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | East European Unrest INFLUENCE East Germany, France, West Germany | 24.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], Junta[50], Cultural Revolution[61], Ask Not What Your Country Can Do For You[78]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Chile, South Africa | 52.30 | 6.00 | 54.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Independent Reds INFLUENCE West Germany, Chile | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 3 | Junta INFLUENCE West Germany, Chile | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 4 | Warsaw Pact Formed INFLUENCE West Germany, Chile, South Africa | 32.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Suez Crisis INFLUENCE West Germany, Chile, South Africa | 32.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Duck and Cover[4], Romanian Abdication[12], Containment[25], East European Unrest[29], The Cambridge Five[36], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, Mexico | 32.47 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:9.33 |
| 2 | Duck and Cover INFLUENCE East Germany, West Germany, Mexico | 27.87 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 3 | Containment INFLUENCE East Germany, West Germany, Mexico | 27.87 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | East European Unrest INFLUENCE East Germany, West Germany, Mexico | 27.87 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Romanian Abdication INFLUENCE Mexico | 16.47 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], Junta[50], Cultural Revolution[61]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, Chile | 34.32 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:9.33 |
| 2 | Junta INFLUENCE West Germany, Chile | 34.32 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:9.33 |
| 3 | Warsaw Pact Formed INFLUENCE West Germany, Chile, South Africa | 30.97 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | Suez Crisis INFLUENCE West Germany, Chile, South Africa | 30.97 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Cultural Revolution INFLUENCE West Germany, Chile, South Africa | 30.97 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12], Containment[25], East European Unrest[29], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 21.60 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 2 | Containment INFLUENCE East Germany, France, West Germany | 21.60 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | East European Unrest INFLUENCE East Germany, France, West Germany | 21.60 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Romanian Abdication INFLUENCE West Germany | 10.80 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 10.20 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Suez Crisis[28], Junta[50], Cultural Revolution[61]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE West Germany, Chile | 32.45 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:11.20 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, Chile, South Africa | 29.10 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | Suez Crisis INFLUENCE West Germany, Chile, South Africa | 29.10 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Cultural Revolution INFLUENCE West Germany, Chile, South Africa | 29.10 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 15.80 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], Containment[25], East European Unrest[29], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | East European Unrest INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 8.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 7.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | John Paul II Elected Pope SPACE | -6.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Suez Crisis[28], Cultural Revolution[61]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Chile, South Africa | 26.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Chile, South Africa | 26.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Cultural Revolution INFLUENCE West Germany, Chile, South Africa | 26.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 13.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:14.00 |
| 5 | Nasser INFLUENCE West Germany | 1.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], East European Unrest[29], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 14.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Romanian Abdication INFLUENCE West Germany | 3.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.67 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 2.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | John Paul II Elected Pope SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | East European Unrest SPACE | -11.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Suez Crisis[28], Cultural Revolution[61]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Chile, South Africa | 21.63 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Cultural Revolution INFLUENCE West Germany, Chile, South Africa | 21.63 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 8.33 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:18.67 |
| 4 | Nasser INFLUENCE West Germany | -3.67 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Suez Crisis SPACE | -11.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | -27.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:49.00 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -27.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | John Paul II Elected Pope SPACE | -41.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Romanian Abdication REALIGN Mexico | -43.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:49.00 |
| 5 | Romanian Abdication EVENT | -46.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Cultural Revolution[61]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, Chile, South Africa | -8.70 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | -22.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:49.00 |
| 3 | Nasser INFLUENCE West Germany | -34.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Cultural Revolution SPACE | -41.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 5 | Captured Nazi Scientist REALIGN Chile | -42.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `John Paul II Elected Pope[69]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -55.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | John Paul II Elected Pope SPACE | -69.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | John Paul II Elected Pope EVENT | -83.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |
| 4 | John Paul II Elected Pope REALIGN Mexico | -88.08 | -1.00 | 6.22 | 0.00 | -16.00 | -0.30 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Captured Nazi Scientist[18]`
- state: `VP -4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | -50.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:77.00 |
| 2 | Nasser INFLUENCE West Germany | -62.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | Captured Nazi Scientist REALIGN Chile | -70.91 | -1.00 | 7.24 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:77.00 |
| 4 | Captured Nazi Scientist EVENT | -74.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:77.00 |
| 5 | Nasser REALIGN Chile | -82.91 | -1.00 | 7.24 | 0.00 | -12.00 | -0.15 | 0.00 | defcon2_realign_window, offside_ops_penalty, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Suez Crisis[28], East European Unrest[29], Kitchen Debates[51], South African Unrest[56], Cultural Revolution[61], OPEC[64], Puppet Governments[67], Ussuri River Skirmish[77], Star Wars[88]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Indo-Pakistani War [24] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Korean War[11], Indo-Pakistani War[24], Junta[50], Allende[57], Muslim Revolution[59], Liberation Theology[76], Che[83], Panama Canal Returned[111]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Che EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `East European Unrest[29], Kitchen Debates[51], South African Unrest[56], Cultural Revolution[61], OPEC[64], Puppet Governments[67], Ussuri River Skirmish[77], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | East European Unrest INFLUENCE East Germany, France, West Germany | 25.91 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Junta[50], Allende[57], Muslim Revolution[59], Liberation Theology[76], Che[83], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 45.06 | 6.00 | 72.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 2 | Junta INFLUENCE France, West Germany | 36.76 | 6.00 | 40.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 32.91 | 6.00 | 56.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 4 | Vietnam Revolts INFLUENCE France, West Germany | 20.76 | 6.00 | 40.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 5 | Korean War INFLUENCE France, West Germany | 20.76 | 6.00 | 40.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `East European Unrest[29], Kitchen Debates[51], South African Unrest[56], OPEC[64], Puppet Governments[67], Ussuri River Skirmish[77], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 4 | East European Unrest INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Puppet Governments INFLUENCE East Germany, West Germany | 12.23 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Korean War[11], Junta[50], Allende[57], Liberation Theology[76], Che[83], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 33.23 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 29.38 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Vietnam Revolts INFLUENCE East Germany, West Germany | 17.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Korean War INFLUENCE East Germany, West Germany | 17.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 17.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `East European Unrest[29], Kitchen Debates[51], South African Unrest[56], Puppet Governments[67], Ussuri River Skirmish[77], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 42.25 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | 26.10 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 3 | East European Unrest INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Puppet Governments INFLUENCE East Germany, West Germany | 10.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Star Wars INFLUENCE East Germany, West Germany | 10.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Allende[57], Liberation Theology[76], Che[83], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 27.25 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 2 | Vietnam Revolts INFLUENCE East Germany, West Germany | 15.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 3 | Korean War INFLUENCE East Germany, West Germany | 15.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | Liberation Theology INFLUENCE East Germany, West Germany | 15.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | Panama Canal Returned INFLUENCE West Germany | 14.95 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `East European Unrest[29], Kitchen Debates[51], South African Unrest[56], Puppet Governments[67], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | East European Unrest INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Star Wars INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Kitchen Debates INFLUENCE West Germany | -5.25 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Allende[57], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Korean War INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Panama Canal Returned INFLUENCE West Germany | 11.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 5 | Allende INFLUENCE West Germany | -0.25 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `East European Unrest[29], Kitchen Debates[51], Puppet Governments[67], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 13.72 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Puppet Governments INFLUENCE East Germany, West Germany | 1.57 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | Star Wars INFLUENCE East Germany, West Germany | 1.57 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | Kitchen Debates INFLUENCE West Germany | -10.58 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 5 | Puppet Governments SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Korean War[11], Allende[57], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 6.57 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 6.57 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | Panama Canal Returned INFLUENCE West Germany | 6.42 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:21.33 |
| 4 | Allende INFLUENCE West Germany | -5.58 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 5 | Korean War SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Kitchen Debates[51], Puppet Governments[67], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | -33.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | Star Wars INFLUENCE East Germany, West Germany | -33.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | Kitchen Debates INFLUENCE West Germany | -45.25 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 4 | Puppet Governments SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | Star Wars SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Allende[57], Liberation Theology[76], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | -28.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | -28.25 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:56.00 |
| 3 | Allende INFLUENCE West Germany | -40.25 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 4 | Liberation Theology SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | Panama Canal Returned REALIGN Morocco | -53.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Star Wars [88] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Kitchen Debates[51], Star Wars[88]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars INFLUENCE East Germany, West Germany | -65.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | Kitchen Debates INFLUENCE West Germany | -77.25 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 3 | Star Wars SPACE | -80.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 4 | Kitchen Debates EVENT | -94.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:88.00 |
| 5 | Star Wars EVENT | -94.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Allende[57], Panama Canal Returned[111]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE West Germany | -60.25 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:88.00 |
| 2 | Allende INFLUENCE West Germany | -72.25 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 3 | Panama Canal Returned REALIGN Morocco | -85.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 4 | Panama Canal Returned EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | Allende EVENT | -94.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `US/Japan Mutual Defense Pact[27], Red Scare/Purge[31], Brush War[39], Flower Power[62], OPEC[64], Sadat Expels Soviets[73], Alliance for Progress[79], Iranian Hostage Crisis[85], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Iranian Hostage Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], Independent Reds[22], Decolonization[30], Red Scare/Purge[31], Portuguese Empire Crumbles[55], Allende[57], Aldrich Ames Remix[101], Pershing II Deployed[102]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Aldrich Ames Remix EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Pershing II Deployed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `US/Japan Mutual Defense Pact[27], Brush War[39], Flower Power[62], OPEC[64], Sadat Expels Soviets[73], Alliance for Progress[79], Iranian Hostage Crisis[85], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, West Germany | 28.46 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | OPEC INFLUENCE East Germany, West Germany | 28.46 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, West Germany | 28.46 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany | 20.61 | 6.00 | 49.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Flower Power INFLUENCE West Germany | 12.31 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], Independent Reds[22], Decolonization[30], Portuguese Empire Crumbles[55], Allende[57], Aldrich Ames Remix[101], Pershing II Deployed[102]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany | 17.31 | 6.00 | 21.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.29 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 13.46 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 3 | Aldrich Ames Remix INFLUENCE East Germany, West Germany | 13.46 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 4 | Pershing II Deployed INFLUENCE East Germany, West Germany | 13.46 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Allende INFLUENCE West Germany | 5.46 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `US/Japan Mutual Defense Pact[27], Flower Power[62], OPEC[64], Sadat Expels Soviets[73], Alliance for Progress[79], Iranian Hostage Crisis[85], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, West Germany | 26.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, West Germany | 26.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany | 18.90 | 6.00 | 49.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Flower Power INFLUENCE West Germany | 10.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Latin American Debt Crisis INFLUENCE West Germany | 10.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], Decolonization[30], Portuguese Empire Crumbles[55], Allende[57], Aldrich Ames Remix[101], Pershing II Deployed[102]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 11.75 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Aldrich Ames Remix INFLUENCE East Germany, West Germany | 11.75 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Pershing II Deployed INFLUENCE East Germany, West Germany | 11.75 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Allende INFLUENCE West Germany | 3.75 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Arab-Israeli War INFLUENCE West Germany | -0.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `US/Japan Mutual Defense Pact[27], Flower Power[62], Sadat Expels Soviets[73], Alliance for Progress[79], Iranian Hostage Crisis[85], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, West Germany | 24.35 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany | 16.50 | 6.00 | 49.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Flower Power INFLUENCE West Germany | 8.20 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 4 | Latin American Debt Crisis INFLUENCE West Germany | 8.20 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, West Germany | 4.35 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Aldrich Ames Remix [101] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Portuguese Empire Crumbles[55], Allende[57], Aldrich Ames Remix[101], Pershing II Deployed[102]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix INFLUENCE East Germany, West Germany | 9.35 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 2 | Pershing II Deployed INFLUENCE East Germany, West Germany | 9.35 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Allende INFLUENCE West Germany | 1.35 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Arab-Israeli War INFLUENCE West Germany | -2.80 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | Decolonization INFLUENCE West Germany | -2.80 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `US/Japan Mutual Defense Pact[27], Flower Power[62], Sadat Expels Soviets[73], Alliance for Progress[79], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany | 12.90 | 6.00 | 49.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Flower Power INFLUENCE West Germany | 4.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 3 | Latin American Debt Crisis INFLUENCE West Germany | 4.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, West Germany | 0.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Alliance for Progress INFLUENCE East Germany, West Germany | 0.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Portuguese Empire Crumbles[55], Allende[57], Pershing II Deployed[102]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, West Germany | 5.75 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Allende INFLUENCE West Germany | -2.25 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Arab-Israeli War INFLUENCE West Germany | -6.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Decolonization INFLUENCE West Germany | -6.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE West Germany | -6.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Flower Power[62], Sadat Expels Soviets[73], Alliance for Progress[79], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE West Germany | -1.40 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 2 | Latin American Debt Crisis INFLUENCE West Germany | -1.40 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, West Germany | -5.25 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Alliance for Progress INFLUENCE East Germany, West Germany | -5.25 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Sadat Expels Soviets SPACE | -16.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Allende [57] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE West Germany | -8.25 | 6.00 | 21.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany | -12.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Decolonization INFLUENCE West Germany | -12.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE West Germany | -12.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Arab-Israeli War SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Latin American Debt Crisis [98] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Sadat Expels Soviets[73], Alliance for Progress[79], Latin American Debt Crisis[98]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis INFLUENCE West Germany | -40.40 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, West Germany | -44.25 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Alliance for Progress INFLUENCE East Germany, West Germany | -44.25 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Sadat Expels Soviets SPACE | -55.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Alliance for Progress SPACE | -55.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], Portuguese Empire Crumbles[55]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany | -51.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Decolonization INFLUENCE West Germany | -51.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany | -51.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Arab-Israeli War SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Decolonization SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Sadat Expels Soviets[73], Alliance for Progress[79]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, West Germany | -80.25 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, West Germany | -80.25 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | Sadat Expels Soviets SPACE | -91.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Alliance for Progress SPACE | -91.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 5 | Sadat Expels Soviets EVENT | -105.45 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Decolonization[30], Portuguese Empire Crumbles[55]`
- state: `VP -6, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany | -87.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany | -87.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | Decolonization SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Portuguese Empire Crumbles SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 5 | Decolonization EVENT | -105.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Socialist Governments[7], Arab-Israeli War[13], The Cambridge Five[36], How I Learned to Stop Worrying[49], Junta[50], Missile Envy[52], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -6, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], Suez Crisis[28], Nuclear Test Ban[34], Willy Brandt[58], Flower Power[62], OAS Founded[71], Voice of America[75], Liberation Theology[76], Che[83]`
- state: `VP -6, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Arab-Israeli War[13], The Cambridge Five[36], How I Learned to Stop Worrying[49], Junta[50], Missile Envy[52], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | The Cambridge Five INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Junta INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Missile Envy INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], Suez Crisis[28], Willy Brandt[58], Flower Power[62], OAS Founded[71], Voice of America[75], Liberation Theology[76], Che[83]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 32.47 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 2 | Voice of America INFLUENCE East Germany, West Germany | 32.47 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 3 | Suez Crisis INFLUENCE East Germany, France, West Germany | 28.62 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 4 | Che INFLUENCE East Germany, France, West Germany | 28.62 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 16.47 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `The Cambridge Five[36], How I Learned to Stop Worrying[49], Junta[50], Missile Envy[52], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Junta INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Missile Envy INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 9.57 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Suez Crisis[28], Willy Brandt[58], Flower Power[62], OAS Founded[71], Voice of America[75], Liberation Theology[76], Che[83]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 30.57 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.33 |
| 2 | Suez Crisis INFLUENCE East Germany, France, West Germany | 26.72 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 26.72 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Willy Brandt INFLUENCE East Germany, West Germany | 14.57 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Flower Power INFLUENCE East Germany, West Germany | 14.57 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `How I Learned to Stop Worrying[49], Junta[50], Missile Envy[52], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Junta INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Missile Envy INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Lone Gunman INFLUENCE West Germany | 6.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Suez Crisis[28], Willy Brandt[58], Flower Power[62], OAS Founded[71], Liberation Theology[76], Che[83]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Flower Power INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Junta[50], Missile Envy[52], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Missile Envy INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 2.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Lone Gunman INFLUENCE West Germany | 2.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | Lonely Hearts Club Band SPACE | -12.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Willy Brandt[58], Flower Power[62], OAS Founded[71], Liberation Theology[76], Che[83]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 20.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Willy Brandt INFLUENCE East Germany, West Germany | 7.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 7.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Liberation Theology INFLUENCE East Germany, West Germany | 7.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | OAS Founded INFLUENCE West Germany | 7.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Missile Envy[52], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 12.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | -3.77 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Lone Gunman INFLUENCE West Germany | -3.92 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 4 | Lonely Hearts Club Band SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 5 | Lone Gunman REALIGN East Germany | -22.85 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Willy Brandt[58], Flower Power[62], OAS Founded[71], Liberation Theology[76]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 1.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Flower Power INFLUENCE East Germany, West Germany | 1.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 1.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | OAS Founded INFLUENCE West Germany | 1.08 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:26.67 |
| 5 | Willy Brandt SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | -47.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Lone Gunman INFLUENCE West Germany | -47.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:70.00 |
| 3 | Lonely Hearts Club Band SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 4 | Lone Gunman REALIGN East Germany | -66.19 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |
| 5 | Lone Gunman EVENT | -67.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Flower Power[62], OAS Founded[71], Liberation Theology[76]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | -42.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | -42.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | OAS Founded INFLUENCE West Germany | -42.25 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:70.00 |
| 4 | Flower Power SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | Liberation Theology SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Lone Gunman[109]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE West Germany | -87.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 2 | Lone Gunman REALIGN East Germany | -106.19 | -1.00 | 4.96 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 3 | Lone Gunman EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `OAS Founded[71], Liberation Theology[76]`
- state: `VP -9, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | -82.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | OAS Founded INFLUENCE West Germany | -82.25 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:110.00 |
| 3 | Liberation Theology SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | OAS Founded REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | OAS Founded EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP -6, DEFCON +0, MilOps U+0/A+0`
