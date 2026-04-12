# minimal_hybrid detailed rollout log

- seed: `20260410`
- winner: `USSR`
- final_vp: `4`
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

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Duck and Cover[4], Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE Pakistan, Thailand | 42.60 | 6.00 | 36.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45 |
| 4 | Duck and Cover INFLUENCE East Germany, Pakistan, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Duck and Cover INFLUENCE East Germany, Israel, Thailand | 42.45 | 6.00 | 56.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Pakistan, Israel, Thailand | 38.85 | 6.00 | 53.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Duck and Cover INFLUENCE Japan, Pakistan, Thailand | 38.60 | 6.00 | 53.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Duck and Cover INFLUENCE Japan, Israel, Thailand | 38.55 | 6.00 | 53.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Duck and Cover INFLUENCE Italy, Pakistan, Thailand | 38.40 | 6.00 | 52.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Duck and Cover INFLUENCE Pakistan, Philippines, Thailand | 38.40 | 6.00 | 52.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Marshall Plan[23], UN Intervention[32]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE India, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Socialist Governments INFLUENCE Japan, Pakistan, Thailand | 62.10 | 6.00 | 56.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Socialist Governments INFLUENCE Italy, Pakistan, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Socialist Governments INFLUENCE Pakistan, Philippines, Thailand | 61.90 | 6.00 | 56.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Socialist Governments INFLUENCE Pakistan, Saudi Arabia, Thailand | 61.75 | 6.00 | 56.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], East European Unrest[29], NORAD[38]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Japan, North Korea, Philippines, Thailand | 54.50 | 6.00 | 73.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 2 | Marshall Plan INFLUENCE Italy, Japan, North Korea, Thailand | 54.50 | 6.00 | 73.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 3 | Marshall Plan INFLUENCE Japan, North Korea, Saudi Arabia, Thailand | 54.35 | 6.00 | 72.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 4 | Marshall Plan INFLUENCE Italy, North Korea, Philippines, Thailand | 54.30 | 6.00 | 72.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 5 | Marshall Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 54.20 | 6.00 | 72.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], East European Unrest[29], NORAD[38]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan, Philippines | 56.80 | 6.00 | 51.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.40 |
| 2 | NORAD INFLUENCE West Germany, Japan, Philippines | 56.80 | 6.00 | 51.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.40 |
| 3 | East European Unrest INFLUENCE Japan, North Korea, Philippines | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.40 |
| 4 | East European Unrest INFLUENCE Japan, South Korea, Philippines | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.40 |
| 5 | NORAD INFLUENCE Japan, North Korea, Philippines | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Indonesia | 49.05 | 4.00 | 45.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | Captured Nazi Scientist COUP Indonesia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP Indonesia | 42.20 | 4.00 | 38.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Olympic Games INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 22: T2 AR3 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], NORAD[38]`
- state: `VP 4, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 54.90 | 4.00 | 51.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 2 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 3 | NORAD INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | NORAD INFLUENCE Japan, North Korea, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 5 | NORAD INFLUENCE West Germany, Japan, Indonesia | 52.70 | 6.00 | 47.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 23: T2 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Five Year Plan INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Five Year Plan INFLUENCE Italy, Saudi Arabia, Thailand | 37.75 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Five Year Plan INFLUENCE India, Japan, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, West Germany, Japan | 36.80 | 6.00 | 51.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | De Gaulle Leads France INFLUENCE Italy, Japan, North Korea | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |
| 3 | De Gaulle Leads France INFLUENCE Italy, Japan, South Korea | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty |
| 4 | De Gaulle Leads France INFLUENCE Italy, Japan, Egypt | 36.35 | 6.00 | 50.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 5 | De Gaulle Leads France INFLUENCE Italy, West Germany, North Korea | 36.20 | 6.00 | 50.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:North Korea:15.55, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Independent Reds INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Independent Reds INFLUENCE Saudi Arabia, Thailand | 25.95 | 6.00 | 36.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Blockade[10], Truman Doctrine[19]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Truman Doctrine INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65 |
| 3 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 4 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |
| 5 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china`
- hand: `Independent Reds[22], UN Intervention[32]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Independent Reds INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 3 | Independent Reds INFLUENCE Saudi Arabia, Thailand | 25.95 | 6.00 | 36.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Independent Reds INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Blockade[10]`
- state: `VP 4, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |
| 3 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty |
| 4 | Fidel INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 5 | Fidel INFLUENCE East Germany, Japan | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-2/A-3`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], COMECON[14], Captured Nazi Scientist[18], CIA Created[26], Red Scare/Purge[31], UN Intervention[32], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Containment[25], Suez Crisis[28], East European Unrest[29], Decolonization[30], Nuclear Test Ban[34], The Cambridge Five[36], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], COMECON[14], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | COMECON INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | COMECON INFLUENCE India, Japan, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 4 | COMECON INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 5 | COMECON INFLUENCE Japan, South Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Duck and Cover [4] as COUP`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Containment[25], Suez Crisis[28], East European Unrest[29], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover COUP Italy | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 2 | Duck and Cover COUP Philippines | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 3 | Containment COUP Italy | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 4 | Containment COUP Philippines | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |
| 5 | East European Unrest COUP Italy | 39.50 | 4.00 | 35.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Italy, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 33: T3 AR2 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 4, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Indonesia | 42.40 | 4.00 | 38.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Indonesia | 42.40 | 4.00 | 38.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Indonesia | 42.40 | 4.00 | 38.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.60, coup_access_open, expected_swing:2.5 |
| 4 | Five Year Plan INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 34: T3 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `none`
- hand: `Containment[25], Suez Crisis[28], East European Unrest[29], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | East European Unrest INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 4 | Containment INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |
| 5 | Containment INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | Five Year Plan INFLUENCE India, Japan, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Five Year Plan INFLUENCE Japan, South Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `none`
- hand: `Suez Crisis[28], East European Unrest[29], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | East European Unrest INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |
| 4 | East European Unrest INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55 |
| 5 | NORAD INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Special Relationship INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `none`
- hand: `Suez Crisis[28], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | NORAD INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |
| 3 | NORAD INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55 |
| 4 | NORAD INFLUENCE Japan, Egypt | 36.90 | 6.00 | 31.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt |
| 5 | NORAD INFLUENCE East Germany, Japan | 36.75 | 6.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 2 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Special Relationship INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Special Relationship INFLUENCE North Korea, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Suez Crisis[28], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Suez Crisis INFLUENCE Japan, North Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |
| 3 | Suez Crisis INFLUENCE Japan, South Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty |
| 4 | Suez Crisis INFLUENCE Japan, Egypt | 16.90 | 6.00 | 31.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 5 | Suez Crisis INFLUENCE East Germany, Japan | 16.75 | 6.00 | 31.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Special Relationship INFLUENCE West Germany, Thailand | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Special Relationship INFLUENCE India, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Special Relationship INFLUENCE North Korea, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Special Relationship INFLUENCE South Korea, Thailand | 25.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U1/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Syria | 9.40 | 4.00 | 21.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | The Cambridge Five COUP Syria | 9.40 | 4.00 | 21.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Decolonization SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 4 | The Cambridge Five SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Decolonization INFLUENCE Japan | 5.85 | 6.00 | 16.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, offside_ops_penalty |

- effects: `VP -2, DEFCON +1, MilOps U-1/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Marshall Plan[23], Suez Crisis[28], East European Unrest[29], Summit[48], Missile Envy[52], Willy Brandt[58], Muslim Revolution[59], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Containment[25], Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], ABM Treaty[60], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Marshall Plan[23], Suez Crisis[28], East European Unrest[29], Summit[48], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Indonesia | 54.29 | 4.00 | 50.74 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:4.5 |
| 2 | Summit COUP Indonesia | 54.29 | 4.00 | 50.74 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:4.5 |
| 3 | Suez Crisis INFLUENCE West Germany, Mexico, Algeria | 53.85 | 6.00 | 48.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 4 | Summit INFLUENCE West Germany, Mexico, Algeria | 53.85 | 6.00 | 48.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 5 | Suez Crisis INFLUENCE UK, West Germany, Mexico | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 46: T4 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Containment[25], Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | Containment INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | Duck and Cover INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | Containment INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | Duck and Cover INFLUENCE East Germany, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Marshall Plan[23], East European Unrest[29], Summit[48], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE West Germany, Mexico, Algeria | 53.85 | 6.00 | 48.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.00 |
| 2 | Summit INFLUENCE UK, West Germany, Mexico | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:1.00 |
| 3 | Summit INFLUENCE East Germany, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:1.00 |
| 4 | Summit INFLUENCE France, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:1.00 |
| 5 | Summit INFLUENCE UK, Mexico, Algeria | 53.35 | 6.00 | 47.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Containment[25], Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Algeria, South Africa | 59.20 | 6.00 | 53.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Containment INFLUENCE France, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Containment INFLUENCE East Germany, Algeria, South Africa | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Containment INFLUENCE France, Algeria, South Africa | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Marshall Plan[23], East European Unrest[29], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, UK, West Germany, Morocco | 45.05 | 6.00 | 63.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 2 | Marshall Plan INFLUENCE France, UK, West Germany, Morocco | 45.05 | 6.00 | 63.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 3 | Marshall Plan INFLUENCE East Germany, France, West Germany, Morocco | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 4 | Marshall Plan INFLUENCE UK, West Germany, Cuba, Morocco | 44.55 | 6.00 | 63.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.20 |
| 5 | Marshall Plan INFLUENCE East Germany, France, UK, Morocco | 44.45 | 6.00 | 63.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:UK:14.15, access_touch:UK, influence:Morocco:14.80, access_touch:Morocco, offside_ops_penalty, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], We Will Bury You[53], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE UK, West Germany, Morocco, South Africa | 49.80 | 6.00 | 68.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | We Will Bury You INFLUENCE East Germany, UK, Morocco, South Africa | 49.20 | 6.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | We Will Bury You INFLUENCE France, UK, Morocco, South Africa | 49.20 | 6.00 | 67.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:UK:14.15, control_break:UK, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | We Will Bury You INFLUENCE East Germany, UK, West Germany, South Africa | 49.05 | 6.00 | 67.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | We Will Bury You INFLUENCE France, UK, West Germany, South Africa | 49.05 | 6.00 | 67.65 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `East European Unrest[29], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |
| 2 | Missile Envy INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |
| 4 | Willy Brandt INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:4`
- hand: `Decolonization[30], Nuclear Subs[44], Kitchen Debates[51], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Indonesia | 48.30 | 4.00 | 44.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | John Paul II Elected Pope COUP Indonesia | 48.30 | 4.00 | 44.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 3 | Kitchen Debates COUP Indonesia | 41.45 | 4.00 | 37.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:1.00, coup_access_open, expected_swing:2.5 |
| 4 | Nuclear Subs INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 53: T4 AR5 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `East European Unrest[29], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 2 | Willy Brandt INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 5 | Willy Brandt INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Decolonization[30], Kitchen Debates[51], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 3 | John Paul II Elected Pope INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 4 | John Paul II Elected Pope INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 5 | John Paul II Elected Pope INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `East European Unrest[29], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Colonial Rear Guards INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Colonial Rear Guards INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:6.00 |
| 5 | Colonial Rear Guards INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Decolonization[30], Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Kitchen Debates INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 3 | Flower Power INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Decolonization INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Decolonization INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `East European Unrest[29], Sadat Expels Soviets[73]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | East European Unrest INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | East European Unrest INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:2`
- hand: `Kitchen Debates[51], Flower Power[62]`
- state: `VP -2, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Syria | 24.05 | 4.00 | 20.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5 |
| 2 | Kitchen Debates COUP Mexico | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Kitchen Debates INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:18.00 |
| 4 | Flower Power INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Kitchen Debates COUP Algeria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +1, DEFCON +1, MilOps U-3/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], COMECON[14], De Gaulle Leads France[17], Red Scare/Purge[31], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Suez Crisis[28], UN Intervention[32], Nuclear Test Ban[34], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `COMECON [14] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], COMECON[14], De Gaulle Leads France[17], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON COUP Indonesia | 54.58 | 4.00 | 51.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 2 | De Gaulle Leads France COUP Indonesia | 54.58 | 4.00 | 51.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | U2 Incident COUP Indonesia | 54.58 | 4.00 | 51.03 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 4 | COMECON INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |
| 5 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 62: T5 AR1 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Suez Crisis[28], UN Intervention[32], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Indonesia | 47.73 | 4.00 | 44.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Indonesia | 40.88 | 4.00 | 37.03 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 3 | CIA Created COUP Indonesia | 40.88 | 4.00 | 37.03 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 4 | UN Intervention COUP Indonesia | 40.88 | 4.00 | 37.03 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 5 | Panama Canal Returned COUP Indonesia | 40.88 | 4.00 | 37.03 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 63: T5 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], De Gaulle Leads France[17], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:2.00 |
| 4 | De Gaulle Leads France INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:2.00 |
| 5 | U2 Incident INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Suez Crisis[28], UN Intervention[32], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 2 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 3 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 4 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 2 | U2 Incident INFLUENCE France, West Germany, Cuba | 57.30 | 6.00 | 51.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:2.40 |
| 3 | U2 Incident INFLUENCE France, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:2.40 |
| 4 | U2 Incident INFLUENCE France, Italy, West Germany | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 5 | U2 Incident INFLUENCE France, West Germany, Morocco | 57.05 | 6.00 | 51.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Morocco:14.80, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Vietnam Revolts[9], CIA Created[26], Suez Crisis[28], UN Intervention[32], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.60 |
| 2 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.60 |
| 3 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.60 |
| 4 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.60 |
| 5 | UN Intervention INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], How I Learned to Stop Worrying[49], Junta[50]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 2 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 3 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 4 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 5 | How I Learned to Stop Worrying INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Suez Crisis[28], UN Intervention[32], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:4.50 |
| 2 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:4.50 |
| 3 | UN Intervention INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.50 |
| 4 | Panama Canal Returned INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.50 |
| 5 | UN Intervention COUP Iraq | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Junta[50]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 2 | Junta INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 3 | Junta INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:4.00 |
| 4 | Junta INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:4.00 |
| 5 | Junta INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Suez Crisis[28], Panama Canal Returned[111]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Panama Canal Returned COUP Iraq | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open |
| 3 | Panama Canal Returned INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | Panama Canal Returned INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:6.00 |
| 5 | Panama Canal Returned INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Five Year Plan INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Five Year Plan INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Five Year Plan INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Five Year Plan INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Suez Crisis[28]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Suez Crisis INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Socialist Governments INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Socialist Governments INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Suez Crisis INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Syria | 24.05 | 4.00 | 20.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5 |
| 2 | Blockade COUP Mexico | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Blockade COUP Algeria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.00 |
| 5 | Blockade INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Suez Crisis [28] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Suez Crisis[28]`
- state: `VP -3, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Mexico | 19.00 | 4.00 | 35.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |
| 2 | Suez Crisis INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Suez Crisis COUP Algeria | 18.25 | 4.00 | 34.70 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:2.5, offside_ops_penalty |
| 4 | Suez Crisis INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Suez Crisis INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U-3/A-2`

## Step 75: T6 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Duck and Cover[4], Korean War[11], Romanian Abdication[12], Independent Reds[22], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Arms Race[42], Quagmire[45], Brezhnev Doctrine[54]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Five Year Plan[5], Truman Doctrine[19], Containment[25], Bear Trap[47], Allende[57], OAS Founded[71], Shuttle Diplomacy[74], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], Independent Reds[22], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Quagmire[45], Brezhnev Doctrine[54]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 2 | Quagmire INFLUENCE France, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 4 | Brezhnev Doctrine INFLUENCE France, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 5 | Quagmire INFLUENCE West Germany, Cuba, Mexico | 53.20 | 6.00 | 47.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Containment[25], Bear Trap[47], Allende[57], OAS Founded[71], Shuttle Diplomacy[74], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 2 | Containment INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 3 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 4 | Bear Trap INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], Independent Reds[22], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Brezhnev Doctrine[54]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 3 | Brezhnev Doctrine INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Bear Trap[47], Allende[57], OAS Founded[71], Shuttle Diplomacy[74], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Bear Trap INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Shuttle Diplomacy INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Independent Reds[22], US/Japan Mutual Defense Pact[27], The Cambridge Five[36]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Cuba | 43.70 | 6.00 | 62.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Mexico | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, Italy, West Germany | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Morocco | 43.45 | 6.00 | 62.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Egypt | 43.35 | 6.00 | 61.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Egypt:13.20, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57], OAS Founded[71], Shuttle Diplomacy[74], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 2 | Shuttle Diplomacy INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 4 | Ussuri River Skirmish INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |
| 5 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], Independent Reds[22], The Cambridge Five[36]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 2 | Korean War INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.00 |
| 5 | Korean War INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57], OAS Founded[71], Ussuri River Skirmish[77], Alliance for Progress[79]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 2 | Ussuri River Skirmish INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 3 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 4 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |
| 5 | Ussuri River Skirmish INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Romanian Abdication[12], Independent Reds[22], The Cambridge Five[36]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:12.00 |
| 4 | The Cambridge Five INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 5 | The Cambridge Five INFLUENCE West Germany, Mexico | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57], OAS Founded[71], Alliance for Progress[79]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 2 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 3 | Alliance for Progress INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 4 | Alliance for Progress INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |
| 5 | Alliance for Progress INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Romanian Abdication[12], Independent Reds[22]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 2 | Romanian Abdication INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:36.00 |
| 3 | Romanian Abdication INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:36.00 |
| 4 | Independent Reds INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Independent Reds INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Allende[57], OAS Founded[71]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:36.00 |
| 2 | OAS Founded INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:36.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 4 | OAS Founded INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 5 | Truman Doctrine INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Independent Reds[22]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Independent Reds INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Independent Reds INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Independent Reds INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Independent Reds INFLUENCE West Germany, Mexico | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `OAS Founded [71] as COUP`
- flags: `milops_shortfall:6`
- hand: `Allende[57], OAS Founded[71]`
- state: `VP -5, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded COUP Colombia | 24.45 | 4.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | OAS Founded COUP Saharan States | 24.45 | 4.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | OAS Founded COUP SE African States | 24.45 | 4.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:SE African States, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | OAS Founded COUP Zimbabwe | 24.45 | 4.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Zimbabwe, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | OAS Founded COUP Guatemala | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32], Brush War[39], Cuban Missile Crisis[43], Portuguese Empire Crumbles[55], South African Unrest[56], Cultural Revolution[61], OPEC[64]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], NORAD[38], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70], Voice of America[75], Ask Not What Your Country Can Do For You[78], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32], Cuban Missile Crisis[43], Portuguese Empire Crumbles[55], South African Unrest[56], Cultural Revolution[61], OPEC[64]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE West Germany, Brazil, Chile | 55.70 | 6.00 | 50.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |
| 2 | Cultural Revolution INFLUENCE West Germany, Brazil, Chile | 55.70 | 6.00 | 50.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |
| 3 | OPEC INFLUENCE West Germany, Brazil, Chile | 55.70 | 6.00 | 50.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |
| 4 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Chile | 55.55 | 6.00 | 50.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |
| 5 | Cuban Missile Crisis INFLUENCE France, West Germany, Chile | 55.55 | 6.00 | 50.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70], Voice of America[75], Ask Not What Your Country Can Do For You[78], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32], Portuguese Empire Crumbles[55], South African Unrest[56], Cultural Revolution[61], OPEC[64]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE Argentina, Brazil, Chile | 59.25 | 6.00 | 53.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 2 | OPEC INFLUENCE Argentina, Brazil, Chile | 59.25 | 6.00 | 53.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 3 | Cultural Revolution INFLUENCE West Germany, Argentina, Brazil | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:7.00 |
| 4 | OPEC INFLUENCE West Germany, Argentina, Brazil | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, non_coup_milops_penalty:7.00 |
| 5 | Cultural Revolution INFLUENCE Argentina, Brazil, Venezuela | 58.15 | 6.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Puppet Governments[67], Grain Sales to Soviets[68], Latin American Death Squads[70], Voice of America[75], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 3 | Latin American Death Squads INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 4 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 5 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32], Portuguese Empire Crumbles[55], South African Unrest[56], OPEC[64]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE West Germany, Argentina, Chile | 64.70 | 6.00 | 59.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.40 |
| 2 | OPEC INFLUENCE Argentina, Chile, Venezuela | 64.25 | 6.00 | 58.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, control_break:Chile, influence:Venezuela:14.20, access_touch:Venezuela, non_coup_milops_penalty:8.40 |
| 3 | OPEC INFLUENCE East Germany, Argentina, Chile | 64.10 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.40 |
| 4 | OPEC INFLUENCE France, Argentina, Chile | 64.10 | 6.00 | 58.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.40 |
| 5 | OPEC INFLUENCE Italy, Argentina, Chile | 63.50 | 6.00 | 57.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Grain Sales to Soviets[68], Latin American Death Squads[70], Voice of America[75], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 2 | Latin American Death Squads INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 3 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 4 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32], Portuguese Empire Crumbles[55], South African Unrest[56]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:10.50 |
| 2 | South African Unrest INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:10.50 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:10.50 |
| 4 | South African Unrest INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:10.50 |
| 5 | Portuguese Empire Crumbles INFLUENCE Chile, Venezuela | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Latin American Death Squads[70], Voice of America[75], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.50 |
| 2 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.50 |
| 3 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.50 |
| 4 | Latin American Death Squads INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:10.50 |
| 5 | Latin American Death Squads INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32], South African Unrest[56]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 2 | South African Unrest INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 3 | South African Unrest INFLUENCE Chile, Venezuela | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, non_coup_milops_penalty:14.00 |
| 4 | South African Unrest INFLUENCE East Germany, Chile | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 5 | South African Unrest INFLUENCE France, Chile | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Chile:16.80, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Voice of America[75], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 2 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 3 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 4 | Voice of America INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |
| 5 | One Small Step INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], East European Unrest[29], UN Intervention[32]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Argentina, Chile | 34.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | East European Unrest INFLUENCE Argentina, Chile, Venezuela | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | East European Unrest INFLUENCE West Germany, Chile, Venezuela | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Venezuela:14.20, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | East European Unrest INFLUENCE East Germany, Argentina, Chile | 34.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | East European Unrest INFLUENCE France, Argentina, Chile | 34.10 | 6.00 | 48.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], One Small Step[81], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 2 | One Small Step INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 3 | One Small Step INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 4 | One Small Step INFLUENCE Iraq, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, non_coup_milops_penalty:42.00 |
| 5 | One Small Step INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP -6, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 34.05 | 4.00 | 30.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Mexico | 33.30 | 4.00 | 29.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | UN Intervention COUP Algeria | 32.55 | 4.00 | 28.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | UN Intervention COUP Morocco | 30.15 | 4.00 | 26.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3 |
| 5 | UN Intervention COUP Israel | 29.75 | 4.00 | 25.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 106: T7 AR7 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Che[83]`
- state: `VP -6, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Che INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Che INFLUENCE West Germany, Iraq, South Africa | 33.80 | 6.00 | 48.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Che INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Che INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 107: T8 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], Special Relationship[37], We Will Bury You[53], Allende[57], One Small Step[81], Che[83], Pershing II Deployed[102]`
- state: `VP -5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Pershing II Deployed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], De-Stalinization[33], Cuban Missile Crisis[43], Nuclear Subs[44], Summit[48], U2 Incident[63], Lonely Hearts Club Band[65], Sadat Expels Soviets[73], Yuri and Samantha[106]`
- state: `VP -5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +3, DEFCON -2, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], Special Relationship[37], Allende[57], One Small Step[81], Che[83], Pershing II Deployed[102]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Che INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Che INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Pershing II Deployed INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], De-Stalinization[33], Nuclear Subs[44], Summit[48], U2 Incident[63], Lonely Hearts Club Band[65], Sadat Expels Soviets[73], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Summit INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Summit INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Pershing II Deployed [102] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], Special Relationship[37], Allende[57], One Small Step[81], Pershing II Deployed[102]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Pershing II Deployed INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Pershing II Deployed INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Pershing II Deployed INFLUENCE East Germany, West Germany, Venezuela | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, non_coup_milops_penalty:8.00 |
| 5 | Pershing II Deployed INFLUENCE France, West Germany, Venezuela | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], De-Stalinization[33], Nuclear Subs[44], U2 Incident[63], Lonely Hearts Club Band[65], Sadat Expels Soviets[73], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Sadat Expels Soviets INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Sadat Expels Soviets INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], Special Relationship[37], Allende[57], One Small Step[81]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | One Small Step INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.60 |
| 4 | One Small Step INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | One Small Step INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], De-Stalinization[33], Nuclear Subs[44], U2 Incident[63], Lonely Hearts Club Band[65], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 2 | Nuclear Subs INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 4 | Lonely Hearts Club Band INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 5 | Nuclear Subs INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], Special Relationship[37], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Containment INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Duck and Cover INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Duck and Cover INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Containment INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Nasser[15], De-Stalinization[33], U2 Incident[63], Lonely Hearts Club Band[65], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Lonely Hearts Club Band INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Lonely Hearts Club Band INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 5 | Lonely Hearts Club Band INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Truman Doctrine[19], Containment[25], Special Relationship[37], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Containment INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Containment INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Containment INFLUENCE East Germany, West Germany, Venezuela | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Containment INFLUENCE France, West Germany, Venezuela | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Venezuela:13.70, access_touch:Venezuela, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], De-Stalinization[33], U2 Incident[63], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, Algeria | 36.95 | 6.00 | 51.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | De-Stalinization INFLUENCE France, West Germany, Algeria | 36.95 | 6.00 | 51.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | U2 Incident INFLUENCE East Germany, West Germany, Algeria | 36.95 | 6.00 | 51.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | U2 Incident INFLUENCE France, West Germany, Algeria | 36.95 | 6.00 | 51.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | De-Stalinization INFLUENCE Poland, West Germany, Algeria | 36.45 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | Special Relationship INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 3 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 4 | Special Relationship INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | Special Relationship INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], U2 Incident[63], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | U2 Incident INFLUENCE East Germany, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 3 | U2 Incident INFLUENCE France, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 4 | U2 Incident INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | U2 Incident INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Allende [57] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Truman Doctrine[19], Allende[57]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:72.00 |
| 2 | Allende INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:72.00 |
| 3 | Allende INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:72.00 |
| 4 | Allende INFLUENCE Italy | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70, non_coup_milops_penalty:72.00 |
| 5 | Allende INFLUENCE Turkey | 21.05 | 6.00 | 15.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Yuri and Samantha [106] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 2 | Yuri and Samantha INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 3 | Yuri and Samantha INFLUENCE Poland, West Germany | 22.40 | 6.00 | 32.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 4 | Yuri and Samantha INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 5 | Yuri and Samantha INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Wargames [103] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Liberation Theology[76], Wargames[103]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Ussuri River Skirmish [77] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Indo-Pakistani War[24], Decolonization[30], Latin American Death Squads[70], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, Angola | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:7.71 |
| 2 | De Gaulle Leads France INFLUENCE France, West Germany, Angola | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:7.71 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, France, Angola | 57.25 | 6.00 | 51.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:7.71 |
| 4 | De Gaulle Leads France INFLUENCE Italy, West Germany, Angola | 57.25 | 6.00 | 51.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:7.71 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Angola, South Africa | 56.85 | 6.00 | 51.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:Angola:12.60, control_break:Angola, access_touch:Angola, influence:South Africa:13.80, access_touch:South Africa, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Indo-Pakistani War[24], Decolonization[30], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | North Sea Oil INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 5 | North Sea Oil INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Blockade[10], The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Vietnam Revolts INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Indo-Pakistani War[24], Decolonization[30], Latin American Death Squads[70], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | North Sea Oil INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | North Sea Oil INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | North Sea Oil INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | North Sea Oil INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], Blockade[10], The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 4 | Willy Brandt INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Indo-Pakistani War[24], Decolonization[30], Latin American Death Squads[70], Our Man in Tehran[84], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | Indo-Pakistani War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 4 | Latin American Death Squads INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], Blockade[10], Willy Brandt[58], Grain Sales to Soviets[68], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 2 | Willy Brandt INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 5 | Willy Brandt INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Decolonization[30], Latin American Death Squads[70], Our Man in Tehran[84], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 2 | Latin American Death Squads INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 5 | Latin American Death Squads INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], Blockade[10], Grain Sales to Soviets[68], Liberation Theology[76]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 2 | Liberation Theology INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 3 | Liberation Theology INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:18.00 |
| 4 | Liberation Theology INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 5 | Liberation Theology INFLUENCE West Germany, South Africa | 37.90 | 6.00 | 32.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Decolonization[30], Our Man in Tehran[84], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 3 | Our Man in Tehran INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 4 | Our Man in Tehran INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:18.00 |
| 5 | Our Man in Tehran INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Grain Sales to Soviets[68]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Five Year Plan INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Five Year Plan INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Five Year Plan INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Five Year Plan INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Decolonization[30], Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Decolonization INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Latin American Debt Crisis INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Blockade[10], Grain Sales to Soviets[68]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Blockade INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:81.00 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Grain Sales to Soviets INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Latin American Debt Crisis [98] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Latin American Debt Crisis[98], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Latin American Debt Crisis INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Latin American Debt Crisis INFLUENCE Poland, West Germany | 22.40 | 6.00 | 32.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], Romanian Abdication[12], Suez Crisis[28], Red Scare/Purge[31], Kitchen Debates[51], ABM Treaty[60], Soviets Shoot Down KAL 007[92], Glasnost[93], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Glasnost EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `East European Unrest[29], Red Scare/Purge[31], Arms Race[42], Portuguese Empire Crumbles[55], South African Unrest[56], Latin American Death Squads[70], OAS Founded[71], Alliance for Progress[79], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], Romanian Abdication[12], Suez Crisis[28], Kitchen Debates[51], ABM Treaty[60], Soviets Shoot Down KAL 007[92], Glasnost[93], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, West Germany | 54.90 | 6.00 | 49.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | Glasnost INFLUENCE East Germany, France, West Germany | 54.90 | 6.00 | 49.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | ABM Treaty INFLUENCE East Germany, Italy, West Germany | 54.30 | 6.00 | 48.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | ABM Treaty INFLUENCE France, Italy, West Germany | 54.30 | 6.00 | 48.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 5 | Glasnost INFLUENCE East Germany, Italy, West Germany | 54.30 | 6.00 | 48.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `East European Unrest[29], Arms Race[42], Portuguese Empire Crumbles[55], South African Unrest[56], Latin American Death Squads[70], OAS Founded[71], Alliance for Progress[79], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | East European Unrest INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | Arms Race INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | Arms Race INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 5 | Alliance for Progress INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Glasnost [93] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], Romanian Abdication[12], Suez Crisis[28], Kitchen Debates[51], Soviets Shoot Down KAL 007[92], Glasnost[93], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost INFLUENCE East Germany, France, West Germany | 54.90 | 6.00 | 49.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | Glasnost INFLUENCE East Germany, Italy, West Germany | 54.30 | 6.00 | 48.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 3 | Glasnost INFLUENCE France, Italy, West Germany | 54.30 | 6.00 | 48.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 4 | Glasnost INFLUENCE East Germany, West Germany, South Africa | 53.90 | 6.00 | 48.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, non_coup_milops_penalty:10.00 |
| 5 | Glasnost INFLUENCE France, West Germany, South Africa | 53.90 | 6.00 | 48.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Arms Race[42], Portuguese Empire Crumbles[55], South African Unrest[56], Latin American Death Squads[70], OAS Founded[71], Alliance for Progress[79], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | Arms Race INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 3 | Alliance for Progress INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 4 | Alliance for Progress INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 5 | Arms Race INFLUENCE Poland, West Germany | 38.25 | 6.00 | 32.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Socialist Governments[7], Romanian Abdication[12], Suez Crisis[28], Kitchen Debates[51], Soviets Shoot Down KAL 007[92], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Socialist Governments INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Suez Crisis INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Socialist Governments INFLUENCE East Germany, France | 38.15 | 6.00 | 32.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56], Latin American Death Squads[70], OAS Founded[71], Alliance for Progress[79], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Alliance for Progress INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Alliance for Progress INFLUENCE Poland, West Germany | 38.25 | 6.00 | 32.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 4 | Alliance for Progress INFLUENCE East Germany, France | 38.15 | 6.00 | 32.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 5 | Alliance for Progress INFLUENCE Italy, West Germany | 38.15 | 6.00 | 32.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Romanian Abdication[12], Suez Crisis[28], Kitchen Debates[51], Soviets Shoot Down KAL 007[92], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 2 | Suez Crisis INFLUENCE France, West Germany | 38.75 | 6.00 | 33.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 3 | Suez Crisis INFLUENCE East Germany, France | 38.15 | 6.00 | 32.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:15.00 |
| 4 | Suez Crisis INFLUENCE Italy, West Germany | 38.15 | 6.00 | 32.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 5 | Suez Crisis INFLUENCE West Germany, South Africa | 37.75 | 6.00 | 32.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `OAS Founded [71] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56], Latin American Death Squads[70], OAS Founded[71], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany | 22.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:15.00 |
| 3 | OAS Founded INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:15.00 |
| 4 | OAS Founded INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:15.00 |
| 5 | Latin American Death Squads INFLUENCE East Germany | 22.00 | 6.00 | 16.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Soviets Shoot Down KAL 007 [92] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Romanian Abdication[12], Kitchen Debates[51], Soviets Shoot Down KAL 007[92], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, France, West Germany | 30.90 | 6.00 | 49.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, Italy, West Germany | 30.30 | 6.00 | 48.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Soviets Shoot Down KAL 007 INFLUENCE France, Italy, West Germany | 30.30 | 6.00 | 48.90 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Soviets Shoot Down KAL 007 INFLUENCE East Germany, West Germany, South Africa | 29.90 | 6.00 | 48.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Soviets Shoot Down KAL 007 INFLUENCE France, West Germany, South Africa | 29.90 | 6.00 | 48.50 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56], Latin American Death Squads[70], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany | 22.60 | 6.00 | 16.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Latin American Death Squads INFLUENCE East Germany | 22.00 | 6.00 | 16.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:20.00 |
| 3 | Latin American Death Squads INFLUENCE France | 22.00 | 6.00 | 16.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, non_coup_milops_penalty:20.00 |
| 4 | Latin American Death Squads INFLUENCE Poland | 21.50 | 6.00 | 15.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, non_coup_milops_penalty:20.00 |
| 5 | Latin American Death Squads INFLUENCE Italy | 21.40 | 6.00 | 15.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Romanian Abdication[12], Kitchen Debates[51], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:60.00 |
| 2 | Romanian Abdication INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:60.00 |
| 3 | Romanian Abdication INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:60.00 |
| 4 | Romanian Abdication INFLUENCE Italy | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70, non_coup_milops_penalty:60.00 |
| 5 | Romanian Abdication INFLUENCE South Africa | 21.15 | 6.00 | 15.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:13.80, access_touch:South Africa, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 2 | Iranian Hostage Crisis INFLUENCE France, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 3 | Iranian Hostage Crisis INFLUENCE Poland, West Germany | 18.25 | 6.00 | 32.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 4 | Iranian Hostage Crisis INFLUENCE East Germany, France | 18.15 | 6.00 | 32.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 5 | Iranian Hostage Crisis INFLUENCE Italy, West Germany | 18.15 | 6.00 | 32.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Kitchen Debates[51], AWACS Sale to Saudis[107]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | AWACS Sale to Saudis INFLUENCE France, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | AWACS Sale to Saudis INFLUENCE East Germany, France | 18.15 | 6.00 | 32.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 4 | AWACS Sale to Saudis INFLUENCE Italy, West Germany | 18.15 | 6.00 | 32.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | AWACS Sale to Saudis INFLUENCE West Germany, South Africa | 17.75 | 6.00 | 32.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.90, influence:South Africa:13.80, access_touch:South Africa, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as SPACE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play, space_play`
- hand: `Portuguese Empire Crumbles[55], South African Unrest[56]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | South African Unrest SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany | 6.60 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 4 | South African Unrest INFLUENCE West Germany | 6.60 | 6.00 | 16.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany | 6.00 | 6.00 | 16.30 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP +6, DEFCON +1, MilOps U+0/A+0`
