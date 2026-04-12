# minimal_hybrid detailed rollout log

- seed: `20260413`
- winner: `USSR`
- final_vp: `4`
- end_turn: `4`
- end_reason: `defcon1`

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

- chosen: `Panama Canal Returned [111] as COUP`
- flags: `milops_shortfall:2`
- hand: `Romanian Abdication[12], Nasser[15], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned COUP Algeria | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:2, coup_access_open, expected_swing:0.5 |
| 2 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 3 | Panama Canal Returned INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 4 | Panama Canal Returned INFLUENCE Algeria | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:12.00 |
| 5 | Panama Canal Returned INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`
