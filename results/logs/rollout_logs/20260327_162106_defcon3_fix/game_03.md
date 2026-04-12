# minimal_hybrid detailed rollout log

- seed: `20260412`
- winner: `USSR`
- final_vp: `5`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Warsaw Pact Formed [16] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Fidel[8], Korean War[11], Arab-Israeli War[13], Warsaw Pact Formed[16], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], Marshall Plan[23], CIA Created[26], US/Japan Mutual Defense Pact[27], Decolonization[30], Red Scare/Purge[31]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `De-Stalinization [33] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Fidel[8], Korean War[11], Arab-Israeli War[13], De-Stalinization[33], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Iran | 76.08 | 4.00 | 72.53 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5, opening_iran_coup_bonus |
| 2 | Fidel COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Korean War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Arab-Israeli War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | The Cambridge Five COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 4: T1 AR1 US

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], CIA Created[26], US/Japan Mutual Defense Pact[27], Decolonization[30], Red Scare/Purge[31]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Italy, Turkey, Indonesia, Philippines | 82.10 | 6.00 | 76.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 2 | Red Scare/Purge INFLUENCE Italy, Turkey, Indonesia, Philippines | 82.10 | 6.00 | 76.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE Italy, North Korea, Indonesia, Philippines | 81.70 | 6.00 | 76.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 4 | Red Scare/Purge INFLUENCE Italy, North Korea, Indonesia, Philippines | 81.70 | 6.00 | 76.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, Italy, Indonesia, Philippines | 81.20 | 6.00 | 75.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Italy:14.45, control_break:Italy, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china`
- hand: `Fidel[8], Korean War[11], Arab-Israeli War[13], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Korean War COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Arab-Israeli War COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | The Cambridge Five COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Fidel INFLUENCE Japan, Thailand | 45.30 | 6.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], CIA Created[26], Decolonization[30], Red Scare/Purge[31]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE East Germany, Japan, North Korea, Panama | 71.35 | 6.00 | 65.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Japan:16.15, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.20 |
| 2 | Red Scare/Purge INFLUENCE East Germany, West Germany, North Korea, Panama | 70.85 | 6.00 | 65.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.20 |
| 3 | Red Scare/Purge INFLUENCE East Germany, West Germany, Japan, North Korea | 70.80 | 6.00 | 65.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 4 | Red Scare/Purge INFLUENCE East Germany, North Korea, South Korea, Panama | 70.75 | 6.00 | 65.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:North Korea:15.55, access_touch:North Korea, influence:South Korea:15.55, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.20 |
| 5 | Red Scare/Purge INFLUENCE East Germany, Japan, North Korea, South Korea | 70.70 | 6.00 | 65.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Japan:16.15, influence:North Korea:15.55, access_touch:North Korea, influence:South Korea:15.55, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china`
- hand: `Korean War[11], Arab-Israeli War[13], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE North Korea, Thailand | 48.20 | 6.00 | 42.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Arab-Israeli War INFLUENCE North Korea, Thailand | 48.20 | 6.00 | 42.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 3 | The Cambridge Five INFLUENCE North Korea, Thailand | 48.20 | 6.00 | 42.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 4 | NORAD INFLUENCE Japan, North Korea, Thailand | 45.70 | 6.00 | 60.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | Korean War INFLUENCE Japan, Thailand | 45.30 | 6.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Nasser[15], Independent Reds[22], CIA Created[26], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:1.50 |
| 2 | Duck and Cover INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:1.50 |
| 3 | Duck and Cover INFLUENCE Japan, North Korea, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:1.50 |
| 4 | Duck and Cover INFLUENCE West Germany, Japan, Egypt | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:1.50 |
| 5 | Duck and Cover INFLUENCE Japan, North Korea, Egypt | 52.45 | 6.00 | 46.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china`
- hand: `Arab-Israeli War[13], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE North Korea, Thailand | 51.70 | 6.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 2 | The Cambridge Five INFLUENCE North Korea, Thailand | 51.70 | 6.00 | 46.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand |
| 3 | NORAD INFLUENCE Japan, North Korea, Thailand | 49.20 | 6.00 | 63.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Arab-Israeli War INFLUENCE Japan, Thailand | 48.80 | 6.00 | 43.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand |
| 5 | The Cambridge Five INFLUENCE Japan, Thailand | 48.80 | 6.00 | 43.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Nasser[15], Independent Reds[22], CIA Created[26], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, Japan | 42.50 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.00 |
| 2 | Independent Reds INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 3 | Independent Reds INFLUENCE Japan, South Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 4 | Independent Reds INFLUENCE Japan, Egypt | 42.05 | 6.00 | 36.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 5 | Independent Reds INFLUENCE East Germany, Japan | 41.90 | 6.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Thailand | 43.80 | 6.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE West Germany, Thailand | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE South Korea, Thailand | 43.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45 |
| 5 | The Cambridge Five INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Nasser[15], CIA Created[26], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Japan | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:6.00 |
| 2 | Decolonization INFLUENCE West Germany, Japan | 26.50 | 6.00 | 36.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Decolonization INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Decolonization INFLUENCE Japan, South Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Decolonization INFLUENCE Japan, Egypt | 26.05 | 6.00 | 36.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, South Korea, Thailand | 40.20 | 6.00 | 54.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE West Germany, Israel, Thailand | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE South Korea, Israel, Thailand | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 4 | NORAD INFLUENCE West Germany, Japan, Thailand | 39.30 | 6.00 | 53.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty |
| 5 | NORAD INFLUENCE Japan, South Korea, Thailand | 39.20 | 6.00 | 53.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], Decolonization[30]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Decolonization INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Decolonization INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Decolonization INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Decolonization INFLUENCE East Germany, Japan | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +3, DEFCON +1, MilOps U-3/A+0`

## Step 15: T2 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Romanian Abdication[12], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], Suez Crisis[28], East European Unrest[29]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], Olympic Games[20], NATO[21], UN Intervention[32], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Romanian Abdication[12], Indo-Pakistani War[24], Containment[25], Suez Crisis[28], East European Unrest[29]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE France, Israel, Thailand | 62.45 | 6.00 | 56.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Suez Crisis INFLUENCE France, Japan, Thailand | 62.20 | 6.00 | 56.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Suez Crisis INFLUENCE France, Italy, Thailand | 62.00 | 6.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Suez Crisis INFLUENCE France, Philippines, Thailand | 62.00 | 6.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Suez Crisis INFLUENCE France, Saudi Arabia, Thailand | 61.85 | 6.00 | 56.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], Olympic Games[20], UN Intervention[32], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE France, West Germany, Japan, North Korea | 69.30 | 6.00 | 63.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 2 | Nuclear Test Ban INFLUENCE France, West Germany, Japan, South Korea | 69.30 | 6.00 | 63.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 3 | Nuclear Test Ban INFLUENCE France, Japan, North Korea, South Korea | 69.20 | 6.00 | 63.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 4 | Nuclear Test Ban INFLUENCE France, West Germany, Japan, Egypt | 68.95 | 6.00 | 63.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 5 | Nuclear Test Ban INFLUENCE France, Japan, North Korea, Egypt | 68.85 | 6.00 | 63.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Romanian Abdication[12], Indo-Pakistani War[24], Containment[25], East European Unrest[29]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 2 | Five Year Plan INFLUENCE France, North Korea, Thailand | 46.60 | 6.00 | 61.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 3 | Containment INFLUENCE France, North Korea, Thailand | 46.60 | 6.00 | 61.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 4 | East European Unrest INFLUENCE France, North Korea, Thailand | 46.60 | 6.00 | 61.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.40 |
| 5 | Indo-Pakistani War INFLUENCE France, North Korea | 46.30 | 6.00 | 40.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.05, control_break:France, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], Olympic Games[20], UN Intervention[32], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, Japan | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 2 | Special Relationship INFLUENCE West Germany, Japan | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:2.40 |
| 3 | Olympic Games INFLUENCE Japan, North Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |
| 4 | Olympic Games INFLUENCE Japan, South Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |
| 5 | Special Relationship INFLUENCE Japan, North Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Romanian Abdication[12], Containment[25], East European Unrest[29]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE France, Japan, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Containment INFLUENCE France, Japan, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | East European Unrest INFLUENCE France, Japan, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Five Year Plan INFLUENCE France, Italy, Thailand | 42.00 | 6.00 | 56.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Five Year Plan INFLUENCE France, Philippines, Thailand | 42.00 | 6.00 | 56.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], UN Intervention[32], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, Japan | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:3.00 |
| 2 | Special Relationship INFLUENCE Japan, North Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 3 | Special Relationship INFLUENCE Japan, South Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | Special Relationship INFLUENCE Japan, Egypt | 37.05 | 6.00 | 31.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 5 | Special Relationship INFLUENCE East Germany, Japan | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Containment[25], East European Unrest[29]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Containment INFLUENCE Japan, Philippines, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | East European Unrest INFLUENCE Italy, Japan, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | East European Unrest INFLUENCE Japan, Philippines, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Containment INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, West Germany, Japan | 36.80 | 6.00 | 51.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | COMECON INFLUENCE Italy, Japan, North Korea | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | COMECON INFLUENCE Italy, Japan, South Korea | 36.70 | 6.00 | 51.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | COMECON INFLUENCE Italy, Japan, Egypt | 36.35 | 6.00 | 50.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | COMECON INFLUENCE Italy, West Germany, North Korea | 36.20 | 6.00 | 50.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], East European Unrest[29]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Philippines, Thailand | 38.10 | 6.00 | 52.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | East European Unrest INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | East European Unrest INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | East European Unrest INFLUENCE Saudi Arabia, Philippines, Thailand | 37.75 | 6.00 | 52.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | East European Unrest INFLUENCE Japan, North Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Philippines | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:1.00, expected_swing:0.5 |
| 2 | UN Intervention COUP Philippines | 26.80 | 4.00 | 22.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:1.00, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Japan | 25.50 | 4.00 | 21.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 4 | UN Intervention COUP Japan | 25.50 | 4.00 | 21.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 5 | Truman Doctrine INFLUENCE Philippines | 25.30 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 27: T2 AR6 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 3, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 2 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 3 | Blockade INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 4 | Romanian Abdication INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 5 | Blockade INFLUENCE Philippines | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:9.00 |
| 3 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:9.00 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Vietnam Revolts INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP -1, DEFCON +1, MilOps U+0/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], CIA Created[26], Suez Crisis[28], Decolonization[30], UN Intervention[32], De-Stalinization[33]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Fidel[8], Vietnam Revolts[9], Blockade[10], East European Unrest[29], Nuclear Test Ban[34], Special Relationship[37], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], Suez Crisis[28], Decolonization[30], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Japan, Philippines, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | De-Stalinization INFLUENCE Japan, Philippines, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | Suez Crisis INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 4 | De-Stalinization INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 5 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Fidel[8], Vietnam Revolts[9], Blockade[10], East European Unrest[29], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Iraq, Philippines | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 2 | East European Unrest INFLUENCE Japan, Iraq, Philippines | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 3 | NORAD INFLUENCE Japan, Iraq, Philippines | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 4 | Duck and Cover INFLUENCE West Germany, Japan, Philippines | 56.80 | 6.00 | 51.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |
| 5 | East European Unrest INFLUENCE West Germany, Japan, Philippines | 56.80 | 6.00 | 51.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], UN Intervention[32], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Iraq, Thailand | 61.45 | 6.00 | 55.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 2 | De-Stalinization INFLUENCE Iraq, Saudi Arabia, Thailand | 61.10 | 6.00 | 55.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 3 | De-Stalinization INFLUENCE West Germany, Iraq, Thailand | 60.95 | 6.00 | 55.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 4 | De-Stalinization INFLUENCE North Korea, Iraq, Thailand | 60.85 | 6.00 | 55.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 5 | De-Stalinization INFLUENCE South Korea, Iraq, Thailand | 60.85 | 6.00 | 55.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:South Korea:15.55, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], East European Unrest[29], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan, Saudi Arabia | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 2 | NORAD INFLUENCE West Germany, Japan, Saudi Arabia | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 3 | East European Unrest INFLUENCE Japan, North Korea, Saudi Arabia | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 4 | East European Unrest INFLUENCE Japan, South Korea, Saudi Arabia | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 5 | NORAD INFLUENCE Japan, North Korea, Saudi Arabia | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Indonesia | 49.55 | 4.00 | 45.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Indonesia | 42.70 | 4.00 | 38.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 3 | UN Intervention COUP Indonesia | 42.70 | 4.00 | 38.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:2.5 |
| 4 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 5 | Decolonization INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 36: T3 AR3 US

- chosen: `NORAD [38] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Special Relationship[37], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD COUP Indonesia | 56.40 | 4.00 | 52.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.75, coup_access_open, expected_swing:4.5 |
| 2 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:4.50 |
| 3 | NORAD INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:4.50 |
| 4 | NORAD INFLUENCE Japan, North Korea, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:4.50 |
| 5 | NORAD INFLUENCE West Germany, Japan, Indonesia | 52.70 | 6.00 | 47.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 37: T3 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Saudi Arabia, Thailand | 37.95 | 6.00 | 52.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 2 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 37.80 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 3 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 4 | Five Year Plan INFLUENCE Japan, South Korea, Thailand | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |
| 5 | Five Year Plan INFLUENCE Japan, Indonesia, Thailand | 37.50 | 6.00 | 51.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `none`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Special Relationship[37]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, Japan | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | Special Relationship INFLUENCE Japan, North Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |
| 3 | Special Relationship INFLUENCE Japan, South Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55 |
| 4 | Special Relationship INFLUENCE Japan, Egypt | 37.05 | 6.00 | 31.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt |
| 5 | Special Relationship INFLUENCE Japan, Iran | 37.05 | 6.00 | 31.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 3 | Captured Nazi Scientist INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 4 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 5 | Captured Nazi Scientist COUP Syria | 21.55 | 4.00 | 17.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 3 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |
| 4 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty |
| 5 | Vietnam Revolts INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:9.00 |
| 2 | UN Intervention COUP Syria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:9.00 |
| 4 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:9.00 |
| 5 | UN Intervention INFLUENCE North Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10]`
- state: `VP 0, DEFCON 3, MilOps U2/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty |
| 2 | Vietnam Revolts INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty |
| 3 | Vietnam Revolts INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty |
| 4 | Vietnam Revolts INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty |
| 5 | Vietnam Revolts INFLUENCE Japan, Iran | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty |

- effects: `VP -1, DEFCON +1, MilOps U-2/A-3`

## Step 43: T4 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Socialist Governments[7], Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], Nuclear Test Ban[34], Quagmire[45], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], East European Unrest[29], De-Stalinization[33], NORAD[38], Nuclear Subs[44], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Socialist Governments[7], Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], Quagmire[45], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, Mexico | 58.70 | 6.00 | 53.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 2 | Quagmire INFLUENCE East Germany, West Germany, Mexico | 58.70 | 6.00 | 53.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Mexico | 58.70 | 6.00 | 53.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 4 | Socialist Governments INFLUENCE East Germany, Mexico, Algeria | 58.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |
| 5 | Quagmire INFLUENCE East Germany, Mexico, Algeria | 58.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], De-Stalinization[33], NORAD[38], Nuclear Subs[44], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | Sadat Expels Soviets INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | NORAD INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | Sadat Expels Soviets INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | NORAD INFLUENCE East Germany, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Quagmire [45] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], Quagmire[45], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Indonesia | 54.48 | 4.00 | 50.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 2 | Brezhnev Doctrine COUP Indonesia | 54.48 | 4.00 | 50.93 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:4.5 |
| 3 | Quagmire INFLUENCE UK, West Germany, Algeria | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 4 | Brezhnev Doctrine INFLUENCE UK, West Germany, Algeria | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 5 | Quagmire INFLUENCE East Germany, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 48: T4 AR2 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], De-Stalinization[33], Nuclear Subs[44], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP 1, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE West Germany, Algeria, South Africa | 59.20 | 6.00 | 53.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Sadat Expels Soviets INFLUENCE France, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Algeria, South Africa | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Sadat Expels Soviets INFLUENCE France, Algeria, South Africa | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE UK, West Germany, Algeria | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.20 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.20 |
| 3 | Brezhnev Doctrine INFLUENCE France, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:1.20 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, UK, West Germany | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, non_coup_milops_penalty:1.20 |
| 5 | Brezhnev Doctrine INFLUENCE France, UK, West Germany | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Independent Reds [22] as COUP`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], De-Stalinization[33], Nuclear Subs[44], U2 Incident[63], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 4, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Indonesia | 47.90 | 4.00 | 44.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 2 | Nuclear Subs COUP Indonesia | 47.90 | 4.00 | 44.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 3 | Grain Sales to Soviets COUP Indonesia | 47.90 | 4.00 | 44.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:3.5 |
| 4 | Independent Reds INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 5 | Nuclear Subs INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 51: T4 AR4 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Morocco | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:1.50 |
| 2 | Decolonization INFLUENCE East Germany, Morocco | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:1.50 |
| 3 | Decolonization INFLUENCE France, Morocco | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:1.50 |
| 4 | Decolonization INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |
| 5 | Decolonization INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `De-Stalinization[33], Nuclear Subs[44], U2 Incident[63], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 2 | Grain Sales to Soviets INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 3 | Nuclear Subs INFLUENCE UK, Morocco | 41.15 | 6.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.00 |
| 4 | Grain Sales to Soviets INFLUENCE UK, Morocco | 41.15 | 6.00 | 35.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.00 |
| 5 | Nuclear Subs INFLUENCE UK, West Germany | 41.00 | 6.00 | 35.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], CIA Created[26], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 3 | Romanian Abdication INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:2.00 |
| 4 | Romanian Abdication INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:2.00 |
| 5 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `De-Stalinization[33], U2 Incident[63], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE Morocco, South Africa | 38.80 | 6.00 | 33.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 3 | Grain Sales to Soviets INFLUENCE West Germany, Morocco | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:4.00 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |
| 5 | Grain Sales to Soviets INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:6.00 |
| 3 | Captured Nazi Scientist INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:6.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Lonely Hearts Club Band INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `De-Stalinization[33], U2 Incident[63], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | De-Stalinization INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | U2 Incident INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | De-Stalinization INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `CIA Created[26], Lonely Hearts Club Band[65]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, France | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, Cuba | 25.30 | 6.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Lonely Hearts Club Band INFLUENCE East Germany, Italy | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Italy:14.95, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, Mexico | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `U2 Incident[63], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U3/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | U2 Incident INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | U2 Incident INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | U2 Incident INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | U2 Incident INFLUENCE East Germany, France, South Africa | 33.45 | 6.00 | 47.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +1, DEFCON +1, MilOps U-3/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Latin American Death Squads [70] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37], Bear Trap[47], Latin American Death Squads[70], Shuttle Diplomacy[74], One Small Step[81]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Bear Trap EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], CIA Created[26], Red Scare/Purge[31], Missile Envy[52], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37], Bear Trap[47], Shuttle Diplomacy[74], One Small Step[81]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Indonesia | 47.73 | 4.00 | 44.03 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |
| 2 | Captured Nazi Scientist COUP Indonesia | 40.88 | 4.00 | 37.03 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 3 | Five Year Plan COUP Indonesia | 34.58 | 4.00 | 51.03 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Bear Trap COUP Indonesia | 34.58 | 4.00 | 51.03 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | Shuttle Diplomacy COUP Indonesia | 34.58 | 4.00 | 51.03 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 62: T5 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Duck and Cover[4], Five Year Plan[5], Fidel[8], CIA Created[26], Missile Envy[52], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 2 | Duck and Cover INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 3 | Five Year Plan INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 4 | Five Year Plan INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 5 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 2 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:3.00 |
| 3 | Captured Nazi Scientist INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:3.00 |
| 4 | Captured Nazi Scientist COUP Syria | 21.05 | 4.00 | 17.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist INFLUENCE Cuba | 20.90 | 6.00 | 15.05 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Five Year Plan[5], Fidel[8], CIA Created[26], Missile Envy[52], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 2 | Five Year Plan INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 3 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 4 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |
| 5 | Five Year Plan INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | Five Year Plan INFLUENCE France, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | Bear Trap INFLUENCE East Germany, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Bear Trap INFLUENCE France, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], CIA Created[26], Missile Envy[52], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Alliance for Progress INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Alliance for Progress INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Alliance for Progress INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | Bear Trap INFLUENCE France, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | Shuttle Diplomacy INFLUENCE France, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | Bear Trap INFLUENCE West Germany, Cuba | 16.75 | 6.00 | 31.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], CIA Created[26], Missile Envy[52], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.50 |
| 2 | Our Man in Tehran INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.50 |
| 3 | Missile Envy INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.50 |
| 4 | Missile Envy INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.50 |
| 5 | Our Man in Tehran INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37], Shuttle Diplomacy[74]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Shuttle Diplomacy INFLUENCE France, West Germany | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Shuttle Diplomacy INFLUENCE West Germany, Cuba | 16.75 | 6.00 | 31.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, France | 16.65 | 6.00 | 31.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Shuttle Diplomacy INFLUENCE Italy, West Germany | 16.65 | 6.00 | 31.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], CIA Created[26], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 2 | Our Man in Tehran INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 3 | Our Man in Tehran INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 4 | Our Man in Tehran INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |
| 5 | Our Man in Tehran INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE East Germany | 14.40 | 6.00 | 20.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, control_break:East Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Formosan Resolution COUP Syria | 13.90 | 4.00 | 26.20 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Special Relationship COUP Syria | 13.90 | 4.00 | 26.20 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Formosan Resolution COUP Mexico | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Special Relationship COUP Mexico | 13.15 | 4.00 | 25.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:5`
- hand: `Fidel[8], CIA Created[26]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Mexico | 24.30 | 4.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:2.50, defcon_penalty:3, expected_swing:0.5 |
| 2 | CIA Created COUP Algeria | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:2.50, defcon_penalty:3, expected_swing:0.5 |
| 3 | Fidel INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:30.00 |
| 5 | Fidel INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 73: T5 AR7 USSR

- chosen: `Formosan Resolution [35] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Formosan Resolution[35], Special Relationship[37]`
- state: `VP 2, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Saharan States | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Special Relationship COUP Saharan States | 9.30 | 4.00 | 21.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:3.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Formosan Resolution SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Special Relationship SPACE | 7.70 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Formosan Resolution INFLUENCE Mexico | 6.15 | 6.00 | 16.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Fidel[8]`
- state: `VP 2, DEFCON 2, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 31.30 | 4.00 | 43.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Fidel INFLUENCE Mexico, South Africa | 26.45 | 6.00 | 36.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Fidel INFLUENCE West Germany, Mexico | 25.80 | 6.00 | 36.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Fidel INFLUENCE East Germany, Mexico | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Fidel INFLUENCE France, Mexico | 25.20 | 6.00 | 35.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:Mexico:14.95, control_break:Mexico, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-1`

## Step 75: T6 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], COMECON[14], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36], Summit[48], How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `SALT Negotiations [46] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Blockade[10], Indo-Pakistani War[24], Suez Crisis[28], Decolonization[30], De-Stalinization[33], SALT Negotiations[46], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], US/Japan Mutual Defense Pact[27], Suez Crisis[28], The Cambridge Five[36], Summit[48], How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 2 | Suez Crisis INFLUENCE France, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 3 | Summit INFLUENCE East Germany, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 4 | Summit INFLUENCE France, West Germany, Mexico | 53.70 | 6.00 | 48.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |
| 5 | Suez Crisis INFLUENCE West Germany, Cuba, Mexico | 53.20 | 6.00 | 47.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Blockade[10], Indo-Pakistani War[24], Suez Crisis[28], Decolonization[30], De-Stalinization[33], Shuttle Diplomacy[74], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE West Germany, Nigeria, South Africa | 58.60 | 6.00 | 53.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, Nigeria, South Africa | 58.00 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 3 | Shuttle Diplomacy INFLUENCE France, Nigeria, South Africa | 58.00 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 4 | Shuttle Diplomacy INFLUENCE Poland, Nigeria, South Africa | 57.50 | 6.00 | 51.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 5 | Shuttle Diplomacy INFLUENCE Cuba, Nigeria, South Africa | 57.50 | 6.00 | 51.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Summit[48], How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Summit INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 3 | Summit INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 4 | Summit INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Summit INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Blockade[10], Indo-Pakistani War[24], Suez Crisis[28], Decolonization[30], De-Stalinization[33], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Indonesia | 48.30 | 4.00 | 44.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:6, milops_urgency:1.00, coup_access_open, expected_swing:3.5 |
| 2 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Indo-Pakistani War INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Indo-Pakistani War INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Indo-Pakistani War INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 81: T6 AR3 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Cuba | 43.70 | 6.00 | 62.30 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Mexico | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, Italy, West Germany | 43.60 | 6.00 | 62.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Morocco | 43.45 | 6.00 | 62.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80, offside_ops_penalty, non_coup_milops_penalty:7.20 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Egypt | 43.35 | 6.00 | 61.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Egypt:13.20, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Socialist Governments[7], Blockade[10], Suez Crisis[28], Decolonization[30], De-Stalinization[33], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Socialist Governments INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Suez Crisis INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Vietnam Revolts[9], The Cambridge Five[36], How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Saharan States | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 2 | The Cambridge Five COUP Saharan States | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 3 | How I Learned to Stop Worrying COUP Saharan States | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 4 | South African Unrest COUP Saharan States | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |
| 5 | Flower Power COUP Saharan States | 42.30 | 4.00 | 38.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:6, milops_urgency:1.50, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 84: T6 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Suez Crisis[28], Decolonization[30], De-Stalinization[33], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Suez Crisis INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | De-Stalinization INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Che INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `The Cambridge Five[36], How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 2 | How I Learned to Stop Worrying COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 3 | South African Unrest COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 4 | Flower Power COUP Saharan States | 41.97 | 4.00 | 38.27 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:3.5 |
| 5 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Decolonization[30], De-Stalinization[33], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | De-Stalinization INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Che INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Che INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | De-Stalinization INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `How I Learned to Stop Worrying[49], South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 2 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 4 | South African Unrest INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |
| 5 | Flower Power INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Decolonization[30], Che[83], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Che INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Che INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Che INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Che INFLUENCE East Germany, France, South Africa | 33.45 | 6.00 | 47.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `South African Unrest[56], Flower Power[62]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 2 | South African Unrest INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 4 | Flower Power INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:36.00 |
| 5 | South African Unrest INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Decolonization[30], Colonial Rear Guards[110]`
- state: `VP 2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Decolonization INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Decolonization INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Vietnam Revolts[9], East European Unrest[29], Nuclear Test Ban[34], Special Relationship[37], Brush War[39], Kitchen Debates[51], Cultural Revolution[61], OPEC[64], Puppet Governments[67]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Cuban Missile Crisis[43], Portuguese Empire Crumbles[55], Allende[57], Muslim Revolution[59], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Voice of America EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Korean War EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +2, DEFCON -2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Vietnam Revolts[9], East European Unrest[29], Special Relationship[37], Brush War[39], Kitchen Debates[51], Cultural Revolution[61], OPEC[64], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | OPEC INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | Brush War INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Brush War INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Portuguese Empire Crumbles[55], Allende[57], Muslim Revolution[59], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, South Africa | 45.45 | 6.00 | 64.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Muslim Revolution INFLUENCE East Germany, Poland, West Germany, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Muslim Revolution INFLUENCE East Germany, West Germany, Cuba, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Muslim Revolution INFLUENCE France, Poland, West Germany, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Muslim Revolution INFLUENCE France, West Germany, Cuba, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Vietnam Revolts[9], East European Unrest[29], Special Relationship[37], Kitchen Debates[51], Cultural Revolution[61], OPEC[64], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.00 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:7.00 |
| 3 | Cultural Revolution INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:7.00 |
| 4 | Cultural Revolution INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:7.00 |
| 5 | Cultural Revolution INFLUENCE France, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Portuguese Empire Crumbles[55], Allende[57], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 2 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 4 | John Paul II Elected Pope INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |
| 5 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Vietnam Revolts[9], East European Unrest[29], Special Relationship[37], Kitchen Debates[51], OPEC[64], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:8.40 |
| 2 | OPEC INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:8.40 |
| 3 | OPEC INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:8.40 |
| 4 | OPEC INFLUENCE France, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:8.40 |
| 5 | OPEC INFLUENCE France, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Portuguese Empire Crumbles[55], Allende[57], Voice of America[75]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 2 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 3 | Voice of America INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 4 | Voice of America INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |
| 5 | Voice of America INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Vietnam Revolts[9], East European Unrest[29], Special Relationship[37], Kitchen Debates[51], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 2 | Vietnam Revolts INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 3 | Vietnam Revolts INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:10.50 |
| 4 | Vietnam Revolts INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, non_coup_milops_penalty:10.50 |
| 5 | Vietnam Revolts INFLUENCE West Germany, Mexico | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Korean War[11], Arab-Israeli War[13], Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 2 | Arab-Israeli War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 4 | Korean War INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 5 | Korean War INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `East European Unrest[29], Special Relationship[37], Kitchen Debates[51], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | East European Unrest INFLUENCE East Germany, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | East European Unrest INFLUENCE East Germany, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | East European Unrest INFLUENCE France, Italy, West Germany | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | East European Unrest INFLUENCE France, West Germany, Mexico | 32.20 | 6.00 | 46.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13], Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Arab-Israeli War INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Arab-Israeli War INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Special Relationship[37], Kitchen Debates[51], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Special Relationship INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Puppet Governments INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Special Relationship INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Portuguese Empire Crumbles[55], Allende[57]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE Poland, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE Cuba, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Kitchen Debates[51], Puppet Governments[67]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Puppet Governments INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Puppet Governments INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Puppet Governments INFLUENCE Italy, West Germany | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Puppet Governments INFLUENCE West Germany, Mexico | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Allende[57]`
- state: `VP 4, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | Allende INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Blockade INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | Allende INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Blockade INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `ABM Treaty [60] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Truman Doctrine[19], Special Relationship[37], Bear Trap[47], ABM Treaty[60], Puppet Governments[67], Che[83], The Iron Lady[86]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Bear Trap EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Containment[25], Quagmire[45], Flower Power[62], John Paul II Elected Pope[69], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Quagmire EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Truman Doctrine[19], Special Relationship[37], Bear Trap[47], Puppet Governments[67], Che[83], The Iron Lady[86]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Che INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Che INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Che INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Che INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Quagmire[45], Flower Power[62], John Paul II Elected Pope[69], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Latin American Death Squads INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, Poland, West Germany | 54.70 | 6.00 | 49.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | John Paul II Elected Pope INFLUENCE France, Poland, West Germany | 54.70 | 6.00 | 49.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Latin American Death Squads INFLUENCE East Germany, Poland, West Germany | 54.70 | 6.00 | 49.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Truman Doctrine[19], Special Relationship[37], Bear Trap[47], Puppet Governments[67], The Iron Lady[86]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Arab-Israeli War INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:8.00 |
| 4 | Arab-Israeli War INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Arab-Israeli War INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Quagmire[45], Flower Power[62], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Latin American Death Squads INFLUENCE East Germany, Poland, West Germany | 54.70 | 6.00 | 49.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Latin American Death Squads INFLUENCE France, Poland, West Germany | 54.70 | 6.00 | 49.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Latin American Death Squads INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 5 | Latin American Death Squads INFLUENCE France, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Duck and Cover[4], Truman Doctrine[19], Special Relationship[37], Bear Trap[47], Puppet Governments[67], The Iron Lady[86]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | The Iron Lady INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Duck and Cover INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Duck and Cover INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Quagmire[45], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, Poland, West Germany | 50.85 | 6.00 | 65.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 2 | Quagmire INFLUENCE East Germany, France, Italy, West Germany | 50.75 | 6.00 | 65.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 3 | Quagmire INFLUENCE East Germany, France, West Germany, Cuba | 50.60 | 6.00 | 65.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 4 | Quagmire INFLUENCE East Germany, Italy, Poland, West Germany | 50.25 | 6.00 | 64.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Quagmire INFLUENCE France, Italy, Poland, West Germany | 50.25 | 6.00 | 64.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37], Bear Trap[47], Puppet Governments[67], The Iron Lady[86]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Bear Trap INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | The Iron Lady INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Flower Power INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37], Puppet Governments[67], The Iron Lady[86]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | The Iron Lady INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | The Iron Lady INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | The Iron Lady INFLUENCE East Germany, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | The Iron Lady INFLUENCE France, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Flower Power[62], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | Flower Power INFLUENCE East Germany, Italy, West Germany | 38.60 | 6.00 | 48.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Truman Doctrine[19], Special Relationship[37], Puppet Governments[67]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | Special Relationship INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 4 | Puppet Governments INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | Special Relationship INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Colonial Rear Guards[110]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, France, West Germany | 39.20 | 6.00 | 49.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 2 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 3 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, Italy, West Germany | 38.60 | 6.00 | 48.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |
| 5 | Colonial Rear Guards INFLUENCE France, Italy, West Germany | 38.60 | 6.00 | 48.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Truman Doctrine[19], Puppet Governments[67]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 2 | Puppet Governments INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 3 | Puppet Governments INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 4 | Puppet Governments INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |
| 5 | Puppet Governments INFLUENCE Turkey, West Germany | 21.80 | 6.00 | 32.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Captured Nazi Scientist[18]`
- state: `VP 5, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE East Germany, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:72.00 |
| 2 | Captured Nazi Scientist INFLUENCE France, West Germany | 39.05 | 6.00 | 33.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:72.00 |
| 3 | Captured Nazi Scientist INFLUENCE East Germany, France | 38.45 | 6.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:72.00 |
| 4 | Captured Nazi Scientist INFLUENCE Italy, West Germany | 38.45 | 6.00 | 32.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:72.00 |
| 5 | Captured Nazi Scientist INFLUENCE West Germany, Cuba | 38.30 | 6.00 | 32.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Arms Race[42], Missile Envy[52], South African Unrest[56], Muslim Revolution[59], Voice of America[75], Alliance for Progress[79], Our Man in Tehran[84], Chernobyl[97]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], East European Unrest[29], De-Stalinization[33], Nuclear Subs[44], Portuguese Empire Crumbles[55], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Arms Race[42], Missile Envy[52], South African Unrest[56], Voice of America[75], Alliance for Progress[79], Our Man in Tehran[84], Chernobyl[97]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | Arms Race INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | Arms Race INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 4 | Arms Race INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 5 | Arms Race INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], De-Stalinization[33], Nuclear Subs[44], Portuguese Empire Crumbles[55], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 2 | Nuclear Subs INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 3 | Puppet Governments INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 4 | Puppet Governments INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Missile Envy[52], South African Unrest[56], Voice of America[75], Alliance for Progress[79], Our Man in Tehran[84], Chernobyl[97]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Missile Envy INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | South African Unrest INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Missile Envy INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], De-Stalinization[33], Portuguese Empire Crumbles[55], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Puppet Governments INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | Grain Sales to Soviets INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], South African Unrest[56], Voice of America[75], Alliance for Progress[79], Our Man in Tehran[84], Chernobyl[97]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | South African Unrest INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | South African Unrest INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:10.80 |
| 4 | South African Unrest INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | South African Unrest INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], De-Stalinization[33], Portuguese Empire Crumbles[55], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 4 | Nixon Plays the China Card INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Voice of America[75], Alliance for Progress[79], Our Man in Tehran[84], Chernobyl[97]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 2 | Chernobyl INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 3 | Alliance for Progress INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 4 | Alliance for Progress INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |
| 5 | Chernobyl INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], De-Stalinization[33], Portuguese Empire Crumbles[55], Nixon Plays the China Card[72], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 2 | Nixon Plays the China Card INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:13.50 |
| 4 | Nixon Plays the China Card INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 5 | Nixon Plays the China Card INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Chernobyl [97] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Voice of America[75], Our Man in Tehran[84], Chernobyl[97]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Chernobyl INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Chernobyl INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Chernobyl INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Chernobyl INFLUENCE East Germany, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Chernobyl INFLUENCE France, Turkey, West Germany | 33.95 | 6.00 | 48.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Fidel[8], De-Stalinization[33], Portuguese Empire Crumbles[55], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | De-Stalinization INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | De-Stalinization INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Che INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Voice of America[75], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Voice of America INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Fidel[8], Portuguese Empire Crumbles[55], Che[83]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Che INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | Che INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Che INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Che INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Our Man in Tehran[84]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:81.00 |
| 4 | Our Man in Tehran INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Our Man in Tehran INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Fidel[8], Portuguese Empire Crumbles[55]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 2 | Fidel INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:81.00 |
| 5 | Fidel INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:81.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Wargames [103] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Nuclear Subs[44], Allende[57], Our Man in Tehran[84], Aldrich Ames Remix[101], Wargames[103], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Aldrich Ames Remix EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Allende EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Shuttle Diplomacy [74] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Decolonization[30], De-Stalinization[33], Brush War[39], We Will Bury You[53], U2 Incident[63], Shuttle Diplomacy[74], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 3 | De-Stalinization EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | Brush War EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | U2 Incident EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Aldrich Ames Remix [101] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Nuclear Subs[44], Allende[57], Our Man in Tehran[84], Aldrich Ames Remix[101], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | Aldrich Ames Remix INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | Aldrich Ames Remix INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | Aldrich Ames Remix INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 5 | Aldrich Ames Remix INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], De-Stalinization[33], Brush War[39], We Will Bury You[53], U2 Incident[63], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, Italy, West Germany | 46.60 | 6.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:8.57 |
| 2 | We Will Bury You INFLUENCE East Germany, France, West Germany, Cuba | 46.45 | 6.00 | 65.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.57 |
| 3 | We Will Bury You INFLUENCE East Germany, France, West Germany, Iraq | 45.95 | 6.00 | 64.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Iraq:13.55, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:8.57 |
| 4 | We Will Bury You INFLUENCE East Germany, Italy, West Germany, Cuba | 45.85 | 6.00 | 64.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.57 |
| 5 | We Will Bury You INFLUENCE France, Italy, West Germany, Cuba | 45.85 | 6.00 | 64.45 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], Nuclear Subs[44], Allende[57], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, Italy, West Germany | 46.60 | 6.00 | 65.20 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, Turkey, West Germany | 46.10 | 6.00 | 64.70 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, UK, West Germany | 45.80 | 6.00 | 64.40 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:UK:14.90, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE East Germany, Italy, Turkey, West Germany | 45.50 | 6.00 | 64.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE France, Italy, Turkey, West Germany | 45.50 | 6.00 | 64.10 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], De-Stalinization[33], Brush War[39], U2 Incident[63], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | Brush War INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | De-Stalinization INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | De-Stalinization INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Nuclear Subs[44], Allende[57], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Arab-Israeli War INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:12.00 |
| 4 | Arab-Israeli War INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 5 | Arab-Israeli War INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], Brush War[39], U2 Incident[63], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Brush War INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Brush War INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | U2 Incident INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Truman Doctrine[19], Nuclear Subs[44], Allende[57], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 2 | Nuclear Subs INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 5 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], U2 Incident[63], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 2 | U2 Incident INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 3 | U2 Incident INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 4 | U2 Incident INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:15.00 |
| 5 | U2 Incident INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:15.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Truman Doctrine[19], Allende[57], Our Man in Tehran[84], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 4 | Lone Gunman INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 5 | Our Man in Tehran INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Decolonization[30], Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Decolonization INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | Marine Barracks Bombing INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Allende [57] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Truman Doctrine[19], Allende[57], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:60.00 |
| 2 | Lone Gunman INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:60.00 |
| 3 | Allende INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:60.00 |
| 4 | Allende INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:60.00 |
| 5 | Lone Gunman INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Marine Barracks Bombing[91], Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 2 | Marine Barracks Bombing INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 3 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 4 | Ortega Elected in Nicaragua INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:60.00 |
| 5 | Marine Barracks Bombing INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:60.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Truman Doctrine[19], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:90.00 |
| 2 | Lone Gunman INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:90.00 |
| 3 | Lone Gunman INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:90.00 |
| 4 | Lone Gunman INFLUENCE Italy | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70, non_coup_milops_penalty:90.00 |
| 5 | Lone Gunman INFLUENCE Turkey | 21.05 | 6.00 | 15.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, non_coup_milops_penalty:90.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Ortega Elected in Nicaragua [94] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Ortega Elected in Nicaragua[94], Lone Gunman[109]`
- state: `VP 5, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ortega Elected in Nicaragua INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 2 | Ortega Elected in Nicaragua INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 3 | Ortega Elected in Nicaragua INFLUENCE East Germany, France | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 4 | Ortega Elected in Nicaragua INFLUENCE Italy, West Germany | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:90.00 |
| 5 | Ortega Elected in Nicaragua INFLUENCE West Germany, Cuba | 22.15 | 6.00 | 32.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:90.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`
