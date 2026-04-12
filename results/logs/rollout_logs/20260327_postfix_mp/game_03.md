# minimal_hybrid detailed rollout log

- seed: `20260412`
- winner: `US`
- final_vp: `3`
- end_turn: `5`
- end_reason: `defcon1`

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
| 4 | Korean War COUP Iran | 46.40 | 4.00 | 42.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 5 | Arab-Israeli War COUP Iran | 46.40 | 4.00 | 42.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |

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

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china`
- hand: `Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Iran | 46.40 | 4.00 | 42.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 43.80 | 6.00 | 38.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE West Germany, Thailand | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE South Korea, Thailand | 43.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45 |
| 5 | The Cambridge Five INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Nasser[15], CIA Created[26], Decolonization[30]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:6.00 |
| 2 | CIA Created INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:6.00 |
| 3 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | CIA Created INFLUENCE North Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, non_coup_milops_penalty:6.00 |
| 5 | CIA Created INFLUENCE South Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Korea:15.55, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, Thailand | 40.80 | 6.00 | 55.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | NORAD INFLUENCE Japan, South Korea, Thailand | 40.70 | 6.00 | 55.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 3 | NORAD INFLUENCE West Germany, South Korea, Thailand | 40.20 | 6.00 | 54.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, offside_ops_penalty |
| 4 | NORAD INFLUENCE Japan, Pakistan, Thailand | 40.10 | 6.00 | 54.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 5 | NORAD INFLUENCE Japan, Israel, Thailand | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], Decolonization[30]`
- state: `VP 0, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Decolonization INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Decolonization INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Decolonization INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Decolonization INFLUENCE East Germany, Japan | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +2, DEFCON +1, MilOps U-3/A+0`

## Step 15: T2 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Blockade[10], Romanian Abdication[12], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], Suez Crisis[28], East European Unrest[29]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE France, South Korea, Thailand | 63.10 | 6.00 | 57.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Suez Crisis INFLUENCE France, Pakistan, Thailand | 62.50 | 6.00 | 56.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | Suez Crisis INFLUENCE France, Israel, Thailand | 62.45 | 6.00 | 56.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | Suez Crisis INFLUENCE France, Japan, Thailand | 62.20 | 6.00 | 56.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Suez Crisis INFLUENCE France, Italy, Thailand | 62.00 | 6.00 | 56.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], Olympic Games[20], UN Intervention[32], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE France, Pakistan, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Containment INFLUENCE France, Pakistan, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | East European Unrest INFLUENCE France, Pakistan, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | Five Year Plan INFLUENCE France, Israel, Thailand | 42.45 | 6.00 | 56.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | Containment INFLUENCE France, Israel, Thailand | 42.45 | 6.00 | 56.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.05, control_break:France, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE India, Pakistan, Thailand | 43.00 | 6.00 | 57.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | East European Unrest INFLUENCE India, Pakistan, Thailand | 43.00 | 6.00 | 57.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Containment INFLUENCE Pakistan, Israel, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | East European Unrest INFLUENCE Pakistan, Israel, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Containment INFLUENCE Japan, Pakistan, Thailand | 42.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], COMECON[14], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | COMECON INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | COMECON INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | COMECON INFLUENCE Japan, North Korea, Egypt | 32.45 | 6.00 | 46.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], East European Unrest[29]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE North Korea, Israel, Thailand | 42.95 | 6.00 | 57.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | East European Unrest INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | East European Unrest INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | East European Unrest INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | East European Unrest INFLUENCE North Korea, Saudi Arabia, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:2`
- hand: `Vietnam Revolts[9], Truman Doctrine[19], UN Intervention[32]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Syria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Syria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:12.00 |
| 4 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:12.00 |
| 5 | Truman Doctrine COUP Israel | 21.75 | 4.00 | 17.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 27: T2 AR6 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 2, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 2 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 3 | Blockade COUP Syria | 24.55 | 4.00 | 20.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication COUP Syria | 24.55 | 4.00 | 20.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:0.5 |
| 5 | Blockade COUP Israel | 23.75 | 4.00 | 19.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:1`
- hand: `Vietnam Revolts[9], UN Intervention[32]`
- state: `VP 2, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Iraq | 26.15 | 4.00 | 22.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iraq, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3, coup_access_open |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:9.00 |
| 3 | UN Intervention COUP Israel | 21.75 | 4.00 | 17.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:1, milops_urgency:1.00, defcon_penalty:3 |
| 4 | Vietnam Revolts INFLUENCE Japan, Iraq | 21.65 | 6.00 | 31.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | UN Intervention INFLUENCE Iraq | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:9.00 |

- effects: `VP -1, DEFCON +0, MilOps U+0/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Socialist Governments[7], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], UN Intervention[32], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Blockade[10], Nasser[15], Suez Crisis[28], East European Unrest[29], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Fidel EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], UN Intervention[32], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, Japan, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | De-Stalinization INFLUENCE Japan, Philippines, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | De-Stalinization INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 4 | De-Stalinization INFLUENCE Italy, Philippines, Thailand | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Blockade[10], Nasser[15], Suez Crisis[28], Formosan Resolution[35], The Cambridge Five[36], NORAD[38]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Italy, Japan, Iraq | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:3.00 |
| 2 | NORAD INFLUENCE Italy, West Germany, Japan | 56.80 | 6.00 | 51.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:3.00 |
| 3 | NORAD INFLUENCE Italy, Japan, North Korea | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | NORAD INFLUENCE Italy, Japan, South Korea | 56.70 | 6.00 | 51.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 5 | NORAD INFLUENCE Italy, West Germany, Iraq | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65, influence:Iraq:14.30, access_touch:Iraq, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Iraq, Thailand | 45.45 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 2 | Decolonization INFLUENCE Iraq, Thailand | 45.45 | 6.00 | 39.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 3 | Vietnam Revolts INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 4 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 5 | Vietnam Revolts INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Blockade[10], Nasser[15], Suez Crisis[28], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Saudi Arabia | 37.65 | 6.00 | 31.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |
| 2 | Formosan Resolution INFLUENCE West Germany, Japan | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:3.60 |
| 3 | Formosan Resolution INFLUENCE Japan, North Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.60 |
| 4 | Formosan Resolution INFLUENCE Japan, South Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.60 |
| 5 | Formosan Resolution INFLUENCE West Germany, Saudi Arabia | 37.15 | 6.00 | 31.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], Decolonization[30], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 2 | Decolonization INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 3 | Decolonization INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 4 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 5 | Decolonization INFLUENCE India, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Nasser[15], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Suez Crisis INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | Suez Crisis INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | Suez Crisis INFLUENCE West Germany, Japan, Iran | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Five Year Plan INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Five Year Plan INFLUENCE North Korea, Saudi Arabia, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Five Year Plan INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Five Year Plan INFLUENCE India, North Korea, Thailand | 42.10 | 6.00 | 56.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:India:15.55, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Nasser[15], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | The Cambridge Five INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], CIA Created[26], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saudi Arabia | 27.15 | 4.00 | 23.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open |
| 2 | UN Intervention COUP Saudi Arabia | 27.15 | 4.00 | 23.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 5 | Captured Nazi Scientist COUP Syria | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 40: T3 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Nasser[15], The Cambridge Five[36]`
- state: `VP 1, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | The Cambridge Five INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | The Cambridge Five INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | The Cambridge Five INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | The Cambridge Five INFLUENCE Japan, Iran | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iran:13.70, access_touch:Iran, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP 1, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 3 | UN Intervention INFLUENCE Philippines | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE Saudi Arabia | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, non_coup_milops_penalty:18.00 |
| 5 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Nasser[15]`
- state: `VP 1, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 2 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Blockade INFLUENCE West Germany | 9.50 | 6.00 | 15.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Nasser INFLUENCE West Germany | 9.50 | 6.00 | 15.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Blockade INFLUENCE North Korea | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 43: T4 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Suez Crisis[28], Nuclear Subs[44], Quagmire[45], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], East European Unrest[29], De-Stalinization[33], NORAD[38], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], One Small Step[81], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Suez Crisis[28], Nuclear Subs[44], Quagmire[45], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, Mexico, Morocco | 58.85 | 6.00 | 53.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |
| 2 | Quagmire INFLUENCE East Germany, Mexico, Morocco | 58.85 | 6.00 | 53.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, Mexico, Morocco | 58.85 | 6.00 | 53.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |
| 4 | Suez Crisis INFLUENCE East Germany, West Germany, Mexico | 58.70 | 6.00 | 53.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 5 | Quagmire INFLUENCE East Germany, West Germany, Mexico | 58.70 | 6.00 | 53.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], De-Stalinization[33], NORAD[38], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], One Small Step[81], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | Sadat Expels Soviets INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | NORAD INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | Sadat Expels Soviets INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | NORAD INFLUENCE East Germany, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Nuclear Subs[44], Quagmire[45], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE UK, West Germany, Algeria | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 2 | Brezhnev Doctrine INFLUENCE UK, West Germany, Algeria | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 3 | Quagmire INFLUENCE East Germany, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 4 | Quagmire INFLUENCE France, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], De-Stalinization[33], U2 Incident[63], Grain Sales to Soviets[68], Sadat Expels Soviets[73], One Small Step[81], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE UK, West Germany, South Africa | 62.65 | 6.00 | 57.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Sadat Expels Soviets INFLUENCE UK, Algeria, South Africa | 62.20 | 6.00 | 56.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, UK, South Africa | 62.05 | 6.00 | 56.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Sadat Expels Soviets INFLUENCE France, UK, South Africa | 62.05 | 6.00 | 56.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Sadat Expels Soviets INFLUENCE Poland, UK, South Africa | 61.55 | 6.00 | 56.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Nuclear Subs[44], Brezhnev Doctrine[54], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 2 | Brezhnev Doctrine INFLUENCE France, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 3 | Brezhnev Doctrine INFLUENCE West Germany, Saudi Arabia, Algeria | 56.20 | 6.00 | 50.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 4 | Brezhnev Doctrine INFLUENCE West Germany, Cuba, Algeria | 55.95 | 6.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, France, Algeria | 55.85 | 6.00 | 50.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Independent Reds[22], De-Stalinization[33], U2 Incident[63], Grain Sales to Soviets[68], One Small Step[81], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 4 | Independent Reds INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 5 | Grain Sales to Soviets INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Nuclear Subs[44], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 2 | Vietnam Revolts INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Vietnam Revolts INFLUENCE West Germany, Saudi Arabia | 37.15 | 6.00 | 31.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, non_coup_milops_penalty:6.00 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, non_coup_milops_penalty:6.00 |
| 5 | Vietnam Revolts INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De-Stalinization[33], U2 Incident[63], Grain Sales to Soviets[68], One Small Step[81], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Grain Sales to Soviets INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | One Small Step INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], CIA Created[26], Nuclear Subs[44], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Saudi Arabia | 26.32 | 4.00 | 22.47 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saudi Arabia, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, coup_access_open |
| 2 | Romanian Abdication COUP Mexico | 25.47 | 4.00 | 21.62 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |
| 3 | Romanian Abdication COUP Syria | 22.72 | 4.00 | 18.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 4 | Romanian Abdication INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:8.00 |
| 5 | Romanian Abdication COUP Israel | 21.92 | 4.00 | 18.07 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:4, milops_urgency:1.33, defcon_penalty:3 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 54: T4 AR5 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De-Stalinization[33], U2 Incident[63], One Small Step[81], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | One Small Step INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | One Small Step INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | One Small Step INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | One Small Step INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Nuclear Subs[44], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Nuclear Subs INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Lonely Hearts Club Band INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Nuclear Subs INFLUENCE West Germany, Saudi Arabia | 21.15 | 6.00 | 31.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `De-Stalinization[33], U2 Incident[63], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | U2 Incident INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | De-Stalinization INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE West Germany, Algeria | 25.05 | 6.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, Algeria | 24.45 | 6.00 | 34.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Lonely Hearts Club Band INFLUENCE France, Algeria | 24.45 | 6.00 | 34.75 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Lonely Hearts Club Band INFLUENCE Saudi Arabia, Algeria | 24.20 | 6.00 | 34.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Lonely Hearts Club Band INFLUENCE Cuba, Algeria | 23.95 | 6.00 | 34.25 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `U2 Incident[63], Lone Gunman[109]`
- state: `VP 2, DEFCON 2, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, Morocco, South Africa | 34.80 | 6.00 | 49.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | U2 Incident INFLUENCE East Germany, Morocco, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | U2 Incident INFLUENCE France, Morocco, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | U2 Incident INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 59: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Red Scare/Purge[31], Formosan Resolution[35], Bear Trap[47], Latin American Death Squads[70], Shuttle Diplomacy[74]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Five Year Plan[5], COMECON[14], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 2 | Bear Trap INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 4 | Five Year Plan INFLUENCE East Germany, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:4.29 |
| 5 | Five Year Plan INFLUENCE France, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as COUP`
- flags: `milops_shortfall:5`
- hand: `COMECON[14], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], Ask Not What Your Country Can Do For You[78], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You COUP Iran | 41.18 | 4.00 | 37.63 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Iran, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 3 | Ask Not What Your Country Can Do For You COUP Mexico | 37.93 | 4.00 | 34.38 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:0.71, defcon_penalty:3, expected_swing:2.5 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE France, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+3`

## Step 63: T5 AR2 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35], Bear Trap[47], Shuttle Diplomacy[74]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 3 | Bear Trap INFLUENCE East Germany, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 4 | Bear Trap INFLUENCE France, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Nasser[15], Captured Nazi Scientist[18], CIA Created[26], The Cambridge Five[36], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 2 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 3 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.00 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.00 |
| 5 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35], Shuttle Diplomacy[74]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Shuttle Diplomacy INFLUENCE France, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Shuttle Diplomacy INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Nasser[15], CIA Created[26], The Cambridge Five[36], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.40 |
| 2 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:2.40 |
| 3 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 4 | Panama Canal Returned INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:2.40 |
| 5 | CIA Created INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Blockade[10], Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 2 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:7.50 |
| 3 | Blockade INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:7.50 |
| 4 | Blockade INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:7.50 |
| 5 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `COMECON[14], Nasser[15], The Cambridge Five[36], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:3.00 |
| 2 | Panama Canal Returned INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:3.00 |
| 3 | Panama Canal Returned INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:3.00 |
| 4 | Panama Canal Returned INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:3.00 |
| 5 | Panama Canal Returned INFLUENCE Poland | 20.90 | 6.00 | 15.05 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Poland:13.55, access_touch:Poland, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.00 |
| 2 | Captured Nazi Scientist INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:10.00 |
| 3 | Captured Nazi Scientist INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55, non_coup_milops_penalty:10.00 |
| 4 | Formosan Resolution INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | Formosan Resolution INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `COMECON[14], Nasser[15], The Cambridge Five[36], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | COMECON INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | COMECON INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | COMECON INFLUENCE Poland, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | COMECON INFLUENCE Cuba, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Truman Doctrine[19], Formosan Resolution[35]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 2 | Formosan Resolution INFLUENCE France, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 3 | Formosan Resolution INFLUENCE West Germany, Saudi Arabia | 21.15 | 6.00 | 31.45 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | Formosan Resolution INFLUENCE West Germany, Cuba | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Formosan Resolution INFLUENCE East Germany, France | 20.80 | 6.00 | 31.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Nasser [15] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Nasser[15], The Cambridge Five[36], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | The Cambridge Five COUP Mexico | 10.15 | 4.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:2, expected_swing:1.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Mexico | 10.15 | 4.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:2, milops_urgency:1.00, defcon_penalty:2, expected_swing:1.5, offside_ops_penalty |
| 4 | Nasser INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Nasser INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Truman Doctrine[19]`
- state: `VP 3, DEFCON 2, MilOps U0/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Mexico | 15.30 | 4.00 | 23.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5, milops_urgency:5.00, defcon_penalty:2, expected_swing:0.5, offside_ops_penalty |
| 2 | Truman Doctrine COUP Algeria | 14.55 | 4.00 | 22.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:5.00, defcon_penalty:2, expected_swing:0.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Morocco | 12.15 | 4.00 | 20.30 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:5, milops_urgency:5.00, defcon_penalty:2, offside_ops_penalty |
| 4 | Truman Doctrine COUP Saharan States | 10.45 | 4.00 | 18.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:5.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |
| 5 | Truman Doctrine INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:45.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`
