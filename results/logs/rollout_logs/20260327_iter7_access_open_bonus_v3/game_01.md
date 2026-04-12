# minimal_hybrid detailed rollout log

- seed: `20260520`
- winner: `US`
- final_vp: `-1`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Romanian Abdication[12], Warsaw Pact Formed[16], Captured Nazi Scientist[18], NATO[21], Independent Reds[22], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Five Year Plan[5], Socialist Governments[7], COMECON[14], De Gaulle Leads France[17], Truman Doctrine[19], Suez Crisis[28], Red Scare/Purge[31], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Romanian Abdication[12], Captured Nazi Scientist[18], NATO[21], Independent Reds[22], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Iran | 71.48 | 4.00 | 67.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Romanian Abdication COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Captured Nazi Scientist COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | UN Intervention COUP Iran | 66.13 | 4.00 | 62.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | NATO COUP Iran | 58.18 | 4.00 | 78.78 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Five Year Plan[5], Socialist Governments[7], COMECON[14], De Gaulle Leads France[17], Truman Doctrine[19], Suez Crisis[28], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | NORAD INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | Socialist Governments INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | COMECON INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | De Gaulle Leads France INFLUENCE North Korea, Indonesia, Philippines | 42.07 | 6.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], NATO[21], Independent Reds[22], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | UN Intervention COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | NATO INFLUENCE Japan, North Korea, Thailand | 42.55 | 6.00 | 61.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | US/Japan Mutual Defense Pact INFLUENCE Japan, North Korea, Thailand | 42.55 | 6.00 | 61.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Socialist Governments[7], COMECON[14], De Gaulle Leads France[17], Truman Doctrine[19], Suez Crisis[28], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, Turkey | 55.50 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, non_coup_milops_penalty:1.60 |
| 2 | Socialist Governments INFLUENCE East Germany, France, Turkey | 35.50 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | COMECON INFLUENCE East Germany, France, Turkey | 35.50 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, France, Turkey | 35.50 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 5 | Suez Crisis INFLUENCE East Germany, France, Turkey | 35.50 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, offside_ops_penalty, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], NATO[21], Independent Reds[22], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Japan, North Korea, Thailand | 42.55 | 6.00 | 61.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Japan, North Korea, Thailand | 42.55 | 6.00 | 61.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 4 | UN Intervention INFLUENCE Thailand | 28.30 | 6.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, access_touch:Thailand |
| 5 | Independent Reds INFLUENCE Thailand | 12.15 | 6.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Socialist Governments[7], COMECON[14], De Gaulle Leads France[17], Truman Doctrine[19], Suez Crisis[28]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Italy, Japan, Panama | 32.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | COMECON INFLUENCE Italy, Japan, Panama | 32.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | De Gaulle Leads France INFLUENCE Italy, Japan, Panama | 32.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Suez Crisis INFLUENCE Italy, Japan, Panama | 32.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Truman Doctrine COUP Syria | 22.80 | 4.00 | 18.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], US/Japan Mutual Defense Pact[27], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, South Korea, Thailand | 42.05 | 6.00 | 60.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 3 | UN Intervention INFLUENCE Thailand | 31.30 | 6.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, control_break:Thailand |
| 4 | Independent Reds INFLUENCE Thailand | 15.15 | 6.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `COMECON[14], De Gaulle Leads France[17], Truman Doctrine[19], Suez Crisis[28]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, West Germany, Japan | 39.13 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | De Gaulle Leads France INFLUENCE Italy, West Germany, Japan | 39.13 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Suez Crisis INFLUENCE Italy, West Germany, Japan | 39.13 | 6.00 | 56.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Truman Doctrine INFLUENCE West Germany | 23.83 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:2.67 |
| 5 | Truman Doctrine COUP Syria | 22.97 | 4.00 | 19.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Independent Reds INFLUENCE Thailand | 10.15 | 6.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 4 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], Suez Crisis[28]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, Egypt | 26.05 | 6.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, Egypt | 26.05 | 6.00 | 47.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Truman Doctrine COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Truman Doctrine INFLUENCE Japan | 15.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:7.00 |
| 5 | De Gaulle Leads France COUP Syria | 14.00 | 4.00 | 30.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china`
- hand: `Independent Reds[22], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Independent Reds INFLUENCE Thailand | 10.15 | 6.00 | 20.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Thailand:20.45, offside_ops_penalty |
| 3 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | Independent Reds SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | UN Intervention REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Truman Doctrine[19], Suez Crisis[28]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Japan, Egypt, Libya | 30.10 | 6.00 | 55.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Truman Doctrine COUP Syria | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine INFLUENCE Japan | 16.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:11.00 |
| 4 | Suez Crisis COUP Syria | 15.00 | 4.00 | 31.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Lebanon | 12.70 | 4.00 | 8.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Fidel[8], Vietnam Revolts[9], Blockade[10], Nasser[15], Containment[25], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], Olympic Games[20], CIA Created[26], East European Unrest[29], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Fidel[8], Vietnam Revolts[9], Blockade[10], Nasser[15], Containment[25], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Israel, Thailand | 40.38 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | Vietnam Revolts INFLUENCE Israel, Thailand | 40.38 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Fidel COUP Italy | 38.57 | 4.00 | 34.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 4 | Fidel COUP Philippines | 38.57 | 4.00 | 34.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 5 | Vietnam Revolts COUP Italy | 38.57 | 4.00 | 34.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], Olympic Games[20], CIA Created[26], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Libya | 37.88 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:2.67 |
| 2 | Formosan Resolution INFLUENCE Japan, Libya | 37.88 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:2.67 |
| 3 | De-Stalinization INFLUENCE West Germany, Japan, Libya | 33.38 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Olympic Games COUP Syria | 29.32 | 4.00 | 25.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 5 | Formosan Resolution COUP Syria | 29.32 | 4.00 | 25.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Blockade[10], Nasser[15], Containment[25], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Italy, Thailand | 39.40 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:3.20 |
| 2 | Vietnam Revolts COUP Italy | 38.70 | 4.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 3 | Vietnam Revolts COUP Philippines | 38.70 | 4.00 | 35.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 4 | Vietnam Revolts COUP Egypt | 37.95 | 4.00 | 34.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Vietnam Revolts COUP Turkey | 36.70 | 4.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Turkey, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Italy, Japan | 38.10 | 6.00 | 35.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, non_coup_milops_penalty:3.20 |
| 2 | De-Stalinization INFLUENCE Italy, West Germany, Japan | 33.60 | 6.00 | 51.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Formosan Resolution COUP Italy | 31.70 | 4.00 | 28.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.40, expected_swing:1.5 |
| 4 | Formosan Resolution COUP Syria | 29.45 | 4.00 | 25.75 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 5 | Formosan Resolution COUP Indonesia | 27.10 | 4.00 | 23.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Containment[25], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE Saudi Arabia, Philippines, Thailand | 34.75 | 6.00 | 53.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Blockade COUP Philippines | 32.55 | 4.00 | 28.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Philippines | 32.55 | 4.00 | 28.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 5 | Blockade COUP Egypt | 31.80 | 4.00 | 27.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan, Philippines | 32.80 | 6.00 | 51.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | CIA Created COUP Italy | 25.55 | 4.00 | 21.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Italy, battleground_coup, milops_need:2, milops_urgency:0.50, expected_swing:0.5 |
| 3 | CIA Created COUP Philippines | 25.55 | 4.00 | 21.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.50, expected_swing:0.5 |
| 4 | CIA Created COUP Japan | 24.50 | 4.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:0.50 |
| 5 | CIA Created COUP West Germany | 24.00 | 4.00 | 20.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:2, milops_urgency:0.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Nasser[15], Containment[25], Special Relationship[37]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Indonesia | 43.28 | 4.00 | 39.43 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 2 | Nasser COUP Indonesia | 43.28 | 4.00 | 39.43 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 3 | Containment COUP Indonesia | 34.98 | 4.00 | 51.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Special Relationship COUP Indonesia | 33.63 | 4.00 | 45.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Containment INFLUENCE Japan, Indonesia, Thailand | 32.67 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 24: T2 AR4 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], CIA Created[26], Decolonization[30], The Cambridge Five[36]`
- state: `VP 4, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Indonesia | 43.28 | 4.00 | 39.43 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5 |
| 2 | Arab-Israeli War COUP Indonesia | 33.63 | 4.00 | 45.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP Indonesia | 33.63 | 4.00 | 45.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Indonesia | 33.63 | 4.00 | 45.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Philippines | 25.88 | 4.00 | 22.03 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.67, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 25: T2 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], Containment[25], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Indonesia, Thailand | 31.00 | 6.00 | 52.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Nasser COUP Egypt | 25.80 | 4.00 | 21.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Nasser INFLUENCE Thailand | 19.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 19.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Nasser COUP Israel | 17.25 | 4.00 | 13.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30], The Cambridge Five[36]`
- state: `VP 4, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Indonesia | 17.70 | 6.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Decolonization INFLUENCE Japan, Indonesia | 17.70 | 6.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | The Cambridge Five INFLUENCE Japan, Indonesia | 17.70 | 6.00 | 35.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Arab-Israeli War COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Decolonization COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Special Relationship[37]`
- state: `VP 4, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Egypt | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Nasser COUP Israel | 18.25 | 4.00 | 14.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |
| 3 | Special Relationship COUP Egypt | 16.15 | 4.00 | 28.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Nasser INFLUENCE Thailand | 15.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 5 | Special Relationship INFLUENCE Japan, Thailand | 15.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36]`
- state: `VP 4, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Japan | 10.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, Japan | 10.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | Decolonization COUP SE African States | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Sudan | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Decolonization COUP Zimbabwe | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], NATO[21], Marshall Plan[23], Indo-Pakistani War[24], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Olympic Games[20], Suez Crisis[28], East European Unrest[29], Decolonization[30]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], NATO[21], Marshall Plan[23], Indo-Pakistani War[24], The Cambridge Five[36]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Japan, Egypt, Iran, Thailand | 45.40 | 6.00 | 68.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Marshall Plan INFLUENCE Japan, Egypt, Iran, Thailand | 45.40 | 6.00 | 68.00 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Iran:13.70, access_touch:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Indo-Pakistani War COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 5 | Indo-Pakistani War INFLUENCE Japan, Thailand | 38.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Olympic Games[20], Suez Crisis[28], East European Unrest[29], Decolonization[30]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan, Egypt | 52.05 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:4.00 |
| 2 | East European Unrest COUP Indonesia | 48.65 | 4.00 | 45.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:4.5 |
| 3 | Olympic Games COUP Indonesia | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:3.5 |
| 4 | East European Unrest COUP Philippines | 38.25 | 4.00 | 34.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 5 | East European Unrest COUP Egypt | 37.50 | 4.00 | 33.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Marshall Plan[23], Indo-Pakistani War[24], The Cambridge Five[36]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, Pakistan, Iran, Thailand | 48.85 | 6.00 | 72.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Indo-Pakistani War COUP Indonesia | 42.50 | 4.00 | 38.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 3 | The Cambridge Five COUP Indonesia | 42.50 | 4.00 | 38.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 4 | Indo-Pakistani War INFLUENCE Iran, Thailand | 40.05 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 5 | The Cambridge Five INFLUENCE Iran, Thailand | 40.05 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:3`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Olympic Games[20], Suez Crisis[28], Decolonization[30]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 42.50 | 4.00 | 38.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:3.5 |
| 2 | Olympic Games INFLUENCE West Germany, Japan | 32.70 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:4.80 |
| 3 | Olympic Games COUP Philippines | 32.10 | 4.00 | 28.40 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:1.5 |
| 4 | Olympic Games COUP Egypt | 31.35 | 4.00 | 27.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, expected_swing:1.5 |
| 5 | Olympic Games COUP Syria | 29.85 | 4.00 | 26.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 35: T3 AR3 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Indo-Pakistani War[24], The Cambridge Five[36]`
- state: `VP 5, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Pakistan, Thailand | 40.10 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | The Cambridge Five INFLUENCE Pakistan, Thailand | 40.10 | 6.00 | 40.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Indo-Pakistani War COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | The Cambridge Five COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Blockade COUP Libya | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], De Gaulle Leads France[17], Suez Crisis[28], Decolonization[30]`
- state: `VP 5, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 30.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, North Korea | 30.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Korean War INFLUENCE West Germany, Japan | 19.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Arab-Israeli War INFLUENCE West Germany, Japan | 19.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Decolonization INFLUENCE West Germany, Japan | 19.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 5, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE North Korea, Thailand | 38.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | The Cambridge Five COUP Libya | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Blockade COUP Libya | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Libya | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | The Cambridge Five COUP Egypt | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Suez Crisis[28], Decolonization[30]`
- state: `VP 5, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, North Korea | 30.23 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Korean War INFLUENCE West Germany, Japan | 18.83 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 3 | Arab-Israeli War INFLUENCE West Germany, Japan | 18.83 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Decolonization INFLUENCE West Germany, Japan | 18.83 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Suez Crisis COUP Syria | 13.67 | 4.00 | 30.12 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19]`
- state: `VP 5, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Libya | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Libya | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Blockade COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Egypt | 20.80 | 4.00 | 16.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Blockade COUP Israel | 19.25 | 4.00 | 15.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 40: T3 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Decolonization[30]`
- state: `VP 5, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Libya | 14.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Arab-Israeli War INFLUENCE Japan, Libya | 14.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Decolonization INFLUENCE Japan, Libya | 14.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Korean War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Arab-Israeli War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19]`
- state: `VP 5, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Sudan | 12.45 | 4.00 | 8.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist INFLUENCE North Korea | 4.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:22.00 |
| 3 | Truman Doctrine COUP Sudan | 0.45 | 4.00 | 8.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Truman Doctrine INFLUENCE North Korea | -7.60 | 6.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 5 | Captured Nazi Scientist REALIGN Cuba | -18.66 | -1.00 | 4.49 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30]`
- state: `VP 5, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Libya | 13.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Decolonization INFLUENCE Japan, Libya | 13.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | Arab-Israeli War COUP SE African States | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Sudan | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | -0.20 | 4.00 | 12.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 43: T4 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Decolonization[30], De-Stalinization[33], Formosan Resolution[35], Special Relationship[37], Arms Race[42], SALT Negotiations[46], Flower Power[62], Sadat Expels Soviets[73]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Flower Power EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Blockade[10], Korean War[11], COMECON[14], East European Unrest[29], UN Intervention[32], Cuban Missile Crisis[43], Nixon Plays the China Card[72], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Decolonization[30], Formosan Resolution[35], Special Relationship[37], Arms Race[42], SALT Negotiations[46], Flower Power[62], Sadat Expels Soviets[73]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, Ethiopia, Nigeria | 62.73 | 6.00 | 61.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.57 |
| 2 | SALT Negotiations INFLUENCE East Germany, Ethiopia, Nigeria | 62.73 | 6.00 | 61.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.57 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, Ethiopia, Nigeria | 42.73 | 6.00 | 61.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | Decolonization INFLUENCE Ethiopia, Nigeria | 42.33 | 6.00 | 41.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.57 |
| 5 | Flower Power INFLUENCE Ethiopia, Nigeria | 42.33 | 6.00 | 41.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Korean War[11], COMECON[14], East European Unrest[29], UN Intervention[32], Cuban Missile Crisis[43], Nixon Plays the China Card[72], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Mexico, Algeria, South Africa | 50.93 | 6.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | Cuban Missile Crisis INFLUENCE Mexico, Algeria, South Africa | 50.93 | 6.00 | 49.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | Nixon Plays the China Card INFLUENCE Mexico, South Africa | 34.88 | 6.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 4 | COMECON INFLUENCE Mexico, Algeria, South Africa | 30.93 | 6.00 | 49.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | East European Unrest COUP Colombia | 25.04 | 4.00 | 21.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.57, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Decolonization[30], Formosan Resolution[35], Special Relationship[37], SALT Negotiations[46], Flower Power[62], Sadat Expels Soviets[73]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE North Korea, Iraq, Chile | 56.62 | 6.00 | 56.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Iraq:13.80, control_break:Iraq, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:5.33 |
| 2 | Decolonization INFLUENCE North Korea, Iraq | 37.97 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Iraq:13.80, control_break:Iraq, non_coup_milops_penalty:5.33 |
| 3 | Flower Power INFLUENCE North Korea, Iraq | 37.97 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Iraq:13.80, control_break:Iraq, non_coup_milops_penalty:5.33 |
| 4 | Sadat Expels Soviets INFLUENCE North Korea, Iraq, Chile | 36.62 | 6.00 | 56.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:13.80, control_break:North Korea, influence:Iraq:13.80, control_break:Iraq, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | SALT Negotiations COUP Cameroon | 25.23 | 4.00 | 21.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:0.67, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Korean War[11], COMECON[14], UN Intervention[32], Cuban Missile Crisis[43], Nixon Plays the China Card[72], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE Mexico, Algeria, South Africa | 61.17 | 6.00 | 60.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | Nixon Plays the China Card INFLUENCE Mexico, South Africa | 42.12 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | COMECON INFLUENCE Mexico, Algeria, South Africa | 41.17 | 6.00 | 60.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Korean War INFLUENCE Mexico, South Africa | 26.12 | 6.00 | 41.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Colonial Rear Guards INFLUENCE Mexico, South Africa | 26.12 | 6.00 | 41.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Decolonization[30], Formosan Resolution[35], Special Relationship[37], Flower Power[62], Sadat Expels Soviets[73]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Pakistan, Argentina | 35.70 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:6.40 |
| 2 | Flower Power INFLUENCE Pakistan, Argentina | 35.70 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Argentina:16.20, access_touch:Argentina, non_coup_milops_penalty:6.40 |
| 3 | Sadat Expels Soviets INFLUENCE Pakistan, Mexico, Argentina | 32.50 | 6.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, access_touch:Argentina, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Formosan Resolution INFLUENCE Pakistan, Argentina | 19.70 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Argentina:16.20, access_touch:Argentina, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Special Relationship INFLUENCE Pakistan, Argentina | 19.70 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:13.20, control_break:Pakistan, influence:Argentina:16.20, access_touch:Argentina, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Korean War[11], COMECON[14], UN Intervention[32], Nixon Plays the China Card[72], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE Morocco, South Africa | 32.90 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 2 | COMECON INFLUENCE West Germany, Morocco, South Africa | 28.90 | 6.00 | 49.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Nixon Plays the China Card COUP Colombia | 19.15 | 4.00 | 15.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 4 | Nixon Plays the China Card COUP Saharan States | 19.15 | 4.00 | 15.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | Nixon Plays the China Card COUP SE African States | 19.15 | 4.00 | 15.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Formosan Resolution[35], Special Relationship[37], Flower Power[62], Sadat Expels Soviets[73]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE Mexico, Argentina | 35.85 | 6.00 | 38.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:8.00 |
| 2 | Sadat Expels Soviets INFLUENCE Mexico, Argentina, Chile | 32.50 | 6.00 | 54.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Formosan Resolution INFLUENCE Mexico, Argentina | 19.85 | 6.00 | 38.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Special Relationship INFLUENCE Mexico, Argentina | 19.85 | 6.00 | 38.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Flower Power COUP Cameroon | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Korean War[11], COMECON[14], UN Intervention[32], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Mexico, South Africa | 30.45 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Korean War INFLUENCE Mexico, South Africa | 18.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Colonial Rear Guards INFLUENCE Mexico, South Africa | 18.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | UN Intervention INFLUENCE Mexico | 17.80 | 6.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:8.00 |
| 5 | UN Intervention COUP Colombia | 13.20 | 4.00 | 9.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Formosan Resolution[35], Special Relationship[37], Sadat Expels Soviets[73]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE Argentina, Brazil, Chile | 24.08 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 2 | Blockade COUP Cameroon | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Blockade COUP SE African States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP Sudan | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Korean War[11], UN Intervention[32], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Colombia | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP SE African States | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Sudan | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Zimbabwe | 13.87 | 4.00 | 10.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 55: T4 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 2, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Colombia | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Formosan Resolution COUP Colombia | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Special Relationship COUP Colombia | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Blockade COUP Cameroon | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 56: T4 AR6 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Korean War COUP Saharan States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP SE African States | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Sudan | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Korean War COUP Zimbabwe | 4.55 | 4.00 | 16.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37]`
- state: `VP 2, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Special Relationship COUP Colombia | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 58: T4 AR7 US

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Sudan | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP Zimbabwe | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `U2 Incident [63] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Portuguese Empire Crumbles[55], U2 Incident[63], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], Olympic Games[20], NATO[21], Suez Crisis[28], Cultural Revolution[61], Lonely Hearts Club Band[65], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78], One Small Step[81]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Brazil, Chile | 40.99 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 2 | Portuguese Empire Crumbles INFLUENCE Brazil, Chile | 40.99 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 3 | One Small Step INFLUENCE Brazil, Chile | 40.99 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:5.71 |
| 4 | Indo-Pakistani War COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 5 | Portuguese Empire Crumbles COUP Colombia | 40.98 | 4.00 | 37.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], Olympic Games[20], Suez Crisis[28], Cultural Revolution[61], Lonely Hearts Club Band[65], Ussuri River Skirmish[77], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE Brazil, Venezuela, South Africa | 49.04 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 2 | Ussuri River Skirmish COUP Brazil | 39.43 | 4.00 | 35.88 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Ussuri River Skirmish COUP Syria | 35.93 | 4.00 | 32.38 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 4 | Ussuri River Skirmish COUP Mexico | 33.18 | 4.00 | 29.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 5 | Olympic Games COUP Brazil | 33.08 | 4.00 | 29.38 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Nasser[15], Truman Doctrine[19], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78], One Small Step[81]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Colombia | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Colombia | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 3 | Portuguese Empire Crumbles INFLUENCE Brazil, Chile | 35.03 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:6.67 |
| 4 | One Small Step INFLUENCE Brazil, Chile | 35.03 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:6.67 |
| 5 | Nasser COUP Colombia | 34.87 | 4.00 | 31.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 64: T5 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], Olympic Games[20], Suez Crisis[28], Cultural Revolution[61], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Argentina, Venezuela | 36.43 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 2 | Lonely Hearts Club Band INFLUENCE Argentina, Venezuela | 36.43 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.67 |
| 3 | Olympic Games COUP Argentina | 35.32 | 4.00 | 31.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Lonely Hearts Club Band COUP Argentina | 35.32 | 4.00 | 31.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Socialist Governments INFLUENCE Argentina, Venezuela, South Africa | 33.08 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Nasser[15], Truman Doctrine[19], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78], One Small Step[81]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE Brazil, Chile | 36.90 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:4.80 |
| 2 | Five Year Plan INFLUENCE Argentina, Brazil, Chile | 32.95 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Brazil, Chile | 32.95 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | One Small Step COUP Venezuela | 32.85 | 4.00 | 29.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | One Small Step COUP Algeria | 32.85 | 4.00 | 29.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Fidel[8], Suez Crisis[28], Cultural Revolution[61], Lonely Hearts Club Band[65], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE Chile, South Africa | 33.30 | 6.00 | 35.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Lonely Hearts Club Band COUP Bolivia | 31.15 | 4.00 | 27.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 3 | Lonely Hearts Club Band COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 4 | Socialist Governments INFLUENCE Argentina, Chile, South Africa | 29.35 | 6.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 29.35 | 6.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Nasser[15], Truman Doctrine[19], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Argentina, Chile, Venezuela | 28.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Chile, Venezuela | 28.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Nasser COUP Venezuela | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Algeria | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Nasser COUP Libya | 25.80 | 4.00 | 21.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Suez Crisis[28], Cultural Revolution[61], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Chile, Venezuela, South Africa | 28.35 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Suez Crisis INFLUENCE Chile, Venezuela, South Africa | 28.35 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Cultural Revolution INFLUENCE Chile, Venezuela, South Africa | 28.35 | 6.00 | 52.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Socialist Governments COUP Bolivia | 18.00 | 4.00 | 34.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Suez Crisis COUP Bolivia | 18.00 | 4.00 | 34.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Truman Doctrine[19], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Algeria | 27.30 | 4.00 | 23.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Chile, Algeria | 26.75 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Nasser COUP Libya | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Argentina | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Nasser COUP Mexico | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Suez Crisis[28], Cultural Revolution[61], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 22.02 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 2 | Cultural Revolution INFLUENCE Argentina, Chile, South Africa | 22.02 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Suez Crisis COUP Bolivia | 18.83 | 4.00 | 35.28 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Cultural Revolution COUP Bolivia | 18.83 | 4.00 | 35.28 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Fidel COUP Bolivia | 16.48 | 4.00 | 28.78 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE Argentina, Chile, Algeria | 18.75 | 6.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 2 | Ask Not What Your Country Can Do For You COUP Colombia | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Ask Not What Your Country Can Do For You COUP Cameroon | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Ask Not What Your Country Can Do For You COUP Saharan States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Ask Not What Your Country Can Do For You COUP SE African States | 6.90 | 4.00 | 23.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Cultural Revolution [61] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Cultural Revolution[61], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Bolivia | 20.50 | 4.00 | 36.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Fidel COUP Bolivia | 18.15 | 4.00 | 30.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Bolivia | 15.80 | 4.00 | 23.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Bolivia, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Cultural Revolution COUP Colombia | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Cultural Revolution COUP Saharan States | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 73: T5 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Bolivia | 19.15 | 4.00 | 31.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Bolivia | 16.80 | 4.00 | 24.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Bolivia, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Bolivia | 17.15 | 4.00 | 29.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Lone Gunman COUP Bolivia | 14.80 | 4.00 | 22.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Bolivia, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Fidel COUP Colombia | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Fidel COUP Saharan States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Fidel COUP SE African States | 5.55 | 4.00 | 17.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `De Gaulle Leads France[17], NATO[21], Marshall Plan[23], CIA Created[26], Nuclear Test Ban[34], Kitchen Debates[51], Alliance for Progress[79], Che[83], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Olympic Games [20] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Suez Crisis[28], Decolonization[30], Quagmire[45], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `De Gaulle Leads France[17], NATO[21], Marshall Plan[23], CIA Created[26], Kitchen Debates[51], Alliance for Progress[79], Che[83], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Indonesia | 54.61 | 4.00 | 51.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 2 | Che COUP Indonesia | 54.61 | 4.00 | 51.06 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 3 | De Gaulle Leads France INFLUENCE Chile, Algeria, Morocco | 51.49 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.86 |
| 4 | Che INFLUENCE Chile, Algeria, Morocco | 51.49 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:6.86 |
| 5 | De Gaulle Leads France COUP Libya | 44.71 | 4.00 | 41.16 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 78: T6 AR1 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], Decolonization[30], Quagmire[45], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Algeria | 39.36 | 4.00 | 35.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |
| 2 | John Paul II Elected Pope COUP Algeria | 39.36 | 4.00 | 35.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |
| 3 | Voice of America COUP Algeria | 39.36 | 4.00 | 35.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:1.5 |
| 4 | Independent Reds COUP Argentina | 34.36 | 4.00 | 30.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:1.5 |
| 5 | John Paul II Elected Pope COUP Argentina | 34.36 | 4.00 | 30.66 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 79: T6 AR2 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `NATO[21], Marshall Plan[23], CIA Created[26], Kitchen Debates[51], Alliance for Progress[79], Che[83], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE Argentina, Chile, Algeria | 50.75 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 2 | NATO INFLUENCE UK, Argentina, Chile, Algeria | 42.75 | 6.00 | 65.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Marshall Plan INFLUENCE UK, Argentina, Chile, Algeria | 42.75 | 6.00 | 65.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Che COUP Algeria | 39.00 | 4.00 | 35.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Che COUP Libya | 38.00 | 4.00 | 34.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Suez Crisis[28], Decolonization[30], Quagmire[45], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 2 | Voice of America INFLUENCE Chile, South Africa | 33.97 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 3 | John Paul II Elected Pope COUP Bolivia | 30.48 | 4.00 | 26.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 4 | Voice of America COUP Bolivia | 30.48 | 4.00 | 26.78 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 5 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 30.02 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `NATO[21], Marshall Plan[23], CIA Created[26], Kitchen Debates[51], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE UK, Argentina, Chile, Morocco | 42.55 | 6.00 | 65.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Marshall Plan INFLUENCE UK, Argentina, Chile, Morocco | 42.55 | 6.00 | 65.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Alliance for Progress INFLUENCE Argentina, Chile, Morocco | 30.55 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | NATO COUP Libya | 19.55 | 4.00 | 40.15 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Marshall Plan COUP Libya | 19.55 | 4.00 | 40.15 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Suez Crisis[28], Decolonization[30], Quagmire[45], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE UK, Chile | 35.25 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Chile:16.80, non_coup_milops_penalty:6.40 |
| 2 | Suez Crisis INFLUENCE UK, Chile, South Africa | 31.90 | 6.00 | 52.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Quagmire INFLUENCE UK, Chile, South Africa | 31.90 | 6.00 | 52.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 4 | Voice of America COUP Bolivia | 30.75 | 4.00 | 27.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Bolivia, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |
| 5 | Voice of America COUP Syria | 29.75 | 4.00 | 26.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Marshall Plan[23], CIA Created[26], Kitchen Debates[51], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, India, Argentina, Chile | 40.35 | 6.00 | 64.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:India:13.80, access_touch:India, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Alliance for Progress INFLUENCE West Germany, Argentina, Chile | 28.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Marshall Plan COUP Libya | 19.85 | 4.00 | 40.45 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Libya | 18.50 | 4.00 | 34.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Our Man in Tehran INFLUENCE Argentina, Chile | 16.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Suez Crisis[28], Decolonization[30], Quagmire[45]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Argentina, Chile, South Africa | 27.35 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Quagmire INFLUENCE Argentina, Chile, South Africa | 27.35 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Captured Nazi Scientist COUP Bolivia | 24.80 | 4.00 | 20.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Bolivia, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Argentina | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE West Germany, Argentina, Chile | 26.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Alliance for Progress COUP Libya | 19.00 | 4.00 | 35.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Libya | 16.65 | 4.00 | 28.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Alliance for Progress COUP Argentina | 15.00 | 4.00 | 31.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |
| 5 | Our Man in Tehran INFLUENCE Argentina, Chile | 14.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:4`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Decolonization[30], Quagmire[45]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Bolivia | 25.47 | 4.00 | 21.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Bolivia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 2 | Quagmire INFLUENCE Argentina, Chile, South Africa | 24.68 | 6.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Captured Nazi Scientist COUP Syria | 24.47 | 4.00 | 20.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Argentina | 22.97 | 4.00 | 19.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Mexico | 21.72 | 4.00 | 17.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Libya | 17.65 | 4.00 | 29.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | CIA Created COUP Libya | 15.30 | 4.00 | 23.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Kitchen Debates COUP Libya | 15.30 | 4.00 | 23.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Our Man in Tehran COUP Argentina | 13.65 | 4.00 | 25.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Our Man in Tehran COUP Mexico | 12.40 | 4.00 | 24.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Decolonization[30], Quagmire[45]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE Libya, Chile, South Africa | 9.35 | 6.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:28.00 |
| 2 | Quagmire COUP Colombia | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Quagmire COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP SE African States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Sudan | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Colombia | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created COUP Cameroon | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | CIA Created COUP Saharan States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | CIA Created COUP SE African States | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | CIA Created COUP Sudan | 5.20 | 4.00 | 13.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Vietnam Revolts[9], Decolonization[30]`
- state: `VP 2, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Colombia | 31.55 | 4.00 | 43.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP SE African States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Sudan | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Marshall Plan[23], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], How I Learned to Stop Worrying[49], Missile Envy[52], Allende[57], Muslim Revolution[59]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], Indo-Pakistani War[24], East European Unrest[29], NORAD[38], Bear Trap[47], ABM Treaty[60], Camp David Accords[66]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Marshall Plan[23], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], How I Learned to Stop Worrying[49], Missile Envy[52], Allende[57]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Indonesia | 48.55 | 4.00 | 44.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | The Cambridge Five COUP Indonesia | 48.55 | 4.00 | 44.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Indonesia | 48.55 | 4.00 | 44.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Missile Envy COUP Indonesia | 48.55 | 4.00 | 44.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Romanian Abdication COUP Indonesia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 94: T7 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], Indo-Pakistani War[24], East European Unrest[29], NORAD[38], Bear Trap[47], Camp David Accords[66]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Chile, South Africa, Indonesia | 50.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 2 | NORAD INFLUENCE Chile, South Africa, Indonesia | 50.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 3 | Bear Trap INFLUENCE Chile, South Africa, Indonesia | 50.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:8.00 |
| 4 | East European Unrest COUP Colombia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | NORAD COUP Colombia | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], Marshall Plan[23], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], How I Learned to Stop Worrying[49], Missile Envy[52], Allende[57]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Egypt, Panama, Argentina, Chile | 47.88 | 6.00 | 73.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Egypt:13.20, control_break:Egypt, influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Egypt, Panama, Argentina, Chile | 47.88 | 6.00 | 73.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Egypt:13.20, control_break:Egypt, influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.67 |
| 3 | The Cambridge Five INFLUENCE Egypt, Chile | 39.03 | 6.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.20, control_break:Egypt, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:6.67 |
| 4 | How I Learned to Stop Worrying INFLUENCE Egypt, Chile | 39.03 | 6.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.20, control_break:Egypt, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:6.67 |
| 5 | Missile Envy INFLUENCE Egypt, Chile | 39.03 | 6.00 | 40.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Egypt:13.20, control_break:Egypt, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], Indo-Pakistani War[24], NORAD[38], Bear Trap[47], Camp David Accords[66]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Panama, Chile, South Africa | 49.77 | 6.00 | 53.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 2 | Bear Trap INFLUENCE Panama, Chile, South Africa | 49.77 | 6.00 | 53.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.33 |
| 3 | NORAD COUP Colombia | 48.23 | 4.00 | 44.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 4 | Bear Trap COUP Colombia | 48.23 | 4.00 | 44.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 5 | Indo-Pakistani War COUP Colombia | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Romanian Abdication[12], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], How I Learned to Stop Worrying[49], Missile Envy[52], Allende[57]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, West Germany, Argentina, Chile | 43.10 | 6.00 | 69.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | The Cambridge Five INFLUENCE Argentina, Chile | 35.70 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.00 |
| 3 | How I Learned to Stop Worrying INFLUENCE Argentina, Chile | 35.70 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.00 |
| 4 | Missile Envy INFLUENCE Argentina, Chile | 35.70 | 6.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.00 |
| 5 | The Cambridge Five COUP Argentina | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Bear Trap [47] as COUP`
- flags: `milops_shortfall:7`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], Indo-Pakistani War[24], Bear Trap[47], Camp David Accords[66]`
- state: `VP 1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Colombia | 48.70 | 4.00 | 45.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5 |
| 2 | Bear Trap INFLUENCE Argentina, Chile, South Africa | 44.15 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:11.20 |
| 3 | Indo-Pakistani War COUP Colombia | 42.35 | 4.00 | 38.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 4 | Camp David Accords COUP Colombia | 42.35 | 4.00 | 38.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:3.5 |
| 5 | Bear Trap COUP Egypt | 39.80 | 4.00 | 36.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 99: T7 AR4 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], The Cambridge Five[36], How I Learned to Stop Worrying[49], Missile Envy[52], Allende[57]`
- state: `VP 1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy COUP Colombia | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 4 | Romanian Abdication COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 5 | Allende COUP Colombia | 35.70 | 4.00 | 31.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], Indo-Pakistani War[24], Camp David Accords[66]`
- state: `VP 1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Colombia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Camp David Accords COUP Colombia | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Captured Nazi Scientist COUP Colombia | 35.20 | 4.00 | 31.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Indo-Pakistani War COUP Egypt | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Camp David Accords COUP Egypt | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:4, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], How I Learned to Stop Worrying[49], Missile Envy[52], Allende[57]`
- state: `VP 1, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Argentina | 29.98 | 4.00 | 26.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:1.5 |
| 2 | Missile Envy COUP Argentina | 29.98 | 4.00 | 26.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:1.5 |
| 3 | How I Learned to Stop Worrying COUP Mexico | 28.73 | 4.00 | 25.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:1.5 |
| 4 | How I Learned to Stop Worrying COUP Panama | 28.73 | 4.00 | 25.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:1.5 |
| 5 | Missile Envy COUP Mexico | 28.73 | 4.00 | 25.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18], Camp David Accords[66]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Colombia | 42.22 | 4.00 | 38.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Colombia | 35.87 | 4.00 | 32.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |
| 3 | Camp David Accords INFLUENCE Chile, South Africa | 28.63 | 6.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:10.67 |
| 4 | Korean War COUP Colombia | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Colombia | 26.22 | 4.00 | 38.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Missile Envy [52] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Missile Envy[52], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Colombia | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |
| 2 | Missile Envy COUP Cameroon | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |
| 3 | Missile Envy COUP Saharan States | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |
| 4 | Missile Envy COUP SE African States | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | Missile Envy COUP Sudan | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Arab-Israeli War[13], Captured Nazi Scientist[18]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Colombia | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Korean War COUP Colombia | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Colombia | 27.55 | 4.00 | 39.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Captured Nazi Scientist COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP SE African States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Allende[57]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Colombia | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5 |
| 2 | Allende COUP Colombia | 43.20 | 4.00 | 39.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Cameroon | 21.20 | 4.00 | 17.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication COUP Saharan States | 21.20 | 4.00 | 17.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication COUP SE African States | 21.20 | 4.00 | 17.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13]`
- state: `VP 1, DEFCON 2, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Korean War COUP Saharan States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP SE African States | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Zimbabwe | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Colombia | 9.55 | 4.00 | 21.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 107: T8 AR0 USSR

- chosen: `Wargames [103] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Korean War[11], Romanian Abdication[12], Indo-Pakistani War[24], Nuclear Subs[44], Quagmire[45], Brezhnev Doctrine[54], Wargames[103], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], Marshall Plan[23], Cultural Revolution[61], Flower Power[62], Ask Not What Your Country Can Do For You[78], Che[83], Star Wars[88], Chernobyl[97]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Chernobyl EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Star Wars EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Quagmire [45] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Korean War[11], Romanian Abdication[12], Indo-Pakistani War[24], Nuclear Subs[44], Quagmire[45], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Colombia | 47.69 | 4.00 | 44.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 2 | Brezhnev Doctrine COUP Colombia | 47.69 | 4.00 | 44.14 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 3 | Quagmire INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 5 | Korean War COUP Colombia | 41.34 | 4.00 | 37.64 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 110: T8 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], Cultural Revolution[61], Flower Power[62], Ask Not What Your Country Can Do For You[78], Che[83], Star Wars[88], Chernobyl[97]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Chernobyl INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 4 | Five Year Plan COUP Egypt | 39.04 | 4.00 | 35.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Ask Not What Your Country Can Do For You COUP Egypt | 39.04 | 4.00 | 35.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.14, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], Indo-Pakistani War[24], Nuclear Subs[44], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 48.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.67 |
| 2 | Brezhnev Doctrine COUP Algeria | 32.67 | 4.00 | 29.12 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |
| 3 | Korean War INFLUENCE East Germany, West Germany | 32.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.67 |
| 4 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 32.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.67 |
| 5 | Brezhnev Doctrine COUP Argentina | 32.17 | 4.00 | 28.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Cultural Revolution[61], Flower Power[62], Ask Not What Your Country Can Do For You[78], Che[83], Star Wars[88], Chernobyl[97]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 44.38 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 3 | Ask Not What Your Country Can Do For You COUP Egypt | 39.42 | 4.00 | 35.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Chernobyl COUP Egypt | 39.42 | 4.00 | 35.87 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | Ask Not What Your Country Can Do For You COUP Syria | 36.92 | 4.00 | 33.37 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], Indo-Pakistani War[24], Nuclear Subs[44], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 30.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 30.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Korean War COUP Algeria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Algeria | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Korean War COUP Argentina | 26.15 | 4.00 | 22.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Cultural Revolution[61], Flower Power[62], Che[83], Star Wars[88], Chernobyl[97]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 42.25 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.80 |
| 2 | Chernobyl COUP Egypt | 39.95 | 4.00 | 36.40 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Chernobyl COUP Syria | 37.45 | 4.00 | 33.90 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 4 | Chernobyl COUP Algeria | 34.20 | 4.00 | 30.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:2.5 |
| 5 | Chernobyl COUP Argentina | 33.70 | 4.00 | 30.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:8, milops_urgency:1.60, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], Nuclear Subs[44], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 28.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | Indo-Pakistani War COUP Algeria | 27.15 | 4.00 | 23.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |
| 3 | Indo-Pakistani War COUP Argentina | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |
| 4 | Indo-Pakistani War COUP Brazil | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Venezuela | 26.65 | 4.00 | 22.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Venezuela, battleground_coup, milops_need:5, milops_urgency:1.25, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Star Wars [88] as COUP`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Cultural Revolution[61], Flower Power[62], Che[83], Star Wars[88]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars COUP Egypt | 34.40 | 4.00 | 30.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Star Wars COUP Syria | 31.90 | 4.00 | 28.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:1.5 |
| 3 | Star Wars COUP Algeria | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Star Wars COUP Argentina | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Argentina, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Star Wars COUP Brazil | 28.15 | 4.00 | 24.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Brazil, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 117: T8 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Romanian Abdication[12], Nuclear Subs[44], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Cameroon | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Saharan States | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP SE African States | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 4 | Romanian Abdication COUP Sudan | 14.53 | 4.00 | 10.68 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |
| 5 | Romanian Abdication COUP Colombia | 14.03 | 4.00 | 10.18 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `De Gaulle Leads France[17], Cultural Revolution[61], Flower Power[62], Che[83]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Flower Power INFLUENCE France, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | De Gaulle Leads France COUP Saharan States | 7.90 | 4.00 | 24.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Nuclear Subs[44], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Cameroon | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Saharan States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Nuclear Subs COUP SE African States | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nuclear Subs COUP Sudan | 6.55 | 4.00 | 18.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Colombia | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Cultural Revolution [61] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Cultural Revolution[61], Flower Power[62], Che[83]`
- state: `VP 1, DEFCON 2, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 2 | Cultural Revolution COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Cultural Revolution COUP Zimbabwe | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Che COUP Saharan States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Che COUP SE African States | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 121: T8 AR7 USSR

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Panama Canal Returned[111]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 31.20 | 4.00 | 39.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Panama Canal Returned COUP Cameroon | 9.20 | 4.00 | 17.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP SE African States | 9.20 | 4.00 | 17.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Panama Canal Returned COUP Sudan | 9.20 | 4.00 | 17.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Panama Canal Returned COUP Colombia | 8.70 | 4.00 | 16.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Che [83] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Flower Power[62], Che[83]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Ivory Coast | 25.50 | 4.00 | 41.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Ivory Coast, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Flower Power COUP Ivory Coast | 23.15 | 4.00 | 35.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Che COUP Saharan States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Che COUP SE African States | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Che COUP Zimbabwe | 13.90 | 4.00 | 30.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 123: T9 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Suez Crisis[28], Red Scare/Purge[31], UN Intervention[32], How I Learned to Stop Worrying[49], Cultural Revolution[61], Flower Power[62], Latin American Death Squads[70], Che[83]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Marshall Plan[23], US/Japan Mutual Defense Pact[27], Decolonization[30], Special Relationship[37], Cuban Missile Crisis[43], South African Unrest[56], Camp David Accords[66], Sadat Expels Soviets[73], One Small Step[81]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Suez Crisis[28], UN Intervention[32], How I Learned to Stop Worrying[49], Cultural Revolution[61], Flower Power[62], Latin American Death Squads[70], Che[83]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Cultural Revolution COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | Che COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | Suez Crisis INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 5 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 126: T9 AR1 US

- chosen: `US/Japan Mutual Defense Pact [27] as COUP`
- flags: `milops_shortfall:9`
- hand: `US/Japan Mutual Defense Pact[27], Decolonization[30], Special Relationship[37], Cuban Missile Crisis[43], South African Unrest[56], Camp David Accords[66], Sadat Expels Soviets[73], One Small Step[81]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact COUP Nigeria | 57.32 | 4.00 | 53.92 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:5.5 |
| 2 | US/Japan Mutual Defense Pact COUP Cameroon | 54.82 | 4.00 | 51.42 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:5.5 |
| 3 | US/Japan Mutual Defense Pact COUP Saharan States | 54.82 | 4.00 | 51.42 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:5.5 |
| 4 | Cuban Missile Crisis COUP Nigeria | 50.97 | 4.00 | 47.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 5 | Sadat Expels Soviets COUP Nigeria | 50.97 | 4.00 | 47.42 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+4`

## Step 127: T9 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], UN Intervention[32], How I Learned to Stop Worrying[49], Cultural Revolution[61], Flower Power[62], Latin American Death Squads[70], Che[83]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 47.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Cultural Revolution COUP Ivory Coast | 37.50 | 4.00 | 33.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Che COUP Ivory Coast | 37.50 | 4.00 | 33.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Vietnam Revolts COUP Ivory Coast | 31.15 | 4.00 | 27.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `milops_shortfall:5`
- hand: `Decolonization[30], Special Relationship[37], Cuban Missile Crisis[43], South African Unrest[56], Camp David Accords[66], Sadat Expels Soviets[73], One Small Step[81]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Cameroon | 47.57 | 4.00 | 44.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP Saharan States | 47.57 | 4.00 | 44.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 3 | Sadat Expels Soviets COUP Cameroon | 47.57 | 4.00 | 44.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 4 | Sadat Expels Soviets COUP Saharan States | 47.57 | 4.00 | 44.02 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 5 | Special Relationship COUP Cameroon | 41.22 | 4.00 | 37.52 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], UN Intervention[32], How I Learned to Stop Worrying[49], Flower Power[62], Latin American Death Squads[70], Che[83]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 45.45 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Che COUP Ivory Coast | 37.90 | 4.00 | 34.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 3 | Vietnam Revolts COUP Ivory Coast | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 4 | How I Learned to Stop Worrying COUP Ivory Coast | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |
| 5 | Flower Power COUP Ivory Coast | 31.55 | 4.00 | 27.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Sadat Expels Soviets [73] as COUP`
- flags: `milops_shortfall:5`
- hand: `Decolonization[30], Special Relationship[37], South African Unrest[56], Camp David Accords[66], Sadat Expels Soviets[73], One Small Step[81]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Special Relationship COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Camp David Accords COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | One Small Step COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, West Germany | 30.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], UN Intervention[32], How I Learned to Stop Worrying[49], Flower Power[62], Latin American Death Squads[70]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | Flower Power COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 5 | UN Intervention COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:5`
- hand: `Decolonization[30], Special Relationship[37], South African Unrest[56], Camp David Accords[66], One Small Step[81]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Cameroon | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 2 | Special Relationship COUP Saharan States | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 3 | Special Relationship COUP SE African States | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 4 | Special Relationship COUP Zimbabwe | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Camp David Accords COUP Cameroon | 20.05 | 4.00 | 16.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `How I Learned to Stop Worrying [49] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], How I Learned to Stop Worrying[49], Flower Power[62], Latin American Death Squads[70]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Flower Power COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Latin American Death Squads COUP Saharan States | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 4 | UN Intervention COUP Saharan States | 37.20 | 4.00 | 33.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 5 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:5`
- hand: `Decolonization[30], South African Unrest[56], Camp David Accords[66], One Small Step[81]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Saharan States | 42.88 | 4.00 | 39.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 3 | Decolonization COUP Saharan States | 26.88 | 4.00 | 39.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | South African Unrest COUP Saharan States | 26.88 | 4.00 | 39.18 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Camp David Accords COUP Cameroon | 20.88 | 4.00 | 17.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Flower Power [62] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], Flower Power[62], Latin American Death Squads[70]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power COUP Ivory Coast | 35.15 | 4.00 | 31.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:1.5 |
| 2 | Latin American Death Squads COUP Ivory Coast | 35.15 | 4.00 | 31.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:1.5 |
| 3 | UN Intervention COUP Ivory Coast | 28.80 | 4.00 | 24.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:0.5 |
| 4 | Flower Power COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Flower Power COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:5`
- hand: `Decolonization[30], South African Unrest[56], One Small Step[81]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5 |
| 2 | Decolonization COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | South African Unrest COUP Saharan States | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | One Small Step COUP Cameroon | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |
| 5 | One Small Step COUP SE African States | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `UN Intervention[32], Latin American Death Squads[70]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 51.55 | 4.00 | 47.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5 |
| 2 | UN Intervention COUP Saharan States | 45.20 | 4.00 | 41.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5 |
| 3 | Latin American Death Squads COUP SE African States | 29.55 | 4.00 | 25.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Latin American Death Squads COUP Sudan | 29.55 | 4.00 | 25.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Latin American Death Squads COUP Colombia | 29.05 | 4.00 | 25.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Decolonization[30], South African Unrest[56]`
- state: `VP 1, DEFCON 2, MilOps U3/A4, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Cameroon | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Saharan States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP SE African States | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Zimbabwe | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Cameroon | 11.55 | 4.00 | 23.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-4`

## Step 139: T10 AR0 USSR

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `The Cambridge Five[36], NORAD[38], SALT Negotiations[46], Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Marine Barracks Bombing[91], Tear Down this Wall[99], Pershing II Deployed[102]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Pershing II Deployed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Marine Barracks Bombing EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | NORAD EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], COMECON[14], Nuclear Test Ban[34], NORAD[38], Muslim Revolution[59], Alliance for Progress[79], The Iron Lady[86], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Pershing II Deployed [102] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `The Cambridge Five[36], NORAD[38], Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Marine Barracks Bombing[91], Tear Down this Wall[99], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed COUP Indonesia | 55.01 | 4.00 | 51.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Pershing II Deployed COUP Saharan States | 48.76 | 4.00 | 45.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | The Cambridge Five COUP Indonesia | 48.66 | 4.00 | 44.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Marine Barracks Bombing COUP Indonesia | 48.66 | 4.00 | 44.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 5 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 142: T10 AR1 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], COMECON[14], NORAD[38], Muslim Revolution[59], Alliance for Progress[79], The Iron Lady[86], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 55.01 | 4.00 | 51.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Indonesia | 55.01 | 4.00 | 51.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 3 | The Iron Lady COUP Indonesia | 55.01 | 4.00 | 51.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:4.5 |
| 4 | NORAD INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 143: T10 AR2 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `The Cambridge Five[36], NORAD[38], Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Marine Barracks Bombing[91], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Saharan States | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 2 | Marine Barracks Bombing COUP Saharan States | 41.88 | 4.00 | 38.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:3.5 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 29.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 4 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 29.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 5 | NORAD COUP Saharan States | 28.23 | 4.00 | 44.68 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Alliance for Progress [79] as COUP`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], COMECON[14], Muslim Revolution[59], Alliance for Progress[79], The Iron Lady[86], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP Saharan States | 48.23 | 4.00 | 44.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 2 | The Iron Lady COUP Saharan States | 48.23 | 4.00 | 44.68 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.17, coup_access_open, expected_swing:4.5 |
| 3 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 45.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 4 | The Iron Lady INFLUENCE East Germany, France, West Germany | 45.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.33 |
| 5 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Congo/Zaire | 37.77 | 6.00 | 65.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Marine Barracks Bombing [91] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `NORAD[38], Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Marine Barracks Bombing[91], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing COUP Nigeria | 44.85 | 4.00 | 41.15 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 2 | NORAD COUP Nigeria | 31.20 | 4.00 | 47.65 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Tear Down this Wall COUP Nigeria | 31.20 | 4.00 | 47.65 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Camp David Accords COUP Nigeria | 28.85 | 4.00 | 41.15 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | John Paul II Elected Pope COUP Nigeria | 28.85 | 4.00 | 41.15 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.40, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `The Iron Lady [86] as COUP`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], COMECON[14], Muslim Revolution[59], The Iron Lady[86], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady COUP Saharan States | 48.70 | 4.00 | 45.15 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 43.85 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.20 |
| 3 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Congo/Zaire | 35.90 | 6.00 | 65.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Muslim Revolution COUP Saharan States | 31.05 | 4.00 | 51.65 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 5 | Socialist Governments COUP Saharan States | 28.70 | 4.00 | 45.15 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `NORAD [38] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `NORAD[38], Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Tear Down this Wall COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Camp David Accords COUP Saharan States | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | John Paul II Elected Pope COUP Saharan States | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], COMECON[14], Muslim Revolution[59], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Congo/Zaire | 33.10 | 6.00 | 65.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Muslim Revolution COUP Saharan States | 31.75 | 4.00 | 52.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 3 | Socialist Governments COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | COMECON COUP Saharan States | 29.40 | 4.00 | 45.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Yuri and Samantha COUP Saharan States | 27.05 | 4.00 | 39.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, France, West Germany | 16.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Tear Down this Wall COUP Saharan States | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 3 | Tear Down this Wall COUP SE African States | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Tear Down this Wall COUP Sudan | 8.57 | 4.00 | 25.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Tear Down this Wall COUP Colombia | 8.07 | 4.00 | 24.52 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Socialist Governments [7] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], COMECON[14], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Saharan States | 30.57 | 4.00 | 47.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | COMECON COUP Saharan States | 30.57 | 4.00 | 47.02 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Yuri and Samantha COUP Saharan States | 28.22 | 4.00 | 40.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Saharan States | 28.22 | 4.00 | 40.52 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Socialist Governments INFLUENCE West Germany, Angola, Congo/Zaire | 23.58 | 6.00 | 56.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Angola:13.60, control_break:Angola, access_touch:Angola, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Camp David Accords [66] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Camp David Accords[66], John Paul II Elected Pope[69], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Camp David Accords COUP SE African States | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Camp David Accords COUP Sudan | 8.55 | 4.00 | 20.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `COMECON [14] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `COMECON[14], Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Saharan States | 32.90 | 4.00 | 49.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Yuri and Samantha COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Saharan States | 30.55 | 4.00 | 42.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | COMECON COUP Cameroon | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP SE African States | 10.90 | 4.00 | 27.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:3.50, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `John Paul II Elected Pope[69], Nixon Plays the China Card[72]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope COUP Saharan States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | John Paul II Elected Pope COUP SE African States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | John Paul II Elected Pope COUP Sudan | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Saharan States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP SE African States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Yuri and Samantha [106] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Yuri and Samantha[106], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha COUP Saharan States | 37.55 | 4.00 | 49.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Saharan States | 37.55 | 4.00 | 49.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Yuri and Samantha COUP Cameroon | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Yuri and Samantha COUP SE African States | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Yuri and Samantha COUP Zimbabwe | 15.55 | 4.00 | 27.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-3/A-3`
