# minimal_hybrid detailed rollout log

- seed: `20260411`
- winner: `USSR`
- final_vp: `1`
- end_turn: `5`
- end_reason: `europe_control`

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

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Thailand | 32.80 | 6.00 | 43.10 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 2 | Independent Reds INFLUENCE West Germany, Thailand | 32.30 | 6.00 | 42.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 3 | Independent Reds INFLUENCE South Korea, Thailand | 32.20 | 6.00 | 42.50 | 0.00 | -16.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 4 | Independent Reds INFLUENCE Pakistan, Thailand | 31.60 | 6.00 | 41.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |
| 5 | Independent Reds INFLUENCE Israel, Thailand | 31.55 | 6.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Arab-Israeli War[13], Nasser[15], Truman Doctrine[19], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:2.00 |
| 2 | Truman Doctrine INFLUENCE Italy | 21.80 | 6.00 | 15.95 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.00 |
| 3 | Truman Doctrine INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:2.00 |
| 4 | Truman Doctrine INFLUENCE North Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, non_coup_milops_penalty:2.00 |
| 5 | Truman Doctrine INFLUENCE South Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Korea:15.55, non_coup_milops_penalty:2.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Romanian Abdication[12], Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Romanian Abdication INFLUENCE West Germany | 23.00 | 6.00 | 17.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, access_touch:West Germany |
| 5 | Captured Nazi Scientist INFLUENCE West Germany | 23.00 | 6.00 | 17.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, access_touch:West Germany |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], De-Stalinization[33]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | Arab-Israeli War COUP Syria | 12.40 | 4.00 | 24.70 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Nasser COUP Syria | 10.55 | 4.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:1.00, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 4 | Nasser INFLUENCE Japan | 10.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | Nasser INFLUENCE West Germany | 9.50 | 6.00 | 15.65 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:15.65, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Blockade[10], Korean War[11], COMECON[14], Warsaw Pact Formed[16], De Gaulle Leads France[17], Formosan Resolution[35]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Japan | 25.50 | 4.00 | 21.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 2 | CIA Created COUP North Korea | 24.90 | 4.00 | 21.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 3 | CIA Created COUP South Korea | 24.90 | 4.00 | 21.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:2, milops_urgency:1.00 |
| 4 | CIA Created COUP Indonesia | 23.20 | 4.00 | 19.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | CIA Created COUP Syria | 22.55 | 4.00 | 18.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 27: T2 AR6 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Formosan Resolution[35]`
- state: `VP 2, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Israel, Thailand | 26.55 | 6.00 | 36.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:18.00 |
| 3 | Formosan Resolution INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Formosan Resolution INFLUENCE Italy, Thailand | 26.10 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Formosan Resolution INFLUENCE Philippines, Thailand | 26.10 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Fidel[8], The Cambridge Five[36]`
- state: `VP 2, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 2 | The Cambridge Five INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 3 | Fidel INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 4 | Fidel INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |
| 5 | The Cambridge Five INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:9.00 |

- effects: `VP -1, DEFCON +1, MilOps U+0/A-1`

## Step 29: T3 AR0 USSR

- chosen: `Korean War [11] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Korean War[11], Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Formosan Resolution[35], Special Relationship[37], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Containment EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Socialist Governments[7], Vietnam Revolts[9], Blockade[10], COMECON[14], De Gaulle Leads France[17], UN Intervention[32], De-Stalinization[33]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | Socialist Governments EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 4 | COMECON EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], Containment[25], Formosan Resolution[35], Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 2 | Indo-Pakistani War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 3 | Arab-Israeli War INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 4 | Arab-Israeli War INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |
| 5 | Indo-Pakistani War INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Blockade[10], COMECON[14], De Gaulle Leads France[17], UN Intervention[32], De-Stalinization[33]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 2 | Socialist Governments INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 3 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 4 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.00 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], Containment[25], Formosan Resolution[35], Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, non_coup_milops_penalty:3.60 |
| 2 | Containment INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | NORAD INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | Containment INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | Containment INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], COMECON[14], De Gaulle Leads France[17], UN Intervention[32], De-Stalinization[33]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 2 | COMECON INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 4 | De Gaulle Leads France INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |
| 5 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:3.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Containment[25], Formosan Resolution[35], Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | NORAD INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | Containment INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | Containment INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | NORAD INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], De Gaulle Leads France[17], UN Intervention[32], De-Stalinization[33]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 2 | De Gaulle Leads France INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 3 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |
| 5 | De Gaulle Leads France INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:4.50 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Formosan Resolution[35], Special Relationship[37], NORAD[38]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE Japan, North Korea, Thailand | 42.70 | 6.00 | 57.15 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | NORAD INFLUENCE Italy, North Korea, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | NORAD INFLUENCE North Korea, Philippines, Thailand | 42.50 | 6.00 | 56.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | NORAD INFLUENCE North Korea, Saudi Arabia, Thailand | 42.35 | 6.00 | 56.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | NORAD INFLUENCE West Germany, North Korea, Thailand | 42.20 | 6.00 | 56.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], UN Intervention[32], De-Stalinization[33]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | De-Stalinization INFLUENCE West Germany, Japan, South Korea | 32.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization INFLUENCE Japan, North Korea, South Korea | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, Egypt | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | De-Stalinization INFLUENCE Japan, North Korea, Egypt | 32.45 | 6.00 | 46.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Romanian Abdication[12], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Special Relationship INFLUENCE North Korea, Thailand | 30.70 | 6.00 | 41.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Romanian Abdication INFLUENCE North Korea | 26.40 | 6.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55, control_break:North Korea, non_coup_milops_penalty:18.00 |
| 4 | Formosan Resolution INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Special Relationship INFLUENCE Japan, North Korea | 26.40 | 6.00 | 36.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `UN Intervention [32] as COUP`
- flags: `milops_shortfall:3`
- hand: `Vietnam Revolts[9], Blockade[10], UN Intervention[32]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP Syria | 23.55 | 4.00 | 19.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:0.5 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, non_coup_milops_penalty:18.00 |
| 3 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65, non_coup_milops_penalty:18.00 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Vietnam Revolts INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 41: T3 AR6 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Romanian Abdication[12], Special Relationship[37]`
- state: `VP -1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Syria | 26.55 | 4.00 | 22.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:3.00, coup_access_open, expected_swing:0.5 |
| 2 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:27.00 |
| 3 | Special Relationship INFLUENCE Japan, Thailand | 26.30 | 6.00 | 36.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Special Relationship INFLUENCE Italy, Thailand | 26.10 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Special Relationship INFLUENCE Philippines, Thailand | 26.10 | 6.00 | 36.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 42: T3 AR6 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10]`
- state: `VP -1, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, Japan | 21.50 | 6.00 | 31.80 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Vietnam Revolts INFLUENCE Japan, North Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Vietnam Revolts INFLUENCE Japan, South Korea | 21.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Vietnam Revolts INFLUENCE Japan, Egypt | 21.05 | 6.00 | 31.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Vietnam Revolts INFLUENCE East Germany, Japan | 20.90 | 6.00 | 31.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.05, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 43: T4 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Olympic Games[20], Containment[25], Nuclear Test Ban[34], Arms Race[42], Allende[57], OAS Founded[71], Ussuri River Skirmish[77]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Captured Nazi Scientist[18], US/Japan Mutual Defense Pact[27], Decolonization[30], Red Scare/Purge[31], Special Relationship[37], Portuguese Empire Crumbles[55], Cultural Revolution[61], Alliance for Progress[79]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +2, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Olympic Games[20], Containment[25], Arms Race[42], Allende[57], OAS Founded[71], Ussuri River Skirmish[77]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE Italy, Mexico, Morocco | 54.75 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |
| 2 | Ussuri River Skirmish INFLUENCE Italy, Mexico, Morocco | 54.75 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |
| 3 | Arms Race INFLUENCE Italy, West Germany, Mexico | 54.60 | 6.00 | 49.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 4 | Ussuri River Skirmish INFLUENCE Italy, West Germany, Mexico | 54.60 | 6.00 | 49.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, non_coup_milops_penalty:3.43 |
| 5 | Arms Race INFLUENCE Italy, West Germany, Morocco | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, access_touch:Italy, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Red Scare/Purge[31], Special Relationship[37], Portuguese Empire Crumbles[55], Cultural Revolution[61], Alliance for Progress[79]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE Italy, Mexico, Morocco, South Africa | 74.90 | 6.00 | 69.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 2 | Red Scare/Purge INFLUENCE Italy, West Germany, Mexico, South Africa | 74.75 | 6.00 | 69.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 3 | Red Scare/Purge INFLUENCE Italy, West Germany, Morocco, South Africa | 74.60 | 6.00 | 69.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 4 | Red Scare/Purge INFLUENCE Italy, Mexico, Algeria, South Africa | 74.30 | 6.00 | 68.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.43 |
| 5 | Red Scare/Purge INFLUENCE Italy, West Germany, Mexico, Morocco | 74.25 | 6.00 | 68.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.95, control_break:Italy, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, non_coup_milops_penalty:3.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Olympic Games[20], Containment[25], Allende[57], OAS Founded[71], Ussuri River Skirmish[77]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE UK, West Germany, Algeria | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 3 | Ussuri River Skirmish INFLUENCE France, West Germany, Algeria | 52.95 | 6.00 | 47.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:4.00 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, UK, West Germany | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |
| 5 | Ussuri River Skirmish INFLUENCE France, UK, West Germany | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Special Relationship[37], Portuguese Empire Crumbles[55], Cultural Revolution[61], Alliance for Progress[79]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE UK, West Germany, South Africa | 62.65 | 6.00 | 57.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 2 | Alliance for Progress INFLUENCE UK, Algeria, South Africa | 62.20 | 6.00 | 56.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, control_break:UK, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 3 | Alliance for Progress INFLUENCE East Germany, UK, South Africa | 62.05 | 6.00 | 56.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 4 | Alliance for Progress INFLUENCE France, UK, South Africa | 62.05 | 6.00 | 56.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |
| 5 | Alliance for Progress INFLUENCE Poland, UK, South Africa | 61.55 | 6.00 | 56.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:UK:14.15, control_break:UK, influence:South Africa:16.80, control_break:South Africa, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Olympic Games[20], Containment[25], Allende[57], OAS Founded[71]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, Algeria | 41.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 2 | Olympic Games INFLUENCE East Germany, Algeria | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 3 | Olympic Games INFLUENCE France, Algeria | 40.45 | 6.00 | 34.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 4 | Olympic Games INFLUENCE Saudi Arabia, Algeria | 40.20 | 6.00 | 34.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |
| 5 | Olympic Games INFLUENCE Cuba, Algeria | 39.95 | 6.00 | 34.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:4.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Special Relationship[37], Portuguese Empire Crumbles[55], Cultural Revolution[61]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 2 | Special Relationship INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 3 | Special Relationship INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 4 | Special Relationship INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, non_coup_milops_penalty:4.80 |
| 5 | Special Relationship COUP Algeria | 38.00 | 4.00 | 34.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.80, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Containment[25], Allende[57], OAS Founded[71]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 32.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Containment INFLUENCE East Germany, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Containment INFLUENCE France, West Germany, Saudi Arabia | 32.55 | 6.00 | 47.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Containment INFLUENCE East Germany, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Containment INFLUENCE France, West Germany, Cuba | 32.30 | 6.00 | 46.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Portuguese Empire Crumbles[55], Cultural Revolution[61]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, Algeria, South Africa | 34.20 | 6.00 | 48.65 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | Cultural Revolution INFLUENCE France, West Germany, South Africa | 34.05 | 6.00 | 48.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 4 | Cultural Revolution INFLUENCE East Germany, Algeria, South Africa | 33.60 | 6.00 | 48.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 5 | Cultural Revolution INFLUENCE France, Algeria, South Africa | 33.60 | 6.00 | 48.05 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:6.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Romanian Abdication[12], Truman Doctrine[19], Allende[57], OAS Founded[71]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Philippines | 30.72 | 4.00 | 26.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 2 | Allende COUP Philippines | 30.72 | 4.00 | 26.87 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:4, milops_urgency:1.33, coup_access_open, expected_swing:0.5 |
| 3 | Romanian Abdication COUP Mexico | 27.97 | 4.00 | 24.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, expected_swing:0.5 |
| 4 | Allende COUP Mexico | 27.97 | 4.00 | 24.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, expected_swing:0.5 |
| 5 | Romanian Abdication COUP Algeria | 27.22 | 4.00 | 23.37 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.33, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 54: T4 AR5 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:4`
- hand: `Blockade[10], Captured Nazi Scientist[18], Decolonization[30], Portuguese Empire Crumbles[55]`
- state: `VP 1, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Mexico | 27.97 | 4.00 | 24.12 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:1.33, expected_swing:0.5 |
| 2 | Captured Nazi Scientist COUP Algeria | 27.22 | 4.00 | 23.37 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:1.33, expected_swing:0.5 |
| 3 | Captured Nazi Scientist COUP Morocco | 24.82 | 4.00 | 20.97 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:4, milops_urgency:1.33 |
| 4 | Captured Nazi Scientist COUP Japan | 24.42 | 4.00 | 20.57 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:4, milops_urgency:1.33 |
| 5 | Captured Nazi Scientist COUP Israel | 24.42 | 4.00 | 20.57 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Israel, battleground_coup, milops_need:4, milops_urgency:1.33 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 55: T4 AR6 USSR

- chosen: `Allende [57] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Truman Doctrine[19], Allende[57], OAS Founded[71]`
- state: `VP 1, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE Algeria | 25.05 | 6.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:18.00 |
| 2 | Allende COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 3 | Allende INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.00 |
| 4 | Allende COUP Algeria | 21.55 | 4.00 | 17.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:0.5 |
| 5 | Allende INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Decolonization[30], Portuguese Empire Crumbles[55]`
- state: `VP 1, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Decolonization INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | Decolonization INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Truman Doctrine [19] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Truman Doctrine[19], OAS Founded[71]`
- state: `VP 1, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Mexico | 13.30 | 4.00 | 21.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 2 | OAS Founded COUP Mexico | 13.30 | 4.00 | 21.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 3 | Truman Doctrine COUP Algeria | 12.55 | 4.00 | 20.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 4 | OAS Founded COUP Algeria | 12.55 | 4.00 | 20.70 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, expected_swing:0.5, offside_ops_penalty |
| 5 | Truman Doctrine COUP Morocco | 10.15 | 4.00 | 18.30 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:3, milops_urgency:3.00, defcon_penalty:3, offside_ops_penalty |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], Portuguese Empire Crumbles[55]`
- state: `VP 1, DEFCON 2, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 22.65 | 6.00 | 32.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 2 | Portuguese Empire Crumbles INFLUENCE East Germany, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 3 | Portuguese Empire Crumbles INFLUENCE France, South Africa | 22.05 | 6.00 | 32.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 4 | Portuguese Empire Crumbles INFLUENCE Poland, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |
| 5 | Portuguese Empire Crumbles INFLUENCE Cuba, South Africa | 21.55 | 6.00 | 31.85 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:27.00 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 59: T5 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], Warsaw Pact Formed[16], De-Stalinization[33], Formosan Resolution[35], NORAD[38], We Will Bury You[53], Puppet Governments[67], Ask Not What Your Country Can Do For You[78]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Five Year Plan EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | NORAD EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Duck and Cover[4], Socialist Governments[7], Indo-Pakistani War[24], Bear Trap[47], Missile Envy[52], Muslim Revolution[59], OPEC[64], John Paul II Elected Pope[69], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON -2, MilOps U+0/A+0`
