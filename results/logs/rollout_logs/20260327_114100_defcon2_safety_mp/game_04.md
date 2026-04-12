# minimal_hybrid detailed rollout log

- seed: `20260413`
- winner: `USSR`
- final_vp: `4`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], Truman Doctrine[19], Indo-Pakistani War[24], De-Stalinization[33], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], COMECON[14], Olympic Games[20], CIA Created[26], US/Japan Mutual Defense Pact[27], Suez Crisis[28], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Truman Doctrine[19], Indo-Pakistani War[24], De-Stalinization[33], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Iran | 76.08 | 4.00 | 72.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Korean War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Arab-Israeli War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Indo-Pakistani War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, Thailand | 62.30 | 6.00 | 56.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], COMECON[14], Olympic Games[20], CIA Created[26], Suez Crisis[28], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Indonesia, Philippines | 45.50 | 6.00 | 39.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 2 | Olympic Games INFLUENCE Turkey, Indonesia | 43.50 | 6.00 | 37.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:1.00 |
| 3 | Olympic Games INFLUENCE North Korea, Indonesia | 43.10 | 6.00 | 37.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:1.00 |
| 4 | COMECON INFLUENCE Turkey, Indonesia, Philippines | 42.80 | 6.00 | 57.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |
| 5 | Suez Crisis INFLUENCE Turkey, Indonesia, Philippines | 42.80 | 6.00 | 57.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Korean War [11] as COUP`
- flags: `holds_china`
- hand: `Korean War[11], Arab-Israeli War[13], Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Arab-Israeli War COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Indo-Pakistani War COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Korean War INFLUENCE Iran, Thailand | 46.35 | 6.00 | 40.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand |
| 5 | Arab-Israeli War INFLUENCE Iran, Thailand | 46.35 | 6.00 | 40.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], COMECON[14], CIA Created[26], Suez Crisis[28], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, Turkey, North Korea | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 2 | COMECON INFLUENCE France, Turkey, North Korea | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 3 | Suez Crisis INFLUENCE East Germany, Turkey, North Korea | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 4 | Suez Crisis INFLUENCE France, Turkey, North Korea | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 5 | COMECON INFLUENCE Turkey, North Korea, Panama | 36.25 | 6.00 | 50.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE North Korea, Thailand | 48.20 | 6.00 | 42.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Indo-Pakistani War INFLUENCE North Korea, Thailand | 48.20 | 6.00 | 42.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 3 | NORAD INFLUENCE North Korea, Iran, Thailand | 46.75 | 6.00 | 61.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | Arab-Israeli War COUP Iran | 46.40 | 4.00 | 42.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Indo-Pakistani War COUP Iran | 46.40 | 4.00 | 42.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], CIA Created[26], Suez Crisis[28], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE France, Japan, Panama | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 2 | Suez Crisis INFLUENCE France, West Germany, Panama | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 3 | Suez Crisis INFLUENCE France, West Germany, Japan | 33.90 | 6.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 4 | Suez Crisis INFLUENCE France, North Korea, Panama | 33.85 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:North Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 5 | Suez Crisis INFLUENCE France, South Korea, Panama | 33.85 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:South Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china`
- hand: `Truman Doctrine[19], Indo-Pakistani War[24], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE Iran, Thailand | 49.85 | 6.00 | 44.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iran:13.70, control_break:Iran, influence:Thailand:20.45, control_break:Thailand |
| 2 | Indo-Pakistani War INFLUENCE Japan, Thailand | 48.80 | 6.00 | 43.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand |
| 3 | Indo-Pakistani War INFLUENCE West Germany, Thailand | 48.30 | 6.00 | 42.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand |
| 4 | Indo-Pakistani War INFLUENCE South Korea, Thailand | 48.20 | 6.00 | 42.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand |
| 5 | Indo-Pakistani War INFLUENCE Pakistan, Thailand | 47.60 | 6.00 | 41.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], CIA Created[26], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 3 | CIA Created INFLUENCE Italy | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.00 |
| 4 | UN Intervention INFLUENCE Italy | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.00 |
| 5 | Fidel INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, Thailand | 40.80 | 6.00 | 55.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Japan, South Korea, Thailand | 40.70 | 6.00 | 55.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE West Germany, South Korea, Thailand | 40.20 | 6.00 | 54.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 4 | NORAD INFLUENCE Japan, Pakistan, Thailand | 40.10 | 6.00 | 54.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 5 | NORAD INFLUENCE Japan, Israel, Thailand | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Fidel[8], UN Intervention[32], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | 26.50 | 6.00 | 20.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, control_break:West Germany, non_coup_milops_penalty:6.00 |
| 2 | Fidel INFLUENCE West Germany, Japan | 26.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | The Cambridge Five INFLUENCE West Germany, Japan | 26.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Fidel INFLUENCE Italy, West Germany | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | The Cambridge Five INFLUENCE Italy, West Germany | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Iran | 30.40 | 4.00 | 42.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus, offside_ops_penalty |
| 2 | Truman Doctrine COUP Iran | 28.55 | 4.00 | 36.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE South Korea, Thailand | 27.20 | 6.00 | 37.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Formosan Resolution INFLUENCE Pakistan, Thailand | 26.60 | 6.00 | 36.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Formosan Resolution INFLUENCE Israel, Thailand | 26.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], The Cambridge Five[36]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | The Cambridge Five INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | The Cambridge Five INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +2, DEFCON +1, MilOps U-3/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], De Gaulle Leads France[17], Marshall Plan[23], East European Unrest[29], Decolonization[30], Red Scare/Purge[31], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Romanian Abdication[12], Nasser[15], NATO[21], Independent Reds[22], Containment[25], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], Socialist Governments[7], De Gaulle Leads France[17], Marshall Plan[23], East European Unrest[29], Decolonization[30], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Pakistan, South Korea, Thailand | 59.50 | 6.00 | 53.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | De Gaulle Leads France INFLUENCE Pakistan, South Korea, Thailand | 59.50 | 6.00 | 53.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Socialist Governments INFLUENCE South Korea, Israel, Thailand | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | De Gaulle Leads France INFLUENCE South Korea, Israel, Thailand | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Socialist Governments INFLUENCE Japan, South Korea, Thailand | 59.20 | 6.00 | 53.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Romanian Abdication[12], Nasser[15], Independent Reds[22], Containment[25], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Italy, West Germany, Japan | 56.65 | 6.00 | 51.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | Nuclear Test Ban INFLUENCE Italy, Japan, North Korea | 56.55 | 6.00 | 51.15 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 3 | Nuclear Test Ban INFLUENCE Italy, Japan, South Korea | 56.55 | 6.00 | 51.15 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 4 | Nuclear Test Ban INFLUENCE Italy, Japan, Egypt | 56.20 | 6.00 | 50.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 5 | Nuclear Test Ban INFLUENCE Italy, West Germany, North Korea | 56.05 | 6.00 | 50.65 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], Marshall Plan[23], East European Unrest[29], Decolonization[30], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE India, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 2 | De Gaulle Leads France INFLUENCE Pakistan, Israel, Thailand | 62.35 | 6.00 | 56.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 3 | De Gaulle Leads France INFLUENCE Japan, Pakistan, Thailand | 62.10 | 6.00 | 56.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 4 | De Gaulle Leads France INFLUENCE Italy, Pakistan, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 5 | De Gaulle Leads France INFLUENCE Pakistan, Philippines, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Romanian Abdication[12], Nasser[15], Independent Reds[22], Containment[25]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 2 | Containment INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 3 | Five Year Plan INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |
| 4 | Five Year Plan INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |
| 5 | Containment INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], Marshall Plan[23], East European Unrest[29], Decolonization[30], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, Israel, Philippines, Thailand | 50.35 | 6.00 | 68.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Marshall Plan INFLUENCE Italy, Japan, Israel, Thailand | 50.35 | 6.00 | 68.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Marshall Plan INFLUENCE Japan, Israel, Saudi Arabia, Thailand | 50.20 | 6.00 | 68.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Marshall Plan INFLUENCE Italy, Israel, Philippines, Thailand | 50.15 | 6.00 | 68.75 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Marshall Plan INFLUENCE West Germany, Japan, Israel, Thailand | 50.05 | 6.00 | 68.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Nasser[15], Independent Reds[22], Containment[25]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Philippines | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 2 | Containment INFLUENCE West Germany, Philippines | 40.65 | 6.00 | 35.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 3 | Containment INFLUENCE North Korea, Philippines | 40.55 | 6.00 | 35.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 4 | Containment INFLUENCE South Korea, Philippines | 40.55 | 6.00 | 35.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:South Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 5 | Containment INFLUENCE Egypt, Philippines | 40.20 | 6.00 | 34.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Egypt:13.70, access_touch:Egypt, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Duck and Cover[4], East European Unrest[29], Decolonization[30], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Decolonization INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Decolonization INFLUENCE India, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Nasser[15], Independent Reds[22]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Syria | 28.73 | 4.00 | 25.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 2 | Independent Reds COUP Israel | 21.93 | 4.00 | 18.23 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3 |
| 3 | Independent Reds INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:4.00 |
| 4 | Independent Reds INFLUENCE West Germany | 21.35 | 6.00 | 15.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:4.00 |
| 5 | Independent Reds INFLUENCE North Korea | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 25: T2 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Duck and Cover[4], East European Unrest[29], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | East European Unrest INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Duck and Cover INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | East European Unrest INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Duck and Cover INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Nasser[15]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 2 | Nasser INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 3 | Romanian Abdication INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 4 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 5 | Romanian Abdication INFLUENCE West Germany | 9.50 | 6.00 | 15.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `East European Unrest[29], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | East European Unrest INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | East European Unrest INFLUENCE India, Japan, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | East European Unrest INFLUENCE Japan, North Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | East European Unrest INFLUENCE Japan, South Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Nasser [15] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty |
| 2 | Nasser INFLUENCE West Germany | 9.50 | 6.00 | 15.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, offside_ops_penalty |
| 3 | Nasser INFLUENCE North Korea | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, offside_ops_penalty |
| 4 | Nasser INFLUENCE South Korea | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Korea:15.55, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Syria | 9.40 | 4.00 | 21.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP -2, DEFCON +1, MilOps U+0/A-2`

## Step 29: T3 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Nuclear Test Ban[34]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Independent Reds[22], Indo-Pakistani War[24], Containment[25], Suez Crisis[28], East European Unrest[29], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, India, Japan, Thailand | 49.20 | 6.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 49.20 | 6.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Marshall Plan INFLUENCE West Germany, Japan, South Korea, Thailand | 49.20 | 6.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Marshall Plan INFLUENCE India, Japan, North Korea, Thailand | 49.10 | 6.00 | 67.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Marshall Plan INFLUENCE India, Japan, South Korea, Thailand | 49.10 | 6.00 | 67.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Independent Reds[22], Indo-Pakistani War[24], Suez Crisis[28], East European Unrest[29], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan, North Korea, South Korea | 68.45 | 6.00 | 62.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 2 | East European Unrest INFLUENCE West Germany, Japan, North Korea, Egypt | 68.10 | 6.00 | 62.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 3 | East European Unrest INFLUENCE West Germany, Japan, South Korea, Egypt | 68.10 | 6.00 | 62.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 4 | East European Unrest INFLUENCE Japan, North Korea, South Korea, Egypt | 68.00 | 6.00 | 62.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 5 | East European Unrest INFLUENCE East Germany, West Germany, Japan, North Korea | 67.95 | 6.00 | 62.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Indonesia | 49.25 | 4.00 | 45.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games COUP Indonesia | 49.25 | 4.00 | 45.55 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:3.5 |
| 3 | Five Year Plan INFLUENCE India, North Korea, Thailand | 47.10 | 6.00 | 61.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, control_break:India, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Arab-Israeli War INFLUENCE India, North Korea | 46.80 | 6.00 | 41.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:3.60 |
| 5 | Olympic Games INFLUENCE India, North Korea | 46.80 | 6.00 | 41.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 34: T3 AR2 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Independent Reds[22], Indo-Pakistani War[24], Suez Crisis[28], UN Intervention[32]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, Japan, North Korea | 53.05 | 6.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.60 |
| 2 | Independent Reds INFLUENCE West Germany, Japan, South Korea | 53.05 | 6.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |
| 3 | Indo-Pakistani War INFLUENCE West Germany, Japan, North Korea | 53.05 | 6.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.60 |
| 4 | Indo-Pakistani War INFLUENCE West Germany, Japan, South Korea | 53.05 | 6.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |
| 5 | Independent Reds INFLUENCE Japan, North Korea, South Korea | 52.95 | 6.00 | 47.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Five Year Plan[5], Blockade[10], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE India, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Thailand:20.45, non_coup_milops_penalty:1.50 |
| 2 | Five Year Plan INFLUENCE India, Japan, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 3 | Olympic Games INFLUENCE India, Japan | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, non_coup_milops_penalty:1.50 |
| 4 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:1.50 |
| 5 | Five Year Plan INFLUENCE West Germany, India, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, control_break:India, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Indo-Pakistani War[24], Suez Crisis[28], UN Intervention[32]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, Japan, North Korea | 53.05 | 6.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:4.50 |
| 2 | Indo-Pakistani War INFLUENCE West Germany, Japan, South Korea | 53.05 | 6.00 | 47.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:4.50 |
| 3 | Indo-Pakistani War INFLUENCE Japan, North Korea, South Korea | 52.95 | 6.00 | 47.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:4.50 |
| 4 | Indo-Pakistani War INFLUENCE West Germany, Japan, Indonesia | 52.85 | 6.00 | 47.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.50 |
| 5 | Indo-Pakistani War INFLUENCE Japan, North Korea, Indonesia | 52.75 | 6.00 | 47.05 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Five Year Plan INFLUENCE India, Japan, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Five Year Plan INFLUENCE Japan, South Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 37.35 | 6.00 | 51.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Suez Crisis[28], UN Intervention[32]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, North Korea, South Korea | 48.45 | 6.00 | 62.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, North Korea, Indonesia | 48.25 | 6.00 | 62.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Suez Crisis INFLUENCE West Germany, Japan, South Korea, Indonesia | 48.25 | 6.00 | 62.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Suez Crisis INFLUENCE Japan, North Korea, South Korea, Indonesia | 48.15 | 6.00 | 62.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, influence:Indonesia:13.85, access_touch:Indonesia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Suez Crisis INFLUENCE West Germany, Japan, North Korea, Egypt | 48.10 | 6.00 | 62.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Blockade[10], Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 4 | Blockade COUP Philippines | 25.80 | 4.00 | 21.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:1, milops_urgency:0.50, expected_swing:0.5 |
| 5 | Nasser COUP Philippines | 25.80 | 4.00 | 21.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:1, milops_urgency:0.50, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:3`
- hand: `Romanian Abdication[12], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 2, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Indonesia | 44.20 | 4.00 | 40.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 2 | UN Intervention COUP Indonesia | 44.20 | 4.00 | 40.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:2.5 |
| 3 | Truman Doctrine INFLUENCE Japan, South Korea | 42.55 | 6.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, control_break:South Korea, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE Japan, South Korea | 42.55 | 6.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, control_break:South Korea, non_coup_milops_penalty:18.00 |
| 5 | Truman Doctrine INFLUENCE West Germany, South Korea | 42.05 | 6.00 | 36.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, influence:South Korea:15.55, control_break:South Korea, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 2, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:9.00 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:9.00 |
| 3 | Nasser INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:9.00 |
| 4 | Captured Nazi Scientist INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:9.00 |
| 5 | Nasser COUP Israel | 21.75 | 4.00 | 17.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], UN Intervention[32]`
- state: `VP 2, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Japan, South Korea | 42.55 | 6.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, control_break:South Korea, non_coup_milops_penalty:18.00 |
| 2 | UN Intervention INFLUENCE West Germany, South Korea | 42.05 | 6.00 | 36.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, influence:South Korea:15.55, control_break:South Korea, non_coup_milops_penalty:18.00 |
| 3 | UN Intervention INFLUENCE North Korea, South Korea | 41.95 | 6.00 | 36.10 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, influence:South Korea:15.55, control_break:South Korea, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE South Korea, Indonesia | 41.75 | 6.00 | 35.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Korea:15.55, control_break:South Korea, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:18.00 |
| 5 | UN Intervention INFLUENCE South Korea, Egypt | 41.60 | 6.00 | 35.75 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Korea:15.55, control_break:South Korea, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:18.00 |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 43: T4 AR0 USSR

- chosen: `Indo-Pakistani War [24] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], Indo-Pakistani War[24], CIA Created[26], Portuguese Empire Crumbles[55], South African Unrest[56], Camp David Accords[66], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Ask Not What Your Country Can Do For You EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36], Brezhnev Doctrine[54], ABM Treaty[60], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Brezhnev Doctrine EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], CIA Created[26], Portuguese Empire Crumbles[55], South African Unrest[56], Camp David Accords[66], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, Mexico | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 2 | South African Unrest INFLUENCE West Germany, Mexico | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 3 | Liberation Theology INFLUENCE West Germany, Mexico | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 4 | Portuguese Empire Crumbles INFLUENCE Mexico, Algeria | 37.85 | 6.00 | 32.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 5 | South African Unrest INFLUENCE Mexico, Algeria | 37.85 | 6.00 | 32.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Indonesia | 47.44 | 4.00 | 43.74 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:3.5 |
| 2 | Truman Doctrine COUP Indonesia | 40.59 | 4.00 | 36.74 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 3 | Panama Canal Returned COUP Indonesia | 40.59 | 4.00 | 36.74 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:2.5 |
| 4 | Indo-Pakistani War INFLUENCE Mexico, South Africa | 38.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 47: T4 AR2 USSR

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Truman Doctrine[19], CIA Created[26], South African Unrest[56], Camp David Accords[66], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 4, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Indonesia | 47.63 | 4.00 | 43.93 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 2 | Liberation Theology COUP Indonesia | 47.63 | 4.00 | 43.93 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:3.5 |
| 3 | South African Unrest INFLUENCE West Germany, Mexico | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.00 |
| 4 | Liberation Theology INFLUENCE West Germany, Mexico | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.00 |
| 5 | South African Unrest INFLUENCE Mexico, Algeria | 41.35 | 6.00 | 35.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 48: T4 AR2 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Decolonization[30], The Cambridge Five[36], Brezhnev Doctrine[54], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE West Germany, Mexico, South Africa | 34.95 | 6.00 | 49.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Brezhnev Doctrine INFLUENCE Mexico, Algeria, South Africa | 34.50 | 6.00 | 48.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, Mexico, South Africa | 34.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Brezhnev Doctrine INFLUENCE France, Mexico, South Africa | 34.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Brezhnev Doctrine INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Truman Doctrine[19], CIA Created[26], Camp David Accords[66], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE West Germany, Algeria | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:2.40 |
| 2 | Liberation Theology INFLUENCE UK, West Germany | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 5 | Liberation Theology INFLUENCE UK, Algeria | 37.05 | 6.00 | 31.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Nasser[15], Truman Doctrine[19], Decolonization[30], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Algeria | 27.85 | 4.00 | 24.00 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.40, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Panama Canal Returned COUP Algeria | 27.85 | 4.00 | 24.00 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.40, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine INFLUENCE South Africa | 27.65 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:2.40 |
| 4 | Decolonization INFLUENCE West Germany, South Africa | 27.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 5 | The Cambridge Five INFLUENCE West Germany, South Africa | 27.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26], Camp David Accords[66], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Algeria, Morocco | 37.20 | 6.00 | 51.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE UK, Algeria, Morocco | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, Algeria, Morocco | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE UK, West Germany, Algeria | 36.55 | 6.00 | 51.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], Decolonization[30], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 27.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, South Africa | 27.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Panama Canal Returned INFLUENCE South Africa | 27.65 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:3.00 |
| 4 | Decolonization INFLUENCE Algeria, South Africa | 27.20 | 6.00 | 37.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | The Cambridge Five INFLUENCE Algeria, South Africa | 27.20 | 6.00 | 37.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26], Camp David Accords[66], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Our Man in Tehran INFLUENCE UK, West Germany | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Camp David Accords INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Camp David Accords INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15], The Cambridge Five[36], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE UK, South Africa | 25.65 | 6.00 | 35.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Panama Canal Returned INFLUENCE UK | 25.00 | 6.00 | 19.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:UK:14.15, control_break:UK, non_coup_milops_penalty:4.00 |
| 3 | The Cambridge Five INFLUENCE UK, West Germany | 25.00 | 6.00 | 35.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | The Cambridge Five INFLUENCE UK, Algeria | 24.55 | 6.00 | 34.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | The Cambridge Five INFLUENCE East Germany, UK | 24.40 | 6.00 | 34.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26], Our Man in Tehran[84]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Our Man in Tehran INFLUENCE West Germany, Cuba | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Our Man in Tehran INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Our Man in Tehran INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Nasser[15], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | Panama Canal Returned INFLUENCE Algeria | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:12.00 |
| 4 | Panama Canal Returned INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:12.00 |
| 5 | Panama Canal Returned INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | CIA Created INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Truman Doctrine INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Truman Doctrine INFLUENCE France | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | CIA Created INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Nasser[15]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Nasser INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Nasser INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Romanian Abdication INFLUENCE Algeria | 9.55 | 6.00 | 15.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Socialist Governments[7], Blockade[10], Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], Red Scare/Purge[31], De-Stalinization[33], Bear Trap[47], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], COMECON[14], Olympic Games[20], UN Intervention[32], Special Relationship[37], SALT Negotiations[46], OAS Founded[71], Sadat Expels Soviets[73]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Socialist Governments[7], Blockade[10], Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], De-Stalinization[33], Bear Trap[47], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 2 | De-Stalinization INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 3 | Socialist Governments INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |
| 4 | Socialist Governments INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |
| 5 | De-Stalinization INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Sadat Expels Soviets [73] as COUP`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], COMECON[14], Olympic Games[20], Decolonization[30], UN Intervention[32], Special Relationship[37], OAS Founded[71], Sadat Expels Soviets[73]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets COUP Indonesia | 54.58 | 4.00 | 51.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 2 | Olympic Games COUP Indonesia | 47.73 | 4.00 | 44.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 3 | Special Relationship COUP Indonesia | 47.73 | 4.00 | 44.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 4 | Sadat Expels Soviets COUP Algeria | 44.68 | 4.00 | 41.13 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 5 | Sadat Expels Soviets INFLUENCE West Germany, South Africa | 43.50 | 6.00 | 37.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 63: T5 AR2 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], De-Stalinization[33], Bear Trap[47], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, Indonesia | 55.85 | 6.00 | 50.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:5.00 |
| 2 | De-Stalinization INFLUENCE France, West Germany, Indonesia | 55.85 | 6.00 | 50.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:5.00 |
| 3 | De-Stalinization INFLUENCE West Germany, Cuba, Indonesia | 55.35 | 6.00 | 49.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:5.00 |
| 4 | De-Stalinization INFLUENCE East Germany, France, Indonesia | 55.25 | 6.00 | 49.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:5.00 |
| 5 | De-Stalinization INFLUENCE Italy, West Germany, Indonesia | 55.25 | 6.00 | 49.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, access_touch:Indonesia, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], COMECON[14], Olympic Games[20], Decolonization[30], UN Intervention[32], Special Relationship[37], OAS Founded[71]`
- state: `VP 4, DEFCON 3, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Algeria | 34.57 | 4.00 | 30.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Special Relationship COUP Algeria | 34.57 | 4.00 | 30.87 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.33, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Olympic Games COUP Mexico | 30.32 | 4.00 | 26.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.33, defcon_penalty:3, expected_swing:1.5 |
| 4 | Special Relationship COUP Mexico | 30.32 | 4.00 | 26.62 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:0.33, defcon_penalty:3, expected_swing:1.5 |
| 5 | UN Intervention COUP Algeria | 27.72 | 4.00 | 23.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:0.33, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], Korean War[11], Captured Nazi Scientist[18], Independent Reds[22], Bear Trap[47], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Korean War INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | Latin American Death Squads INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Korean War INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], COMECON[14], Decolonization[30], UN Intervention[32], Special Relationship[37], OAS Founded[71]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.40 |
| 2 | OAS Founded INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.40 |
| 3 | Special Relationship INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.40 |
| 4 | UN Intervention INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 5 | OAS Founded INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], Captured Nazi Scientist[18], Independent Reds[22], Bear Trap[47], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 2 | Latin American Death Squads INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 3 | Latin American Death Squads INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:7.50 |
| 4 | Latin American Death Squads INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:7.50 |
| 5 | Latin American Death Squads INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `OAS Founded [71] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], COMECON[14], Decolonization[30], Special Relationship[37], OAS Founded[71]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 2 | Special Relationship INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 3 | OAS Founded INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 4 | Special Relationship INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 5 | OAS Founded INFLUENCE Algeria | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Independent Reds[22], Bear Trap[47]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Bear Trap INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Bear Trap INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Bear Trap INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], COMECON[14], Decolonization[30], Special Relationship[37]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Special Relationship INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 3 | Special Relationship INFLUENCE Algeria | 21.40 | 6.00 | 15.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 4 | Special Relationship INFLUENCE East Germany | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:4.00 |
| 5 | Special Relationship INFLUENCE France | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], Captured Nazi Scientist[18], Independent Reds[22]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE France | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:30.00 |
| 2 | Captured Nazi Scientist INFLUENCE France | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, control_break:France, non_coup_milops_penalty:30.00 |
| 3 | Independent Reds INFLUENCE France, West Germany | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | Independent Reds INFLUENCE East Germany, France | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Independent Reds INFLUENCE France, Cuba | 25.30 | 6.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], COMECON[14], Decolonization[30]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | COMECON INFLUENCE Algeria, South Africa | 18.05 | 6.00 | 32.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | COMECON INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | COMECON INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | COMECON INFLUENCE Poland, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Independent Reds[22]`
- state: `VP 4, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 22.45 | 4.00 | 18.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:45.00 |
| 3 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:45.00 |
| 4 | Captured Nazi Scientist INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:45.00 |
| 5 | Independent Reds INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:45.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 74: T5 AR7 US

- chosen: `Arab-Israeli War [13] as SPACE`
- flags: `milops_shortfall:2, offside_ops_play, space_play`
- hand: `Arab-Israeli War[13], Decolonization[30]`
- state: `VP 4, DEFCON 2, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Decolonization SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Arab-Israeli War COUP Colombia | 7.30 | 4.00 | 19.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP SE African States | 7.30 | 4.00 | 19.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Zimbabwe | 7.30 | 4.00 | 19.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -3, DEFCON +1, MilOps U-1/A-3`

## Step 75: T6 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], How I Learned to Stop Worrying[49], Junta[50], Kitchen Debates[51], Allende[57], U2 Incident[63], OPEC[64], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Blockade[10], Arab-Israeli War[13], Suez Crisis[28], Willy Brandt[58], Cultural Revolution[61], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Five Year Plan[5], How I Learned to Stop Worrying[49], Junta[50], Kitchen Debates[51], Allende[57], U2 Incident[63], OPEC[64], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, West Germany, Nigeria | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:5.14 |
| 2 | U2 Incident INFLUENCE France, West Germany, Nigeria | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:5.14 |
| 3 | OPEC INFLUENCE East Germany, West Germany, Nigeria | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:5.14 |
| 4 | OPEC INFLUENCE France, West Germany, Nigeria | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:5.14 |
| 5 | U2 Incident INFLUENCE West Germany, Cuba, Nigeria | 56.85 | 6.00 | 51.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Suez Crisis[28], Willy Brandt[58], Cultural Revolution[61], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE France, South Africa | 39.55 | 6.00 | 33.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 2 | John Paul II Elected Pope INFLUENCE France, South Africa | 39.55 | 6.00 | 33.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 3 | Voice of America INFLUENCE France, South Africa | 39.55 | 6.00 | 33.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 4 | Lonely Hearts Club Band INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, non_coup_milops_penalty:5.14 |
| 5 | John Paul II Elected Pope INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Five Year Plan[5], How I Learned to Stop Worrying[49], Junta[50], Kitchen Debates[51], Allende[57], OPEC[64], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | OPEC INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 3 | OPEC INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | OPEC INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | OPEC INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Suez Crisis[28], Willy Brandt[58], Cultural Revolution[61], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | John Paul II Elected Pope INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Voice of America INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Five Year Plan[5], How I Learned to Stop Worrying[49], Junta[50], Kitchen Debates[51], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |
| 2 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |
| 3 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |
| 4 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Suez Crisis[28], Willy Brandt[58], Cultural Revolution[61], Voice of America[75]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 2 | Voice of America INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 3 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 4 | Voice of America INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 5 | Voice of America INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Five Year Plan[5], Junta[50], Kitchen Debates[51], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 2 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 5 | Junta INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Suez Crisis[28], Willy Brandt[58], Cultural Revolution[61]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Cultural Revolution INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Suez Crisis INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Five Year Plan[5], Kitchen Debates[51], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany, Algeria | 41.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:12.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, Algeria | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:12.00 |
| 3 | Colonial Rear Guards INFLUENCE France, Algeria | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:12.00 |
| 4 | Colonial Rear Guards INFLUENCE Cuba, Algeria | 39.95 | 6.00 | 34.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:12.00 |
| 5 | Colonial Rear Guards INFLUENCE Italy, Algeria | 39.85 | 6.00 | 34.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Willy Brandt[58], Cultural Revolution[61]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, Morocco, South Africa | 34.80 | 6.00 | 49.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, Morocco, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Cultural Revolution INFLUENCE France, Morocco, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Cultural Revolution INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, behind_on_space, offside_ops_play`
- hand: `Five Year Plan[5], Kitchen Debates[51], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Five Year Plan INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Five Year Plan INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Five Year Plan INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Five Year Plan INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Saharan States | 29.30 | 4.00 | 41.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Saharan States | 29.30 | 4.00 | 41.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Blockade COUP Saharan States | 26.45 | 4.00 | 34.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Arab-Israeli War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Willy Brandt INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 89: T6 AR7 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:6, behind_on_space`
- hand: `Kitchen Debates[51], Allende[57]`
- state: `VP -1, DEFCON 2, MilOps U0/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Cameroon | 24.45 | 4.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Allende COUP Saharan States | 24.45 | 4.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP Guatemala | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:54.00 |
| 5 | Allende INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 90: T6 AR7 US

- chosen: `Willy Brandt [58] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Willy Brandt[58]`
- state: `VP -1, DEFCON 2, MilOps U1/A2, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt COUP Saharan States | 31.30 | 4.00 | 43.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Blockade COUP Saharan States | 28.45 | 4.00 | 36.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Willy Brandt INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Willy Brandt INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Willy Brandt INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Romanian Abdication[12], Marshall Plan[23], Suez Crisis[28], Nuclear Test Ban[34], Formosan Resolution[35], Nixon Plays the China Card[72], Ussuri River Skirmish[77], One Small Step[81]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Olympic Games[20], East European Unrest[29], Arms Race[42], Cuban Missile Crisis[43], Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Romanian Abdication[12], Marshall Plan[23], Suez Crisis[28], Formosan Resolution[35], Nixon Plays the China Card[72], Ussuri River Skirmish[77], One Small Step[81]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | Suez Crisis INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Arms Race [42] as COUP`
- flags: `milops_shortfall:7`
- hand: `Olympic Games[20], Arms Race[42], Cuban Missile Crisis[43], Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race COUP Nigeria | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 2 | Cuban Missile Crisis COUP Nigeria | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 3 | Alliance for Progress COUP Nigeria | 56.65 | 4.00 | 53.10 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 4 | Arms Race COUP Indonesia | 55.15 | 4.00 | 51.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |
| 5 | Cuban Missile Crisis COUP Indonesia | 55.15 | 4.00 | 51.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:7, milops_urgency:1.00, coup_access_open, expected_swing:4.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 95: T7 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Romanian Abdication[12], Marshall Plan[23], Formosan Resolution[35], Nixon Plays the China Card[72], Ussuri River Skirmish[77], One Small Step[81]`
- state: `VP -1, DEFCON 4, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:7.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Cuba | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:7.00 |
| 3 | Ussuri River Skirmish INFLUENCE France, West Germany, Cuba | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, control_break:West Germany, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:7.00 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, non_coup_milops_penalty:7.00 |
| 5 | Ussuri River Skirmish INFLUENCE France, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, control_break:West Germany, influence:Mexico:14.95, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Cuban Missile Crisis [43] as COUP`
- flags: `milops_shortfall:4`
- hand: `Olympic Games[20], Cuban Missile Crisis[43], Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP -1, DEFCON 4, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis COUP Indonesia | 54.48 | 4.00 | 50.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 2 | Alliance for Progress COUP Indonesia | 54.48 | 4.00 | 50.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 3 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 4 | Cuban Missile Crisis INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 5 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `Romanian Abdication[12], Marshall Plan[23], Formosan Resolution[35], Nixon Plays the China Card[72], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, West Germany, Cuba | 43.70 | 6.00 | 62.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 2 | Marshall Plan INFLUENCE East Germany, France, West Germany, Mexico | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 3 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 4 | Marshall Plan INFLUENCE East Germany, France, West Germany, Morocco | 43.45 | 6.00 | 62.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 5 | Marshall Plan INFLUENCE East Germany, France, West Germany, Egypt | 43.35 | 6.00 | 61.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Egypt:13.20, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Olympic Games[20], Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Alliance for Progress[79], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | Alliance for Progress INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 4 | Alliance for Progress INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 5 | Alliance for Progress INFLUENCE Italy, West Germany, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:7, behind_on_space`
- hand: `Romanian Abdication[12], Formosan Resolution[35], Nixon Plays the China Card[72], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U0/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Saharan States | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:1.75, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 3 | One Small Step INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 4 | One Small Step INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:10.50 |
| 5 | One Small Step INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 100: T7 AR4 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:4`
- hand: `Olympic Games[20], Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Saharan States | 41.30 | 4.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Nuclear Subs COUP Saharan States | 41.30 | 4.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy COUP Saharan States | 41.30 | 4.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 4 | Grain Sales to Soviets COUP Saharan States | 41.30 | 4.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 5 | Olympic Games INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space`
- hand: `Romanian Abdication[12], Formosan Resolution[35], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 3, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Nigeria | 41.78 | 4.00 | 37.93 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Formosan Resolution COUP Nigeria | 32.63 | 4.00 | 44.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Nixon Plays the China Card COUP Nigeria | 32.63 | 4.00 | 44.93 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Nigeria, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Romanian Abdication COUP Mexico | 26.13 | 4.00 | 22.28 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |
| 5 | Romanian Abdication COUP Algeria | 25.38 | 4.00 | 21.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.67, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:4`
- hand: `Nuclear Subs[44], Missile Envy[52], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | Missile Envy COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 4 | Nuclear Subs INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Missile Envy INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Formosan Resolution[35], Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 28.30 | 4.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card COUP Saharan States | 28.30 | 4.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:2.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | Formosan Resolution INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Missile Envy [52] as COUP`
- flags: `milops_shortfall:4`
- hand: `Missile Envy[52], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy COUP Saharan States | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets COUP Saharan States | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:24.00 |
| 4 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:24.00 |
| 5 | Missile Envy INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as COUP`
- flags: `holds_china, milops_shortfall:5, behind_on_space, offside_ops_play`
- hand: `Nixon Plays the China Card[72]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card COUP Saharan States | 33.30 | 4.00 | 45.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 3 | Nixon Plays the China Card INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 4 | Nixon Plays the China Card INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 5 | Nixon Plays the China Card INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:45.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `milops_shortfall:4`
- hand: `Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP -1, DEFCON 2, MilOps U2/A3, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 47.30 | 4.00 | 43.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:36.00 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:36.00 |
| 4 | Grain Sales to Soviets INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:36.00 |
| 5 | Grain Sales to Soviets INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-3`

## Step 107: T8 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `Five Year Plan[5], Fidel[8], CIA Created[26], UN Intervention[32], Formosan Resolution[35], Bear Trap[47], ABM Treaty[60], Camp David Accords[66], Star Wars[88]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Bear Trap EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Olympic Games [20] as EVENT`
- flags: `milops_shortfall:8`
- hand: `COMECON[14], Nasser[15], Olympic Games[20], Decolonization[30], Formosan Resolution[35], Cultural Revolution[61], Grain Sales to Soviets[68], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `Five Year Plan[5], Fidel[8], CIA Created[26], UN Intervention[32], Formosan Resolution[35], Bear Trap[47], Camp David Accords[66], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Fidel INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Fidel INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:6.86 |
| 4 | Fidel INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Fidel INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `COMECON[14], Nasser[15], Decolonization[30], Formosan Resolution[35], Cultural Revolution[61], Grain Sales to Soviets[68], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Formosan Resolution INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Grain Sales to Soviets INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, behind_on_space, offside_ops_play`
- hand: `Five Year Plan[5], CIA Created[26], UN Intervention[32], Formosan Resolution[35], Bear Trap[47], Camp David Accords[66], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Five Year Plan INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Five Year Plan INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `COMECON[14], Nasser[15], Decolonization[30], Cultural Revolution[61], Grain Sales to Soviets[68], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], UN Intervention[32], Formosan Resolution[35], Bear Trap[47], Camp David Accords[66], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Bear Trap INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Bear Trap INFLUENCE East Germany, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Bear Trap INFLUENCE France, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `COMECON[14], Nasser[15], Decolonization[30], Cultural Revolution[61], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | One Small Step INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.60 |
| 4 | One Small Step INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | One Small Step INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:8, behind_on_space`
- hand: `CIA Created[26], UN Intervention[32], Formosan Resolution[35], Camp David Accords[66], Star Wars[88]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Mexico | 25.30 | 4.00 | 21.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | UN Intervention COUP Algeria | 25.05 | 4.00 | 21.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | UN Intervention COUP Israel | 23.00 | 4.00 | 19.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:8, milops_urgency:2.00, defcon_penalty:3 |
| 4 | Formosan Resolution INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Formosan Resolution INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 116: T8 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `COMECON[14], Nasser[15], Decolonization[30], Cultural Revolution[61]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | COMECON INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | COMECON INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Cultural Revolution INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Formosan Resolution[35], Camp David Accords[66], Star Wars[88]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Formosan Resolution INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Camp David Accords INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Camp David Accords INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Star Wars INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Decolonization[30], Cultural Revolution[61]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Cultural Revolution INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Cultural Revolution INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Cultural Revolution INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Camp David Accords[66], Star Wars[88]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Camp David Accords INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Star Wars INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Star Wars INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Camp David Accords INFLUENCE Italy, West Germany | 27.30 | 6.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Decolonization[30]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | Decolonization INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 3 | Decolonization INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 4 | Decolonization INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | Decolonization INFLUENCE West Germany, Cuba | 22.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Star Wars [88] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, behind_on_space, offside_ops_play`
- hand: `CIA Created[26], Star Wars[88]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Star Wars INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Star Wars INFLUENCE Italy, West Germany | 27.30 | 6.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Star Wars INFLUENCE Turkey, West Germany | 26.80 | 6.00 | 37.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Star Wars INFLUENCE UK, West Germany | 26.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:UK:14.90, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Colombia | 15.95 | 4.00 | 24.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 2 | Nasser COUP Guatemala | 15.70 | 4.00 | 23.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 3 | Nasser COUP Cameroon | 15.45 | 4.00 | 23.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 4 | Nasser COUP Saharan States | 15.45 | 4.00 | 23.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Nasser COUP SE African States | 15.45 | 4.00 | 23.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:8, milops_urgency:8.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-1/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Che [83] as EVENT`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], NORAD[38], Missile Envy[52], Sadat Expels Soviets[73], Voice of America[75], Che[83], Iran-Iraq War[105], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Special Relationship [37] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Korean War[11], Truman Doctrine[19], Special Relationship[37], Brezhnev Doctrine[54], U2 Incident[63], John Paul II Elected Pope[69], Liberation Theology[76], Pershing II Deployed[102]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Brezhnev Doctrine EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], NORAD[38], Missile Envy[52], Sadat Expels Soviets[73], Voice of America[75], Iran-Iraq War[105], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | Missile Envy INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 4 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Korean War[11], Truman Doctrine[19], Brezhnev Doctrine[54], U2 Incident[63], John Paul II Elected Pope[69], Liberation Theology[76], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | John Paul II Elected Pope INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | John Paul II Elected Pope INFLUENCE West Germany, Chile | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:7.71 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:7.71 |
| 5 | John Paul II Elected Pope INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], NORAD[38], Sadat Expels Soviets[73], Voice of America[75], Iran-Iraq War[105], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Iran-Iraq War INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Socialist Governments[7], Korean War[11], Truman Doctrine[19], Brezhnev Doctrine[54], U2 Incident[63], Liberation Theology[76], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Socialist Governments INFLUENCE East Germany, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], NORAD[38], Sadat Expels Soviets[73], Voice of America[75], Lone Gunman[109], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:10.80 |
| 4 | Colonial Rear Guards INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Colonial Rear Guards INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], Brezhnev Doctrine[54], U2 Incident[63], Liberation Theology[76], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 3 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:10.80 |
| 5 | Brezhnev Doctrine INFLUENCE France, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space, offside_ops_play`
- hand: `Romanian Abdication[12], NORAD[38], Sadat Expels Soviets[73], Voice of America[75], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 3 | NORAD INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 4 | NORAD INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], U2 Incident[63], Liberation Theology[76], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 2 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 3 | U2 Incident INFLUENCE East Germany, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 4 | U2 Incident INFLUENCE France, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 5 | Pershing II Deployed INFLUENCE East Germany, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space, offside_ops_play`
- hand: `Romanian Abdication[12], Sadat Expels Soviets[73], Voice of America[75], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Sadat Expels Soviets INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Sadat Expels Soviets INFLUENCE France, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], Liberation Theology[76], Pershing II Deployed[102]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Pershing II Deployed INFLUENCE East Germany, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Pershing II Deployed INFLUENCE France, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Pershing II Deployed INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Pershing II Deployed INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, behind_on_space, offside_ops_play`
- hand: `Romanian Abdication[12], Voice of America[75], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Voice of America INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:54.00 |
| 4 | Lone Gunman INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:54.00 |
| 5 | Voice of America INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Korean War[11], Truman Doctrine[19], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Korean War INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Truman Doctrine INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:9, behind_on_space`
- hand: `Romanian Abdication[12], Lone Gunman[109]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Dominican Republic | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Dominican Republic, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Romanian Abdication COUP Guatemala | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Romanian Abdication COUP Haiti | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman COUP Dominican Republic | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Dominican Republic, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Lone Gunman COUP Guatemala | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 138: T9 AR7 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:9`
- hand: `Truman Doctrine[19], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U1/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 29.95 | 4.00 | 26.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Truman Doctrine COUP El Salvador | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Truman Doctrine COUP Guatemala | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Truman Doctrine COUP Nicaragua | 29.70 | 4.00 | 25.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nicaragua, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Truman Doctrine COUP Cameroon | 29.45 | 4.00 | 25.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Cameroon, milops_need:9, milops_urgency:9.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Five Year Plan[5], Cuban Missile Crisis[43], Kitchen Debates[51], OPEC[64], Voice of America[75], Our Man in Tehran[84], Marine Barracks Bombing[91], Iran-Contra Scandal[96], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Marine Barracks Bombing EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Iran-Contra Scandal EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Marshall Plan[23], De-Stalinization[33], Arms Race[42], Summit[48], Portuguese Empire Crumbles[55], Allende[57], Ask Not What Your Country Can Do For You[78], The Iron Lady[86], Chernobyl[97]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Five Year Plan[5], Kitchen Debates[51], OPEC[64], Voice of America[75], Our Man in Tehran[84], Marine Barracks Bombing[91], Iran-Contra Scandal[96], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | OPEC INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | OPEC INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | OPEC INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 5 | OPEC INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `De-Stalinization[33], Arms Race[42], Summit[48], Portuguese Empire Crumbles[55], Allende[57], Ask Not What Your Country Can Do For You[78], The Iron Lady[86], Chernobyl[97]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | Summit INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | The Iron Lady INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 5 | Chernobyl INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Five Year Plan[5], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Marine Barracks Bombing[91], Iran-Contra Scandal[96], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | Marine Barracks Bombing INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 3 | Iran-Contra Scandal INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 4 | Iran-Contra Scandal INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 5 | Marine Barracks Bombing INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `De-Stalinization[33], Summit[48], Portuguese Empire Crumbles[55], Allende[57], Ask Not What Your Country Can Do For You[78], The Iron Lady[86], Chernobyl[97]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 3 | The Iron Lady INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 4 | Chernobyl INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 5 | Summit INFLUENCE East Germany, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Iran-Contra Scandal [96] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space`
- hand: `Five Year Plan[5], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Iran-Contra Scandal[96], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Contra Scandal INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Iran-Contra Scandal INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Iran-Contra Scandal INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 4 | Iran-Contra Scandal INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Iran-Contra Scandal INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `De-Stalinization[33], Portuguese Empire Crumbles[55], Allende[57], Ask Not What Your Country Can Do For You[78], The Iron Lady[86], Chernobyl[97]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Chernobyl INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:12.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE France, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Five Year Plan[5], Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 2 | Five Year Plan INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 3 | Five Year Plan INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 4 | Five Year Plan INFLUENCE East Germany, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 5 | Five Year Plan INFLUENCE France, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `De-Stalinization[33], Portuguese Empire Crumbles[55], Allende[57], The Iron Lady[86], Chernobyl[97]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 3 | The Iron Lady INFLUENCE East Germany, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:15.00 |
| 4 | The Iron Lady INFLUENCE France, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:15.00 |
| 5 | Chernobyl INFLUENCE East Germany, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Kitchen Debates[51], Voice of America[75], Our Man in Tehran[84], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Voice of America INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Voice of America INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `De-Stalinization[33], Portuguese Empire Crumbles[55], Allende[57], Chernobyl[97]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Chernobyl INFLUENCE East Germany, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:20.00 |
| 3 | Chernobyl INFLUENCE France, West Germany, Chile | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, non_coup_milops_penalty:20.00 |
| 4 | Chernobyl INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | Chernobyl INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Kitchen Debates[51], Our Man in Tehran[84], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 4 | Our Man in Tehran INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 5 | Our Man in Tehran INFLUENCE Turkey, West Germany | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `De-Stalinization[33], Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 2 | De-Stalinization INFLUENCE East Germany, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 3 | De-Stalinization INFLUENCE France, West Germany, Chile | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 4 | De-Stalinization INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 5 | De-Stalinization INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Kitchen Debates [51] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, behind_on_space, offside_ops_play`
- hand: `Kitchen Debates[51], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates INFLUENCE West Germany | 10.75 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | 10.75 | 6.00 | 16.90 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | Kitchen Debates INFLUENCE East Germany | 10.15 | 6.00 | 16.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 4 | Kitchen Debates INFLUENCE France | 10.15 | 6.00 | 16.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | Panama Canal Returned INFLUENCE East Germany | 10.15 | 6.00 | 16.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP 0, DEFCON 2, MilOps U0/A0, Space U0/A1, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, Chile | 22.40 | 6.00 | 32.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Chile:14.30, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP +4, DEFCON +1, MilOps U+0/A+0`
