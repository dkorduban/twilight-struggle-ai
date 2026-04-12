# minimal_hybrid detailed rollout log

- seed: `20260414`
- winner: `USSR`
- final_vp: `1`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], Marshall Plan[23], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], Nasser[15], Captured Nazi Scientist[18], Marshall Plan[23], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Nasser COUP Iran | 64.38 | 4.00 | 60.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | Captured Nazi Scientist COUP Iran | 64.38 | 4.00 | 60.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Marshall Plan COUP Iran | 57.93 | 4.00 | 78.53 | 0.00 | -24.00 | -0.60 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:3.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | East European Unrest COUP Iran | 56.08 | 4.00 | 72.53 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], De Gaulle Leads France[17], Indo-Pakistani War[24], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Turkey, Indonesia, Philippines | 62.95 | 6.00 | 57.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 2 | Special Relationship INFLUENCE Turkey, Indonesia, Philippines | 62.95 | 6.00 | 57.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 3 | Indo-Pakistani War INFLUENCE North Korea, Indonesia, Philippines | 62.55 | 6.00 | 56.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 4 | Special Relationship INFLUENCE North Korea, Indonesia, Philippines | 62.55 | 6.00 | 56.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 5 | Indo-Pakistani War INFLUENCE East Germany, Indonesia, Philippines | 62.05 | 6.00 | 56.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Marshall Plan[23], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, Japan, Iran, Thailand | 56.85 | 6.00 | 75.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | Marshall Plan INFLUENCE Japan, South Korea, Iran, Thailand | 56.75 | 6.00 | 75.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | Marshall Plan INFLUENCE Japan, Iran, Thailand, Thailand | 56.42 | 6.00 | 75.03 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand, offside_ops_penalty |
| 4 | Marshall Plan INFLUENCE West Germany, South Korea, Iran, Thailand | 56.25 | 6.00 | 74.85 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | Marshall Plan INFLUENCE Japan, Pakistan, Iran, Thailand | 56.15 | 6.00 | 74.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Pakistan:14.95, access_touch:Pakistan, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], De Gaulle Leads France[17], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany, North Korea | 59.95 | 6.00 | 54.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 2 | Special Relationship INFLUENCE France, West Germany, North Korea | 59.95 | 6.00 | 54.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 3 | Special Relationship INFLUENCE West Germany, North Korea, Panama | 59.60 | 6.00 | 53.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.20 |
| 4 | Special Relationship INFLUENCE West Germany, Japan, North Korea | 59.55 | 6.00 | 53.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 5 | Special Relationship INFLUENCE East Germany, France, West Germany | 59.45 | 6.00 | 53.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, North Korea, Thailand | 51.60 | 6.00 | 66.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | NORAD INFLUENCE East Germany, North Korea, Thailand | 51.60 | 6.00 | 66.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | East European Unrest INFLUENCE North Korea, South Korea, Thailand | 48.60 | 6.00 | 63.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | NORAD INFLUENCE North Korea, South Korea, Thailand | 48.60 | 6.00 | 63.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | East European Unrest INFLUENCE East Germany, South Korea, Thailand | 48.10 | 6.00 | 62.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], De Gaulle Leads France[17], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE France, West Germany, Japan, Panama | 50.10 | 6.00 | 64.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 2 | De-Stalinization INFLUENCE France, West Germany, Japan, Panama | 50.10 | 6.00 | 64.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 3 | De Gaulle Leads France INFLUENCE France, Japan, North Korea, Panama | 50.00 | 6.00 | 64.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:North Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 4 | De Gaulle Leads France INFLUENCE France, Japan, South Korea, Panama | 50.00 | 6.00 | 64.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:South Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 5 | De-Stalinization INFLUENCE France, Japan, North Korea, Panama | 50.00 | 6.00 | 64.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:North Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china`
- hand: `Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Iran | 43.05 | 4.00 | 39.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Captured Nazi Scientist COUP Iran | 43.05 | 4.00 | 39.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | NORAD INFLUENCE Pakistan, South Korea, Thailand | 39.50 | 6.00 | 53.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 4 | NORAD INFLUENCE South Korea, Israel, Thailand | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 5 | NORAD INFLUENCE Japan, South Korea, Thailand | 39.20 | 6.00 | 53.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, West Germany, Japan, North Korea | 48.85 | 6.00 | 63.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | De-Stalinization INFLUENCE Italy, West Germany, Japan, South Korea | 48.85 | 6.00 | 63.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | De-Stalinization INFLUENCE Italy, Japan, North Korea, South Korea | 48.75 | 6.00 | 63.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | De-Stalinization INFLUENCE Italy, West Germany, Japan, Egypt | 48.50 | 6.00 | 62.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, North Korea, South Korea | 48.45 | 6.00 | 62.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE North Korea, South Korea, Thailand | 43.60 | 6.00 | 58.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE North Korea, Pakistan, Thailand | 43.00 | 6.00 | 57.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE North Korea, Israel, Thailand | 42.95 | 6.00 | 57.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 4 | NORAD INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty |
| 5 | NORAD INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Italy, West Germany, Japan | 40.95 | 6.00 | 51.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Arab-Israeli War INFLUENCE Italy, Japan, North Korea | 40.85 | 6.00 | 51.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Arab-Israeli War INFLUENCE Italy, Japan, South Korea | 40.85 | 6.00 | 51.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Arab-Israeli War INFLUENCE Italy, Japan, Egypt | 40.50 | 6.00 | 50.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Arab-Israeli War INFLUENCE Italy, West Germany, North Korea | 40.35 | 6.00 | 50.65 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Pakistan, Thailand | 26.60 | 6.00 | 36.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Formosan Resolution INFLUENCE Israel, Thailand | 26.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Formosan Resolution INFLUENCE Italy, Thailand | 26.10 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany, Japan | 30.65 | 6.00 | 36.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Romanian Abdication INFLUENCE West Germany, Japan | 30.65 | 6.00 | 36.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Blockade INFLUENCE Japan, North Korea | 30.55 | 6.00 | 36.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Blockade INFLUENCE Japan, South Korea | 30.55 | 6.00 | 36.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Romanian Abdication INFLUENCE Japan, North Korea | 30.55 | 6.00 | 36.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], Red Scare/Purge[31], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Duck and Cover[4], Five Year Plan[5], COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON -1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE India, Pakistan, Israel, Thailand | 79.25 | 6.00 | 73.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Nuclear Test Ban INFLUENCE India, Japan, Pakistan, Thailand | 79.00 | 6.00 | 73.60 | 0.00 | 0.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Nuclear Test Ban INFLUENCE Italy, India, Pakistan, Thailand | 78.80 | 6.00 | 73.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Nuclear Test Ban INFLUENCE India, Pakistan, Philippines, Thailand | 78.80 | 6.00 | 73.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Nuclear Test Ban INFLUENCE India, Pakistan, Saudi Arabia, Thailand | 78.65 | 6.00 | 73.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | Five Year Plan INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 4 | Five Year Plan INFLUENCE Japan, Egypt | 36.90 | 6.00 | 31.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 5 | Five Year Plan INFLUENCE East Germany, Japan | 36.75 | 6.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Italy, Japan, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 2 | Socialist Governments INFLUENCE Japan, Philippines, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 3 | Socialist Governments INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 4 | Socialist Governments INFLUENCE Italy, Philippines, Thailand | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 5 | Socialist Governments INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Syria | 28.20 | 4.00 | 24.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 2 | Independent Reds COUP Syria | 28.20 | 4.00 | 24.50 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5 |
| 3 | Truman Doctrine INFLUENCE Italy | 25.30 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.40 |
| 4 | UN Intervention INFLUENCE Italy | 25.30 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.40 |
| 5 | Olympic Games INFLUENCE Italy | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 21: T2 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Japan, Saudi Arabia, Philippines, Thailand | 49.75 | 6.00 | 68.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Philippines, Thailand | 49.60 | 6.00 | 68.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE India, Japan, Philippines, Thailand | 49.50 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE Japan, North Korea, Philippines, Thailand | 49.50 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE Japan, South Korea, Philippines, Thailand | 49.50 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `COMECON[14], Truman Doctrine[19], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 2 | UN Intervention INFLUENCE Japan | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 3 | Independent Reds INFLUENCE Japan | 26.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 4 | COMECON INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 5 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Fidel INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `none`
- hand: `COMECON[14], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Japan | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 2 | Independent Reds INFLUENCE Japan | 26.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 3 | COMECON INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 4 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 5 | Suez Crisis INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 3 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 4 | Korean War INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 5 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `none`
- hand: `COMECON[14], Independent Reds[22], Suez Crisis[28]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan | 26.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 2 | COMECON INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 3 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 4 | Suez Crisis INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 5 | Suez Crisis INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 3 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 4 | The Cambridge Five INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 5 | Decolonization INFLUENCE India, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `COMECON[14], Suez Crisis[28]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 2 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 3 | Suez Crisis INFLUENCE Italy, Japan | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty |
| 4 | Suez Crisis INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |
| 5 | COMECON INFLUENCE Italy, Philippines | 24.45 | 6.00 | 38.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty |

- effects: `VP -2, DEFCON +1, MilOps U+0/A-2`

## Step 29: T3 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Olympic Games[20], NATO[21], Independent Reds[22], Marshall Plan[23], CIA Created[26], UN Intervention[32], De-Stalinization[33]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], US/Japan Mutual Defense Pact[27], Decolonization[30], Nuclear Test Ban[34], NORAD[38]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], NATO[21], Independent Reds[22], Marshall Plan[23], CIA Created[26], UN Intervention[32]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Italy, Japan, Mexico, Thailand | 50.15 | 6.00 | 68.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Mexico:11.20, control_break:Mexico, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Marshall Plan INFLUENCE Italy, Japan, Mexico, Thailand | 50.15 | 6.00 | 68.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Mexico:11.20, control_break:Mexico, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | NATO INFLUENCE West Germany, Japan, Mexico, Thailand | 49.85 | 6.00 | 68.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Mexico:11.20, control_break:Mexico, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Marshall Plan INFLUENCE West Germany, Japan, Mexico, Thailand | 49.85 | 6.00 | 68.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Mexico:11.20, control_break:Mexico, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | NATO INFLUENCE India, Japan, Mexico, Thailand | 49.75 | 6.00 | 68.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Mexico:11.20, control_break:Mexico, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Nuclear Test Ban[34], NORAD[38]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, Iraq, Philippines | 77.45 | 6.00 | 72.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 2 | Nuclear Test Ban INFLUENCE Japan, North Korea, Iraq, Philippines | 77.35 | 6.00 | 71.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 3 | Nuclear Test Ban INFLUENCE Japan, South Korea, Iraq, Philippines | 77.35 | 6.00 | 71.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 4 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, Philippines | 77.20 | 6.00 | 71.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 5 | Nuclear Test Ban INFLUENCE West Germany, Japan, South Korea, Philippines | 77.20 | 6.00 | 71.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], Independent Reds[22], Marshall Plan[23], CIA Created[26], UN Intervention[32]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, Japan, Iraq, Thailand | 52.95 | 6.00 | 71.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | Marshall Plan INFLUENCE India, Japan, Iraq, Thailand | 52.85 | 6.00 | 71.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | Marshall Plan INFLUENCE Japan, North Korea, Iraq, Thailand | 52.85 | 6.00 | 71.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Marshall Plan INFLUENCE Japan, South Korea, Iraq, Thailand | 52.85 | 6.00 | 71.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Marshall Plan INFLUENCE Japan, Iraq, Indonesia, Thailand | 52.65 | 6.00 | 71.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30], NORAD[38]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, Saudi Arabia | 58.15 | 6.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 2 | NORAD INFLUENCE Japan, North Korea, Saudi Arabia | 58.05 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 3 | NORAD INFLUENCE Japan, South Korea, Saudi Arabia | 58.05 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 4 | NORAD INFLUENCE West Germany, Japan, North Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, non_coup_milops_penalty:3.60 |
| 5 | NORAD INFLUENCE West Germany, Japan, South Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Olympic Games[20], Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | UN Intervention COUP Indonesia | 42.70 | 4.00 | 38.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 3 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 4 | Olympic Games INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 5 | Olympic Games INFLUENCE India, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 36: T3 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | Socialist Governments INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Five Year Plan INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE India, North Korea, Thailand | 42.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Five Year Plan INFLUENCE North Korea, South Korea, Thailand | 42.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Five Year Plan INFLUENCE North Korea, Egypt, Thailand | 41.75 | 6.00 | 56.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | COMECON INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | COMECON INFLUENCE West Germany, Japan, Indonesia | 32.70 | 6.00 | 47.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | COMECON INFLUENCE Japan, North Korea, Indonesia | 32.60 | 6.00 | 47.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Independent Reds INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | UN Intervention INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:6.00 |
| 4 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 5 | Independent Reds INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iran | 26.05 | 4.00 | 22.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Mexico | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Captured Nazi Scientist INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:18.00 |
| 5 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:9.00 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:9.00 |
| 3 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:9.00 |
| 4 | UN Intervention INFLUENCE India | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55, non_coup_milops_penalty:9.00 |
| 5 | UN Intervention INFLUENCE North Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Decolonization[30]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Pakistan, Iran | 24.85 | 6.00 | 35.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Decolonization INFLUENCE Japan, Iran | 24.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Decolonization INFLUENCE West Germany, Iran | 24.05 | 6.00 | 34.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Decolonization INFLUENCE North Korea, Iran | 23.95 | 6.00 | 34.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Decolonization INFLUENCE South Korea, Iran | 23.95 | 6.00 | 34.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, influence:Iran:13.70, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 43: T4 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Marshall Plan[23], Arms Race[42], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Latin American Death Squads[70]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], COMECON[14], NATO[21], Decolonization[30], SALT Negotiations[46], Allende[57], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Korean War EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |
| 5 | Decolonization EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Marshall Plan[23], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Latin American Death Squads[70]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE UK, West Germany, Pakistan, Algeria | 47.10 | 6.00 | 65.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:3.43 |
| 2 | Marshall Plan INFLUENCE East Germany, West Germany, Pakistan, Algeria | 47.00 | 6.00 | 65.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:3.43 |
| 3 | Marshall Plan INFLUENCE France, West Germany, Pakistan, Algeria | 47.00 | 6.00 | 65.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:3.43 |
| 4 | Marshall Plan INFLUENCE East Germany, UK, West Germany, Pakistan | 46.95 | 6.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:3.43 |
| 5 | Marshall Plan INFLUENCE France, UK, West Germany, Pakistan | 46.95 | 6.00 | 65.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Pakistan:13.20, control_break:Pakistan, offside_ops_penalty, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], COMECON[14], Decolonization[30], SALT Negotiations[46], Allende[57], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE UK, Mexico, South Africa | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | SALT Negotiations INFLUENCE UK, West Germany, South Africa | 57.65 | 6.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | SALT Negotiations INFLUENCE UK, West Germany, Mexico | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 4 | SALT Negotiations INFLUENCE UK, Algeria, South Africa | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | SALT Negotiations INFLUENCE East Germany, UK, South Africa | 57.05 | 6.00 | 51.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65], Latin American Death Squads[70]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE Mexico, Algeria | 44.85 | 6.00 | 39.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.00 |
| 2 | Latin American Death Squads INFLUENCE Mexico, Morocco | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 3 | Latin American Death Squads INFLUENCE West Germany, Mexico | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.00 |
| 4 | Latin American Death Squads INFLUENCE East Germany, Mexico | 41.20 | 6.00 | 35.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.00 |
| 5 | Latin American Death Squads INFLUENCE France, Mexico | 41.20 | 6.00 | 35.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], COMECON[14], Decolonization[30], Allende[57], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Algeria, South Africa | 39.20 | 6.00 | 53.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | COMECON INFLUENCE East Germany, West Germany, South Africa | 39.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | COMECON INFLUENCE France, West Germany, South Africa | 39.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | COMECON INFLUENCE West Germany, India, South Africa | 38.80 | 6.00 | 53.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:India:13.80, access_touch:India, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | COMECON INFLUENCE East Germany, Algeria, South Africa | 38.60 | 6.00 | 53.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Algeria, Morocco | 37.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Bear Trap INFLUENCE West Germany, Algeria, Morocco | 37.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Duck and Cover INFLUENCE East Germany, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Duck and Cover INFLUENCE France, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Bear Trap INFLUENCE East Germany, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Decolonization[30], Allende[57], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Morocco, South Africa | 22.80 | 6.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Decolonization INFLUENCE Morocco, South Africa | 22.80 | 6.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Colonial Rear Guards INFLUENCE Morocco, South Africa | 22.80 | 6.00 | 33.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Korean War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Decolonization INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Bear Trap INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Bear Trap INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Bear Trap INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Decolonization[30], Allende[57], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Decolonization INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Decolonization INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Blockade[10], Nasser[15], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Iran | 25.22 | 4.00 | 21.37 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Nasser COUP Iran | 25.22 | 4.00 | 21.37 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Blockade COUP Syria | 22.72 | 4.00 | 18.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Syria | 22.72 | 4.00 | 18.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 5 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 54: T4 AR5 US

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Allende[57], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Colonial Rear Guards INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Colonial Rear Guards INFLUENCE India, South Africa | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:13.80, access_touch:India, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Colonial Rear Guards INFLUENCE Poland, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.00 |
| 2 | Nasser INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:18.00 |
| 3 | Nasser INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:18.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Lonely Hearts Club Band INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Tunisia | 13.05 | 4.00 | 21.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 2 | Allende COUP Tunisia | 13.05 | 4.00 | 21.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Lone Gunman COUP Tunisia | 13.05 | 4.00 | 21.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Romanian Abdication INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Allende INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP 0, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 2 | Lonely Hearts Club Band INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Lonely Hearts Club Band INFLUENCE West Germany, Cuba | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Lonely Hearts Club Band INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Allende [57] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Allende[57], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 2 | Lone Gunman INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Allende INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Lone Gunman INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Allende INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 59: T5 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Olympic Games[20], CIA Created[26], UN Intervention[32], The Cambridge Five[36], Brush War[39], Cuban Missile Crisis[43], Brezhnev Doctrine[54], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Five Year Plan[5], Arab-Israeli War[13], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], UN Intervention[32], We Will Bury You[53], Cultural Revolution[61], OPEC[64]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Olympic Games[20], CIA Created[26], UN Intervention[32], The Cambridge Five[36], Cuban Missile Crisis[43], Brezhnev Doctrine[54], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 3 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |
| 4 | Cuban Missile Crisis INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], UN Intervention[32], We Will Bury You[53], Cultural Revolution[61], OPEC[64]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, West Germany, Ethiopia, South Africa | 50.00 | 6.00 | 68.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 2 | We Will Bury You INFLUENCE France, West Germany, Ethiopia, South Africa | 50.00 | 6.00 | 68.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 3 | We Will Bury You INFLUENCE West Germany, India, Ethiopia, South Africa | 49.75 | 6.00 | 68.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:India:13.80, access_touch:India, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 4 | We Will Bury You INFLUENCE Poland, West Germany, Ethiopia, South Africa | 49.50 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 5 | We Will Bury You INFLUENCE West Germany, Cuba, Ethiopia, South Africa | 49.50 | 6.00 | 68.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Olympic Games[20], CIA Created[26], UN Intervention[32], The Cambridge Five[36], Brezhnev Doctrine[54], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:5.00 |
| 2 | Brezhnev Doctrine INFLUENCE France, West Germany, Cuba | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.00 |
| 3 | Brezhnev Doctrine INFLUENCE France, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:5.00 |
| 4 | Brezhnev Doctrine INFLUENCE France, Italy, West Germany | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:5.00 |
| 5 | Brezhnev Doctrine INFLUENCE France, West Germany, Morocco | 57.05 | 6.00 | 51.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Morocco:14.80, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Independent Reds[22], Suez Crisis[28], UN Intervention[32], Cultural Revolution[61], OPEC[64]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 2 | Independent Reds INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 3 | Independent Reds INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 4 | Independent Reds INFLUENCE India, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:13.80, access_touch:India, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 5 | Independent Reds INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Olympic Games[20], CIA Created[26], UN Intervention[32], The Cambridge Five[36], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Olympic Games INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Olympic Games INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Suez Crisis[28], UN Intervention[32], Cultural Revolution[61], OPEC[64]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Suez Crisis INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Cultural Revolution INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | OPEC INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `CIA Created[26], UN Intervention[32], The Cambridge Five[36], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 3 | The Cambridge Five INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:7.50 |
| 4 | The Cambridge Five INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:7.50 |
| 5 | The Cambridge Five INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], UN Intervention[32], Cultural Revolution[61], OPEC[64]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.50 |
| 2 | Cultural Revolution INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.50 |
| 3 | OPEC INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.50 |
| 4 | OPEC INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.50 |
| 5 | Cultural Revolution INFLUENCE West Germany, India, South Africa | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:India:13.80, access_touch:India, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `CIA Created[26], UN Intervention[32], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 2 | UN Intervention INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:10.00 |
| 3 | UN Intervention INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:10.00 |
| 4 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Our Man in Tehran INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], UN Intervention[32], OPEC[64]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | OPEC INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | OPEC INFLUENCE West Germany, India, South Africa | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:India:13.80, access_touch:India, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | OPEC INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | OPEC INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `CIA Created[26], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 3 | Our Man in Tehran INFLUENCE West Germany, Cuba | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | Our Man in Tehran INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Our Man in Tehran INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 2 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:30.00 |
| 3 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:30.00 |
| 4 | Arab-Israeli War INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Arab-Israeli War INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `CIA Created[26]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Saharan States | 10.45 | 4.00 | 18.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 3 | CIA Created INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 4 | CIA Created INFLUENCE France | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 5 | CIA Created COUP Guatemala | 9.20 | 4.00 | 17.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 74: T5 AR7 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:45.00 |
| 2 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:45.00 |
| 3 | Captured Nazi Scientist COUP Colombia | 22.45 | 4.00 | 18.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 22.45 | 4.00 | 18.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist COUP SE African States | 22.45 | 4.00 | 18.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Nuclear Test Ban[34], Quagmire[45], Muslim Revolution[59], Sadat Expels Soviets[73], Liberation Theology[76], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `How I Learned to Stop Worrying [49] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Blockade[10], How I Learned to Stop Worrying[49], Missile Envy[52], South African Unrest[56], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Voice of America[75], One Small Step[81]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+5`

## Step 77: T6 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Quagmire[45], Muslim Revolution[59], Sadat Expels Soviets[73], Liberation Theology[76], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 4, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 67.70 | 6.00 | 62.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.14 |
| 2 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Mexico | 67.60 | 6.00 | 62.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:5.14 |
| 3 | Muslim Revolution INFLUENCE East Germany, France, Italy, West Germany | 67.60 | 6.00 | 62.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:5.14 |
| 4 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Morocco | 67.45 | 6.00 | 62.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, non_coup_milops_penalty:5.14 |
| 5 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Egypt | 67.35 | 6.00 | 61.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Egypt:13.20, access_touch:Egypt, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Missile Envy [52] as COUP`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], Missile Envy[52], South African Unrest[56], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Voice of America[75], One Small Step[81]`
- state: `VP 2, DEFCON 4, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Indonesia | 45.59 | 4.00 | 41.89 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.14, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Indonesia | 45.59 | 4.00 | 41.89 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.14, coup_access_open, expected_swing:3.5 |
| 3 | Nixon Plays the China Card COUP Indonesia | 45.59 | 4.00 | 41.89 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.14, coup_access_open, expected_swing:3.5 |
| 4 | Voice of America COUP Indonesia | 45.59 | 4.00 | 41.89 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.14, coup_access_open, expected_swing:3.5 |
| 5 | One Small Step COUP Indonesia | 45.59 | 4.00 | 41.89 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.14, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Quagmire[45], Sadat Expels Soviets[73], Liberation Theology[76], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Quagmire INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Quagmire INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |
| 4 | Quagmire INFLUENCE France, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Quagmire INFLUENCE France, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], South African Unrest[56], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Voice of America[75], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.00 |
| 2 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.00 |
| 3 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.00 |
| 4 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.00 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Sadat Expels Soviets[73], Liberation Theology[76], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, West Germany, Mexico | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 2 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 3 | Marshall Plan INFLUENCE East Germany, France, West Germany, Morocco | 43.45 | 6.00 | 62.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 4 | Marshall Plan INFLUENCE East Germany, France, West Germany, Egypt | 43.35 | 6.00 | 61.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Egypt:13.20, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 5 | Marshall Plan INFLUENCE East Germany, France, West Germany, Iran | 43.35 | 6.00 | 61.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Iran:13.20, access_touch:Iran, offside_ops_penalty, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], South African Unrest[56], Nixon Plays the China Card[72], Voice of America[75], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.20 |
| 2 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.20 |
| 3 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.20 |
| 4 | Nixon Plays the China Card INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:1.20 |
| 5 | Nixon Plays the China Card INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Sadat Expels Soviets[73], Liberation Theology[76], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 2 | Olympic Games INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 5 | Olympic Games INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], South African Unrest[56], Voice of America[75], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.50 |
| 2 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:1.50 |
| 3 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:1.50 |
| 4 | Voice of America INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:1.50 |
| 5 | One Small Step INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Sadat Expels Soviets[73], Liberation Theology[76], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 2 | Liberation Theology INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | Liberation Theology INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:12.00 |
| 4 | Liberation Theology INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 5 | Liberation Theology INFLUENCE West Germany, Mexico | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], Blockade[10], South African Unrest[56], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 2 | One Small Step INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 3 | One Small Step INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 4 | One Small Step INFLUENCE India, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:13.80, access_touch:India, influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 5 | One Small Step INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Sadat Expels Soviets[73], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Sadat Expels Soviets INFLUENCE France, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], South African Unrest[56]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | South African Unrest INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Vietnam Revolts INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Vietnam Revolts INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | South African Unrest INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Ask Not What Your Country Can Do For You[78]`
- state: `VP 2, DEFCON 3, MilOps U0/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iran | 34.55 | 4.00 | 30.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:6, milops_urgency:6.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE France, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 90: T6 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], South African Unrest[56]`
- state: `VP 2, DEFCON 2, MilOps U1/A5, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | South African Unrest INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | South African Unrest INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | South African Unrest INFLUENCE India, South Africa | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:13.80, access_touch:India, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | South African Unrest INFLUENCE Poland, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-5`

## Step 91: T7 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Indo-Pakistani War[24], Decolonization[30], Red Scare/Purge[31], Special Relationship[37], Junta[50], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Independent Reds[22], Nuclear Test Ban[34], Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Socialist Governments [7] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Indo-Pakistani War[24], Decolonization[30], Special Relationship[37], Junta[50], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments COUP Indonesia | 55.15 | 4.00 | 51.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Socialist Governments INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Socialist Governments INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | Socialist Governments INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |
| 5 | Socialist Governments INFLUENCE France, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 94: T7 AR1 US

- chosen: `Ussuri River Skirmish [77] as COUP`
- flags: `milops_shortfall:7`
- hand: `De Gaulle Leads France[17], Independent Reds[22], Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish COUP Indonesia | 55.15 | 4.00 | 51.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Indonesia | 55.15 | 4.00 | 51.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Independent Reds COUP Indonesia | 48.30 | 4.00 | 44.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | John Paul II Elected Pope COUP Indonesia | 48.30 | 4.00 | 44.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Ussuri River Skirmish COUP Mexico | 41.00 | 4.00 | 37.45 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.00, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 95: T7 AR2 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Fidel[8], Indo-Pakistani War[24], Decolonization[30], Special Relationship[37], Junta[50], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Indonesia | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 2 | Indo-Pakistani War INFLUENCE West Germany, Indonesia | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE West Germany, Indonesia | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 4 | Junta INFLUENCE West Germany, Indonesia | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:4.00 |
| 5 | Willy Brandt INFLUENCE West Germany, Indonesia | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], Independent Reds[22], Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63], John Paul II Elected Pope[69], Alliance for Progress[79]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 3 | Alliance for Progress INFLUENCE France, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 4 | Alliance for Progress INFLUENCE India, South Africa | 37.65 | 6.00 | 32.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:13.80, access_touch:India, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 5 | Alliance for Progress INFLUENCE Poland, South Africa | 37.40 | 6.00 | 31.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Indo-Pakistani War[24], Decolonization[30], Special Relationship[37], Junta[50], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 2 | Indo-Pakistani War INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 3 | Decolonization INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 4 | Decolonization INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 5 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], Independent Reds[22], Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 3, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Mexico | 27.75 | 4.00 | 24.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 2 | John Paul II Elected Pope COUP Mexico | 27.75 | 4.00 | 24.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 3 | Independent Reds COUP Algeria | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 4 | John Paul II Elected Pope COUP Algeria | 27.00 | 4.00 | 23.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:1.5 |
| 5 | Independent Reds COUP Ethiopia | 23.40 | 4.00 | 19.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Ethiopia, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Decolonization[30], Special Relationship[37], Junta[50], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Decolonization INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63], John Paul II Elected Pope[69]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | John Paul II Elected Pope INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | John Paul II Elected Pope COUP Colombia | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | John Paul II Elected Pope COUP Saharan States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | John Paul II Elected Pope COUP SE African States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Special Relationship[37], Junta[50], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Willy Brandt INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Junta INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `De Gaulle Leads France[17], Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | U2 Incident INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | De Gaulle Leads France INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | U2 Incident INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Special Relationship[37], Willy Brandt[58], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 2 | Willy Brandt INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 3 | Willy Brandt INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:24.00 |
| 4 | Willy Brandt INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 5 | Willy Brandt INFLUENCE West Germany, Mexico | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], Flower Power[62], U2 Incident[63]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | U2 Incident INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | U2 Incident INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | U2 Incident INFLUENCE India, South Africa | 17.65 | 6.00 | 32.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:13.80, access_touch:India, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | U2 Incident INFLUENCE Poland, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Special Relationship[37], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Special Relationship INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Special Relationship INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Special Relationship INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Special Relationship INFLUENCE West Germany, Mexico | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], Flower Power[62]`
- state: `VP 0, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Colombia | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Portuguese Empire Crumbles COUP Saharan States | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Portuguese Empire Crumbles COUP SE African States | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Portuguese Empire Crumbles COUP Sudan | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Portuguese Empire Crumbles COUP Zimbabwe | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 107: T8 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Socialist Governments[7], Romanian Abdication[12], Arab-Israeli War[13], Junta[50], Portuguese Empire Crumbles[55], U2 Incident[63], John Paul II Elected Pope[69], One Small Step[81], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Pershing II Deployed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Summit [48] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37], Summit[48], Flower Power[62], Lone Gunman[109]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Vietnam Revolts EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |
| 5 | The Cambridge Five EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Junta[50], Portuguese Empire Crumbles[55], U2 Incident[63], John Paul II Elected Pope[69], One Small Step[81], Pershing II Deployed[102]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | U2 Incident INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | U2 Incident INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Pershing II Deployed INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], Indo-Pakistani War[24], The Cambridge Five[36], Special Relationship[37], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Indonesia | 47.84 | 4.00 | 44.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 2 | Special Relationship COUP Indonesia | 47.84 | 4.00 | 44.14 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 3 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Indo-Pakistani War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Special Relationship INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 111: T8 AR2 USSR

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Junta[50], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69], One Small Step[81], Pershing II Deployed[102]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Pershing II Deployed INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Pershing II Deployed INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Pershing II Deployed INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Pershing II Deployed INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], The Cambridge Five[36], Special Relationship[37], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.00 |
| 2 | Special Relationship INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.00 |
| 3 | Special Relationship INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.00 |
| 4 | Special Relationship INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:6.00 |
| 5 | Special Relationship INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Junta[50], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Junta INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 4 | Junta INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], The Cambridge Five[36], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 2 | Vietnam Revolts INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 5 | Flower Power INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Junta[50], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Junta INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], The Cambridge Five[36], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Flower Power INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | The Cambridge Five INFLUENCE Poland, West Germany | 22.40 | 6.00 | 32.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], Portuguese Empire Crumbles[55], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Flower Power INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Flower Power INFLUENCE Poland, West Germany | 22.40 | 6.00 | 32.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Flower Power INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Flower Power INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], John Paul II Elected Pope[69], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 2 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 3 | One Small Step INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:48.00 |
| 4 | One Small Step INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 5 | One Small Step INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Cuba | 14.40 | 4.00 | 22.55 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |
| 2 | Romanian Abdication COUP Cuba | 14.40 | 4.00 | 22.55 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |
| 3 | Lone Gunman COUP Cuba | 14.40 | 4.00 | 22.55 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cuba, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |
| 4 | Blockade COUP Mexico | 11.80 | 4.00 | 19.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP Mexico | 11.80 | 4.00 | 19.95 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Romanian Abdication[12], John Paul II Elected Pope[69]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Guatemala | 27.70 | 4.00 | 23.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Haiti | 27.70 | 4.00 | 23.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Saharan States | 27.45 | 4.00 | 23.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 5 | John Paul II Elected Pope INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 122: T8 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Romanian Abdication[12], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Guatemala | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Lone Gunman COUP Guatemala | 31.70 | 4.00 | 39.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Romanian Abdication COUP Colombia | 11.95 | 4.00 | 20.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Lone Gunman COUP Colombia | 11.95 | 4.00 | 20.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Romanian Abdication COUP El Salvador | 11.70 | 4.00 | 19.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 123: T9 AR0 USSR

- chosen: `Vietnam Revolts [9] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Korean War[11], Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Voice of America EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Arms Race [42] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Brush War[39], Arms Race[42], Muslim Revolution[59], Cultural Revolution[61], Camp David Accords[66], Nixon Plays the China Card[72], Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Brush War EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Korean War[11], Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | Iran-Iraq War INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | Korean War INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 4 | Korean War INFLUENCE France, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 5 | Iran-Iraq War INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Brush War[39], Muslim Revolution[59], Cultural Revolution[61], Camp David Accords[66], Nixon Plays the China Card[72], Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 46.70 | 6.00 | 65.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.71 |
| 2 | Muslim Revolution INFLUENCE East Germany, France, Italy, West Germany | 46.60 | 6.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:7.71 |
| 3 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 46.45 | 6.00 | 65.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:7.71 |
| 4 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Brazil | 46.10 | 6.00 | 64.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Brazil:13.70, access_touch:Brazil, offside_ops_penalty, non_coup_milops_penalty:7.71 |
| 5 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Venezuela | 46.10 | 6.00 | 64.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Star Wars[88], Iran-Iraq War[105]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, Poland, West Germany | 58.20 | 6.00 | 52.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Iran-Iraq War INFLUENCE France, Poland, West Germany | 58.20 | 6.00 | 52.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | Iran-Iraq War INFLUENCE East Germany, France, Poland | 57.60 | 6.00 | 51.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, control_break:Poland, non_coup_milops_penalty:9.00 |
| 4 | Iran-Iraq War INFLUENCE Italy, Poland, West Germany | 57.60 | 6.00 | 51.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:Poland:14.30, control_break:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Iran-Iraq War INFLUENCE Poland, Turkey, West Germany | 57.10 | 6.00 | 51.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, control_break:Poland, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Brush War[39], Cultural Revolution[61], Camp David Accords[66], Nixon Plays the China Card[72], Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Camp David Accords INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | Nixon Plays the China Card INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Camp David Accords INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Star Wars[88]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 2 | Our Man in Tehran INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 3 | Star Wars INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 4 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Brush War[39], Cultural Revolution[61], Nixon Plays the China Card[72], Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | Nixon Plays the China Card INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:10.80 |
| 4 | Nixon Plays the China Card INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Nixon Plays the China Card INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51], Our Man in Tehran[84], Star Wars[88]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 2 | Star Wars INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 3 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 4 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 5 | Our Man in Tehran INFLUENCE East Germany, Italy, West Germany | 38.60 | 6.00 | 48.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Brush War[39], Cultural Revolution[61], Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 2 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 3 | Che INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 4 | Brush War INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 5 | Brush War INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Star Wars [88] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51], Star Wars[88]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 3 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 4 | Star Wars INFLUENCE East Germany, Italy, West Germany | 38.60 | 6.00 | 48.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Star Wars INFLUENCE France, Italy, West Germany | 38.60 | 6.00 | 48.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Cultural Revolution[61], Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Cultural Revolution INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Cultural Revolution INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Che INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Kitchen Debates[51]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:54.00 |
| 2 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:54.00 |
| 3 | Captured Nazi Scientist INFLUENCE East Germany, France | 38.45 | 6.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:54.00 |
| 4 | Captured Nazi Scientist INFLUENCE Italy, West Germany | 38.45 | 6.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:54.00 |
| 5 | Captured Nazi Scientist INFLUENCE Turkey, West Germany | 37.95 | 6.00 | 32.10 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Che[83], Yuri and Samantha[106]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Che INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Che INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Che INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Che INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `CIA Created[26], Kitchen Debates[51]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Iran | 28.30 | 4.00 | 36.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:9, milops_urgency:9.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 2 | Kitchen Debates COUP Iran | 28.30 | 4.00 | 36.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:9, milops_urgency:9.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | CIA Created INFLUENCE East Germany, West Germany | 27.05 | 6.00 | 33.20 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 4 | CIA Created INFLUENCE France, West Germany | 27.05 | 6.00 | 33.20 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Kitchen Debates INFLUENCE East Germany, West Germany | 27.05 | 6.00 | 33.20 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 138: T9 AR7 US

- chosen: `Yuri and Samantha [106] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Yuri and Samantha[106]`
- state: `VP 1, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Yuri and Samantha INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Yuri and Samantha INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 4 | Yuri and Samantha INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Yuri and Samantha INFLUENCE West Germany, Cuba | 22.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Glasnost [93] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Olympic Games[20], Quagmire[45], Allende[57], Grain Sales to Soviets[68], Liberation Theology[76], Glasnost[93], Chernobyl[97], Defectors[108]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Tear Down this Wall [99] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Independent Reds[22], Quagmire[45], We Will Bury You[53], Willy Brandt[58], Puppet Governments[67], Terrorism[95], Tear Down this Wall[99], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | AWACS Sale to Saudis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Terrorism EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Olympic Games[20], Quagmire[45], Allende[57], Grain Sales to Soviets[68], Liberation Theology[76], Chernobyl[97], Defectors[108]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, West Germany, Iran | 58.20 | 6.00 | 52.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, access_touch:East Germany, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, non_coup_milops_penalty:8.57 |
| 2 | Quagmire INFLUENCE East Germany, France, Iran | 57.60 | 6.00 | 52.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, access_touch:East Germany, influence:France:16.30, influence:Iran:12.95, control_break:Iran, non_coup_milops_penalty:8.57 |
| 3 | Quagmire INFLUENCE East Germany, Italy, Iran | 57.00 | 6.00 | 51.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, access_touch:East Germany, influence:Italy:15.70, influence:Iran:12.95, control_break:Iran, non_coup_milops_penalty:8.57 |
| 4 | Quagmire INFLUENCE France, West Germany, Iran | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, non_coup_milops_penalty:8.57 |
| 5 | Quagmire INFLUENCE East Germany, France, West Germany | 56.55 | 6.00 | 51.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, access_touch:East Germany, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Independent Reds[22], Quagmire[45], We Will Bury You[53], Willy Brandt[58], Puppet Governments[67], Terrorism[95], Solidarity[104], AWACS Sale to Saudis[107]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | AWACS Sale to Saudis INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.57 |
| 5 | AWACS Sale to Saudis INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Olympic Games[20], Allende[57], Grain Sales to Soviets[68], Liberation Theology[76], Chernobyl[97], Defectors[108]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Indonesia | 48.88 | 4.00 | 45.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games COUP Indonesia | 48.88 | 4.00 | 45.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 3 | Liberation Theology COUP Indonesia | 48.88 | 4.00 | 45.18 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:3.5 |
| 4 | Allende COUP Indonesia | 42.03 | 4.00 | 38.18 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:10, milops_urgency:1.67, coup_access_open, expected_swing:2.5 |
| 5 | Fidel INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 144: T10 AR2 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Independent Reds[22], Quagmire[45], We Will Bury You[53], Willy Brandt[58], Puppet Governments[67], Terrorism[95], Solidarity[104]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, Italy, West Germany | 46.60 | 6.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | We Will Bury You INFLUENCE East Germany, France, West Germany, Cuba | 46.45 | 6.00 | 65.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | We Will Bury You INFLUENCE East Germany, France, West Germany, Brazil | 46.10 | 6.00 | 64.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Brazil:13.70, access_touch:Brazil, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | We Will Bury You INFLUENCE East Germany, France, West Germany, Venezuela | 46.10 | 6.00 | 64.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | We Will Bury You INFLUENCE East Germany, France, West Germany, India | 45.95 | 6.00 | 64.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:India:13.55, access_touch:India, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Olympic Games[20], Allende[57], Grain Sales to Soviets[68], Liberation Theology[76], Chernobyl[97], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Olympic Games INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Olympic Games INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Independent Reds[22], Quagmire[45], Willy Brandt[58], Puppet Governments[67], Terrorism[95], Solidarity[104]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Independent Reds INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Puppet Governments INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Terrorism INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Allende[57], Grain Sales to Soviets[68], Liberation Theology[76], Chernobyl[97], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Liberation Theology INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Liberation Theology INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 4 | Liberation Theology INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Liberation Theology INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Quagmire[45], Willy Brandt[58], Puppet Governments[67], Terrorism[95], Solidarity[104]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 2 | Puppet Governments INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 3 | Terrorism INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 4 | Terrorism INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 5 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Allende[57], Grain Sales to Soviets[68], Chernobyl[97], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Chernobyl INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Chernobyl INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Chernobyl INFLUENCE East Germany, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Chernobyl INFLUENCE France, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Terrorism [95] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Quagmire[45], Willy Brandt[58], Terrorism[95], Solidarity[104]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Terrorism INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Terrorism INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 3 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 4 | Solidarity INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | Terrorism INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Allende[57], Grain Sales to Soviets[68], Defectors[108]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Jordan | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Jordan, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:0.5 |
| 2 | Allende COUP Syria | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:0.5 |
| 3 | Allende COUP Mexico | 25.80 | 4.00 | 21.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:4.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Allende COUP Algeria | 25.55 | 4.00 | 21.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:4.00, defcon_penalty:3, expected_swing:0.5 |
| 5 | Allende COUP Israel | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:8, milops_urgency:4.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Solidarity [104] as COUP`
- flags: `milops_shortfall:10`
- hand: `Quagmire[45], Willy Brandt[58], Solidarity[104]`
- state: `VP 4, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity COUP Iran | 39.15 | 4.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:10, milops_urgency:5.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:60.00 |
| 3 | Solidarity INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:60.00 |
| 4 | Solidarity INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:60.00 |
| 5 | Solidarity INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 153: T10 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Grain Sales to Soviets[68], Defectors[108]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 3 | Defectors INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 4 | Defectors INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Quagmire[45], Willy Brandt[58]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, West Germany, Iran | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 2 | Quagmire INFLUENCE France, West Germany, Iran | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 3 | Quagmire INFLUENCE East Germany, France, Iran | 36.10 | 6.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Iran:12.95, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 4 | Quagmire INFLUENCE Italy, West Germany, Iran | 36.10 | 6.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 5 | Quagmire INFLUENCE West Germany, Iran, Cuba | 35.95 | 6.00 | 50.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Iran:12.95, control_break:Iran, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:72.00 |

- effects: `VP -3, DEFCON +1, MilOps U-2/A-2`
