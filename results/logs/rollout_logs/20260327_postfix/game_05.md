# minimal_hybrid detailed rollout log

- seed: `20260414`
- winner: `USSR`
- final_vp: `-1`
- end_turn: `4`
- end_reason: `defcon1`

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

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Iran | 40.55 | 4.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Formosan Resolution COUP Iran | 30.40 | 4.00 | 42.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE Pakistan, Thailand | 26.60 | 6.00 | 36.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution INFLUENCE Israel, Thailand | 26.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Japan, Pakistan, Israel, Thailand | 74.85 | 6.00 | 69.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Nuclear Test Ban INFLUENCE Italy, Pakistan, Israel, Thailand | 74.65 | 6.00 | 69.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Nuclear Test Ban INFLUENCE Pakistan, Israel, Philippines, Thailand | 74.65 | 6.00 | 69.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Nuclear Test Ban INFLUENCE Pakistan, Israel, Saudi Arabia, Thailand | 74.50 | 6.00 | 69.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Nuclear Test Ban INFLUENCE Italy, Japan, Pakistan, Thailand | 74.40 | 6.00 | 69.00 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan | 42.35 | 6.00 | 36.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.00 |
| 2 | Five Year Plan INFLUENCE Japan, North Korea | 42.25 | 6.00 | 36.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE Japan, South Korea | 42.25 | 6.00 | 36.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 4 | Five Year Plan INFLUENCE Japan, Egypt | 41.90 | 6.00 | 36.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 5 | Five Year Plan INFLUENCE East Germany, Japan | 41.75 | 6.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE India, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 2 | Socialist Governments INFLUENCE Japan, Pakistan, Thailand | 62.10 | 6.00 | 56.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 3 | Socialist Governments INFLUENCE Italy, Pakistan, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 4 | Socialist Governments INFLUENCE Pakistan, Philippines, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 5 | Socialist Governments INFLUENCE Pakistan, Saudi Arabia, Thailand | 61.75 | 6.00 | 56.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 3 | Olympic Games INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 4 | Independent Reds INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 5 | Truman Doctrine INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, Japan, Philippines, Thailand | 49.90 | 6.00 | 68.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE Italy, Japan, Saudi Arabia, Thailand | 49.75 | 6.00 | 68.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE Japan, Saudi Arabia, Philippines, Thailand | 49.75 | 6.00 | 68.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE Italy, West Germany, Japan, Thailand | 49.60 | 6.00 | 68.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Philippines, Thailand | 49.60 | 6.00 | 68.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Italy | 25.30 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:3.00 |
| 2 | UN Intervention INFLUENCE Philippines | 25.30 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 3 | Olympic Games INFLUENCE Italy | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:3.00 |
| 4 | Olympic Games INFLUENCE Philippines | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 5 | Independent Reds INFLUENCE Italy | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Fidel INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Olympic Games[20], Independent Reds[22], Suez Crisis[28]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan | 26.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |
| 2 | Independent Reds INFLUENCE Japan | 26.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:4.00 |
| 3 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Suez Crisis INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Olympic Games INFLUENCE Philippines | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 3 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 4 | Korean War INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 5 | Decolonization INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Independent Reds[22], Suez Crisis[28]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan | 26.85 | 6.00 | 21.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:12.00 |
| 2 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Suez Crisis INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Independent Reds INFLUENCE Philippines | 25.15 | 6.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:12.00 |
| 5 | COMECON INFLUENCE West Germany, Japan | 22.35 | 6.00 | 36.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 3 | Decolonization INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 4 | The Cambridge Five INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 5 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `COMECON[14], Suez Crisis[28]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Suez Crisis INFLUENCE Japan, Philippines | 26.15 | 6.00 | 40.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | COMECON INFLUENCE West Germany, Japan | 22.35 | 6.00 | 36.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Suez Crisis INFLUENCE West Germany, Japan | 22.35 | 6.00 | 36.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | COMECON INFLUENCE Japan, North Korea | 22.25 | 6.00 | 36.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 29: T3 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Olympic Games[20], NATO[21], Independent Reds[22], Marshall Plan[23], CIA Created[26], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Italy, Japan, Ethiopia, Thailand | 51.30 | 6.00 | 69.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Marshall Plan INFLUENCE Italy, Japan, Ethiopia, Thailand | 51.30 | 6.00 | 69.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | NATO INFLUENCE Japan, Saudi Arabia, Ethiopia, Thailand | 51.15 | 6.00 | 69.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Marshall Plan INFLUENCE Japan, Saudi Arabia, Ethiopia, Thailand | 51.15 | 6.00 | 69.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | NATO INFLUENCE West Germany, Japan, Ethiopia, Thailand | 51.00 | 6.00 | 69.60 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Ethiopia:10.85, control_break:Ethiopia, access_touch:Ethiopia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30], Nuclear Test Ban[34], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, South Korea | 73.30 | 6.00 | 67.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 2 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, Egypt | 72.95 | 6.00 | 67.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 3 | Nuclear Test Ban INFLUENCE West Germany, Japan, South Korea, Egypt | 72.95 | 6.00 | 67.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 4 | Nuclear Test Ban INFLUENCE Japan, North Korea, South Korea, Egypt | 72.85 | 6.00 | 67.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:South Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 5 | Nuclear Test Ban INFLUENCE East Germany, West Germany, Japan, North Korea | 72.80 | 6.00 | 67.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], Independent Reds[22], Marshall Plan[23], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, North Korea, Saudi Arabia, Thailand | 54.35 | 6.00 | 72.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 54.20 | 6.00 | 72.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | Marshall Plan INFLUENCE India, Japan, North Korea, Thailand | 54.10 | 6.00 | 72.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Marshall Plan INFLUENCE Japan, North Korea, South Korea, Thailand | 54.10 | 6.00 | 72.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Marshall Plan INFLUENCE Japan, North Korea, Indonesia, Thailand | 53.90 | 6.00 | 72.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, North Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, non_coup_milops_penalty:3.60 |
| 2 | NORAD INFLUENCE West Germany, Japan, South Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |
| 3 | NORAD INFLUENCE Japan, North Korea, South Korea | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |
| 4 | NORAD INFLUENCE West Germany, Japan, Egypt | 57.55 | 6.00 | 52.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.60 |
| 5 | NORAD INFLUENCE Japan, North Korea, Egypt | 57.45 | 6.00 | 51.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Olympic Games[20], Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 2 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Olympic Games INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:4.50 |
| 4 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 5 | Five Year Plan INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Five Year Plan INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Five Year Plan INFLUENCE India, North Korea, Thailand | 42.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Five Year Plan INFLUENCE North Korea, South Korea, Thailand | 42.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Five Year Plan INFLUENCE North Korea, Indonesia, Thailand | 41.90 | 6.00 | 56.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], COMECON[14], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | COMECON INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | COMECON INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | COMECON INFLUENCE Japan, North Korea, Egypt | 32.45 | 6.00 | 46.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Independent Reds INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | UN Intervention INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 5 | Independent Reds INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Syria | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Israel | 22.75 | 4.00 | 18.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |
| 3 | Captured Nazi Scientist INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:18.00 |
| 5 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:27.00 |
| 2 | UN Intervention COUP Israel | 25.75 | 4.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3 |
| 3 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:27.00 |
| 4 | UN Intervention COUP Ethiopia | 21.70 | 4.00 | 17.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Ethiopia, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Decolonization INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Decolonization INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Decolonization INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Decolonization INFLUENCE East Germany, Japan | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP -1, DEFCON +1, MilOps U+0/A-1`

## Step 43: T4 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Independent Reds[22], Decolonization[30], Arms Race[42], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], NATO[21], CIA Created[26], SALT Negotiations[46], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Korean War EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Independent Reds[22], Decolonization[30], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Indonesia | 47.44 | 4.00 | 43.74 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |
| 2 | Blockade COUP Indonesia | 40.59 | 4.00 | 36.74 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 3 | Nasser COUP Indonesia | 40.59 | 4.00 | 36.74 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 4 | Decolonization INFLUENCE West Germany, Mexico | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 5 | Decolonization INFLUENCE Mexico, Algeria | 37.85 | 6.00 | 32.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 46: T4 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], SALT Negotiations[46], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | SALT Negotiations INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | SALT Negotiations INFLUENCE East Germany, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | SALT Negotiations INFLUENCE France, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | SALT Negotiations INFLUENCE West Germany, Algeria, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Blockade[10], Nasser[15], Independent Reds[22], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Mexico, Algeria | 33.85 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Bear Trap INFLUENCE West Germany, Mexico, Algeria | 33.85 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Duck and Cover INFLUENCE UK, West Germany, Mexico | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Bear Trap INFLUENCE UK, West Germany, Mexico | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Duck and Cover INFLUENCE East Germany, West Germany, Mexico | 33.70 | 6.00 | 48.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 43.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Latin American Death Squads INFLUENCE Algeria, South Africa | 43.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Latin American Death Squads INFLUENCE East Germany, South Africa | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Latin American Death Squads INFLUENCE France, South Africa | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Latin American Death Squads INFLUENCE Poland, South Africa | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Nasser[15], Independent Reds[22], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE West Germany, Algeria, Morocco | 37.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 2 | Bear Trap INFLUENCE UK, Algeria, Morocco | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 3 | Bear Trap INFLUENCE East Germany, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 4 | Bear Trap INFLUENCE France, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 5 | Bear Trap INFLUENCE UK, West Germany, Algeria | 36.55 | 6.00 | 51.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Algeria | 28.65 | 4.00 | 24.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created COUP Mexico | 24.40 | 4.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.80, defcon_penalty:3, expected_swing:0.5 |
| 3 | Korean War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 5 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 51: T4 AR4 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Nasser[15], Independent Reds[22], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 2 | Nasser INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 3 | Blockade INFLUENCE UK | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:UK:14.15, access_touch:UK, non_coup_milops_penalty:3.00 |
| 4 | Nasser INFLUENCE UK | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:UK:14.15, access_touch:UK, non_coup_milops_penalty:3.00 |
| 5 | Independent Reds INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Korean War INFLUENCE Algeria, South Africa | 22.20 | 6.00 | 32.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | Colonial Rear Guards INFLUENCE Algeria, South Africa | 22.20 | 6.00 | 32.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | Korean War INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Nasser[15], Independent Reds[22], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 2 | Nasser INFLUENCE UK | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:UK:14.15, access_touch:UK, non_coup_milops_penalty:4.00 |
| 3 | Independent Reds INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Lonely Hearts Club Band INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Nasser INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Colonial Rear Guards INFLUENCE Algeria, South Africa | 22.20 | 6.00 | 32.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Colonial Rear Guards INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Colonial Rear Guards INFLUENCE Poland, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Independent Reds[22], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Lonely Hearts Club Band INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Independent Reds INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Independent Reds INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE UK | 13.00 | 6.00 | 19.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:UK:14.15, control_break:UK, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Allende INFLUENCE UK | 13.00 | 6.00 | 19.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:UK:14.15, control_break:UK, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Romanian Abdication COUP Algeria | 12.55 | 4.00 | 20.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:2, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Allende COUP Algeria | 12.55 | 4.00 | 20.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:2, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Romanian Abdication INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Lonely Hearts Club Band INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Lonely Hearts Club Band INFLUENCE West Germany, Cuba | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Lonely Hearts Club Band INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Allende [57] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Algeria | 15.55 | 4.00 | 23.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:2, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 2 | Allende COUP Mexico | 11.30 | 4.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:2, expected_swing:0.5, offside_ops_penalty |
| 3 | Allende INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Allende INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Allende INFLUENCE Algeria | 9.55 | 6.00 | 15.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`
