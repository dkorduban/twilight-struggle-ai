# minimal_hybrid detailed rollout log

- seed: `20260411`
- winner: `US`
- final_vp: `-7`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], Indo-Pakistani War[24], Decolonization[30], Red Scare/Purge[31], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], NATO[21], US/Japan Mutual Defense Pact[27], East European Unrest[29], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Indo-Pakistani War [24] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], Indo-Pakistani War[24], Decolonization[30], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Decolonization COUP Iran | 70.23 | 4.00 | 66.53 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Romanian Abdication COUP Iran | 64.38 | 4.00 | 60.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 64.38 | 4.00 | 60.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | UN Intervention COUP Iran | 64.38 | 4.00 | 60.53 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], US/Japan Mutual Defense Pact[27], East European Unrest[29], De-Stalinization[33]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Turkey, Indonesia, Philippines | 62.65 | 6.00 | 57.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 2 | US/Japan Mutual Defense Pact INFLUENCE North Korea, Indonesia, Philippines | 62.25 | 6.00 | 56.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, Indonesia, Philippines | 61.75 | 6.00 | 56.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE France, Indonesia, Philippines | 61.75 | 6.00 | 56.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.05, access_touch:France, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE Panama, Indonesia, Philippines | 61.40 | 6.00 | 56.00 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Panama:11.20, control_break:Panama, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], Decolonization[30], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Iran | 48.90 | 4.00 | 45.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | Decolonization INFLUENCE Japan, Thailand | 45.30 | 6.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand |
| 3 | Decolonization INFLUENCE West Germany, Thailand | 44.80 | 6.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, access_touch:Thailand |
| 4 | Decolonization INFLUENCE South Korea, Thailand | 44.70 | 6.00 | 39.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand |
| 5 | Decolonization INFLUENCE Thailand, Thailand | 44.38 | 6.00 | 38.67 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], East European Unrest[29], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, North Korea | 39.15 | 6.00 | 33.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 2 | Duck and Cover INFLUENCE France, North Korea | 39.15 | 6.00 | 33.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 3 | East European Unrest INFLUENCE East Germany, North Korea | 39.15 | 6.00 | 33.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 4 | East European Unrest INFLUENCE France, North Korea | 39.15 | 6.00 | 33.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:North Korea:15.55, access_touch:North Korea, non_coup_milops_penalty:1.20 |
| 5 | Duck and Cover INFLUENCE North Korea, Panama | 38.80 | 6.00 | 33.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32], NORAD[38]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, North Korea, Thailand | 48.10 | 6.00 | 62.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | NORAD INFLUENCE Japan, North Korea, Thailand | 45.70 | 6.00 | 60.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 3 | NORAD INFLUENCE East Germany, Japan, Thailand | 45.20 | 6.00 | 59.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 4 | NORAD INFLUENCE West Germany, North Korea, Thailand | 45.20 | 6.00 | 59.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 5 | NORAD INFLUENCE North Korea, South Korea, Thailand | 45.10 | 6.00 | 59.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], East European Unrest[29], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE France, Panama | 38.30 | 6.00 | 32.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.50 |
| 2 | East European Unrest INFLUENCE France, Japan | 38.25 | 6.00 | 32.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Japan:16.15, non_coup_milops_penalty:1.50 |
| 3 | East European Unrest INFLUENCE Japan, Panama | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:1.50 |
| 4 | East European Unrest INFLUENCE France, West Germany | 37.75 | 6.00 | 32.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:West Germany:15.65, non_coup_milops_penalty:1.50 |
| 5 | East European Unrest INFLUENCE France, North Korea | 37.65 | 6.00 | 32.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:North Korea:15.55, non_coup_milops_penalty:1.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Iran | 40.55 | 4.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Captured Nazi Scientist COUP Iran | 40.55 | 4.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | UN Intervention COUP Iran | 40.55 | 4.00 | 36.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, defcon_penalty:3, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Independent Reds INFLUENCE Japan, Thailand | 32.80 | 6.00 | 43.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE West Germany, Thailand | 32.30 | 6.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], De-Stalinization[33]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | Truman Doctrine INFLUENCE Italy | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:2.00 |
| 4 | Truman Doctrine INFLUENCE North Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 5 | Truman Doctrine INFLUENCE South Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Korea:15.55, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Thailand | 32.80 | 6.00 | 43.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Independent Reds INFLUENCE West Germany, Thailand | 32.30 | 6.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Independent Reds INFLUENCE South Korea, Thailand | 32.20 | 6.00 | 42.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Independent Reds INFLUENCE Pakistan, Thailand | 31.60 | 6.00 | 41.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE Israel, Thailand | 31.55 | 6.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], De-Stalinization[33]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Italy, Japan | 17.65 | 6.00 | 32.10 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | De-Stalinization INFLUENCE West Germany, Japan | 17.35 | 6.00 | 31.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization INFLUENCE Japan, North Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | De-Stalinization INFLUENCE Japan, South Korea | 17.25 | 6.00 | 31.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | De-Stalinization INFLUENCE Italy, West Germany | 17.15 | 6.00 | 31.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 23.00 | 6.00 | 17.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, access_touch:West Germany |
| 4 | UN Intervention INFLUENCE West Germany | 23.00 | 6.00 | 17.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, access_touch:West Germany |
| 5 | Captured Nazi Scientist INFLUENCE South Korea | 22.90 | 6.00 | 17.05 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Korea:15.55, access_touch:South Korea |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Nasser [15] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Nasser INFLUENCE West Germany | 9.50 | 6.00 | 15.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Nasser INFLUENCE North Korea | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Nasser INFLUENCE South Korea | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Blockade[10], Korean War[11], COMECON[14], Warsaw Pact Formed[16], De Gaulle Leads France[17], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], Olympic Games[20], Marshall Plan[23], CIA Created[26], Suez Crisis[28], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Blockade[10], Korean War[11], COMECON[14], Warsaw Pact Formed[16], De Gaulle Leads France[17], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, South Korea, Thailand | 60.20 | 6.00 | 54.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, South Korea, Thailand | 60.20 | 6.00 | 54.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, South Korea, Thailand | 60.20 | 6.00 | 54.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 4 | COMECON INFLUENCE West Germany, Pakistan, Thailand | 59.60 | 6.00 | 54.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |
| 5 | Warsaw Pact Formed INFLUENCE West Germany, Pakistan, Thailand | 59.60 | 6.00 | 54.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], Olympic Games[20], CIA Created[26], Suez Crisis[28], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, South Korea | 73.30 | 6.00 | 67.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |
| 2 | Nuclear Test Ban INFLUENCE West Germany, Japan, North Korea, Egypt | 72.95 | 6.00 | 67.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 3 | Nuclear Test Ban INFLUENCE West Germany, Japan, South Korea, Egypt | 72.95 | 6.00 | 67.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:South Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.00 |
| 4 | Nuclear Test Ban INFLUENCE East Germany, West Germany, Japan, North Korea | 72.80 | 6.00 | 67.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 5 | Nuclear Test Ban INFLUENCE East Germany, West Germany, Japan, South Korea | 72.80 | 6.00 | 67.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.05, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Blockade[10], Korean War[11], Warsaw Pact Formed[16], De Gaulle Leads France[17], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE North Korea, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 2 | De Gaulle Leads France INFLUENCE North Korea, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 3 | Warsaw Pact Formed INFLUENCE North Korea, Israel, Thailand | 62.95 | 6.00 | 57.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 4 | De Gaulle Leads France INFLUENCE North Korea, Israel, Thailand | 62.95 | 6.00 | 57.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |
| 5 | Warsaw Pact Formed INFLUENCE Japan, North Korea, Thailand | 62.70 | 6.00 | 57.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], Olympic Games[20], CIA Created[26], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan, North Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, non_coup_milops_penalty:2.40 |
| 2 | Five Year Plan INFLUENCE West Germany, Japan, South Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |
| 3 | Five Year Plan INFLUENCE Japan, North Korea, South Korea | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:2.40 |
| 4 | Five Year Plan INFLUENCE West Germany, Japan, Egypt | 57.55 | 6.00 | 52.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.40 |
| 5 | Five Year Plan INFLUENCE Japan, North Korea, Egypt | 57.45 | 6.00 | 51.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:2.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Blockade[10], Korean War[11], De Gaulle Leads France[17], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE North Korea, Pakistan, Thailand | 66.50 | 6.00 | 60.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | De Gaulle Leads France INFLUENCE India, North Korea, Thailand | 63.60 | 6.00 | 58.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | De Gaulle Leads France INFLUENCE India, North Korea, Pakistan | 63.10 | 6.00 | 57.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:North Korea:15.55, control_break:North Korea, influence:Pakistan:14.95, control_break:Pakistan, non_coup_milops_penalty:3.00 |
| 4 | De Gaulle Leads France INFLUENCE India, Pakistan, Thailand | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 5 | De Gaulle Leads France INFLUENCE North Korea, Israel, Thailand | 62.95 | 6.00 | 57.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Olympic Games[20], CIA Created[26], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, Japan | 37.50 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:3.00 |
| 2 | Olympic Games INFLUENCE Japan, North Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 3 | Olympic Games INFLUENCE Japan, South Korea | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | Olympic Games INFLUENCE Japan, Egypt | 37.05 | 6.00 | 31.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 5 | Olympic Games INFLUENCE East Germany, Japan | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Blockade[10], Korean War[11], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE India, Thailand | 43.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Korean War INFLUENCE India, Thailand | 43.20 | 6.00 | 37.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 3 | Vietnam Revolts INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 4 | Korean War INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 5 | Vietnam Revolts INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], CIA Created[26], Suez Crisis[28], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Suez Crisis INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Suez Crisis INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Suez Crisis INFLUENCE Japan, North Korea, Egypt | 32.45 | 6.00 | 46.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Korean War[11], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 2 | Korean War INFLUENCE North Korea, Israel | 42.65 | 6.00 | 36.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Israel:14.90, access_touch:Israel, non_coup_milops_penalty:12.00 |
| 3 | Korean War INFLUENCE Israel, Thailand | 42.55 | 6.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |
| 4 | Korean War INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:12.00 |
| 5 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], CIA Created[26], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Syria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:12.00 |
| 3 | CIA Created INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:12.00 |
| 4 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | The Cambridge Five INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 27: T2 AR6 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Blockade[10], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Israel | 28.75 | 4.00 | 24.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:2, milops_urgency:2.00, defcon_penalty:3, coup_access_open |
| 2 | Formosan Resolution INFLUENCE Israel, Thailand | 26.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 4 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Formosan Resolution INFLUENCE Italy, Thailand | 26.10 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 28: T2 AR6 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], The Cambridge Five[36]`
- state: `VP 2, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | The Cambridge Five INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Korean War[11], Romanian Abdication[12], De Gaulle Leads France[17], Containment[25], Nuclear Test Ban[34], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], Arab-Israeli War[13], COMECON[14], UN Intervention[32], De-Stalinization[33], NORAD[38]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Korean War[11], Romanian Abdication[12], De Gaulle Leads France[17], Containment[25], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Japan, Israel, Thailand | 58.55 | 6.00 | 53.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | De Gaulle Leads France INFLUENCE Italy, Israel, Thailand | 58.35 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | De Gaulle Leads France INFLUENCE Israel, Philippines, Thailand | 58.35 | 6.00 | 52.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 4 | De Gaulle Leads France INFLUENCE Israel, Saudi Arabia, Thailand | 58.20 | 6.00 | 52.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 5 | De Gaulle Leads France INFLUENCE Italy, Japan, Thailand | 58.10 | 6.00 | 52.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Arab-Israeli War[13], COMECON[14], UN Intervention[32], De-Stalinization[33], NORAD[38]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, non_coup_milops_penalty:3.00 |
| 2 | NORAD INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 3 | NORAD INFLUENCE Japan, North Korea, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, non_coup_milops_penalty:3.00 |
| 4 | NORAD INFLUENCE West Germany, Japan, Egypt | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |
| 5 | NORAD INFLUENCE Japan, North Korea, Egypt | 52.45 | 6.00 | 46.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Korean War[11], Romanian Abdication[12], Containment[25], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 2 | The Cambridge Five INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 3 | Containment INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Containment INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Containment INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Arab-Israeli War[13], COMECON[14], UN Intervention[32], De-Stalinization[33]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Romanian Abdication[12], Containment[25], The Cambridge Five[36], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:4.50 |
| 2 | Containment INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Containment INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | Containment INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | The Cambridge Five INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], COMECON[14], UN Intervention[32], De-Stalinization[33]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | COMECON INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Containment[25], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Containment INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Containment INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Containment INFLUENCE North Korea, Saudi Arabia, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Containment INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], UN Intervention[32], De-Stalinization[33]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | De-Stalinization INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | De-Stalinization INFLUENCE Japan, North Korea, Egypt | 32.45 | 6.00 | 46.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], Romanian Abdication[12], Special Relationship[37]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Philippines | 32.80 | 4.00 | 28.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 2 | Romanian Abdication COUP Philippines | 32.80 | 4.00 | 28.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 3 | Special Relationship INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Blockade COUP Japan | 26.50 | 4.00 | 22.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3, milops_urgency:1.50 |
| 5 | Romanian Abdication COUP Japan | 26.50 | 4.00 | 22.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3, milops_urgency:1.50 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 40: T3 AR5 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13], UN Intervention[32]`
- state: `VP 3, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention COUP Israel | 22.75 | 4.00 | 18.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3 |
| 3 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:18.00 |
| 5 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Romanian Abdication[12], Special Relationship[37]`
- state: `VP 3, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Romanian Abdication INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:18.00 |
| 3 | Special Relationship INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 5 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13]`
- state: `VP 3, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Vietnam Revolts INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Vietnam Revolts INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Arab-Israeli War INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 43: T4 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Korean War[11], Truman Doctrine[19], Containment[25], CIA Created[26], East European Unrest[29], Decolonization[30], De-Stalinization[33]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], UN Intervention[32], Nuclear Test Ban[34], Missile Envy[52], Brezhnev Doctrine[54], ABM Treaty[60], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Korean War[11], Truman Doctrine[19], Containment[25], CIA Created[26], East European Unrest[29], Decolonization[30]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Argentina, Vietnam | 42.00 | 6.00 | 36.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Vietnam:12.10, control_break:Vietnam, access_touch:Vietnam, non_coup_milops_penalty:3.43 |
| 2 | Decolonization INFLUENCE Argentina, Vietnam | 42.00 | 6.00 | 36.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Vietnam:12.10, control_break:Vietnam, access_touch:Vietnam, non_coup_milops_penalty:3.43 |
| 3 | Korean War INFLUENCE Italy, Vietnam | 40.75 | 6.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Vietnam:12.10, control_break:Vietnam, access_touch:Vietnam, non_coup_milops_penalty:3.43 |
| 4 | Korean War INFLUENCE Mexico, Vietnam | 40.75 | 6.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Vietnam:12.10, control_break:Vietnam, access_touch:Vietnam, non_coup_milops_penalty:3.43 |
| 5 | Korean War INFLUENCE Panama, Vietnam | 40.75 | 6.00 | 35.05 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Vietnam:12.10, control_break:Vietnam, access_touch:Vietnam, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], UN Intervention[32], Missile Envy[52], Brezhnev Doctrine[54], ABM Treaty[60], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE West Germany, Mexico, Morocco, South Africa | 71.10 | 6.00 | 65.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | ABM Treaty INFLUENCE Mexico, Algeria, Morocco, South Africa | 70.65 | 6.00 | 65.25 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | ABM Treaty INFLUENCE East Germany, Mexico, Morocco, South Africa | 70.50 | 6.00 | 65.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | ABM Treaty INFLUENCE France, Mexico, Morocco, South Africa | 70.50 | 6.00 | 65.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | ABM Treaty INFLUENCE West Germany, Mexico, Algeria, South Africa | 70.50 | 6.00 | 65.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], CIA Created[26], East European Unrest[29], Decolonization[30]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Argentina, Chile | 45.20 | 6.00 | 39.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, control_break:Argentina, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:4.00 |
| 2 | Decolonization INFLUENCE Italy, Argentina | 43.35 | 6.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE Mexico, Argentina | 43.35 | 6.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:4.00 |
| 4 | Decolonization INFLUENCE Panama, Argentina | 43.35 | 6.00 | 37.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:4.00 |
| 5 | Decolonization INFLUENCE West Germany, Argentina | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], UN Intervention[32], Missile Envy[52], Brezhnev Doctrine[54], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Mexico, South Africa | 63.45 | 6.00 | 57.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Ussuri River Skirmish INFLUENCE West Germany, Mexico, South Africa | 63.45 | 6.00 | 57.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Mexico, South Africa | 63.45 | 6.00 | 57.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Five Year Plan INFLUENCE Mexico, Algeria, South Africa | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Ussuri River Skirmish INFLUENCE Mexico, Algeria, South Africa | 63.00 | 6.00 | 57.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Truman Doctrine[19], Containment[25], CIA Created[26], East European Unrest[29]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Italy, Mexico, Chile | 35.25 | 6.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 2 | Duck and Cover INFLUENCE Italy, Panama, Chile | 35.25 | 6.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 3 | Duck and Cover INFLUENCE Mexico, Panama, Chile | 35.25 | 6.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Containment INFLUENCE Italy, Mexico, Chile | 35.25 | 6.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 5 | Containment INFLUENCE Italy, Panama, Chile | 35.25 | 6.00 | 49.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], UN Intervention[32], Missile Envy[52], Brezhnev Doctrine[54], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE Italy, Mexico, South Africa | 62.25 | 6.00 | 56.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Italy, Mexico, South Africa | 62.25 | 6.00 | 56.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Mexico:14.95, control_break:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | Ussuri River Skirmish INFLUENCE Italy, West Germany, Mexico | 61.60 | 6.00 | 56.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.80 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE Italy, West Germany, Mexico | 61.60 | 6.00 | 56.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:West Germany:16.15, influence:Mexico:14.95, control_break:Mexico, non_coup_milops_penalty:4.80 |
| 5 | Ussuri River Skirmish INFLUENCE Italy, Mexico, Algeria | 61.15 | 6.00 | 55.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Mexico:14.95, control_break:Mexico, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], Containment[25], CIA Created[26], East European Unrest[29]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Panama, Argentina, Chile | 40.00 | 6.00 | 54.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | East European Unrest INFLUENCE Panama, Argentina, Chile | 40.00 | 6.00 | 54.45 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Panama:14.95, access_touch:Panama, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Containment INFLUENCE West Germany, Panama, Chile | 39.95 | 6.00 | 54.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | East European Unrest INFLUENCE West Germany, Panama, Chile | 39.95 | 6.00 | 54.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Panama:14.95, access_touch:Panama, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Containment INFLUENCE West Germany, Argentina, Chile | 39.70 | 6.00 | 54.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, control_break:Chile, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], UN Intervention[32], Missile Envy[52], Brezhnev Doctrine[54], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Panama, South Africa | 58.45 | 6.00 | 52.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE Panama, Algeria, South Africa | 58.00 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Panama:14.95, control_break:Panama, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Panama, South Africa | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, Panama, South Africa | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE Poland, Panama, South Africa | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:Panama:14.95, control_break:Panama, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26], East European Unrest[29]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Argentina, Chile | 34.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | East European Unrest INFLUENCE Argentina, Brazil, Chile | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | East European Unrest INFLUENCE Argentina, Chile, Algeria | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | East European Unrest INFLUENCE UK, Argentina, Chile | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | East European Unrest INFLUENCE West Germany, Chile, Algeria | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `De Gaulle Leads France[17], UN Intervention[32], Missile Envy[52], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Missile Envy INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 3 | Missile Envy INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 4 | Missile Envy INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 5 | Missile Envy INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Truman Doctrine[19], CIA Created[26]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Philippines | 20.05 | 4.00 | 28.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 2 | CIA Created COUP Philippines | 20.05 | 4.00 | 28.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:4, milops_urgency:2.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Mexico | 17.30 | 4.00 | 25.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:2.00, expected_swing:0.5, offside_ops_penalty |
| 4 | Truman Doctrine COUP Panama | 17.30 | 4.00 | 25.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:4, milops_urgency:2.00, expected_swing:0.5, offside_ops_penalty |
| 5 | CIA Created COUP Mexico | 17.30 | 4.00 | 25.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:2.00, expected_swing:0.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 56: T4 AR6 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `De Gaulle Leads France[17], UN Intervention[32], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Brezhnev Doctrine INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | De Gaulle Leads France INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `CIA Created[26]`
- state: `VP 1, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Algeria | 23.55 | 4.00 | 31.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 2 | CIA Created COUP Mexico | 19.30 | 4.00 | 27.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, expected_swing:0.5, offside_ops_penalty |
| 3 | CIA Created COUP Panama | 19.30 | 4.00 | 27.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:3, milops_urgency:3.00, expected_swing:0.5, offside_ops_penalty |
| 4 | CIA Created COUP Japan | 15.75 | 4.00 | 23.90 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3, milops_urgency:3.00, offside_ops_penalty |
| 5 | CIA Created COUP Israel | 15.75 | 4.00 | 23.90 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:3.00, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `UN Intervention[32], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE West Germany, Algeria, South Africa | 37.70 | 6.00 | 52.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, Algeria, South Africa | 37.10 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Brezhnev Doctrine INFLUENCE France, Algeria, South Africa | 37.10 | 6.00 | 51.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Brezhnev Doctrine INFLUENCE Poland, Algeria, South Africa | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Brezhnev Doctrine INFLUENCE Cuba, Algeria, South Africa | 36.60 | 6.00 | 51.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 59: T5 AR0 USSR

- chosen: `Arms Race [42] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], The Cambridge Five[36], Arms Race[42], U2 Incident[63], Camp David Accords[66]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Nuclear Test Ban[34], We Will Bury You[53], Cultural Revolution[61], Nixon Plays the China Card[72], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Nixon Plays the China Card EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | We Will Bury You EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], The Cambridge Five[36], U2 Incident[63], Camp David Accords[66]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE West Germany, Argentina, Chile | 54.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:4.29 |
| 2 | U2 Incident INFLUENCE Argentina, Brazil, Chile | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:4.29 |
| 3 | U2 Incident INFLUENCE Argentina, Chile, Algeria | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.29 |
| 4 | U2 Incident INFLUENCE UK, Argentina, Chile | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:4.29 |
| 5 | U2 Incident INFLUENCE West Germany, Chile, Algeria | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], We Will Bury You[53], Cultural Revolution[61], Nixon Plays the China Card[72], Alliance for Progress[79], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 2 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 3 | Alliance for Progress INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 4 | Alliance for Progress INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |
| 5 | Alliance for Progress INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], The Cambridge Five[36], Camp David Accords[66]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE East Germany, Chile | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, non_coup_milops_penalty:5.00 |
| 2 | Arab-Israeli War INFLUENCE East Germany, Chile | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, non_coup_milops_penalty:5.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, Chile | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, non_coup_milops_penalty:5.00 |
| 4 | Vietnam Revolts INFLUENCE East Germany, Argentina | 42.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Argentina:16.20, non_coup_milops_penalty:5.00 |
| 5 | Arab-Israeli War INFLUENCE East Germany, Argentina | 42.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Argentina:16.20, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], We Will Bury You[53], Cultural Revolution[61], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE East Germany, France, West Germany, South Africa | 45.45 | 6.00 | 64.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 2 | We Will Bury You INFLUENCE East Germany, Poland, West Germany, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 3 | We Will Bury You INFLUENCE East Germany, West Germany, Cuba, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 4 | We Will Bury You INFLUENCE France, Poland, West Germany, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.00 |
| 5 | We Will Bury You INFLUENCE France, West Germany, Cuba, South Africa | 44.95 | 6.00 | 63.55 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Captured Nazi Scientist[18], The Cambridge Five[36], Camp David Accords[66]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, Chile | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 2 | The Cambridge Five INFLUENCE East Germany, Chile | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 3 | Arab-Israeli War INFLUENCE East Germany, Argentina | 42.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Argentina:16.20, non_coup_milops_penalty:6.00 |
| 4 | The Cambridge Five INFLUENCE East Germany, Argentina | 42.45 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:Argentina:16.20, non_coup_milops_penalty:6.00 |
| 5 | Arab-Israeli War INFLUENCE East Germany, West Germany | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, control_break:East Germany, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Cultural Revolution[61], Nixon Plays the China Card[72], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE France, South Africa | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Our Man in Tehran INFLUENCE France, South Africa | 43.05 | 6.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | Nixon Plays the China Card INFLUENCE France, West Germany | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 5 | Nixon Plays the China Card INFLUENCE East Germany, France | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `The Cambridge Five [36] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Duck and Cover[4], Nasser[15], Captured Nazi Scientist[18], The Cambridge Five[36], Camp David Accords[66]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five COUP Algeria | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:5, milops_urgency:1.25, coup_access_open, expected_swing:1.5 |
| 2 | The Cambridge Five INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:7.50 |
| 3 | The Cambridge Five INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:7.50 |
| 4 | The Cambridge Five INFLUENCE Brazil, Chile | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:7.50 |
| 5 | The Cambridge Five INFLUENCE Chile, Algeria | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 68: T5 AR4 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Cultural Revolution[61], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE Algeria, South Africa | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:7.50 |
| 2 | Our Man in Tehran INFLUENCE West Germany, Algeria | 41.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:7.50 |
| 3 | Our Man in Tehran INFLUENCE East Germany, Algeria | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:7.50 |
| 4 | Our Man in Tehran INFLUENCE France, Algeria | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:7.50 |
| 5 | Our Man in Tehran INFLUENCE Poland, Algeria | 39.95 | 6.00 | 34.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:7.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Captured Nazi Scientist[18], Camp David Accords[66]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Argentina, Chile | 34.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Duck and Cover INFLUENCE Argentina, Brazil, Chile | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Duck and Cover INFLUENCE Argentina, Chile, Algeria | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Duck and Cover INFLUENCE UK, Argentina, Chile | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Duck and Cover INFLUENCE West Germany, Chile, Algeria | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], De Gaulle Leads France[17], Cultural Revolution[61]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 2 | De Gaulle Leads France INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 3 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 4 | Cultural Revolution INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |
| 5 | De Gaulle Leads France INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Captured Nazi Scientist[18], Camp David Accords[66]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Algeria | 32.55 | 4.00 | 28.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Algeria | 32.55 | 4.00 | 28.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 3 | Nasser COUP Mexico | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, expected_swing:0.5 |
| 4 | Nasser COUP Panama | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:3, milops_urgency:1.50, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Mexico | 28.30 | 4.00 | 24.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Cultural Revolution[61]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 2 | Cultural Revolution INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 3 | Cultural Revolution INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 4 | Cultural Revolution INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |
| 5 | Cultural Revolution INFLUENCE East Germany, France, South Africa | 33.45 | 6.00 | 47.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:30.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Camp David Accords[66]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Algeria | 33.05 | 4.00 | 29.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Mexico | 28.80 | 4.00 | 24.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Panama | 28.80 | 4.00 | 24.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Israel | 25.25 | 4.00 | 21.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3 |
| 5 | Camp David Accords COUP Algeria | 23.90 | 4.00 | 36.20 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12]`
- state: `VP 0, DEFCON 2, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 2 | Vietnam Revolts INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 3 | Vietnam Revolts INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 4 | Vietnam Revolts INFLUENCE Poland, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:45.00 |
| 5 | Vietnam Revolts INFLUENCE Cuba, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:45.00 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], Warsaw Pact Formed[16], Red Scare/Purge[31], NORAD[38], South African Unrest[56], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], NORAD[38], Nuclear Subs[44], Summit[48], Junta[50], Willy Brandt[58], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], COMECON[14], Warsaw Pact Formed[16], NORAD[38], South African Unrest[56], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Argentina, Chile | 54.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:5.14 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, Argentina, Chile | 54.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:5.14 |
| 3 | COMECON INFLUENCE Argentina, Brazil, Chile | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:5.14 |
| 4 | COMECON INFLUENCE Argentina, Chile, Algeria | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.14 |
| 5 | Warsaw Pact Formed INFLUENCE Argentina, Brazil, Chile | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Nuclear Subs[44], Summit[48], Junta[50], Willy Brandt[58], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 2 | Summit COUP Mexico | 38.21 | 4.00 | 34.66 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:2.5 |
| 3 | Summit COUP Panama | 38.21 | 4.00 | 34.66 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:0.86, defcon_penalty:3, expected_swing:2.5 |
| 4 | Summit INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |
| 5 | Summit INFLUENCE France, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:5.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Warsaw Pact Formed[16], NORAD[38], South African Unrest[56], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE West Germany, Argentina, Chile | 54.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 2 | Warsaw Pact Formed INFLUENCE Argentina, Brazil, Chile | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 3 | Warsaw Pact Formed INFLUENCE Argentina, Chile, Algeria | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:6.00 |
| 4 | Warsaw Pact Formed INFLUENCE UK, Argentina, Chile | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 5 | Warsaw Pact Formed INFLUENCE West Germany, Chile, Algeria | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Nuclear Subs[44], Junta[50], Willy Brandt[58], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Mexico | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 2 | Nuclear Subs COUP Panama | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 3 | Junta COUP Mexico | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 4 | Junta COUP Panama | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |
| 5 | Lonely Hearts Club Band COUP Mexico | 31.65 | 4.00 | 27.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6, milops_urgency:1.00, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 81: T6 AR3 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], NORAD[38], South African Unrest[56], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Mexico, Chile | 38.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, non_coup_milops_penalty:7.20 |
| 2 | South African Unrest INFLUENCE Mexico, Chile | 38.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Chile:16.80, non_coup_milops_penalty:7.20 |
| 3 | Korean War INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:7.20 |
| 4 | South African Unrest INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:7.20 |
| 5 | Korean War INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Junta[50], Willy Brandt[58], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Lonely Hearts Club Band INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | Junta INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 4 | Lonely Hearts Club Band INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:4.80 |
| 5 | Junta INFLUENCE East Germany | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `NORAD[38], South African Unrest[56], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:9.00 |
| 2 | South African Unrest INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:9.00 |
| 3 | South African Unrest INFLUENCE Brazil, Chile | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:9.00 |
| 4 | South African Unrest INFLUENCE Chile, Algeria | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:9.00 |
| 5 | South African Unrest INFLUENCE UK, Chile | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Chile:16.80, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Willy Brandt[58], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | Lonely Hearts Club Band INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:6.00 |
| 3 | Lonely Hearts Club Band COUP Colombia | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | Lonely Hearts Club Band COUP Saharan States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | Lonely Hearts Club Band COUP SE African States | 21.30 | 4.00 | 17.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `NORAD[38], Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Argentina, Chile | 34.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | NORAD INFLUENCE Argentina, Brazil, Chile | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | NORAD INFLUENCE Argentina, Chile, Algeria | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | NORAD INFLUENCE UK, Argentina, Chile | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | NORAD INFLUENCE West Germany, Chile, Algeria | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], COMECON[14], Willy Brandt[58]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, South Africa | 18.50 | 6.00 | 32.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | COMECON INFLUENCE East Germany, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | COMECON INFLUENCE France, South Africa | 17.90 | 6.00 | 32.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | COMECON INFLUENCE Poland, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | COMECON INFLUENCE Cuba, South Africa | 17.40 | 6.00 | 31.85 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Puppet Governments[67], John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | John Paul II Elected Pope INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | Voice of America INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Puppet Governments INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | John Paul II Elected Pope INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Willy Brandt[58]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Romanian Abdication INFLUENCE South Africa | 10.65 | 6.00 | 16.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | Blockade INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Romanian Abdication INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Blockade INFLUENCE East Germany | 9.40 | 6.00 | 15.55 | 0.00 | -12.00 | -0.15 | 0.00 | influence:East Germany:15.55, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `John Paul II Elected Pope[69], Voice of America[75]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 2 | Voice of America INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 3 | John Paul II Elected Pope INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Voice of America INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | John Paul II Elected Pope INFLUENCE Brazil, Chile | 22.20 | 6.00 | 32.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Willy Brandt[58]`
- state: `VP 2, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Costa Rica | 13.40 | 4.00 | 21.55 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Costa Rica, milops_need:4, milops_urgency:4.00, coup_access_open, offside_ops_penalty |
| 2 | Willy Brandt COUP Colombia | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Willy Brandt COUP Saharan States | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Willy Brandt COUP SE African States | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Zimbabwe | 11.30 | 4.00 | 23.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:4, milops_urgency:4.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -2, DEFCON +1, MilOps U+0/A-2`

## Step 91: T7 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Socialist Governments[7], Containment[25], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], SALT Negotiations[46], Portuguese Empire Crumbles[55], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Colonial Rear Guards EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Latin American Death Squads [70] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], The Cambridge Five[36], Brush War[39], Kitchen Debates[51], Latin American Death Squads[70], Liberation Theology[76], One Small Step[81]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Kitchen Debates EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Brush War EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Containment[25], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], SALT Negotiations[46], Portuguese Empire Crumbles[55], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE West Germany, Argentina, Chile | 54.70 | 6.00 | 49.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 2 | SALT Negotiations INFLUENCE Argentina, Brazil, Chile | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 3 | SALT Negotiations INFLUENCE Argentina, Chile, Algeria | 54.25 | 6.00 | 48.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:6.00 |
| 4 | SALT Negotiations INFLUENCE UK, Argentina, Chile | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:6.00 |
| 5 | SALT Negotiations INFLUENCE West Germany, Chile, Algeria | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], The Cambridge Five[36], Brush War[39], Kitchen Debates[51], Liberation Theology[76], One Small Step[81]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 2 | One Small Step INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 3 | One Small Step INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 4 | One Small Step INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |
| 5 | One Small Step INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Containment[25], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], Portuguese Empire Crumbles[55], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 2 | Colonial Rear Guards INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 4 | Colonial Rear Guards INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:7.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE Brazil, Chile | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Blockade[10], The Cambridge Five[36], Brush War[39], Kitchen Debates[51], Liberation Theology[76]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Socialist Governments INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Brush War INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Brush War INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Socialist Governments INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Containment[25], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], Colonial Rear Guards[110], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE Argentina, Chile | 38.70 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, non_coup_milops_penalty:8.40 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, Chile | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, non_coup_milops_penalty:8.40 |
| 3 | Colonial Rear Guards INFLUENCE Brazil, Chile | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, non_coup_milops_penalty:8.40 |
| 4 | Colonial Rear Guards INFLUENCE Chile, Algeria | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:8.40 |
| 5 | Colonial Rear Guards INFLUENCE UK, Chile | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Chile:16.80, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Fidel[8], Blockade[10], The Cambridge Five[36], Brush War[39], Kitchen Debates[51], Liberation Theology[76]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 2 | Brush War INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 3 | Brush War INFLUENCE Poland, West Germany, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 4 | Brush War INFLUENCE West Germany, Cuba, South Africa | 33.55 | 6.00 | 48.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |
| 5 | Brush War INFLUENCE East Germany, France, South Africa | 33.45 | 6.00 | 47.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Containment[25], UN Intervention[32], Formosan Resolution[35], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Argentina, Chile | 34.70 | 6.00 | 49.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 2 | Containment INFLUENCE Argentina, Brazil, Chile | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 3 | Containment INFLUENCE Argentina, Chile, Algeria | 34.25 | 6.00 | 48.70 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 4 | Containment INFLUENCE UK, Argentina, Chile | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 5 | Containment INFLUENCE West Germany, Chile, Algeria | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Kitchen Debates [51] as COUP`
- flags: `milops_shortfall:7`
- hand: `Fidel[8], Blockade[10], The Cambridge Five[36], Kitchen Debates[51], Liberation Theology[76]`
- state: `VP 0, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Kitchen Debates COUP Mexico | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:1.75, defcon_penalty:3, expected_swing:0.5 |
| 2 | Kitchen Debates COUP Panama | 26.30 | 4.00 | 22.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:7, milops_urgency:1.75, defcon_penalty:3, expected_swing:0.5 |
| 3 | Kitchen Debates COUP Israel | 22.75 | 4.00 | 18.90 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:7, milops_urgency:1.75, defcon_penalty:3 |
| 4 | Fidel INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 5 | The Cambridge Five INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 101: T7 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `UN Intervention[32], Formosan Resolution[35], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Special Relationship INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | UN Intervention INFLUENCE Chile | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:14.00 |
| 4 | Formosan Resolution INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Special Relationship INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Fidel[8], Blockade[10], The Cambridge Five[36], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Liberation Theology INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Fidel INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Fidel INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `UN Intervention[32], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Argentina, Chile | 22.70 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Argentina:16.20, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | UN Intervention INFLUENCE Chile | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:42.00 |
| 3 | Special Relationship INFLUENCE West Germany, Chile | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Special Relationship INFLUENCE Brazil, Chile | 22.20 | 6.00 | 32.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Brazil:14.20, access_touch:Brazil, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Special Relationship INFLUENCE Chile, Algeria | 22.20 | 6.00 | 32.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Chile:16.80, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], The Cambridge Five[36], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | Liberation Theology INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | The Cambridge Five INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | The Cambridge Five INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Liberation Theology INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `UN Intervention[32], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 2, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Colombia | 26.45 | 4.00 | 22.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | UN Intervention COUP El Salvador | 25.20 | 4.00 | 21.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | UN Intervention COUP Guatemala | 25.20 | 4.00 | 21.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Nicaragua | 25.20 | 4.00 | 21.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nicaragua, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention INFLUENCE Chile | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Chile:16.80, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 106: T7 AR7 US

- chosen: `Liberation Theology [76] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Liberation Theology[76]`
- state: `VP 0, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology COUP Colombia | 35.30 | 4.00 | 47.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Blockade COUP Colombia | 32.45 | 4.00 | 40.60 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Liberation Theology INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | Liberation Theology INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | Liberation Theology INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-1`

## Step 107: T8 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Suez Crisis[28], Decolonization[30], Brush War[39], Allende[57], Sadat Expels Soviets[73], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Duck and Cover[4], COMECON[14], De Gaulle Leads France[17], Nuclear Subs[44], Brezhnev Doctrine[54], U2 Incident[63], OPEC[64], One Small Step[81], Iran-Iraq War[105]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Brush War[39], Allende[57], Sadat Expels Soviets[73], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, UK, West Germany | 55.15 | 6.00 | 49.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:UK:14.90, access_touch:UK, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 2 | Brush War INFLUENCE France, UK, West Germany | 55.15 | 6.00 | 49.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:UK:14.90, access_touch:UK, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, UK, West Germany | 55.15 | 6.00 | 49.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:UK:14.90, access_touch:UK, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 4 | Ussuri River Skirmish INFLUENCE France, UK, West Germany | 55.15 | 6.00 | 49.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:UK:14.90, access_touch:UK, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Brush War INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Nuclear Subs [44] as COUP`
- flags: `milops_shortfall:8`
- hand: `COMECON[14], De Gaulle Leads France[17], Nuclear Subs[44], Brezhnev Doctrine[54], U2 Incident[63], OPEC[64], One Small Step[81], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Colombia | 41.09 | 4.00 | 37.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Colombia | 41.09 | 4.00 | 37.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 3 | Iran-Iraq War COUP Colombia | 41.09 | 4.00 | 37.39 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.14, coup_access_open, expected_swing:3.5 |
| 4 | Nuclear Subs INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |
| 5 | Nuclear Subs INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 111: T8 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Allende[57], Sadat Expels Soviets[73], Ussuri River Skirmish[77], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 3 | Ussuri River Skirmish INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.00 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.00 |
| 5 | Ussuri River Skirmish INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `COMECON[14], De Gaulle Leads France[17], Brezhnev Doctrine[54], U2 Incident[63], OPEC[64], One Small Step[81], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:6.00 |
| 2 | Iran-Iraq War INFLUENCE France, West Germany | 43.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:West Germany:16.90, non_coup_milops_penalty:6.00 |
| 3 | One Small Step INFLUENCE East Germany, France | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, non_coup_milops_penalty:6.00 |
| 4 | Iran-Iraq War INFLUENCE East Germany, France | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, non_coup_milops_penalty:6.00 |
| 5 | One Small Step INFLUENCE France, Poland | 42.80 | 6.00 | 37.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, control_break:France, influence:Poland:14.30, access_touch:Poland, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Captured Nazi Scientist[18], Decolonization[30], Allende[57], Sadat Expels Soviets[73], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Colombia | 42.00 | 4.00 | 38.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5 |
| 2 | Decolonization INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 3 | Decolonization INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |
| 4 | Decolonization INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:9.60 |
| 5 | Decolonization INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 114: T8 AR3 US

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `COMECON[14], De Gaulle Leads France[17], Brezhnev Doctrine[54], U2 Incident[63], OPEC[64], Iran-Iraq War[105]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.20 |
| 2 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.20 |
| 3 | Iran-Iraq War INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:7.20 |
| 4 | Iran-Iraq War INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:7.20 |
| 5 | Iran-Iraq War INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:7.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Allende[57], Sadat Expels Soviets[73], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Sadat Expels Soviets INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `COMECON[14], De Gaulle Leads France[17], Brezhnev Doctrine[54], U2 Incident[63], OPEC[64]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | U2 Incident INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | OPEC INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Allende[57], Ask Not What Your Country Can Do For You[78], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE France, Italy, West Germany | 34.45 | 6.00 | 48.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE France, West Germany, Cuba | 34.30 | 6.00 | 48.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `De Gaulle Leads France[17], Brezhnev Doctrine[54], U2 Incident[63], OPEC[64]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 3 | U2 Incident INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | OPEC INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, control_break:France, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | De Gaulle Leads France INFLUENCE France, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, control_break:France, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Allende[57], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:36.00 |
| 2 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:36.00 |
| 3 | Lone Gunman INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:36.00 |
| 4 | Captured Nazi Scientist INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30, non_coup_milops_penalty:36.00 |
| 5 | Captured Nazi Scientist INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Brezhnev Doctrine[54], U2 Incident[63], OPEC[64]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 2 | U2 Incident INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 3 | OPEC INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:36.00 |
| 5 | Brezhnev Doctrine INFLUENCE France, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:36.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Allende [57] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Allende[57], Lone Gunman[109]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende COUP Colombia | 23.95 | 4.00 | 20.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Lone Gunman COUP Colombia | 23.95 | 4.00 | 20.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Allende COUP El Salvador | 23.70 | 4.00 | 19.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Allende COUP Guatemala | 23.70 | 4.00 | 19.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Allende COUP Nicaragua | 23.70 | 4.00 | 19.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Nicaragua, milops_need:6, milops_urgency:6.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `U2 Incident [63] as COUP`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `U2 Incident[63], OPEC[64]`
- state: `VP -3, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident COUP Colombia | 37.65 | 4.00 | 54.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | OPEC COUP Colombia | 37.65 | 4.00 | 54.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:6, milops_urgency:6.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | U2 Incident INFLUENCE East Germany, West Germany, Morocco | 37.55 | 6.00 | 52.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 4 | U2 Incident INFLUENCE France, West Germany, Morocco | 37.55 | 6.00 | 52.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:54.00 |
| 5 | OPEC INFLUENCE East Germany, West Germany, Morocco | 37.55 | 6.00 | 52.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, offside_ops_penalty, non_coup_milops_penalty:54.00 |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 123: T9 AR0 USSR

- chosen: `Pershing II Deployed [102] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Arab-Israeli War[13], Independent Reds[22], CIA Created[26], Special Relationship[37], Junta[50], Missile Envy[52], Our Man in Tehran[84], Pershing II Deployed[102]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Pershing II Deployed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Independent Reds EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Vietnam Revolts[9], US/Japan Mutual Defense Pact[27], Formosan Resolution[35], SALT Negotiations[46], Willy Brandt[58], ABM Treaty[60], Shuttle Diplomacy[74], Iranian Hostage Crisis[85]`
- state: `VP -3, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +1, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Arab-Israeli War[13], Independent Reds[22], CIA Created[26], Special Relationship[37], Junta[50], Missile Envy[52], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Colombia | 41.37 | 4.00 | 37.67 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 2 | Junta COUP Colombia | 41.37 | 4.00 | 37.67 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 3 | Missile Envy COUP Colombia | 41.37 | 4.00 | 37.67 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:1.29, coup_access_open, expected_swing:3.5 |
| 4 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |
| 5 | Arab-Israeli War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 126: T9 AR1 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Formosan Resolution[35], SALT Negotiations[46], Willy Brandt[58], ABM Treaty[60], Shuttle Diplomacy[74], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE East Germany, France, West Germany, Morocco | 73.70 | 6.00 | 68.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, non_coup_milops_penalty:7.71 |
| 2 | ABM Treaty INFLUENCE East Germany, Poland, West Germany, Morocco | 73.20 | 6.00 | 67.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, non_coup_milops_penalty:7.71 |
| 3 | ABM Treaty INFLUENCE France, Poland, West Germany, Morocco | 73.20 | 6.00 | 67.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, non_coup_milops_penalty:7.71 |
| 4 | ABM Treaty INFLUENCE East Germany, Italy, West Germany, Morocco | 73.10 | 6.00 | 67.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, non_coup_milops_penalty:7.71 |
| 5 | ABM Treaty INFLUENCE France, Italy, West Germany, Morocco | 73.10 | 6.00 | 67.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Morocco:13.80, control_break:Morocco, non_coup_milops_penalty:7.71 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Independent Reds[22], CIA Created[26], Special Relationship[37], Junta[50], Missile Envy[52], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.00 |
| 2 | Junta INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.00 |
| 3 | Missile Envy INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.00 |
| 4 | Missile Envy INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:7.00 |
| 5 | Junta INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Formosan Resolution[35], SALT Negotiations[46], Willy Brandt[58], Shuttle Diplomacy[74], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 3 | SALT Negotiations INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 4 | SALT Negotiations INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:9.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Independent Reds[22], CIA Created[26], Special Relationship[37], Missile Envy[52], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.40 |
| 2 | Missile Envy INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.40 |
| 3 | Missile Envy INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:8.40 |
| 4 | Missile Envy INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.40 |
| 5 | Missile Envy INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:8.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Formosan Resolution[35], Willy Brandt[58], Shuttle Diplomacy[74], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 3 | Shuttle Diplomacy INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |
| 5 | Shuttle Diplomacy INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], Special Relationship[37], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 2 | Independent Reds INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 4 | Special Relationship INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.50 |
| 5 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Formosan Resolution [35] as COUP`
- flags: `milops_shortfall:9`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Formosan Resolution[35], Willy Brandt[58], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution COUP Colombia | 43.30 | 4.00 | 39.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:9, milops_urgency:2.25, coup_access_open, expected_swing:3.5 |
| 2 | Formosan Resolution INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 3 | Formosan Resolution INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 4 | Formosan Resolution INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, non_coup_milops_penalty:13.50 |
| 5 | Formosan Resolution INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:13.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 133: T9 AR5 USSR

- chosen: `Special Relationship [37] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Special Relationship[37], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Colombia | 27.47 | 4.00 | 39.77 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Our Man in Tehran COUP Colombia | 27.47 | 4.00 | 39.77 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | CIA Created COUP Colombia | 24.62 | 4.00 | 32.77 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:2.33, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Special Relationship INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Willy Brandt[58], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Socialist Governments INFLUENCE East Germany, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 4 | Socialist Governments INFLUENCE France, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Iranian Hostage Crisis INFLUENCE East Germany, Poland, West Germany | 34.55 | 6.00 | 49.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26], Our Man in Tehran[84]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Colombia | 29.80 | 4.00 | 42.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | CIA Created COUP Colombia | 26.95 | 4.00 | 35.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Our Man in Tehran COUP Algeria | 23.90 | 4.00 | 36.20 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:3.50, defcon_penalty:3, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Our Man in Tehran INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Our Man in Tehran INFLUENCE France, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Willy Brandt[58], Iranian Hostage Crisis[85]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 40.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, Poland, West Germany | 39.55 | 6.00 | 54.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, Italy, West Germany | 39.45 | 6.00 | 53.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:Italy:15.70, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Iranian Hostage Crisis INFLUENCE East Germany, West Germany, Cuba | 39.30 | 6.00 | 53.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Iranian Hostage Crisis INFLUENCE East Germany, France, Poland | 38.95 | 6.00 | 53.40 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, control_break:East Germany, influence:France:16.30, influence:Poland:14.30, access_touch:Poland, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `CIA Created [26] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `CIA Created[26]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Colombia | 33.95 | 4.00 | 42.10 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | CIA Created COUP Algeria | 28.05 | 4.00 | 36.20 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 3 | CIA Created COUP Mexico | 23.30 | 4.00 | 31.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 4 | CIA Created COUP Panama | 23.30 | 4.00 | 31.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Panama, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 5 | CIA Created COUP El Salvador | 13.70 | 4.00 | 21.85 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:El Salvador, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:2.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Willy Brandt[58]`
- state: `VP -2, DEFCON 3, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP Colombia | 36.80 | 4.00 | 49.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Willy Brandt COUP Colombia | 36.80 | 4.00 | 49.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Mexico | 26.15 | 4.00 | 38.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Panama | 26.15 | 4.00 | 38.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |
| 5 | Willy Brandt COUP Mexico | 26.15 | 4.00 | 38.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7, milops_urgency:7.00, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 139: T10 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Fidel[8], Arab-Israeli War[13], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], Red Scare/Purge[31], Portuguese Empire Crumbles[55], One Small Step[81], The Reformer[90]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Reformer EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Soviets Shoot Down KAL 007 [92] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Truman Doctrine[19], Quagmire[45], South African Unrest[56], Lonely Hearts Club Band[65], Latin American Death Squads[70], Che[83], Our Man in Tehran[84], Soviets Shoot Down KAL 007[92], Yuri and Samantha[106]`
- state: `VP -2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Soviets Shoot Down KAL 007 EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Fidel[8], Arab-Israeli War[13], De Gaulle Leads France[17], Indo-Pakistani War[24], Containment[25], Portuguese Empire Crumbles[55], One Small Step[81], The Reformer[90]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 2 | The Reformer INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 4 | De Gaulle Leads France INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |
| 5 | The Reformer INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:8.57 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Lonely Hearts Club Band [65] as COUP`
- flags: `holds_china, milops_shortfall:10`
- hand: `Truman Doctrine[19], Quagmire[45], South African Unrest[56], Lonely Hearts Club Band[65], Latin American Death Squads[70], Che[83], Our Man in Tehran[84], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 3, MilOps U0/A0, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band COUP Colombia | 41.66 | 4.00 | 37.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 2 | Latin American Death Squads COUP Colombia | 41.66 | 4.00 | 37.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 3 | Our Man in Tehran COUP Colombia | 41.66 | 4.00 | 37.96 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:3.5 |
| 4 | Truman Doctrine COUP Colombia | 34.81 | 4.00 | 30.96 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:1.43, coup_access_open, expected_swing:2.5 |
| 5 | Lonely Hearts Club Band COUP Mexico | 31.01 | 4.00 | 27.31 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:10, milops_urgency:1.43, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+2`

## Step 143: T10 AR2 USSR

- chosen: `The Reformer [90] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Fidel[8], Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Portuguese Empire Crumbles[55], One Small Step[81], The Reformer[90]`
- state: `VP -4, DEFCON 3, MilOps U0/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 2 | The Reformer INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 3 | The Reformer INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, non_coup_milops_penalty:10.00 |
| 4 | The Reformer INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.00 |
| 5 | The Reformer INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba, non_coup_milops_penalty:10.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Latin American Death Squads [70] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Truman Doctrine[19], Quagmire[45], South African Unrest[56], Latin American Death Squads[70], Che[83], Our Man in Tehran[84], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 3, MilOps U0/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads COUP Mexico | 30.82 | 4.00 | 27.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 2 | Latin American Death Squads COUP Panama | 30.82 | 4.00 | 27.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 3 | Our Man in Tehran COUP Mexico | 30.82 | 4.00 | 27.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 4 | Our Man in Tehran COUP Panama | 30.82 | 4.00 | 27.12 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Panama, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:1.5 |
| 5 | Truman Doctrine COUP Mexico | 23.97 | 4.00 | 20.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:8, milops_urgency:1.33, defcon_penalty:3, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:10`
- hand: `Fidel[8], Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Portuguese Empire Crumbles[55], One Small Step[81]`
- state: `VP -4, DEFCON 2, MilOps U0/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Arab-Israeli War COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Indo-Pakistani War COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 4 | Portuguese Empire Crumbles COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 5 | One Small Step COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:10, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+2/A+0`

## Step 146: T10 AR3 US

- chosen: `Our Man in Tehran [84] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Truman Doctrine[19], Quagmire[45], South African Unrest[56], Che[83], Our Man in Tehran[84], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran COUP Colombia | 42.00 | 4.00 | 38.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5 |
| 2 | Truman Doctrine COUP Colombia | 35.15 | 4.00 | 31.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:2.5 |
| 3 | Quagmire COUP Colombia | 28.85 | 4.00 | 45.30 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | Che COUP Colombia | 28.85 | 4.00 | 45.30 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 5 | South African Unrest COUP Colombia | 26.00 | 4.00 | 38.30 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:1.60, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Arab-Israeli War [13] as COUP`
- flags: `milops_shortfall:8`
- hand: `Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Portuguese Empire Crumbles[55], One Small Step[81]`
- state: `VP -4, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 2 | Indo-Pakistani War COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 3 | Portuguese Empire Crumbles COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 4 | One Small Step COUP Colombia | 42.80 | 4.00 | 39.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5 |
| 5 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:8`
- hand: `Truman Doctrine[19], Quagmire[45], South African Unrest[56], Che[83], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Colombia | 35.95 | 4.00 | 32.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:2.5 |
| 2 | Quagmire COUP Colombia | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | Che COUP Colombia | 29.65 | 4.00 | 46.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 4 | South African Unrest COUP Colombia | 26.80 | 4.00 | 39.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Yuri and Samantha COUP Colombia | 26.80 | 4.00 | 39.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Indo-Pakistani War[24], Containment[25], Portuguese Empire Crumbles[55], One Small Step[81]`
- state: `VP -4, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Indo-Pakistani War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Quagmire [45] as COUP`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Quagmire[45], South African Unrest[56], Che[83], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 2, MilOps U2/A2, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire COUP Colombia | 30.98 | 4.00 | 47.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Che COUP Colombia | 30.98 | 4.00 | 47.43 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | South African Unrest COUP Colombia | 28.13 | 4.00 | 40.43 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Yuri and Samantha COUP Colombia | 28.13 | 4.00 | 40.43 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:2.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 5 | Quagmire INFLUENCE East Germany, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 151: T10 AR6 USSR

- chosen: `Portuguese Empire Crumbles [55] as COUP`
- flags: `milops_shortfall:8`
- hand: `Containment[25], Portuguese Empire Crumbles[55], One Small Step[81]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles COUP Colombia | 46.80 | 4.00 | 43.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:3.5 |
| 2 | One Small Step COUP Colombia | 46.80 | 4.00 | 43.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:4.00, coup_access_open, expected_swing:3.5 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:48.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Che [83] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `South African Unrest[56], Che[83], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che COUP Colombia | 32.65 | 4.00 | 49.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | South African Unrest COUP Colombia | 29.80 | 4.00 | 42.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Yuri and Samantha COUP Colombia | 29.80 | 4.00 | 42.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:3.50, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Che INFLUENCE East Germany, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Che INFLUENCE France, West Germany | 18.75 | 6.00 | 33.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `One Small Step [81] as COUP`
- flags: `milops_shortfall:8`
- hand: `Containment[25], One Small Step[81]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step COUP Colombia | 54.80 | 4.00 | 51.10 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:8.00, coup_access_open, expected_swing:3.5 |
| 2 | Containment COUP Colombia | 41.65 | 4.00 | 58.10 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:8, milops_urgency:8.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:72.00 |
| 4 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:72.00 |
| 5 | One Small Step INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, non_coup_milops_penalty:72.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `South African Unrest [56] as COUP`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `South African Unrest[56], Yuri and Samantha[106]`
- state: `VP -4, DEFCON 2, MilOps U2/A3, Space U0/A0, China US (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest COUP Colombia | 36.80 | 4.00 | 49.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Yuri and Samantha COUP Colombia | 36.80 | 4.00 | 49.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:7, milops_urgency:7.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | South African Unrest COUP Guatemala | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Yuri and Samantha COUP Guatemala | 16.55 | 4.00 | 28.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | South African Unrest COUP Saharan States | 16.30 | 4.00 | 28.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:7, milops_urgency:7.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP -3, DEFCON +1, MilOps U-2/A-3`
