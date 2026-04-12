# minimal_hybrid detailed rollout log

- seed: `20260410`
- winner: `USSR`
- final_vp: `2`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Romanian Abdication[12], Warsaw Pact Formed[16], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Formosan Resolution [35] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], COMECON[14], Nasser[15], CIA Created[26], Suez Crisis[28], De-Stalinization[33], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Romanian Abdication[12], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Indo-Pakistani War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Decolonization COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | The Cambridge Five COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Romanian Abdication COUP Iran | 64.38 | 4.00 | 60.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], COMECON[14], Nasser[15], CIA Created[26], Suez Crisis[28], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Turkey, Indonesia, Philippines | 42.80 | 6.00 | 57.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |
| 2 | Suez Crisis INFLUENCE Turkey, Indonesia, Philippines | 42.80 | 6.00 | 57.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |
| 3 | De-Stalinization INFLUENCE Turkey, Indonesia, Philippines | 42.80 | 6.00 | 57.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |
| 4 | COMECON INFLUENCE North Korea, Indonesia, Philippines | 42.40 | 6.00 | 56.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |
| 5 | Suez Crisis INFLUENCE North Korea, Indonesia, Philippines | 42.40 | 6.00 | 56.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, South Korea, Thailand | 55.20 | 6.00 | 73.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Thailand, Thailand | 54.88 | 6.00 | 73.47 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand, offside_ops_penalty |
| 3 | US/Japan Mutual Defense Pact INFLUENCE Japan, South Korea, Thailand, Thailand | 54.77 | 6.00 | 73.38 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand, offside_ops_penalty |
| 4 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Pakistan, Thailand | 54.60 | 6.00 | 73.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Israel, Thailand | 54.55 | 6.00 | 73.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], CIA Created[26], Suez Crisis[28], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, North Korea | 39.80 | 6.00 | 54.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 2 | Suez Crisis INFLUENCE France, West Germany, North Korea | 39.80 | 6.00 | 54.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, North Korea | 39.80 | 6.00 | 54.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 4 | De-Stalinization INFLUENCE France, West Germany, North Korea | 39.80 | 6.00 | 54.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 5 | Suez Crisis INFLUENCE West Germany, North Korea, Panama | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china`
- hand: `Duck and Cover[4], Romanian Abdication[12], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE North Korea, Thailand | 51.70 | 6.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 2 | Decolonization INFLUENCE North Korea, Thailand | 51.70 | 6.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 3 | The Cambridge Five INFLUENCE North Korea, Thailand | 51.70 | 6.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 4 | Duck and Cover INFLUENCE East Germany, North Korea, Thailand | 51.60 | 6.00 | 66.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Indo-Pakistani War INFLUENCE East Germany, Thailand | 51.20 | 6.00 | 45.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45, control_break:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], CIA Created[26], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE France, Japan, Panama | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 2 | De-Stalinization INFLUENCE France, West Germany, Panama | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 3 | De-Stalinization INFLUENCE France, West Germany, Japan | 33.90 | 6.00 | 48.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 4 | De-Stalinization INFLUENCE France, North Korea, Panama | 33.85 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:North Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |
| 5 | De-Stalinization INFLUENCE France, South Korea, Panama | 33.85 | 6.00 | 48.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:South Korea:15.55, influence:Panama:11.20, control_break:Panama, offside_ops_penalty, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china`
- hand: `Duck and Cover[4], Romanian Abdication[12], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | The Cambridge Five COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Decolonization INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 5 | Romanian Abdication COUP Iran | 43.05 | 4.00 | 39.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | CIA Created INFLUENCE Italy | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.00 |
| 3 | Korean War INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Arab-Israeli War INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | CIA Created INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china`
- hand: `Duck and Cover[4], Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Iran | 46.40 | 4.00 | 42.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | The Cambridge Five INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE Pakistan, Thailand | 42.60 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45 |
| 5 | Duck and Cover INFLUENCE East Germany, Pakistan, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Arab-Israeli War INFLUENCE Italy, Japan | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Korean War INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Arab-Israeli War INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Korean War INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Duck and Cover[4], Romanian Abdication[12]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, Pakistan, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Duck and Cover INFLUENCE East Germany, Israel, Thailand | 42.45 | 6.00 | 56.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Duck and Cover INFLUENCE East Germany, Japan, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Duck and Cover INFLUENCE East Germany, Italy, Thailand | 42.00 | 6.00 | 56.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Duck and Cover INFLUENCE East Germany, Philippines, Thailand | 42.00 | 6.00 | 56.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Italy, Japan | 30.30 | 6.00 | 40.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, Japan | 26.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Arab-Israeli War INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Arab-Israeli War INFLUENCE Japan, South Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Arab-Israeli War INFLUENCE Japan, Egypt | 26.05 | 6.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Marshall Plan[23], UN Intervention[32], Nuclear Test Ban[34]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], NATO[21], Containment[25], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Marshall Plan[23], UN Intervention[32]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE India, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Socialist Governments INFLUENCE Pakistan, Israel, Thailand | 62.35 | 6.00 | 56.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Socialist Governments INFLUENCE Japan, Pakistan, Thailand | 62.10 | 6.00 | 56.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Socialist Governments INFLUENCE Italy, Pakistan, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Socialist Governments INFLUENCE Pakistan, Philippines, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 2 | Containment INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 3 | East European Unrest INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 4 | East European Unrest INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 5 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Marshall Plan[23], UN Intervention[32]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, North Korea, Israel, Thailand | 54.95 | 6.00 | 73.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 2 | Marshall Plan INFLUENCE North Korea, Israel, Philippines, Thailand | 54.75 | 6.00 | 73.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 3 | Marshall Plan INFLUENCE Italy, North Korea, Israel, Thailand | 54.75 | 6.00 | 73.35 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 4 | Marshall Plan INFLUENCE North Korea, Israel, Saudi Arabia, Thailand | 54.60 | 6.00 | 73.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 5 | Marshall Plan INFLUENCE Japan, North Korea, Philippines, Thailand | 54.50 | 6.00 | 73.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], East European Unrest[29], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |
| 2 | East European Unrest INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |
| 3 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |
| 4 | NORAD INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |
| 5 | East European Unrest INFLUENCE Japan, North Korea, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Five Year Plan INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Five Year Plan INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Olympic Games INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], NORAD[38]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 2 | NORAD INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 3 | NORAD INFLUENCE Japan, North Korea, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | NORAD INFLUENCE West Germany, Japan, Egypt | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 5 | NORAD INFLUENCE Japan, North Korea, Egypt | 52.45 | 6.00 | 46.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Five Year Plan INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Five Year Plan INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Five Year Plan INFLUENCE North Korea, Saudi Arabia, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Five Year Plan INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | De Gaulle Leads France INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | De Gaulle Leads France INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | De Gaulle Leads France INFLUENCE Japan, North Korea, Egypt | 32.45 | 6.00 | 46.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Philippines | 31.80 | 4.00 | 27.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Philippines | 31.80 | 4.00 | 27.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | Independent Reds INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Captured Nazi Scientist INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:12.00 |
| 5 | Independent Reds INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 26: T2 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Truman Doctrine[19]`
- state: `VP 3, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Philippines | 31.80 | 4.00 | 27.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | Truman Doctrine COUP Japan | 25.50 | 4.00 | 21.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 3 | Truman Doctrine COUP North Korea | 24.90 | 4.00 | 21.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 4 | Truman Doctrine COUP South Korea | 24.90 | 4.00 | 21.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 5 | Truman Doctrine COUP Israel | 24.25 | 4.00 | 20.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:1.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 27: T2 AR6 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Independent Reds[22], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Independent Reds INFLUENCE North Korea, Philippines | 29.70 | 6.00 | 40.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, control_break:Philippines, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Independent Reds INFLUENCE Philippines, Thailand | 29.60 | 6.00 | 39.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, control_break:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Independent Reds INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | UN Intervention INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], Blockade[10]`
- state: `VP 3, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Philippines | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Fidel INFLUENCE West Germany, Philippines | 21.30 | 6.00 | 31.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Philippines:14.45, access_touch:Philippines, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Containment[25], CIA Created[26], Red Scare/Purge[31], UN Intervention[32], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], COMECON[14], Nasser[15], Suez Crisis[28], Decolonization[30], De-Stalinization[33], The Cambridge Five[36], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -1, DEFCON -1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Containment[25], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Containment INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Five Year Plan INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `COMECON[14], Nasser[15], Suez Crisis[28], Decolonization[30], De-Stalinization[33], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Italy, Japan | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, non_coup_milops_penalty:3.00 |
| 2 | NORAD INFLUENCE Italy, West Germany | 40.65 | 6.00 | 35.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, non_coup_milops_penalty:3.00 |
| 3 | NORAD INFLUENCE Italy, North Korea | 40.55 | 6.00 | 35.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | NORAD INFLUENCE Italy, South Korea | 40.55 | 6.00 | 35.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 5 | NORAD INFLUENCE Italy, Egypt | 40.20 | 6.00 | 34.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Containment[25], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | Containment INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | Containment INFLUENCE India, Japan, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Containment INFLUENCE Japan, North Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Containment INFLUENCE Japan, South Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `COMECON[14], Nasser[15], Suez Crisis[28], Decolonization[30], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | COMECON INFLUENCE Japan, North Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | COMECON INFLUENCE Japan, South Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 3 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 4 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Suez Crisis[28], Decolonization[30], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Suez Crisis INFLUENCE Japan, North Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | Suez Crisis INFLUENCE Japan, South Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | De-Stalinization INFLUENCE Japan, North Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Special Relationship INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Decolonization[30], De-Stalinization[33], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | De-Stalinization INFLUENCE Japan, North Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization INFLUENCE Japan, South Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | De-Stalinization INFLUENCE Japan, Egypt | 16.90 | 6.00 | 31.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | De-Stalinization INFLUENCE East Germany, Japan | 16.75 | 6.00 | 31.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 2 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Special Relationship INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Special Relationship INFLUENCE North Korea, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Decolonization[30], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Syria | 14.40 | 4.00 | 26.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Syria | 14.40 | 4.00 | 26.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Nasser COUP Syria | 11.55 | 4.00 | 19.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Nasser COUP Israel | 10.75 | 4.00 | 18.90 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, offside_ops_penalty |
| 5 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 41: T3 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 2 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Special Relationship INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Special Relationship INFLUENCE North Korea, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Special Relationship INFLUENCE South Korea, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Iraq | 14.15 | 4.00 | 22.30 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |
| 2 | The Cambridge Five COUP Iraq | 10.00 | 4.00 | 22.30 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open, offside_ops_penalty |
| 3 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Nasser COUP Israel | 9.75 | 4.00 | 17.90 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, offside_ops_penalty |
| 5 | Nasser INFLUENCE Iraq | 9.65 | 6.00 | 15.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP -2, DEFCON +0, MilOps U+0/A-2`

## Step 43: T4 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Suez Crisis[28], Summit[48], Missile Envy[52], We Will Bury You[53], Muslim Revolution[59], ABM Treaty[60], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], COMECON[14], De Gaulle Leads France[17], Marshall Plan[23], Suez Crisis[28], Nuclear Subs[44], Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Suez Crisis[28], Summit[48], Missile Envy[52], Muslim Revolution[59], ABM Treaty[60], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE UK, West Germany, Mexico, Algeria | 69.35 | 6.00 | 63.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 2 | ABM Treaty INFLUENCE UK, West Germany, Mexico, Algeria | 69.35 | 6.00 | 63.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 3 | Muslim Revolution INFLUENCE East Germany, West Germany, Mexico, Algeria | 69.25 | 6.00 | 63.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 4 | Muslim Revolution INFLUENCE France, West Germany, Mexico, Algeria | 69.25 | 6.00 | 63.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 5 | ABM Treaty INFLUENCE East Germany, West Germany, Mexico, Algeria | 69.25 | 6.00 | 63.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], COMECON[14], De Gaulle Leads France[17], Suez Crisis[28], Nuclear Subs[44], Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE UK, Mexico, South Africa | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | Duck and Cover INFLUENCE UK, Morocco, South Africa | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | Duck and Cover INFLUENCE UK, West Germany, South Africa | 57.65 | 6.00 | 52.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | Duck and Cover INFLUENCE UK, Mexico, Morocco | 57.45 | 6.00 | 51.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |
| 5 | Duck and Cover INFLUENCE UK, West Germany, Mexico | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Suez Crisis[28], Summit[48], Missile Envy[52], ABM Treaty[60], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, West Germany, Algeria, Morocco | 72.60 | 6.00 | 67.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 2 | ABM Treaty INFLUENCE France, West Germany, Algeria, Morocco | 72.60 | 6.00 | 67.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 3 | ABM Treaty INFLUENCE West Germany, Cuba, Algeria, Morocco | 72.10 | 6.00 | 66.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 4 | ABM Treaty INFLUENCE East Germany, France, Algeria, Morocco | 72.00 | 6.00 | 66.60 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 5 | ABM Treaty INFLUENCE Italy, West Germany, Algeria, Morocco | 72.00 | 6.00 | 66.60 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `COMECON[14], De Gaulle Leads France[17], Suez Crisis[28], Nuclear Subs[44], Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE Morocco, South Africa | 43.80 | 6.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Nuclear Subs INFLUENCE West Germany, South Africa | 43.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Nuclear Subs INFLUENCE Algeria, South Africa | 43.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Nuclear Subs INFLUENCE East Germany, South Africa | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Nuclear Subs INFLUENCE France, South Africa | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Suez Crisis[28], Summit[48], Missile Envy[52], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 2 | Summit INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.80 |
| 4 | Suez Crisis INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.80 |
| 5 | Summit INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `COMECON[14], De Gaulle Leads France[17], Suez Crisis[28], Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | De Gaulle Leads France INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Suez Crisis INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | COMECON INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | COMECON INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Summit[48], Missile Envy[52], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 2 | Summit INFLUENCE France, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 3 | Summit INFLUENCE West Germany, Cuba, Algeria | 55.95 | 6.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 4 | Summit INFLUENCE East Germany, France, Algeria | 55.85 | 6.00 | 50.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |
| 5 | Summit INFLUENCE Italy, West Germany, Algeria | 55.85 | 6.00 | 50.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `De Gaulle Leads France[17], Suez Crisis[28], Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | De Gaulle Leads France INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Suez Crisis INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Iraq, South Africa | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Missile Envy[52], John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 2 | Missile Envy INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Missile Envy INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Suez Crisis[28], Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Suez Crisis INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Suez Crisis INFLUENCE West Germany, Iraq, South Africa | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Suez Crisis INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Suez Crisis INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `John Paul II Elected Pope[69], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 2 | Colonial Rear Guards INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 3 | Colonial Rear Guards INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:24.00 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:24.00 |
| 5 | Colonial Rear Guards INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Kitchen Debates [51] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Kitchen Debates[51], Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:24.00 |
| 2 | Willy Brandt INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Flower Power INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Willy Brandt INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Willy Brandt INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `John Paul II Elected Pope[69], Sadat Expels Soviets[73]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Sadat Expels Soviets INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Willy Brandt[58], Flower Power[62]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Flower Power INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Willy Brandt INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Willy Brandt INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Flower Power INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 59: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], Red Scare/Purge[31], UN Intervention[32], De-Stalinization[33], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], The Cambridge Five[36], Quagmire[45], Ussuri River Skirmish[77], Che[83]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Quagmire EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], UN Intervention[32], De-Stalinization[33], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |
| 4 | De-Stalinization INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |
| 5 | U2 Incident INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], Nuclear Test Ban[34], The Cambridge Five[36], Quagmire[45], Ussuri River Skirmish[77], Che[83]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE East Germany, West Germany, South Africa | 53.90 | 6.00 | 48.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 2 | Nuclear Test Ban INFLUENCE France, West Germany, South Africa | 53.90 | 6.00 | 48.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 3 | Nuclear Test Ban INFLUENCE West Germany, Iraq, South Africa | 53.65 | 6.00 | 48.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 4 | Nuclear Test Ban INFLUENCE Poland, West Germany, South Africa | 53.40 | 6.00 | 48.00 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 5 | Nuclear Test Ban INFLUENCE West Germany, Cuba, South Africa | 53.40 | 6.00 | 48.00 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], UN Intervention[32], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:5.00 |
| 2 | U2 Incident INFLUENCE France, West Germany, Cuba | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.00 |
| 3 | U2 Incident INFLUENCE France, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:5.00 |
| 4 | U2 Incident INFLUENCE France, Italy, West Germany | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:5.00 |
| 5 | U2 Incident INFLUENCE France, West Germany, Morocco | 57.05 | 6.00 | 51.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Morocco:14.80, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], The Cambridge Five[36], Quagmire[45], Ussuri River Skirmish[77], Che[83]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 2 | Ussuri River Skirmish COUP Mexico | 38.17 | 4.00 | 34.62 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.83, defcon_penalty:3, expected_swing:2.5 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 4 | Ussuri River Skirmish INFLUENCE France, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 5 | Ussuri River Skirmish INFLUENCE Iraq, South Africa | 37.65 | 6.00 | 32.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], UN Intervention[32], How I Learned to Stop Worrying[49], Junta[50]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Vietnam Revolts INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:5`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], The Cambridge Five[36], Quagmire[45], Che[83]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Iraq | 25.65 | 4.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, coup_access_open |
| 2 | CIA Created COUP Mexico | 24.80 | 4.00 | 20.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | CIA Created COUP Algeria | 24.05 | 4.00 | 20.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 67: T5 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], UN Intervention[32], How I Learned to Stop Worrying[49], Junta[50]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 2 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 3 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 4 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 5 | How I Learned to Stop Worrying INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], The Cambridge Five[36], Quagmire[45], Che[83]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Che INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Quagmire INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Quagmire INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Che INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], UN Intervention[32], Junta[50]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 2 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 3 | Junta INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:10.00 |
| 4 | Junta INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:10.00 |
| 5 | Junta INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], The Cambridge Five[36], Che[83]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Che INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Che INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Che INFLUENCE Iraq, South Africa | 17.65 | 6.00 | 32.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Che INFLUENCE Poland, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], UN Intervention[32]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 2 | Five Year Plan INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 3 | Five Year Plan INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | Five Year Plan INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Five Year Plan INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Romanian Abdication INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Romanian Abdication INFLUENCE France | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Romanian Abdication INFLUENCE Iraq | 9.15 | 6.00 | 15.30 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], UN Intervention[32]`
- state: `VP 3, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Saharan States | 22.45 | 4.00 | 18.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP Saharan States | 22.45 | 4.00 | 18.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:45.00 |
| 4 | UN Intervention INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:45.00 |
| 5 | Blockade INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:45.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 74: T5 AR7 US

- chosen: `Korean War [11] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], The Cambridge Five[36]`
- state: `VP 3, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War COUP Colombia | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Korean War COUP Saharan States | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Korean War COUP SE African States | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Korean War COUP Zimbabwe | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | The Cambridge Five COUP Colombia | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-1`

## Step 75: T6 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], Special Relationship[37], Arms Race[42], Bear Trap[47], Brezhnev Doctrine[54], Cultural Revolution[61], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Containment[25], Decolonization[30], Special Relationship[37], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67], Shuttle Diplomacy[74]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], Special Relationship[37], Bear Trap[47], Brezhnev Doctrine[54], Cultural Revolution[61], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.14 |
| 2 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.14 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.14 |
| 4 | Brezhnev Doctrine INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.14 |
| 5 | Cultural Revolution INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Decolonization[30], Special Relationship[37], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67], Shuttle Diplomacy[74]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE West Germany, Brazil, Venezuela, South Africa | 69.90 | 6.00 | 64.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Brazil, South Africa | 69.75 | 6.00 | 64.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Venezuela, South Africa | 69.75 | 6.00 | 64.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 4 | Shuttle Diplomacy INFLUENCE France, West Germany, Brazil, South Africa | 69.75 | 6.00 | 64.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 5 | Shuttle Diplomacy INFLUENCE France, West Germany, Venezuela, South Africa | 69.75 | 6.00 | 64.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], Special Relationship[37], Bear Trap[47], Cultural Revolution[61], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 3 | Cultural Revolution INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | Cultural Revolution INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Cultural Revolution INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Decolonization[30], Special Relationship[37], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Argentina, Brazil, Venezuela | 61.80 | 6.00 | 56.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.00 |
| 2 | Lonely Hearts Club Band INFLUENCE Argentina, Brazil, Venezuela | 61.80 | 6.00 | 56.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.00 |
| 3 | Puppet Governments INFLUENCE Argentina, Brazil, Venezuela | 61.80 | 6.00 | 56.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:6.00 |
| 4 | Special Relationship INFLUENCE Brazil, Venezuela, South Africa | 60.90 | 6.00 | 55.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Lonely Hearts Club Band INFLUENCE Brazil, Venezuela, South Africa | 60.90 | 6.00 | 55.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], Special Relationship[37], Bear Trap[47], One Small Step[81]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |
| 2 | One Small Step INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |
| 3 | One Small Step INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:7.20 |
| 4 | One Small Step INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:7.20 |
| 5 | One Small Step INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Decolonization[30], Portuguese Empire Crumbles[55], Lonely Hearts Club Band[65], Puppet Governments[67]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE Argentina, Chile, South Africa | 62.00 | 6.00 | 56.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 2 | Puppet Governments INFLUENCE Argentina, Chile, South Africa | 62.00 | 6.00 | 56.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 3 | Lonely Hearts Club Band INFLUENCE West Germany, Argentina, Chile | 61.35 | 6.00 | 55.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:7.20 |
| 4 | Puppet Governments INFLUENCE West Germany, Argentina, Chile | 61.35 | 6.00 | 55.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:7.20 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, Argentina, Chile | 60.75 | 6.00 | 55.05 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], Special Relationship[37], Bear Trap[47]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Duck and Cover INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Duck and Cover INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Bear Trap INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Decolonization[30], Portuguese Empire Crumbles[55], Puppet Governments[67]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE Argentina, Chile, South Africa | 55.50 | 6.00 | 49.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 2 | Puppet Governments INFLUENCE West Germany, Chile, South Africa | 55.45 | 6.00 | 49.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 3 | Puppet Governments INFLUENCE East Germany, Chile, South Africa | 54.85 | 6.00 | 49.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 4 | Puppet Governments INFLUENCE France, Chile, South Africa | 54.85 | 6.00 | 49.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 5 | Puppet Governments INFLUENCE West Germany, Argentina, Chile | 54.85 | 6.00 | 49.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Nasser[15], Independent Reds[22], Special Relationship[37], Bear Trap[47]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Bear Trap INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Bear Trap INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Bear Trap INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Decolonization[30], Portuguese Empire Crumbles[55]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Chile, South Africa | 49.45 | 6.00 | 59.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, Chile, South Africa | 49.45 | 6.00 | 59.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Decolonization INFLUENCE West Germany, Argentina, Chile | 48.85 | 6.00 | 59.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE West Germany, Argentina, Chile | 48.85 | 6.00 | 59.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Truman Doctrine INFLUENCE West Germany, Chile | 48.80 | 6.00 | 42.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Nasser[15], Independent Reds[22], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Mexico | 28.80 | 4.00 | 24.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5 |
| 2 | Nasser COUP Algeria | 28.05 | 4.00 | 24.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Nasser COUP Syria | 26.05 | 4.00 | 22.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:6, milops_urgency:3.00, coup_access_open, expected_swing:0.5 |
| 4 | Nasser COUP Morocco | 25.65 | 4.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3 |
| 5 | Nasser COUP Israel | 25.25 | 4.00 | 21.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:6, milops_urgency:3.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 88: T6 AR6 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Portuguese Empire Crumbles[55]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE Mexico, Chile, South Africa | 39.75 | 6.00 | 50.05 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE Argentina, Chile, South Africa | 39.50 | 6.00 | 49.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Truman Doctrine INFLUENCE Chile, South Africa | 39.45 | 6.00 | 33.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:36.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE West Germany, Chile, South Africa | 39.45 | 6.00 | 49.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE Mexico, Argentina, Chile | 39.15 | 6.00 | 49.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Independent Reds[22], Special Relationship[37]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, Mexico | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 2 | Special Relationship INFLUENCE West Germany, Mexico | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 3 | Independent Reds INFLUENCE East Germany, Mexico | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 4 | Independent Reds INFLUENCE France, Mexico | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 5 | Special Relationship INFLUENCE East Germany, Mexico | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:45.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE West Germany, Chile | 43.80 | 6.00 | 37.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:54.00 |
| 2 | Truman Doctrine INFLUENCE West Germany, South Africa | 43.80 | 6.00 | 37.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:54.00 |
| 3 | Truman Doctrine INFLUENCE West Germany, Argentina | 43.20 | 6.00 | 37.35 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, non_coup_milops_penalty:54.00 |
| 4 | Truman Doctrine INFLUENCE East Germany, West Germany | 42.55 | 6.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:54.00 |
| 5 | Truman Doctrine INFLUENCE France, West Germany | 42.55 | 6.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:54.00 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 91: T7 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], COMECON[14], NORAD[38], Brush War[39], Allende[57], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], De-Stalinization[33], Cuban Missile Crisis[43], SALT Negotiations[46], OPEC[64], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], NORAD[38], Brush War[39], Allende[57], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Brush War INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 3 | Brush War INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | Brush War INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Brush War INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], De-Stalinization[33], SALT Negotiations[46], OPEC[64], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE West Germany, Chile, South Africa | 60.30 | 6.00 | 54.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Chile, South Africa | 60.30 | 6.00 | 54.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | SALT Negotiations INFLUENCE West Germany, Argentina, Chile | 59.70 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 4 | SALT Negotiations INFLUENCE West Germany, Argentina, South Africa | 59.70 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Argentina, Chile | 59.70 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], NORAD[38], Allende[57], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | NORAD INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | NORAD INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | NORAD INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | NORAD INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], De-Stalinization[33], OPEC[64], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Chile, South Africa | 60.30 | 6.00 | 54.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Argentina, Chile | 59.70 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Argentina, South Africa | 59.70 | 6.00 | 54.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Chile | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Allende[57], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.40 |
| 2 | Allende INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.40 |
| 3 | Lone Gunman INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.40 |
| 4 | Blockade INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:8.40 |
| 5 | Blockade INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], De-Stalinization[33], OPEC[64]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Chile, South Africa | 40.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 2 | De-Stalinization INFLUENCE West Germany, Chile, South Africa | 40.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 3 | OPEC INFLUENCE West Germany, Chile, South Africa | 40.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 4 | Socialist Governments INFLUENCE West Germany, Argentina, Chile | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 5 | Socialist Governments INFLUENCE West Germany, Argentina, South Africa | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Allende [57] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Allende[57], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 2 | Lone Gunman INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 3 | Allende INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:10.50 |
| 4 | Allende INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:10.50 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], De-Stalinization[33], OPEC[64]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Chile, South Africa | 40.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 2 | OPEC INFLUENCE West Germany, Chile, South Africa | 40.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 3 | De-Stalinization INFLUENCE West Germany, Argentina, Chile | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 4 | De-Stalinization INFLUENCE West Germany, Argentina, South Africa | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 5 | OPEC INFLUENCE West Germany, Argentina, Chile | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 2 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Grain Sales to Soviets INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Nixon Plays the China Card INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], OPEC[64]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE West Germany, Chile, South Africa | 40.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | OPEC INFLUENCE West Germany, Argentina, Chile | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | OPEC INFLUENCE West Germany, Argentina, South Africa | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | OPEC INFLUENCE East Germany, West Germany, Chile | 39.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | OPEC INFLUENCE East Germany, West Germany, South Africa | 39.05 | 6.00 | 53.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Grain Sales to Soviets[68], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Nixon Plays the China Card INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, Chile | 27.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, South Africa | 27.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Arab-Israeli War INFLUENCE West Germany, Argentina | 27.05 | 6.00 | 37.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:42.00 |
| 5 | Arab-Israeli War INFLUENCE East Germany, West Germany | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Nixon Plays the China Card INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Nixon Plays the China Card INFLUENCE West Germany, Cuba | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:63.00 |
| 2 | Captured Nazi Scientist INFLUENCE Chile | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:63.00 |
| 3 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:63.00 |
| 4 | Captured Nazi Scientist INFLUENCE Argentina | 22.05 | 6.00 | 16.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Argentina:16.20, non_coup_milops_penalty:63.00 |
| 5 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], De Gaulle Leads France[17], UN Intervention[32], Summit[48], Missile Envy[52], OPEC[64], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], NORAD[38], Arms Race[42], Bear Trap[47], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], UN Intervention[32], Summit[48], Missile Envy[52], OPEC[64], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Summit INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Summit INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | OPEC INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Arms Race[42], Bear Trap[47], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 61.55 | 6.00 | 56.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:6.86 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 61.55 | 6.00 | 56.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:6.86 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 61.55 | 6.00 | 56.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:6.86 |
| 4 | Arms Race INFLUENCE France, Poland, West Germany | 61.05 | 6.00 | 55.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:6.86 |
| 5 | Bear Trap INFLUENCE France, Poland, West Germany | 61.05 | 6.00 | 55.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], UN Intervention[32], Missile Envy[52], OPEC[64], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | OPEC INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | OPEC INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | OPEC INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.00 |
| 5 | OPEC INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Bear Trap[47], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 60.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 60.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 3 | Bear Trap INFLUENCE East Germany, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 4 | Bear Trap INFLUENCE France, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.00 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], UN Intervention[32], Missile Envy[52], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Missile Envy INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 4 | Latin American Death Squads INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Missile Envy INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 60.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 3 | Sadat Expels Soviets INFLUENCE France, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |
| 5 | Sadat Expels Soviets INFLUENCE France, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], UN Intervention[32], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Latin American Death Squads INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Latin American Death Squads INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 4 | Latin American Death Squads INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Latin American Death Squads INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], U2 Incident[63], Grain Sales to Soviets[68], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 3 | Grain Sales to Soviets INFLUENCE Poland, West Germany | 43.40 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 4 | Grain Sales to Soviets INFLUENCE Italy, West Germany | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 5 | Grain Sales to Soviets INFLUENCE West Germany, Cuba | 43.15 | 6.00 | 37.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Duck and Cover[4], UN Intervention[32], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Duck and Cover INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Duck and Cover INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], U2 Incident[63], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | U2 Incident INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | U2 Incident INFLUENCE France, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Che INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `UN Intervention[32], Ask Not What Your Country Can Do For You[78], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | AWACS Sale to Saudis INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Che[83], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | Che INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 3 | Che INFLUENCE France, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 4 | Che INFLUENCE East Germany, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | Che INFLUENCE France, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `UN Intervention[32], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 3 | AWACS Sale to Saudis INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 5 | AWACS Sale to Saudis INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE West Germany | 27.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:72.00 |
| 2 | Panama Canal Returned INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:72.00 |
| 3 | Panama Canal Returned INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:72.00 |
| 4 | Panama Canal Returned INFLUENCE Poland | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Poland:14.30, access_touch:Poland, non_coup_milops_penalty:72.00 |
| 5 | Panama Canal Returned INFLUENCE Italy | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], COMECON[14], Independent Reds[22], Suez Crisis[28], Our Man in Tehran[84], North Sea Oil[89], Defectors[108], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Wargames [103] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], NORAD[38], Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Nixon Plays the China Card[72], Iranian Hostage Crisis[85], Reagan Bombs Libya[87], Wargames[103]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Independent Reds[22], Suez Crisis[28], Our Man in Tehran[84], North Sea Oil[89], Defectors[108], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | Suez Crisis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | Suez Crisis INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 4 | Suez Crisis INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:7.71 |
| 5 | Suez Crisis INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], NORAD[38], Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Nixon Plays the China Card[72], Iranian Hostage Crisis[85], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 60.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:7.71 |
| 2 | NORAD INFLUENCE East Germany, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:7.71 |
| 3 | NORAD INFLUENCE France, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:7.71 |
| 4 | NORAD INFLUENCE East Germany, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:7.71 |
| 5 | NORAD INFLUENCE France, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Independent Reds[22], Our Man in Tehran[84], North Sea Oil[89], Defectors[108], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Vietnam Revolts INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Vietnam Revolts INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], Nuclear Subs[44], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Nixon Plays the China Card[72], Iranian Hostage Crisis[85], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.00 |
| 2 | Nuclear Subs INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.00 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.00 |
| 4 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.00 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Independent Reds[22], Our Man in Tehran[84], North Sea Oil[89], Defectors[108], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:10.80 |
| 4 | Colonial Rear Guards INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Colonial Rear Guards INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], How I Learned to Stop Worrying[49], Brezhnev Doctrine[54], Nixon Plays the China Card[72], Iranian Hostage Crisis[85], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.80 |
| 2 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.80 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.80 |
| 4 | Nixon Plays the China Card INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.80 |
| 5 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Independent Reds[22], Our Man in Tehran[84], North Sea Oil[89], Defectors[108]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 2 | North Sea Oil INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 3 | North Sea Oil INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 4 | North Sea Oil INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 5 | North Sea Oil INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], Brezhnev Doctrine[54], Nixon Plays the China Card[72], Iranian Hostage Crisis[85], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.50 |
| 2 | Nixon Plays the China Card INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.50 |
| 3 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.50 |
| 4 | Reagan Bombs Libya INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.50 |
| 5 | Nixon Plays the China Card INFLUENCE Poland, West Germany | 43.40 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Independent Reds[22], Our Man in Tehran[84], Defectors[108]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Independent Reds INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Defectors INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Reagan Bombs Libya [87] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Arab-Israeli War[13], Brezhnev Doctrine[54], Iranian Hostage Crisis[85], Reagan Bombs Libya[87]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Reagan Bombs Libya INFLUENCE East Germany, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:18.00 |
| 2 | Reagan Bombs Libya INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:18.00 |
| 3 | Reagan Bombs Libya INFLUENCE Poland, West Germany | 43.40 | 6.00 | 37.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:18.00 |
| 4 | Reagan Bombs Libya INFLUENCE Italy, West Germany | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:18.00 |
| 5 | Reagan Bombs Libya INFLUENCE West Germany, Cuba | 43.15 | 6.00 | 37.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Our Man in Tehran[84], Defectors[108]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Defectors INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Defectors INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Brezhnev Doctrine[54], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Brezhnev Doctrine INFLUENCE France, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Iranian Hostage Crisis INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Defectors [108] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Defectors[108]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Defectors INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Defectors INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:81.00 |
| 4 | Defectors INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Defectors INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Arab-Israeli War[13], Iranian Hostage Crisis[85]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Iranian Hostage Crisis INFLUENCE France, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 4 | Iranian Hostage Crisis INFLUENCE East Germany, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Iranian Hostage Crisis INFLUENCE France, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Summit [48] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], Summit[48], Brezhnev Doctrine[54], Cultural Revolution[61], Lonely Hearts Club Band[65], Chernobyl[97], Latin American Debt Crisis[98]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Latin American Debt Crisis EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Ussuri River Skirmish [77] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Decolonization[30], The Cambridge Five[36], Muslim Revolution[59], Liberation Theology[76], Ussuri River Skirmish[77], The Iron Lady[86], The Reformer[90], Glasnost[93], Lone Gunman[109]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 4 | Glasnost EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | The Reformer EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +2, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], Brezhnev Doctrine[54], Cultural Revolution[61], Lonely Hearts Club Band[65], Chernobyl[97], Latin American Debt Crisis[98]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Angola | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:8.57 |
| 2 | Brezhnev Doctrine INFLUENCE France, West Germany, Angola | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:8.57 |
| 3 | Cultural Revolution INFLUENCE East Germany, West Germany, Angola | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:8.57 |
| 4 | Cultural Revolution INFLUENCE France, West Germany, Angola | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:8.57 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, France, Angola | 57.25 | 6.00 | 51.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Decolonization[30], The Cambridge Five[36], Muslim Revolution[59], Liberation Theology[76], The Iron Lady[86], The Reformer[90], Glasnost[93], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 60.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.57 |
| 2 | The Iron Lady INFLUENCE East Germany, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.57 |
| 3 | The Iron Lady INFLUENCE France, Poland, West Germany | 59.55 | 6.00 | 54.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.57 |
| 4 | The Iron Lady INFLUENCE East Germany, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.57 |
| 5 | The Iron Lady INFLUENCE France, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], Cultural Revolution[61], Lonely Hearts Club Band[65], Chernobyl[97], Latin American Debt Crisis[98]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 3 | Cultural Revolution INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 4 | Cultural Revolution INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.00 |
| 5 | Cultural Revolution INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Muslim Revolution[59], Liberation Theology[76], The Reformer[90], Glasnost[93], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Poland, West Germany | 51.70 | 6.00 | 70.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Glasnost INFLUENCE East Germany, France, Poland, West Germany | 51.70 | 6.00 | 70.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Muslim Revolution INFLUENCE East Germany, France, Italy, West Germany | 51.60 | 6.00 | 70.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Glasnost INFLUENCE East Germany, France, Italy, West Germany | 51.60 | 6.00 | 70.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 51.45 | 6.00 | 70.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Latin American Debt Crisis [98] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], Lonely Hearts Club Band[65], Chernobyl[97], Latin American Debt Crisis[98]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Latin American Debt Crisis INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Latin American Debt Crisis INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 4 | Latin American Debt Crisis INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Latin American Debt Crisis INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Glasnost [93] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Liberation Theology[76], The Reformer[90], Glasnost[93], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost INFLUENCE East Germany, France, Italy, West Germany | 51.60 | 6.00 | 70.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Glasnost INFLUENCE East Germany, France, West Germany, Cuba | 51.45 | 6.00 | 70.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Glasnost INFLUENCE East Germany, France, West Germany, Iraq | 50.95 | 6.00 | 69.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Iraq:13.55, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Glasnost INFLUENCE East Germany, Italy, West Germany, Cuba | 50.85 | 6.00 | 69.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Glasnost INFLUENCE France, Italy, West Germany, Cuba | 50.85 | 6.00 | 69.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Special Relationship[37], Lonely Hearts Club Band[65], Chernobyl[97]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 3 | Duck and Cover INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 4 | Duck and Cover INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 5 | Chernobyl INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `The Reformer [90] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Liberation Theology[76], The Reformer[90], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 2 | The Reformer INFLUENCE East Germany, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 3 | The Reformer INFLUENCE France, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 4 | The Reformer INFLUENCE East Germany, West Germany, Cuba | 39.30 | 6.00 | 53.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 5 | The Reformer INFLUENCE France, West Germany, Cuba | 39.30 | 6.00 | 53.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Special Relationship[37], Lonely Hearts Club Band[65], Chernobyl[97]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Chernobyl INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Chernobyl INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Chernobyl INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Chernobyl INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Liberation Theology[76], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Decolonization INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Special Relationship[37], Lonely Hearts Club Band[65]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 2 | Special Relationship INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 4 | Lonely Hearts Club Band INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `The Cambridge Five[36], Liberation Theology[76], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 5 | The Cambridge Five INFLUENCE Italy, West Germany | 27.30 | 6.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Lonely Hearts Club Band[65]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | Lonely Hearts Club Band INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:90.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | Lonely Hearts Club Band INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Liberation Theology[76], Lone Gunman[109]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | Liberation Theology INFLUENCE France, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | Liberation Theology INFLUENCE Italy, West Germany | 27.30 | 6.00 | 37.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 4 | Liberation Theology INFLUENCE West Germany, Cuba | 27.15 | 6.00 | 37.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | Liberation Theology INFLUENCE West Germany, Iraq | 26.65 | 6.00 | 36.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, influence:Iraq:13.55, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP -3, DEFCON +1, MilOps U+0/A+0`
