# minimal_hybrid detailed rollout log

- seed: `20260542`
- winner: `USSR`
- final_vp: `2`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], Olympic Games[20], NATO[21], Marshall Plan[23], Nuclear Test Ban[34], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Independent Reds [22] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], Truman Doctrine[19], Independent Reds[22], Indo-Pakistani War[24], Suez Crisis[28], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `De Gaulle Leads France [17] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], De Gaulle Leads France[17], Olympic Games[20], NATO[21], Marshall Plan[23], Special Relationship[37], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France COUP Iran | 77.00 | 4.00 | 73.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Vietnam Revolts COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Olympic Games COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | De Gaulle Leads France INFLUENCE West Germany, Japan, Thailand | 61.47 | 5.00 | 58.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.33 |
| 5 | NATO COUP Iran | 58.35 | 4.00 | 78.95 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Warsaw Pact Formed[16], Truman Doctrine[19], Indo-Pakistani War[24], Suez Crisis[28], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Indonesia, Philippines | 43.67 | 5.00 | 40.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | Warsaw Pact Formed INFLUENCE North Korea, Indonesia, Philippines | 41.07 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 3 | Suez Crisis INFLUENCE North Korea, Indonesia, Philippines | 41.07 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 4 | De-Stalinization INFLUENCE North Korea, Indonesia, Philippines | 41.07 | 5.00 | 57.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.33 |
| 5 | Truman Doctrine COUP North Korea | 30.40 | 4.00 | 26.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Vietnam Revolts[9], Olympic Games[20], NATO[21], Marshall Plan[23], Special Relationship[37], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, South Korea, Thailand | 56.20 | 5.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, South Korea, Thailand | 56.20 | 5.00 | 75.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Olympic Games COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Vietnam Revolts INFLUENCE Japan, Thailand | 45.30 | 5.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Warsaw Pact Formed[16], Truman Doctrine[19], Suez Crisis[28], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Turkey, West Germany, North Korea | 38.60 | 5.00 | 55.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 2 | Suez Crisis INFLUENCE Turkey, West Germany, North Korea | 38.60 | 5.00 | 55.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 3 | De-Stalinization INFLUENCE Turkey, West Germany, North Korea | 38.60 | 5.00 | 55.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |
| 4 | Truman Doctrine COUP North Korea | 30.50 | 4.00 | 26.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.20, coup_access_open |
| 5 | Korean War INFLUENCE West Germany, North Korea | 25.30 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Vietnam Revolts[9], Olympic Games[20], Marshall Plan[23], Special Relationship[37], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE North Korea, Pakistan, Israel, Thailand | 60.25 | 5.00 | 79.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Vietnam Revolts INFLUENCE North Korea, Thailand | 50.70 | 5.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 3 | Olympic Games INFLUENCE North Korea, Thailand | 50.70 | 5.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 4 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Olympic Games COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], Suez Crisis[28], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, Italy | 33.10 | 5.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Italy:14.45, access_touch:Italy, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | De-Stalinization INFLUENCE East Germany, France, Italy | 33.10 | 5.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Italy:14.45, access_touch:Italy, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Truman Doctrine COUP Japan | 24.25 | 4.00 | 20.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 4 | Truman Doctrine COUP North Korea | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |
| 5 | Truman Doctrine COUP South Korea | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:1, milops_urgency:0.25 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china`
- hand: `Vietnam Revolts[9], Olympic Games[20], Special Relationship[37], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Olympic Games COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Vietnam Revolts INFLUENCE East Germany, Thailand | 45.20 | 5.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 4 | Olympic Games INFLUENCE East Germany, Thailand | 45.20 | 5.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 5 | NORAD INFLUENCE East Germany, Pakistan, Thailand | 45.00 | 5.00 | 60.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, Japan, Panama | 33.68 | 5.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Truman Doctrine COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 3 | Korean War INFLUENCE Italy, Panama | 21.68 | 5.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | The Cambridge Five INFLUENCE Italy, Panama | 21.68 | 5.00 | 35.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Truman Doctrine INFLUENCE Italy | 21.63 | 5.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china`
- hand: `Olympic Games[20], Special Relationship[37], NORAD[38]`
- state: `VP 3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, Thailand | 45.20 | 5.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 2 | NORAD INFLUENCE East Germany, Pakistan, Thailand | 45.00 | 5.00 | 60.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Special Relationship INFLUENCE East Germany, Thailand | 29.20 | 5.00 | 40.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Olympic Games COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 5 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Truman Doctrine[19], The Cambridge Five[36]`
- state: `VP 3, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | Truman Doctrine COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3 |
| 3 | Truman Doctrine INFLUENCE Japan | 14.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:7.00 |
| 4 | Korean War INFLUENCE Japan, Egypt | 13.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | The Cambridge Five INFLUENCE Japan, Egypt | 13.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 13: T1 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Special Relationship[37], NORAD[38]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE India, Pakistan, Thailand | 42.50 | 5.00 | 57.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Special Relationship INFLUENCE Pakistan, Thailand | 29.10 | 5.00 | 40.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Special Relationship SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | NORAD SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | NORAD COUP Lebanon | 0.40 | 4.00 | 16.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Korean War[11], The Cambridge Five[36]`
- state: `VP 3, DEFCON 3, MilOps U3/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 2 | The Cambridge Five INFLUENCE Japan, Egypt | 20.55 | 5.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 3 | Korean War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Korean War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +2, DEFCON +1, MilOps U-3/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Romanian Abdication[12], COMECON[14], Nasser[15], Captured Nazi Scientist[18], Containment[25], Red Scare/Purge[31], Formosan Resolution[35]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], Arab-Israeli War[13], CIA Created[26], US/Japan Mutual Defense Pact[27], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Romanian Abdication[12], COMECON[14], Nasser[15], Captured Nazi Scientist[18], Containment[25], Formosan Resolution[35]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, Philippines, Thailand | 55.23 | 5.00 | 53.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 2 | COMECON COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 3 | COMECON COUP Egypt | 43.50 | 4.00 | 39.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 4 | Duck and Cover INFLUENCE Italy, Philippines, Thailand | 35.23 | 5.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Containment INFLUENCE Italy, Philippines, Thailand | 35.23 | 5.00 | 53.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], Arab-Israeli War[13], CIA Created[26], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Italy, Philippines | 40.78 | 5.00 | 38.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 2 | East European Unrest INFLUENCE Italy, Philippines | 40.78 | 5.00 | 38.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.67 |
| 3 | Five Year Plan COUP Philippines | 37.25 | 4.00 | 33.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 4 | East European Unrest COUP Philippines | 37.25 | 4.00 | 33.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, expected_swing:2.5 |
| 5 | Five Year Plan COUP Syria | 35.00 | 4.00 | 31.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Romanian Abdication[12], Nasser[15], Captured Nazi Scientist[18], Containment[25], Formosan Resolution[35]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Indonesia | 43.15 | 4.00 | 39.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 2 | Nasser COUP Indonesia | 43.15 | 4.00 | 39.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Indonesia | 43.15 | 4.00 | 39.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 4 | Duck and Cover COUP Indonesia | 34.85 | 4.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Containment COUP Indonesia | 34.85 | 4.00 | 51.30 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 20: T2 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], East European Unrest[29], Decolonization[30], UN Intervention[32]`
- state: `VP 5, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Egypt | 36.20 | 5.00 | 34.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 2 | East European Unrest COUP Syria | 35.20 | 4.00 | 31.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 3 | East European Unrest COUP Lebanon | 23.60 | 4.00 | 20.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:0.40, empty_coup_penalty, expected_swing:4.5 |
| 4 | CIA Created COUP Syria | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:0.5 |
| 5 | UN Intervention COUP Syria | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Captured Nazi Scientist[18], Containment[25], Formosan Resolution[35]`
- state: `VP 5, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Saudi Arabia, Thailand | 35.45 | 5.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 35.45 | 5.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Formosan Resolution INFLUENCE Saudi Arabia, Thailand | 23.45 | 5.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Nasser INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Captured Nazi Scientist INFLUENCE Thailand | 23.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Arab-Israeli War[13], CIA Created[26], Decolonization[30], UN Intervention[32]`
- state: `VP 5, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Syria | 23.80 | 4.00 | 19.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 3 | CIA Created COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3 |
| 4 | UN Intervention COUP Israel | 17.75 | 4.00 | 13.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:0.50, defcon_penalty:3 |
| 5 | CIA Created INFLUENCE Japan | 17.00 | 5.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Containment[25], Formosan Resolution[35]`
- state: `VP 5, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Egypt, Thailand | 34.18 | 5.00 | 52.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Nasser INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 22.63 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 4 | Formosan Resolution INFLUENCE Japan, Thailand | 22.63 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | Nasser COUP Lebanon | 11.70 | 4.00 | 7.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], Arab-Israeli War[13], Decolonization[30], UN Intervention[32]`
- state: `VP 5, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Japan | 23.33 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.67 |
| 2 | UN Intervention COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 3 | Fidel COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Decolonization COUP Syria | 12.65 | 4.00 | 24.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 5, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Egypt | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Egypt | 19.30 | 4.00 | 15.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, expected_swing:0.5 |
| 3 | Nasser INFLUENCE Thailand | 18.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 18.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:7.00 |
| 5 | Formosan Resolution INFLUENCE Japan, Thailand | 18.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Fidel [8] as SPACE`
- flags: `milops_shortfall:1, offside_ops_play, space_play`
- hand: `Fidel[8], Arab-Israeli War[13], Decolonization[30]`
- state: `VP 5, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Arab-Israeli War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Decolonization SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Fidel COUP SE African States | -0.70 | 4.00 | 11.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Fidel COUP Zimbabwe | -0.70 | 4.00 | 11.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:0.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -2, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, behind_on_space`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 3, DEFCON 2, MilOps U1/A1, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 14.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 14.30 | 5.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 3 | Captured Nazi Scientist COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Formosan Resolution SPACE | 2.20 | 1.00 | 5.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 5 | Formosan Resolution COUP Sudan | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Decolonization[30]`
- state: `VP 3, DEFCON 2, MilOps U1/A1, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP SE African States | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Zimbabwe | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Decolonization COUP SE African States | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Decolonization COUP Zimbabwe | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Colombia | 0.30 | 4.00 | 12.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Socialist Governments[7], Blockade[10], Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Olympic Games[20], Suez Crisis[28], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], NATO[21], Containment[25], CIA Created[26], Red Scare/Purge[31], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Olympic Games[20], Suez Crisis[28], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Libya, Thailand | 52.85 | 5.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Suez Crisis INFLUENCE Japan, Libya, Thailand | 52.85 | 5.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Korean War INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Arab-Israeli War INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Olympic Games INFLUENCE Japan, Thailand | 37.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], Containment[25], CIA Created[26], Red Scare/Purge[31], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE Japan, Egypt, Angola, Indonesia | 70.95 | 5.00 | 70.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, influence:Angola:10.85, control_break:Angola, access_touch:Angola, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE Japan, Angola, Indonesia | 55.40 | 5.00 | 54.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Angola:10.85, control_break:Angola, access_touch:Angola, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 3 | Red Scare/Purge COUP Egypt | 44.35 | 4.00 | 40.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 4 | Red Scare/Purge COUP Syria | 41.85 | 4.00 | 38.45 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 5 | Special Relationship INFLUENCE Japan, Angola | 39.70 | 5.00 | 39.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Angola:10.85, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Olympic Games[20], Suez Crisis[28], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Egypt, Indonesia, Thailand | 57.75 | 5.00 | 58.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | Korean War INFLUENCE Indonesia, Thailand | 39.20 | 5.00 | 39.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | Arab-Israeli War INFLUENCE Indonesia, Thailand | 39.20 | 5.00 | 39.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 4 | Olympic Games INFLUENCE Indonesia, Thailand | 39.20 | 5.00 | 39.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 5 | NORAD INFLUENCE Egypt, Indonesia, Thailand | 37.75 | 5.00 | 58.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Egypt:13.70, control_break:Egypt, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], Containment[25], CIA Created[26], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Japan, Libya | 47.25 | 5.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:4.80 |
| 2 | Containment COUP Libya | 39.30 | 4.00 | 35.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 3 | Containment COUP Syria | 36.80 | 4.00 | 33.25 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 4 | Special Relationship COUP Libya | 32.95 | 4.00 | 29.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 5 | Containment COUP Egypt | 32.30 | 4.00 | 28.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Olympic Games[20], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | Arab-Israeli War INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Olympic Games INFLUENCE Japan, Thailand | 35.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 4 | NORAD INFLUENCE UK, Japan, Thailand | 30.80 | 5.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Korean War COUP Egypt | 26.40 | 4.00 | 22.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], CIA Created[26], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Syria | 30.90 | 4.00 | 27.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:1.5 |
| 2 | Special Relationship INFLUENCE West Germany, Japan | 30.50 | 5.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 3 | Special Relationship COUP Egypt | 26.40 | 4.00 | 22.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |
| 4 | Special Relationship COUP Libya | 26.40 | 4.00 | 22.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, expected_swing:1.5 |
| 5 | Captured Nazi Scientist COUP Syria | 24.55 | 4.00 | 20.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 37: T3 AR4 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Blockade[10], Arab-Israeli War[13], Olympic Games[20], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Thailand | 33.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 2 | Olympic Games INFLUENCE Japan, Thailand | 33.30 | 5.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 3 | Arab-Israeli War COUP Syria | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 4 | Olympic Games COUP Syria | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:1.5 |
| 5 | NORAD INFLUENCE UK, Japan, Thailand | 28.80 | 5.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], CIA Created[26], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Iraq | 23.48 | 5.00 | 37.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 2 | Captured Nazi Scientist INFLUENCE Japan | 23.33 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.67 |
| 3 | Truman Doctrine INFLUENCE Japan | 23.33 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.67 |
| 4 | CIA Created INFLUENCE Japan | 23.33 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.67 |
| 5 | Captured Nazi Scientist COUP Lebanon | 11.70 | 4.00 | 7.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, milops_need:1, milops_urgency:0.33, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Blockade[10], Olympic Games[20], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Syria | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5 |
| 2 | Olympic Games COUP Egypt | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 3 | Olympic Games COUP Libya | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |
| 4 | Blockade COUP Syria | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 5 | Olympic Games INFLUENCE Iraq, Thailand | 23.45 | 5.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:21.00 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 40: T3 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], CIA Created[26]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iran | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Truman Doctrine COUP Iran | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | CIA Created COUP Iran | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Saudi Arabia | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open |
| 5 | Truman Doctrine COUP Saudi Arabia | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:1, milops_urgency:0.50, defcon_penalty:3, coup_access_open |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, behind_on_space, offside_ops_play`
- hand: `Blockade[10], NORAD[38]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, Iraq, Thailand | 29.45 | 5.00 | 55.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:11.00 |
| 2 | Blockade INFLUENCE Thailand | 14.30 | 5.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 3 | Blockade COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | NORAD COUP Sudan | 2.15 | 4.00 | 18.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | NORAD SPACE | 2.05 | 1.00 | 5.00 | 0.00 | 7.50 | -0.45 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:11.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Truman Doctrine[19], CIA Created[26]`
- state: `VP 2, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 15.00 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:11.00 |
| 2 | CIA Created INFLUENCE Japan | 15.00 | 5.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:11.00 |
| 3 | Truman Doctrine COUP Mozambique | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP SE African States | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 43: T4 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Suez Crisis[28], Missile Envy[52], Allende[57], Puppet Governments[67], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Nasser[15], Olympic Games[20], Indo-Pakistani War[24], Containment[25], Brush War[39], Latin American Death Squads[70], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Missile Envy[52], Allende[57], Puppet Governments[67], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE Mexico, Algeria | 33.28 | 5.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 2 | Colonial Rear Guards INFLUENCE Mexico, Algeria | 33.28 | 5.00 | 33.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.57 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE UK, Mexico, Algeria | 29.28 | 5.00 | 49.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 4 | Missile Envy COUP Sudan | 19.26 | 4.00 | 15.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, empty_coup_penalty, expected_swing:3.5 |
| 5 | Colonial Rear Guards COUP Sudan | 19.26 | 4.00 | 15.56 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.57, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], Containment[25], Brush War[39], Latin American Death Squads[70], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Israel, Mexico, South Africa | 50.13 | 5.00 | 50.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Israel:14.40, access_touch:Israel, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 2 | Olympic Games INFLUENCE Mexico, South Africa | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 3 | Indo-Pakistani War INFLUENCE Mexico, South Africa | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 4 | Latin American Death Squads INFLUENCE Mexico, South Africa | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |
| 5 | Nixon Plays the China Card INFLUENCE Mexico, South Africa | 33.88 | 5.00 | 33.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Allende[57], Puppet Governments[67], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE Algeria, Morocco | 35.37 | 5.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:5.33 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE UK, Algeria, Morocco | 31.37 | 5.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Colonial Rear Guards COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 4 | Colonial Rear Guards COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Puppet Governments INFLUENCE Algeria, Morocco | 19.37 | 5.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Nasser[15], Olympic Games[20], Indo-Pakistani War[24], Brush War[39], Latin American Death Squads[70], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Algeria, South Africa | 37.37 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 2 | Indo-Pakistani War INFLUENCE Algeria, South Africa | 37.37 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 3 | Latin American Death Squads INFLUENCE Algeria, South Africa | 37.37 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 4 | Nixon Plays the China Card INFLUENCE Algeria, South Africa | 37.37 | 5.00 | 38.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:5.33 |
| 5 | Brush War INFLUENCE Algeria, Congo/Zaire, South Africa | 33.42 | 5.00 | 54.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Allende[57], Puppet Governments[67], Ask Not What Your Country Can Do For You[78]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE UK, West Germany, Algeria | 29.65 | 5.00 | 51.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 2 | Blockade INFLUENCE Algeria | 17.65 | 5.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 3 | Captured Nazi Scientist INFLUENCE Algeria | 17.65 | 5.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 4 | Allende INFLUENCE Algeria | 17.65 | 5.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 5 | Puppet Governments INFLUENCE UK, Algeria | 17.65 | 5.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Nasser[15], Indo-Pakistani War[24], Brush War[39], Latin American Death Squads[70], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Morocco, South Africa | 31.90 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 2 | Latin American Death Squads INFLUENCE Morocco, South Africa | 31.90 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 3 | Nixon Plays the China Card INFLUENCE Morocco, South Africa | 31.90 | 5.00 | 33.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:6.40 |
| 4 | Brush War INFLUENCE Congo/Zaire, Morocco, South Africa | 27.95 | 5.00 | 49.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 5 | Indo-Pakistani War COUP Colombia | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Allende[57], Puppet Governments[67]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 52: T4 AR4 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `milops_shortfall:4`
- hand: `Nasser[15], Brush War[39], Latin American Death Squads[70], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Nixon Plays the China Card COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Panama Canal Returned COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Latin American Death Squads INFLUENCE Congo/Zaire, South Africa | 29.70 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Nixon Plays the China Card INFLUENCE Congo/Zaire, South Africa | 29.70 | 5.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 53: T4 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], Allende[57], Puppet Governments[67]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Puppet Governments COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Sudan | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Nasser[15], Brush War[39], Nixon Plays the China Card[72], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE Nigeria, South Africa | 36.77 | 5.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 2 | Brush War INFLUENCE Congo/Zaire, Nigeria, South Africa | 32.82 | 5.00 | 53.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | Panama Canal Returned INFLUENCE Nigeria | 20.12 | 5.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:5.33 |
| 4 | Nixon Plays the China Card COUP Colombia | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Nixon Plays the China Card COUP Mozambique | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space`
- hand: `Truman Doctrine[19], Allende[57], Puppet Governments[67]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Saharan States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | Puppet Governments COUP Saharan States | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Saharan States | 25.70 | 4.00 | 33.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Sudan | 15.70 | 4.00 | 11.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Guatemala | 14.45 | 4.00 | 10.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Nasser[15], Brush War[39], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE West Germany, Congo/Zaire, South Africa | 19.70 | 5.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Panama Canal Returned COUP Colombia | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Cameroon | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Mozambique | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Puppet Governments [67] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space, offside_ops_play`
- hand: `Truman Doctrine[19], Puppet Governments[67]`
- state: `VP 0, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Saharan States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Puppet Governments COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Puppet Governments COUP Guatemala | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Sudan | 8.20 | 4.00 | 16.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 58: T4 AR7 US

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:2`
- hand: `Nasser[15], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U2/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Saharan States | 39.20 | 4.00 | 35.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Nasser COUP Saharan States | 27.20 | 4.00 | 35.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Panama Canal Returned COUP Colombia | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Cameroon | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Mozambique | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Korean War[11], Arab-Israeli War[13], CIA Created[26], De-Stalinization[33], Formosan Resolution[35], Bear Trap[47], South African Unrest[56], Cultural Revolution[61], U2 Incident[63]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Vietnam Revolts[9], Warsaw Pact Formed[16], Red Scare/Purge[31], NORAD[38], Willy Brandt[58], Shuttle Diplomacy[74], Liberation Theology[76], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Cultural Revolution [61] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Korean War[11], Arab-Israeli War[13], CIA Created[26], Formosan Resolution[35], Bear Trap[47], South African Unrest[56], Cultural Revolution[61], U2 Incident[63]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution COUP Nigeria | 50.54 | 4.00 | 46.99 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | U2 Incident COUP Nigeria | 50.54 | 4.00 | 46.99 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 3 | Korean War COUP Nigeria | 44.19 | 4.00 | 40.49 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War COUP Nigeria | 44.19 | 4.00 | 40.49 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 5 | South African Unrest COUP Nigeria | 44.19 | 4.00 | 40.49 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 62: T5 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Vietnam Revolts[9], Warsaw Pact Formed[16], NORAD[38], Willy Brandt[58], Shuttle Diplomacy[74], Liberation Theology[76], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Congo/Zaire, South Africa, Indonesia | 51.94 | 5.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:5.71 |
| 2 | Shuttle Diplomacy INFLUENCE Congo/Zaire, South Africa, Indonesia | 51.94 | 5.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:5.71 |
| 3 | NORAD COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 4 | Shuttle Diplomacy COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 5 | NORAD COUP Guatemala | 46.79 | 4.00 | 43.24 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, behind_on_space`
- hand: `Korean War[11], Arab-Israeli War[13], CIA Created[26], Formosan Resolution[35], Bear Trap[47], South African Unrest[56], U2 Incident[63]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, Algeria | 37.23 | 5.00 | 35.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:2.67 |
| 2 | U2 Incident COUP Cameroon | 23.90 | 4.00 | 20.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:4.5 |
| 3 | U2 Incident COUP Saharan States | 23.90 | 4.00 | 20.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:4.5 |
| 4 | U2 Incident COUP Sudan | 23.90 | 4.00 | 20.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:4.5 |
| 5 | U2 Incident COUP El Salvador | 22.65 | 4.00 | 19.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:El Salvador, milops_need:2, milops_urgency:0.33, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Shuttle Diplomacy [74] as COUP`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], Vietnam Revolts[9], Warsaw Pact Formed[16], Willy Brandt[58], Shuttle Diplomacy[74], Liberation Theology[76], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy COUP Saharan States | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 2 | Shuttle Diplomacy COUP Guatemala | 47.15 | 4.00 | 43.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 3 | Shuttle Diplomacy INFLUENCE West Germany, Saudi Arabia, South Africa | 46.63 | 5.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:South Africa:16.80, non_coup_milops_penalty:6.67 |
| 4 | Our Man in Tehran COUP Saharan States | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | Our Man in Tehran COUP Guatemala | 40.80 | 4.00 | 37.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 65: T5 AR3 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space`
- hand: `Korean War[11], Arab-Israeli War[13], CIA Created[26], Formosan Resolution[35], Bear Trap[47], South African Unrest[56]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 3 | South African Unrest COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 4 | Bear Trap COUP Saharan States | 26.10 | 4.00 | 42.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Saharan States | 24.75 | 4.00 | 37.05 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Vietnam Revolts[9], Warsaw Pact Formed[16], Willy Brandt[58], Liberation Theology[76], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP Guatemala | 39.50 | 4.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 3 | Our Man in Tehran INFLUENCE West Germany, South Africa | 34.45 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:3.20 |
| 4 | Warsaw Pact Formed INFLUENCE West Germany, Saudi Arabia, South Africa | 30.10 | 5.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Warsaw Pact Formed COUP Saharan States | 26.10 | 4.00 | 42.55 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space`
- hand: `Arab-Israeli War[13], CIA Created[26], Formosan Resolution[35], Bear Trap[47], South African Unrest[56]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | South African Unrest COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | Bear Trap COUP Saharan States | 26.40 | 4.00 | 42.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Saharan States | 25.05 | 4.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | CIA Created COUP Saharan States | 22.70 | 4.00 | 30.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Warsaw Pact Formed[16], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Saudi Arabia, South Africa | 29.30 | 5.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Warsaw Pact Formed COUP Guatemala | 25.15 | 4.00 | 41.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Fidel COUP Guatemala | 23.80 | 4.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Guatemala | 23.80 | 4.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Guatemala | 23.80 | 4.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space`
- hand: `CIA Created[26], Formosan Resolution[35], Bear Trap[47], South African Unrest[56]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Saharan States | 41.55 | 4.00 | 37.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Bear Trap COUP Saharan States | 26.90 | 4.00 | 43.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | CIA Created COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | South African Unrest COUP Cameroon | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Fidel COUP Guatemala | 24.30 | 4.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Bear Trap [47] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35], Bear Trap[47]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Saharan States | 27.90 | 4.00 | 44.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Formosan Resolution COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Saharan States | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Bear Trap COUP Cameroon | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Bear Trap COUP Sudan | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Willy Brandt[58], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Guatemala | 25.30 | 4.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Guatemala | 25.30 | 4.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:2, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Formosan Resolution COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP El Salvador | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:El Salvador, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Willy Brandt[58], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Liberation Theology COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Liberation Theology COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Guatemala | 28.30 | 4.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Truman Doctrine[19], Marshall Plan[23], Nuclear Test Ban[34], Special Relationship[37], Nuclear Subs[44], Grain Sales to Soviets[68], Alliance for Progress[79]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Alliance for Progress EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Containment[25], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Camp David Accords[66], Voice of America[75]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Marshall Plan[23], Special Relationship[37], Nuclear Subs[44], Grain Sales to Soviets[68], Alliance for Progress[79]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, West Germany, Congo/Zaire | 36.99 | 5.00 | 63.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:6.86 |
| 2 | Romanian Abdication COUP Indonesia | 35.77 | 4.00 | 31.92 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Indonesia | 35.77 | 4.00 | 31.92 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:0.86, expected_swing:2.5 |
| 4 | Romanian Abdication COUP Congo/Zaire | 33.87 | 4.00 | 30.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Congo/Zaire | 33.87 | 4.00 | 30.02 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Congo/Zaire, battleground_coup, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Containment[25], East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Camp David Accords[66], Voice of America[75]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Congo/Zaire, South Africa | 49.84 | 5.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | East European Unrest INFLUENCE West Germany, Congo/Zaire, South Africa | 49.84 | 5.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | Summit INFLUENCE West Germany, Congo/Zaire, South Africa | 49.84 | 5.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 4 | Containment COUP Cameroon | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |
| 5 | Containment COUP Saharan States | 48.47 | 4.00 | 44.92 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:0.86, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Special Relationship[37], Nuclear Subs[44], Grain Sales to Soviets[68], Alliance for Progress[79]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Angola | 46.70 | 4.00 | 42.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Angola | 46.70 | 4.00 | 42.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 3 | Alliance for Progress COUP Angola | 39.40 | 4.00 | 55.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Special Relationship COUP Angola | 37.05 | 4.00 | 49.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Nuclear Subs COUP Angola | 37.05 | 4.00 | 49.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 80: T6 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `East European Unrest[29], UN Intervention[32], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Camp David Accords[66], Voice of America[75]`
- state: `VP 1, DEFCON 4, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Angola, South Africa | 52.10 | 5.00 | 55.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Summit INFLUENCE West Germany, Angola, South Africa | 52.10 | 5.00 | 55.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | East European Unrest COUP Cameroon | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | East European Unrest COUP Saharan States | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | East European Unrest COUP Indonesia | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Captured Nazi Scientist[18], Special Relationship[37], Nuclear Subs[44], Grain Sales to Soviets[68], Alliance for Progress[79]`
- state: `VP 1, DEFCON 4, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Angola | 46.70 | 4.00 | 42.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 2 | Alliance for Progress COUP Angola | 39.40 | 4.00 | 55.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Special Relationship COUP Angola | 37.05 | 4.00 | 49.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Nuclear Subs COUP Angola | 37.05 | 4.00 | 49.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Angola | 37.05 | 4.00 | 49.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Summit [48] as COUP`
- flags: `milops_shortfall:6`
- hand: `UN Intervention[32], The Cambridge Five[36], Summit[48], Kitchen Debates[51], Camp David Accords[66], Voice of America[75]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Angola | 54.00 | 4.00 | 50.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | Summit COUP Cameroon | 49.50 | 4.00 | 45.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 3 | Summit COUP Saharan States | 49.50 | 4.00 | 45.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 4 | Summit COUP Guatemala | 48.25 | 4.00 | 44.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 5 | Camp David Accords COUP Angola | 47.65 | 4.00 | 43.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:6, milops_urgency:1.20, defcon_penalty:3, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 83: T6 AR4 USSR

- chosen: `Alliance for Progress [79] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Special Relationship[37], Nuclear Subs[44], Grain Sales to Soviets[68], Alliance for Progress[79]`
- state: `VP 1, DEFCON 2, MilOps U1/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress COUP SE African States | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Alliance for Progress INFLUENCE East Germany, West Germany, Angola | 28.85 | 5.00 | 54.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Special Relationship COUP SE African States | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Nuclear Subs COUP SE African States | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP SE African States | 27.30 | 4.00 | 39.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 84: T6 AR4 US

- chosen: `Camp David Accords [66] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32], The Cambridge Five[36], Kitchen Debates[51], Camp David Accords[66], Voice of America[75]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords COUP Cameroon | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | Camp David Accords COUP Saharan States | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 3 | Camp David Accords COUP SE African States | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 4 | Voice of America COUP Cameroon | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 5 | Voice of America COUP Saharan States | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space, offside_ops_play`
- hand: `Special Relationship[37], Nuclear Subs[44], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Cameroon | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nuclear Subs COUP Cameroon | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Cameroon | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE Angola, South Africa | 22.10 | 5.00 | 41.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Nuclear Subs INFLUENCE Angola, South Africa | 22.10 | 5.00 | 41.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Voice of America [75] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32], The Cambridge Five[36], Kitchen Debates[51], Voice of America[75]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Voice of America COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Voice of America COUP SE African States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Voice of America COUP Guatemala | 41.30 | 4.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | UN Intervention COUP Cameroon | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space, offside_ops_play`
- hand: `Nuclear Subs[44], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Grain Sales to Soviets COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nuclear Subs INFLUENCE Angola, South Africa | 9.10 | 5.00 | 41.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 4 | Grain Sales to Soviets INFLUENCE Angola, South Africa | 9.10 | 5.00 | 41.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:21.00 |
| 5 | Nuclear Subs COUP Mozambique | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:3`
- hand: `UN Intervention[32], The Cambridge Five[36], Kitchen Debates[51]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Saharan States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP SE African States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Saharan States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 4 | Kitchen Debates COUP SE African States | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 5 | UN Intervention COUP Guatemala | 36.45 | 4.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:3, behind_on_space, offside_ops_play`
- hand: `Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Grain Sales to Soviets COUP Cameroon | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Mozambique | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP SE African States | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Grain Sales to Soviets COUP Sudan | 10.55 | 4.00 | 22.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:3`
- hand: `The Cambridge Five[36], Kitchen Debates[51]`
- state: `VP 1, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Saharan States | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Kitchen Debates COUP SE African States | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 3 | Kitchen Debates COUP Guatemala | 40.95 | 4.00 | 37.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 4 | The Cambridge Five COUP Saharan States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP SE African States | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 91: T7 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Blockade[10], Arab-Israeli War[13], Decolonization[30], Red Scare/Purge[31], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], Muslim Revolution[59], John Paul II Elected Pope[69], Che[83]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], Olympic Games[20], Suez Crisis[28], The Cambridge Five[36], NORAD[38], Cuban Missile Crisis[43], SALT Negotiations[46], ABM Treaty[60], Ussuri River Skirmish[77]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Blockade[10], Arab-Israeli War[13], Decolonization[30], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], Muslim Revolution[59], John Paul II Elected Pope[69], Che[83]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, West Germany, Angola, South Africa | 69.50 | 5.00 | 73.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, access_touch:South Africa, non_coup_milops_penalty:8.00 |
| 2 | Muslim Revolution COUP Indonesia | 55.25 | 4.00 | 51.85 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:5.5 |
| 3 | Che INFLUENCE West Germany, Angola, South Africa | 54.10 | 5.00 | 57.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Angola:15.60, control_break:Angola, access_touch:Angola, influence:South Africa:16.80, access_touch:South Africa, non_coup_milops_penalty:8.00 |
| 4 | Che COUP Indonesia | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:4.5 |
| 5 | Muslim Revolution COUP Mexico | 47.10 | 4.00 | 43.70 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:7`
- hand: `COMECON[14], Olympic Games[20], Suez Crisis[28], The Cambridge Five[36], NORAD[38], Cuban Missile Crisis[43], SALT Negotiations[46], Ussuri River Skirmish[77]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Angola | 59.40 | 4.00 | 55.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP Angola | 59.40 | 4.00 | 55.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | SALT Negotiations COUP Angola | 59.40 | 4.00 | 55.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | Ussuri River Skirmish COUP Angola | 59.40 | 4.00 | 55.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | Olympic Games COUP Angola | 53.05 | 4.00 | 49.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 95: T7 AR2 USSR

- chosen: `Che [83] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Blockade[10], Arab-Israeli War[13], Decolonization[30], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69], Che[83]`
- state: `VP 0, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Angola | 53.90 | 4.00 | 50.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | Arab-Israeli War COUP Angola | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 3 | Decolonization COUP Angola | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 4 | How I Learned to Stop Worrying COUP Angola | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:3.5 |
| 5 | Portuguese Empire Crumbles COUP Angola | 47.55 | 4.00 | 43.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Angola, battleground_coup, milops_need:7, milops_urgency:1.17, defcon_penalty:3, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 96: T7 AR2 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], Olympic Games[20], Suez Crisis[28], The Cambridge Five[36], Cuban Missile Crisis[43], SALT Negotiations[46], Ussuri River Skirmish[77]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP SE African States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 3 | SALT Negotiations COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 4 | SALT Negotiations COUP SE African States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 5 | Ussuri River Skirmish COUP Saharan States | 47.90 | 4.00 | 44.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Arab-Israeli War[13], Decolonization[30], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Decolonization COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 4 | Portuguese Empire Crumbles COUP Saharan States | 41.95 | 4.00 | 38.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 5 | Blockade COUP Saharan States | 35.60 | 4.00 | 31.75 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `SALT Negotiations [46] as COUP`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], Olympic Games[20], Suez Crisis[28], The Cambridge Five[36], SALT Negotiations[46], Ussuri River Skirmish[77]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations COUP Saharan States | 48.30 | 4.00 | 44.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |
| 2 | SALT Negotiations COUP SE African States | 48.30 | 4.00 | 44.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |
| 3 | Ussuri River Skirmish COUP Saharan States | 48.30 | 4.00 | 44.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |
| 4 | Ussuri River Skirmish COUP SE African States | 48.30 | 4.00 | 44.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |
| 5 | SALT Negotiations COUP Guatemala | 47.05 | 4.00 | 43.50 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Decolonization[30], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Portuguese Empire Crumbles COUP Saharan States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Blockade COUP Saharan States | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 5 | Decolonization INFLUENCE West Germany, South Africa | 29.65 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], Olympic Games[20], Suez Crisis[28], The Cambridge Five[36], Ussuri River Skirmish[77]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP SE African States | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Ussuri River Skirmish COUP Guatemala | 47.65 | 4.00 | 44.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Olympic Games COUP SE African States | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Olympic Games COUP Guatemala | 41.30 | 4.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Ussuri River Skirmish INFLUENCE Angola, South Africa | 30.95 | 5.00 | 34.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Angola:15.60, access_touch:Angola, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], How I Learned to Stop Worrying[49], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE West Germany, South Africa | 26.98 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.67 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 26.98 | 5.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.67 |
| 3 | How I Learned to Stop Worrying COUP Cameroon | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 4 | How I Learned to Stop Worrying COUP Saharan States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |
| 5 | How I Learned to Stop Worrying COUP SE African States | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], Olympic Games[20], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Guatemala | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | COMECON COUP Guatemala | 28.65 | 4.00 | 45.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Suez Crisis COUP Guatemala | 28.65 | 4.00 | 45.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Guatemala | 26.30 | 4.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Olympic Games COUP Colombia | 21.55 | 4.00 | 17.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Guatemala | 44.30 | 4.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Guatemala | 37.95 | 4.00 | 34.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 3 | John Paul II Elected Pope COUP Guatemala | 28.30 | 4.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Cameroon | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Portuguese Empire Crumbles COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `COMECON [14] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `COMECON[14], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Guatemala | 30.65 | 4.00 | 47.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Suez Crisis COUP Guatemala | 30.65 | 4.00 | 47.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Guatemala | 28.30 | 4.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | COMECON COUP Colombia | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | COMECON COUP Cameroon | 9.90 | 4.00 | 26.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:4, behind_on_space`
- hand: `Blockade[10], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Cameroon | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Blockade COUP Saharan States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade COUP SE African States | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Blockade COUP Sudan | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Blockade COUP Zimbabwe | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Suez Crisis [28] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Cameroon | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Suez Crisis COUP Guatemala | 36.65 | 4.00 | 53.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | The Cambridge Five COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | The Cambridge Five COUP Guatemala | 34.30 | 4.00 | 46.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Suez Crisis COUP Colombia | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 107: T8 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `Socialist Governments[7], Fidel[8], COMECON[14], Truman Doctrine[19], We Will Bury You[53], Willy Brandt[58], U2 Incident[63], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Containment[25], East European Unrest[29], Red Scare/Purge[31], Quagmire[45], Junta[50], ABM Treaty[60], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `Socialist Governments[7], Fidel[8], COMECON[14], Truman Doctrine[19], Willy Brandt[58], U2 Incident[63], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Cameroon | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 2 | COMECON COUP Cameroon | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 3 | U2 Incident COUP Cameroon | 49.33 | 4.00 | 45.78 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 4 | Fidel COUP Cameroon | 42.98 | 4.00 | 39.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 5 | Willy Brandt COUP Cameroon | 42.98 | 4.00 | 39.28 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 110: T8 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Containment[25], East European Unrest[29], Quagmire[45], Junta[50], ABM Treaty[60], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, Poland, West Germany | 61.06 | 5.00 | 65.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | ABM Treaty COUP Guatemala | 54.93 | 4.00 | 51.53 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:5.5 |
| 3 | Containment COUP Guatemala | 48.58 | 4.00 | 45.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 4 | East European Unrest COUP Guatemala | 48.58 | 4.00 | 45.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:4.5 |
| 5 | ABM Treaty COUP Ivory Coast | 45.28 | 4.00 | 41.88 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Ivory Coast, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `COMECON [14] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Fidel[8], COMECON[14], Truman Doctrine[19], Willy Brandt[58], U2 Incident[63], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Cameroon | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 2 | U2 Incident COUP Cameroon | 48.40 | 4.00 | 44.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:4.5 |
| 3 | Fidel COUP Cameroon | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 4 | Willy Brandt COUP Cameroon | 42.05 | 4.00 | 38.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:0.83, coup_access_open, expected_swing:3.5 |
| 5 | COMECON INFLUENCE Poland, West Germany | 34.08 | 5.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Containment [25] as COUP`
- flags: `milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Containment[25], East European Unrest[29], Quagmire[45], Junta[50], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 3, DEFCON 2, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment COUP Cameroon | 49.90 | 4.00 | 46.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:4.5 |
| 2 | East European Unrest COUP Cameroon | 49.90 | 4.00 | 46.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:4.5 |
| 3 | Containment COUP Guatemala | 49.15 | 4.00 | 45.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:4.5 |
| 4 | East European Unrest COUP Guatemala | 49.15 | 4.00 | 45.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:4.5 |
| 5 | Junta COUP Cameroon | 43.55 | 4.00 | 39.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 113: T8 AR3 USSR

- chosen: `U2 Incident [63] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Fidel[8], Truman Doctrine[19], Willy Brandt[58], U2 Incident[63], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Cameroon | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Fidel COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Willy Brandt COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | U2 Incident INFLUENCE Poland, West Germany | 32.75 | 5.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Sadat Expels Soviets COUP Cameroon | 28.90 | 4.00 | 45.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `East European Unrest [29] as COUP`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], Quagmire[45], Junta[50], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest COUP Cameroon | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | East European Unrest COUP Guatemala | 48.15 | 4.00 | 44.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | East European Unrest INFLUENCE East Germany, France, West Germany | 46.05 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Junta COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Junta COUP Guatemala | 41.80 | 4.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Fidel[8], Truman Doctrine[19], Willy Brandt[58], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Cameroon | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 2 | Fidel COUP Saharan States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 3 | Fidel COUP SE African States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 4 | Fidel COUP Sudan | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |
| 5 | Fidel COUP Zimbabwe | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:5, milops_urgency:1.25, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Junta [50] as COUP`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Quagmire[45], Junta[50], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta COUP Cameroon | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Guatemala | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:3.5 |
| 3 | Captured Nazi Scientist COUP Cameroon | 36.95 | 4.00 | 33.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Guatemala | 36.20 | 4.00 | 32.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:2.5 |
| 5 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 35.95 | 5.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Willy Brandt [58] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Truman Doctrine[19], Willy Brandt[58], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Cameroon | 44.55 | 4.00 | 40.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | Sadat Expels Soviets COUP Cameroon | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Cameroon | 28.55 | 4.00 | 40.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Cameroon | 26.20 | 4.00 | 34.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Saharan States | 22.55 | 4.00 | 18.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:1.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Quagmire[45], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Guatemala | 37.45 | 4.00 | 33.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 2 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 32.62 | 5.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 3 | Glasnost COUP Guatemala | 32.50 | 4.00 | 53.10 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 4 | Quagmire COUP Guatemala | 30.15 | 4.00 | 46.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Captured Nazi Scientist COUP Ivory Coast | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Ivory Coast, milops_need:5, milops_urgency:1.67, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Sadat Expels Soviets [73] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Truman Doctrine[19], Nixon Plays the China Card[72], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets COUP Cameroon | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Sadat Expels Soviets COUP Guatemala | 32.65 | 4.00 | 49.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Cameroon | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Nixon Plays the China Card COUP Guatemala | 30.30 | 4.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Cameroon | 28.70 | 4.00 | 36.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Glasnost [93] as COUP`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Quagmire[45], Marine Barracks Bombing[91], Glasnost[93]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost COUP Cameroon | 35.75 | 4.00 | 56.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:5.5, offside_ops_penalty |
| 2 | Quagmire COUP Cameroon | 33.40 | 4.00 | 49.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Marine Barracks Bombing COUP Cameroon | 31.05 | 4.00 | 43.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Glasnost COUP Saharan States | 13.75 | 4.00 | 34.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:5.5, offside_ops_penalty |
| 5 | Glasnost COUP SE African States | 13.75 | 4.00 | 34.35 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:2.50, empty_coup_penalty, expected_swing:5.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 121: T8 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Truman Doctrine[19], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Cameroon | 38.55 | 4.00 | 50.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Guatemala | 37.80 | 4.00 | 50.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Cameroon | 36.20 | 4.00 | 44.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Guatemala | 35.45 | 4.00 | 43.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Nixon Plays the China Card COUP Saharan States | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Quagmire [45] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Quagmire[45], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 2, MilOps U3/A4, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Cameroon | 37.90 | 4.00 | 54.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Marine Barracks Bombing COUP Cameroon | 35.55 | 4.00 | 47.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Quagmire COUP Saharan States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | Quagmire COUP SE African States | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Quagmire COUP Sudan | 15.90 | 4.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-4`

## Step 123: T9 AR0 USSR

- chosen: `Wargames [103] as EVENT`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Fidel[8], Olympic Games[20], UN Intervention[32], Formosan Resolution[35], Summit[48], Che[83], Star Wars[88], The Reformer[90], Wargames[103]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | The Reformer EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Red Scare/Purge[31], Bear Trap[47], Allende[57], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Summit [48] as COUP`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Fidel[8], Olympic Games[20], UN Intervention[32], Formosan Resolution[35], Summit[48], Che[83], Star Wars[88], The Reformer[90]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit COUP Guatemala | 49.01 | 4.00 | 45.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 2 | Che COUP Guatemala | 49.01 | 4.00 | 45.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 3 | The Reformer COUP Guatemala | 49.01 | 4.00 | 45.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | Fidel COUP Guatemala | 42.66 | 4.00 | 38.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 5 | Olympic Games COUP Guatemala | 42.66 | 4.00 | 38.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 126: T9 AR1 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:9`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Bear Trap[47], Allende[57], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 3, MilOps U3/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Angola | 52.26 | 4.00 | 48.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 2 | Bear Trap COUP Angola | 52.26 | 4.00 | 48.71 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Angola, battleground_coup, milops_need:9, milops_urgency:1.29, defcon_penalty:3, coup_access_open, expected_swing:4.5 |
| 3 | Duck and Cover COUP Cameroon | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 4 | Bear Trap COUP Cameroon | 49.76 | 4.00 | 46.21 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |
| 5 | Duck and Cover COUP Guatemala | 49.01 | 4.00 | 45.46 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 127: T9 AR2 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Olympic Games[20], UN Intervention[32], Formosan Resolution[35], Che[83], Star Wars[88], The Reformer[90]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE Poland, West Germany | 32.75 | 5.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | The Reformer INFLUENCE Poland, West Germany | 32.75 | 5.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Che COUP Cameroon | 26.90 | 4.00 | 23.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |
| 4 | Che COUP Saharan States | 26.90 | 4.00 | 23.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |
| 5 | Che COUP SE African States | 26.90 | 4.00 | 23.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Bear Trap [47] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Bear Trap[47], Allende[57], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap COUP Cameroon | 48.90 | 4.00 | 45.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Bear Trap COUP Guatemala | 48.15 | 4.00 | 44.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Bear Trap INFLUENCE East Germany, France, West Germany | 46.05 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Puppet Governments COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Our Man in Tehran COUP Cameroon | 42.55 | 4.00 | 38.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `The Reformer [90] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Olympic Games[20], UN Intervention[32], Formosan Resolution[35], Star Wars[88], The Reformer[90]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer COUP Cameroon | 49.50 | 4.00 | 45.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5 |
| 2 | Fidel COUP Cameroon | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Olympic Games COUP Cameroon | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | UN Intervention COUP Cameroon | 36.80 | 4.00 | 32.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:2.5 |
| 5 | The Reformer INFLUENCE East Germany, West Germany | 28.15 | 5.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Puppet Governments [67] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Allende[57], U2 Incident[63], Puppet Governments[67], Our Man in Tehran[84], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments COUP Cameroon | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP Cameroon | 43.15 | 4.00 | 39.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 3 | Puppet Governments COUP Guatemala | 42.40 | 4.00 | 38.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 4 | Our Man in Tehran COUP Guatemala | 42.40 | 4.00 | 38.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:3.5 |
| 5 | U2 Incident COUP Cameroon | 29.50 | 4.00 | 45.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.20, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Fidel[8], Olympic Games[20], UN Intervention[32], Formosan Resolution[35], Star Wars[88]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Cameroon | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games COUP Cameroon | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | UN Intervention COUP Cameroon | 37.70 | 4.00 | 33.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 4 | Formosan Resolution COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Star Wars COUP Cameroon | 28.05 | 4.00 | 40.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Allende[57], U2 Incident[63], Our Man in Tehran[84], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Cameroon | 44.05 | 4.00 | 40.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | Our Man in Tehran COUP Guatemala | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | U2 Incident COUP Cameroon | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Iranian Hostage Crisis COUP Cameroon | 30.40 | 4.00 | 46.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | U2 Incident COUP Guatemala | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Olympic Games[20], UN Intervention[32], Formosan Resolution[35], Star Wars[88]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Cameroon | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 2 | Olympic Games COUP Saharan States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 3 | Olympic Games COUP SE African States | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Olympic Games COUP Sudan | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Olympic Games COUP Zimbabwe | 23.55 | 4.00 | 19.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `U2 Incident [63] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Allende[57], U2 Incident[63], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Cameroon | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Iranian Hostage Crisis COUP Cameroon | 31.90 | 4.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | U2 Incident COUP Guatemala | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Iranian Hostage Crisis COUP Guatemala | 31.15 | 4.00 | 47.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Cameroon | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `UN Intervention[32], Formosan Resolution[35], Star Wars[88]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Cameroon | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5 |
| 2 | Formosan Resolution COUP Cameroon | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Star Wars COUP Cameroon | 32.55 | 4.00 | 44.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | UN Intervention COUP Saharan States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP SE African States | 20.20 | 4.00 | 16.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:3.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Iranian Hostage Crisis [85] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Allende[57], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis COUP Guatemala | 34.15 | 4.00 | 50.60 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Guatemala | 31.80 | 4.00 | 44.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Guatemala | 29.45 | 4.00 | 37.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Iranian Hostage Crisis COUP Ivory Coast | 24.50 | 4.00 | 40.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Ivory Coast | 22.15 | 4.00 | 34.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Ivory Coast, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Formosan Resolution[35], Star Wars[88]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Cameroon | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Star Wars COUP Cameroon | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP SE African States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Formosan Resolution COUP Sudan | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Allende[57]`
- state: `VP 3, DEFCON 2, MilOps U3/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Cameroon | 41.55 | 4.00 | 53.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Guatemala | 40.80 | 4.00 | 53.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Cameroon | 39.20 | 4.00 | 47.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Allende COUP Guatemala | 38.45 | 4.00 | 46.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Saharan States | 19.55 | 4.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 139: T10 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Blockade[10], De Gaulle Leads France[17], UN Intervention[32], NORAD[38], How I Learned to Stop Worrying[49], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Iran-Iraq War[105], Yuri and Samantha[106]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Ortega Elected in Nicaragua EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Yuri and Samantha EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Formosan Resolution[35], Cuban Missile Crisis[43], Nuclear Subs[44], Summit[48], South African Unrest[56], Ussuri River Skirmish[77], Che[83], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Blockade[10], UN Intervention[32], NORAD[38], How I Learned to Stop Worrying[49], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Iran-Iraq War[105], Yuri and Samantha[106]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Ortega Elected in Nicaragua INFLUENCE France, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | Iran-Iraq War INFLUENCE France, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Yuri and Samantha INFLUENCE France, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | NORAD INFLUENCE East Germany, France, West Germany | 27.62 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Formosan Resolution[35], Nuclear Subs[44], Summit[48], South African Unrest[56], Ussuri River Skirmish[77], Che[83], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 47.62 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 47.62 | 5.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 3 | Formosan Resolution INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 4 | Nuclear Subs INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | 31.47 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Ortega Elected in Nicaragua [94] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Blockade[10], UN Intervention[32], NORAD[38], Reagan Bombs Libya[87], Ortega Elected in Nicaragua[94], Iran-Iraq War[105], Yuri and Samantha[106]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua INFLUENCE East Germany, France | 33.97 | 5.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, non_coup_milops_penalty:13.33 |
| 2 | Iran-Iraq War INFLUENCE East Germany, France | 33.97 | 5.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, non_coup_milops_penalty:13.33 |
| 3 | Yuri and Samantha INFLUENCE East Germany, France | 33.97 | 5.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, non_coup_milops_penalty:13.33 |
| 4 | NORAD INFLUENCE East Germany, France, West Germany | 30.72 | 5.00 | 59.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Reagan Bombs Libya INFLUENCE East Germany, France | 17.97 | 5.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Formosan Resolution[35], Nuclear Subs[44], South African Unrest[56], Ussuri River Skirmish[77], Che[83], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 40.72 | 5.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Nuclear Subs INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Our Man in Tehran INFLUENCE East Germany, West Germany | 24.57 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 5 | Che INFLUENCE East Germany, France, West Germany | 20.72 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Blockade[10], UN Intervention[32], NORAD[38], Reagan Bombs Libya[87], Iran-Iraq War[105], Yuri and Samantha[106]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, France | 31.30 | 5.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, non_coup_milops_penalty:16.00 |
| 2 | Yuri and Samantha INFLUENCE East Germany, France | 31.30 | 5.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, non_coup_milops_penalty:16.00 |
| 3 | NORAD INFLUENCE East Germany, France, West Germany | 28.05 | 5.00 | 59.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Reagan Bombs Libya INFLUENCE East Germany, France | 15.30 | 5.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, control_break:France, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Blockade INFLUENCE East Germany | 10.15 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Formosan Resolution[35], Nuclear Subs[44], South African Unrest[56], Che[83], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Nuclear Subs INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Che INFLUENCE East Germany, France, West Germany | 18.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | South African Unrest INFLUENCE East Germany, West Germany | 5.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Yuri and Samantha [106] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Blockade[10], UN Intervention[32], NORAD[38], Reagan Bombs Libya[87], Yuri and Samantha[106]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha INFLUENCE East Germany, West Germany | 22.90 | 5.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | NORAD INFLUENCE East Germany, France, West Germany | 19.05 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 6.90 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Blockade INFLUENCE East Germany | 6.15 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:20.00 |
| 5 | UN Intervention INFLUENCE East Germany | 6.15 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Nuclear Subs[44], South African Unrest[56], Che[83], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Our Man in Tehran INFLUENCE East Germany, West Germany | 17.90 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 14.05 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 1.90 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Blockade[10], UN Intervention[32], NORAD[38], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 12.38 | 5.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 0.23 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | Blockade INFLUENCE East Germany | -0.52 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:26.67 |
| 4 | UN Intervention INFLUENCE East Germany | -0.52 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:26.67 |
| 5 | Reagan Bombs Libya SPACE | -14.47 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `South African Unrest[56], Che[83], Our Man in Tehran[84], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 11.23 | 5.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 7.38 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, West Germany | -4.77 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 5 | South African Unrest SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Reagan Bombs Libya [87] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Blockade[10], UN Intervention[32], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | -43.10 | 5.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | Blockade INFLUENCE East Germany | -43.85 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:70.00 |
| 3 | UN Intervention INFLUENCE East Germany | -43.85 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:70.00 |
| 4 | Reagan Bombs Libya SPACE | -57.80 | 1.00 | 4.00 | 0.00 | 7.50 | -0.30 | 0.00 | space_when_behind, space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | Blockade REALIGN Morocco | -65.01 | -1.00 | 6.14 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `South African Unrest[56], Che[83], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | -35.95 | 5.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | -48.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 4 | South African Unrest SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | Colonial Rear Guards SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Blockade[10], UN Intervention[32]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE East Germany | -83.85 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:110.00 |
| 2 | UN Intervention INFLUENCE East Germany | -83.85 | 5.00 | 21.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, control_break:East Germany, non_coup_milops_penalty:110.00 |
| 3 | Blockade REALIGN Morocco | -105.01 | -1.00 | 6.14 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:110.00 |
| 4 | UN Intervention REALIGN Morocco | -105.01 | -1.00 | 6.14 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:110.00 |
| 5 | Blockade EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `South African Unrest[56], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | -88.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | -88.10 | 5.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 3 | South African Unrest SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | Colonial Rear Guards SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 5 | South African Unrest EVENT | -116.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:110.00 |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`
