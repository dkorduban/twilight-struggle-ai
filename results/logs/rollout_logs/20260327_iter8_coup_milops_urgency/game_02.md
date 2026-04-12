# minimal_hybrid detailed rollout log

- seed: `20260531`
- winner: `US`
- final_vp: `-8`
- end_turn: `10`
- end_reason: `turn_limit`

## Step 1: T1 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:1`
- hand: `COMECON[14], Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], NATO[21], UN Intervention[32], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 2: T1 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Blockade[10], Arab-Israeli War[13], Truman Doctrine[19], CIA Created[26], US/Japan Mutual Defense Pact[27], East European Unrest[29], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 3: T1 AR1 USSR

- chosen: `Olympic Games [20] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Captured Nazi Scientist[18], Olympic Games[20], NATO[21], UN Intervention[32], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 2 | The Cambridge Five COUP Iran | 71.65 | 4.00 | 67.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | UN Intervention COUP Iran | 66.30 | 4.00 | 62.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 4: T1 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Duck and Cover[4], Blockade[10], Arab-Israeli War[13], Truman Doctrine[19], CIA Created[26], East European Unrest[29], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 2 | East European Unrest INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 3 | NORAD INFLUENCE North Korea, Indonesia, Philippines | 62.07 | 6.00 | 57.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines, non_coup_milops_penalty:1.33 |
| 4 | Duck and Cover COUP Syria | 33.50 | 4.00 | 29.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5 |
| 5 | East European Unrest COUP Syria | 33.50 | 4.00 | 29.95 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.17, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], NATO[21], UN Intervention[32], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE West Germany, Japan, North Korea, Thailand | 60.20 | 6.00 | 78.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand, offside_ops_penalty |
| 2 | The Cambridge Five INFLUENCE North Korea, Thailand | 48.70 | 6.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, access_touch:Thailand |
| 3 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 4 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Arab-Israeli War[13], Truman Doctrine[19], CIA Created[26], East European Unrest[29], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Turkey, West Germany, Japan | 63.20 | 6.00 | 59.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:1.60 |
| 2 | NORAD INFLUENCE Turkey, West Germany, Japan | 63.20 | 6.00 | 59.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15, control_break:Japan, non_coup_milops_penalty:1.60 |
| 3 | East European Unrest COUP Syria | 33.60 | 4.00 | 30.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 4 | NORAD COUP Syria | 33.60 | 4.00 | 30.05 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.20, coup_access_open, expected_swing:2.5 |
| 5 | East European Unrest COUP Indonesia | 31.25 | 4.00 | 27.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.20, empty_coup_penalty, expected_swing:4.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china`
- hand: `Nasser[15], Captured Nazi Scientist[18], UN Intervention[32], Formosan Resolution[35], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE South Korea, Thailand | 48.70 | 6.00 | 43.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, control_break:Thailand |
| 2 | The Cambridge Five COUP Iran | 48.15 | 4.00 | 44.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus |
| 3 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 5 | UN Intervention COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Arab-Israeli War[13], Truman Doctrine[19], CIA Created[26], NORAD[38]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, Panama | 53.85 | 6.00 | 50.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama, non_coup_milops_penalty:2.00 |
| 2 | NORAD COUP Syria | 33.75 | 4.00 | 30.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.25, coup_access_open, expected_swing:2.5 |
| 3 | NORAD COUP Indonesia | 31.40 | 4.00 | 27.85 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:1, milops_urgency:0.25, empty_coup_penalty, expected_swing:4.5 |
| 4 | NORAD COUP North Korea | 26.10 | 4.00 | 22.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:1, milops_urgency:0.25, expected_swing:0.5 |
| 5 | NORAD COUP South Korea | 26.10 | 4.00 | 22.55 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:1, milops_urgency:0.25, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china`
- hand: `Nasser[15], Captured Nazi Scientist[18], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 2 | Captured Nazi Scientist COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 3 | UN Intervention COUP Iran | 42.80 | 4.00 | 38.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:0.5, opening_iran_coup_bonus |
| 4 | Formosan Resolution COUP Iran | 32.15 | 4.00 | 44.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Iran, battleground_coup, empty_coup_penalty, expected_swing:1.5, opening_iran_coup_bonus, offside_ops_penalty |
| 5 | Nasser COUP Philippines | 30.55 | 4.00 | 26.70 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Arab-Israeli War[13], Truman Doctrine[19], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created COUP Syria | 23.30 | 4.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:1, milops_urgency:0.33, coup_access_open, expected_swing:0.5 |
| 3 | Truman Doctrine INFLUENCE Italy | 19.63 | 6.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.67 |
| 4 | CIA Created INFLUENCE Italy | 19.63 | 6.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, non_coup_milops_penalty:2.67 |
| 5 | Arab-Israeli War INFLUENCE Italy, Japan | 19.63 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 11: T1 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], Formosan Resolution[35]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Pakistan, Thailand | 27.10 | 6.00 | 37.40 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Pakistan:14.95, access_touch:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `none`
- hand: `Blockade[10], Arab-Israeli War[13], CIA Created[26]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Italy | 22.30 | 6.00 | 16.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy |
| 2 | Arab-Israeli War INFLUENCE Italy, Japan | 22.30 | 6.00 | 32.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, offside_ops_penalty |
| 3 | CIA Created COUP Syria | 21.30 | 4.00 | 17.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5 |
| 4 | Arab-Israeli War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Blockade INFLUENCE Italy | 10.30 | 6.00 | 16.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, access_touch:Italy, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `holds_china`
- hand: `Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Captured Nazi Scientist COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 4 | UN Intervention COUP Lebanon | 9.70 | 4.00 | 5.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:2.5 |
| 5 | Captured Nazi Scientist REALIGN Israel | 3.04 | -1.00 | 4.20 | 0.00 | 0.00 | -0.15 | 0.00 |  |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `offside_ops_play`
- hand: `Blockade[10], Arab-Israeli War[13]`
- state: `VP 0, DEFCON 3, MilOps U2/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Italy, Japan | 25.30 | 6.00 | 35.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty |
| 2 | Blockade INFLUENCE Italy | 13.30 | 6.00 | 19.45 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Syria | 10.65 | 4.00 | 22.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Blockade COUP Syria | 9.30 | 4.00 | 17.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Arab-Israeli War SPACE | 8.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty |

- effects: `VP +1, DEFCON +1, MilOps U-2/A-1`

## Step 15: T2 AR0 USSR

- chosen: `Socialist Governments [7] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Marshall Plan[23], Indo-Pakistani War[24], Containment[25], Suez Crisis[28]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 16: T2 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], De Gaulle Leads France[17], Independent Reds[22], Red Scare/Purge[31], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Suez Crisis [28] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Marshall Plan[23], Indo-Pakistani War[24], Containment[25], Suez Crisis[28]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis COUP Philippines | 44.25 | 4.00 | 40.70 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:2.5 |
| 2 | Suez Crisis INFLUENCE Pakistan, Thailand | 43.28 | 6.00 | 40.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, non_coup_milops_penalty:2.67 |
| 3 | Vietnam Revolts COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 4 | Korean War COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |
| 5 | Indo-Pakistani War COUP Philippines | 38.90 | 4.00 | 35.20 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+3/A+0`

## Step 18: T2 AR1 US

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], De Gaulle Leads France[17], Independent Reds[22], De-Stalinization[33], Nuclear Test Ban[34], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE West Germany, Japan, Egypt, Philippines | 66.68 | 6.00 | 63.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:2.67 |
| 2 | Five Year Plan INFLUENCE Japan, Egypt, Philippines | 51.18 | 6.00 | 48.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:2.67 |
| 3 | Nuclear Test Ban COUP Syria | 40.35 | 4.00 | 36.95 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 4 | Independent Reds INFLUENCE Japan, Philippines | 35.63 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:2.67 |
| 5 | Special Relationship INFLUENCE Japan, Philippines | 35.63 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Marshall Plan[23], Indo-Pakistani War[24], Containment[25]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE India, Pakistan, Thailand | 39.35 | 6.00 | 57.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | Vietnam Revolts INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 4 | Korean War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 5 | Indo-Pakistani War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], Fidel[8], De Gaulle Leads France[17], Independent Reds[22], De-Stalinization[33], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Egypt, Libya | 52.90 | 6.00 | 50.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, non_coup_milops_penalty:3.20 |
| 2 | Independent Reds INFLUENCE Japan, Egypt | 37.35 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 3 | Special Relationship INFLUENCE Japan, Egypt | 37.35 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, non_coup_milops_penalty:3.20 |
| 4 | Five Year Plan COUP Syria | 35.20 | 4.00 | 31.65 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |
| 5 | De Gaulle Leads France INFLUENCE Japan, Egypt, Libya | 32.90 | 6.00 | 50.55 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, control_break:Egypt, influence:Libya:13.70, access_touch:Libya, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china`
- hand: `Vietnam Revolts[9], Korean War[11], Romanian Abdication[12], Indo-Pakistani War[24], Containment[25]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | Vietnam Revolts INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 3 | Korean War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 4 | Indo-Pakistani War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 5 | Containment INFLUENCE Israel, Thailand | 22.90 | 6.00 | 37.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], De Gaulle Leads France[17], Independent Reds[22], De-Stalinization[33], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Libya | 36.55 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 2 | Special Relationship INFLUENCE Japan, Libya | 36.55 | 6.00 | 34.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, non_coup_milops_penalty:4.00 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Japan, Libya | 32.05 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, Libya | 32.05 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Libya:13.70, control_break:Libya, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Independent Reds COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china`
- hand: `Vietnam Revolts[9], Korean War[11], Indo-Pakistani War[24], Containment[25]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 2 | Korean War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 3 | Indo-Pakistani War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 4 | Containment INFLUENCE Israel, Thailand | 22.90 | 6.00 | 37.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 5 | Vietnam Revolts COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], De Gaulle Leads France[17], De-Stalinization[33], Special Relationship[37]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, Japan | 32.17 | 6.00 | 31.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, non_coup_milops_penalty:5.33 |
| 2 | Special Relationship COUP Syria | 30.65 | 4.00 | 26.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 27.57 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 27.57 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | Special Relationship COUP Lebanon | 19.05 | 4.00 | 15.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china`
- hand: `Korean War[11], Indo-Pakistani War[24], Containment[25]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 2 | Indo-Pakistani War INFLUENCE Thailand | 26.15 | 6.00 | 20.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Thailand:20.45 |
| 3 | Containment INFLUENCE Israel, Thailand | 22.90 | 6.00 | 37.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, offside_ops_penalty |
| 4 | Korean War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 5 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], De Gaulle Leads France[17], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Japan, North Korea | 18.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 18.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | De Gaulle Leads France COUP Syria | 17.00 | 4.00 | 33.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | De-Stalinization COUP Syria | 17.00 | 4.00 | 33.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Fidel COUP Syria | 15.65 | 4.00 | 27.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, offside_ops_play`
- hand: `Indo-Pakistani War[24], Containment[25]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE North Korea, Thailand | 26.55 | 6.00 | 41.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45, offside_ops_penalty |
| 2 | Indo-Pakistani War INFLUENCE North Korea | 26.25 | 6.00 | 20.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea |
| 3 | Indo-Pakistani War COUP Lebanon | 15.05 | 4.00 | 11.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Lebanon, empty_coup_penalty, expected_swing:3.5 |
| 4 | Containment SPACE | 8.55 | 1.00 | 3.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty |
| 5 | Indo-Pakistani War COUP Jordan | 4.65 | 4.00 | 0.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Jordan, empty_coup_penalty, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `De-Stalinization [33] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization COUP Syria | 20.00 | 4.00 | 36.45 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 2 | Fidel COUP Syria | 18.65 | 4.00 | 30.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | De-Stalinization INFLUENCE West Germany, Japan, North Korea | 10.90 | 6.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 4 | De-Stalinization COUP Lebanon | 8.40 | 4.00 | 24.85 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | Fidel COUP Lebanon | 7.05 | 4.00 | 19.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Lebanon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A+0`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], NATO[21], Decolonization[30], Red Scare/Purge[31], De-Stalinization[33], Nuclear Test Ban[34]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `NORAD [38] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26], NORAD[38]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 3 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | De Gaulle Leads France EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Fidel EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], NATO[21], Decolonization[30], De-Stalinization[33], Nuclear Test Ban[34]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Italy, Israel, Saudi Arabia, Thailand | 71.50 | 6.00 | 70.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |
| 2 | Nuclear Test Ban COUP Indonesia | 61.50 | 4.00 | 58.10 | 0.00 | 0.00 | -0.60 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:5.5 |
| 3 | Warsaw Pact Formed COUP Indonesia | 56.15 | 4.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 4 | De-Stalinization COUP Indonesia | 56.15 | 4.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Indonesia, battleground_coup, milops_need:3, milops_urgency:0.50, coup_access_open, expected_swing:4.5 |
| 5 | Warsaw Pact Formed INFLUENCE Italy, Israel, Thailand | 55.35 | 6.00 | 53.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Truman Doctrine [19] as COUP`
- flags: `milops_shortfall:3`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine COUP Philippines | 26.05 | 4.00 | 22.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:0.5 |
| 2 | CIA Created COUP Philippines | 26.05 | 4.00 | 22.20 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Philippines, battleground_coup, milops_need:3, milops_urgency:0.50, expected_swing:0.5 |
| 3 | Truman Doctrine COUP Japan | 25.00 | 4.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3, milops_urgency:0.50 |
| 4 | CIA Created COUP Japan | 25.00 | 4.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3, milops_urgency:0.50 |
| 5 | Truman Doctrine COUP North Korea | 24.40 | 4.00 | 20.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:3, milops_urgency:0.50 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 33: T3 AR2 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Warsaw Pact Formed[16], Captured Nazi Scientist[18], NATO[21], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Japan, Indonesia, Thailand | 53.20 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 2 | De-Stalinization INFLUENCE Japan, Indonesia, Thailand | 53.20 | 6.00 | 52.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:4.80 |
| 3 | NATO INFLUENCE Japan, Egypt, Indonesia, Thailand | 44.75 | 6.00 | 68.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:4.80 |
| 4 | Warsaw Pact Formed COUP Egypt | 39.30 | 4.00 | 35.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 5 | De-Stalinization COUP Egypt | 39.30 | 4.00 | 35.75 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.60, defcon_penalty:3, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `CIA Created [26] as COUP`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17], CIA Created[26]`
- state: `VP 1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created COUP Syria | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:0.5 |
| 2 | CIA Created INFLUENCE Italy | 22.10 | 6.00 | 19.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, non_coup_milops_penalty:3.20 |
| 3 | De Gaulle Leads France INFLUENCE Italy, Indonesia | 20.65 | 6.00 | 38.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Indonesia:13.85, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | De Gaulle Leads France COUP Syria | 15.20 | 4.00 | 31.65 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Fidel COUP Syria | 13.85 | 4.00 | 26.15 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Captured Nazi Scientist[18], NATO[21], Decolonization[30], De-Stalinization[33]`
- state: `VP 1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE Japan, Indonesia, Thailand | 55.00 | 6.00 | 55.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 2 | NATO INFLUENCE Japan, Egypt, Indonesia, Thailand | 46.55 | 6.00 | 71.15 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:6.00 |
| 3 | De-Stalinization COUP Egypt | 39.75 | 4.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:2.5 |
| 4 | Decolonization INFLUENCE Indonesia, Thailand | 39.00 | 6.00 | 39.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, control_break:Indonesia, influence:Thailand:20.45, non_coup_milops_penalty:6.00 |
| 5 | Decolonization COUP Egypt | 33.40 | 4.00 | 29.70 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:0.75, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13], De Gaulle Leads France[17]`
- state: `VP 1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, Japan | 17.15 | 6.00 | 35.60 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France COUP Syria | 15.50 | 4.00 | 31.95 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 3 | Fidel COUP Syria | 14.15 | 4.00 | 26.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Vietnam Revolts COUP Syria | 14.15 | 4.00 | 26.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Syria | 14.15 | 4.00 | 26.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], NATO[21], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE UK, Japan, Egypt, Thailand | 41.35 | 6.00 | 67.95 | 0.00 | -24.00 | -0.60 | 0.00 | influence:UK:13.65, access_touch:UK, influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 34.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45, non_coup_milops_penalty:8.00 |
| 3 | Decolonization COUP Egypt | 34.15 | 4.00 | 30.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 4 | Nasser COUP Egypt | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Captured Nazi Scientist COUP Egypt | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.00, defcon_penalty:3, coup_access_open, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13]`
- state: `VP 1, DEFCON 3, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Syria | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Syria | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 3 | Arab-Israeli War COUP Syria | 14.65 | 4.00 | 26.95 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:1.5, offside_ops_penalty |
| 4 | Blockade COUP Syria | 12.30 | 4.00 | 20.45 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Syria, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:0.5, offside_ops_penalty |
| 5 | Fidel COUP Egypt | 10.15 | 4.00 | 22.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:2, milops_urgency:0.67, defcon_penalty:3, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+1`

## Step 39: T3 AR5 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Nasser[15], Captured Nazi Scientist[18], Decolonization[30]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Libya | 35.65 | 4.00 | 31.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Decolonization COUP Syria | 33.15 | 4.00 | 29.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:3, milops_urgency:1.50, coup_access_open, expected_swing:1.5 |
| 3 | Nasser COUP Libya | 29.30 | 4.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 4 | Captured Nazi Scientist COUP Libya | 29.30 | 4.00 | 25.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Libya, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, coup_access_open, expected_swing:0.5 |
| 5 | Decolonization COUP Egypt | 28.65 | 4.00 | 24.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Egypt, battleground_coup, milops_need:3, milops_urgency:1.50, defcon_penalty:3, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 40: T3 AR5 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], Arab-Israeli War[13]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Egypt | 5.55 | 6.00 | 18.70 | 0.00 | -12.00 | -0.15 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 2 | Vietnam Revolts SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 3 | Arab-Israeli War SPACE | 1.70 | 1.00 | 3.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 4 | Vietnam Revolts INFLUENCE Egypt | 1.40 | 6.00 | 18.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |
| 5 | Arab-Israeli War INFLUENCE Egypt | 1.40 | 6.00 | 18.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Egypt:13.70, control_break:Egypt, offside_ops_penalty, non_coup_milops_penalty:7.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Nasser [15] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser INFLUENCE Thailand | 15.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 2 | Captured Nazi Scientist INFLUENCE Thailand | 15.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45, non_coup_milops_penalty:11.00 |
| 3 | Nasser COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Sudan | 11.45 | 4.00 | 7.60 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Nasser COUP Tunisia | 1.05 | 4.00 | -2.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Tunisia, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:0.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Vietnam Revolts [9] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Arab-Israeli War[13]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts COUP SE African States | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Vietnam Revolts COUP Sudan | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Vietnam Revolts COUP Zimbabwe | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Zimbabwe, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Arab-Israeli War COUP SE African States | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Arab-Israeli War COUP Sudan | 0.80 | 4.00 | 13.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:1, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 43: T4 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Korean War[11], De Gaulle Leads France[17], NATO[21], Independent Reds[22], Formosan Resolution[35], Bear Trap[47], Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Lone Gunman EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Five Year Plan[5], Fidel[8], Warsaw Pact Formed[16], Decolonization[30], Special Relationship[37], Allende[57], Muslim Revolution[59], Puppet Governments[67], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Muslim Revolution EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], NATO[21], Independent Reds[22], Bear Trap[47], Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Libya, Mexico, Morocco, Indonesia | 45.88 | 6.00 | 69.05 | 0.00 | -24.00 | -0.60 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Mexico:14.95, access_touch:Mexico, influence:Morocco:14.80, access_touch:Morocco, influence:Indonesia:12.10, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Korean War INFLUENCE Libya, Indonesia | 36.43 | 6.00 | 35.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:4.57 |
| 3 | Willy Brandt INFLUENCE Libya, Indonesia | 36.43 | 6.00 | 35.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:4.57 |
| 4 | Bear Trap INFLUENCE Libya, Mexico, Indonesia | 33.23 | 6.00 | 52.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Libya:13.20, control_break:Libya, influence:Mexico:14.95, access_touch:Mexico, influence:Indonesia:12.10, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Korean War COUP Syria | 29.86 | 4.00 | 26.16 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.57, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Fidel[8], Warsaw Pact Formed[16], Decolonization[30], Special Relationship[37], Allende[57], Muslim Revolution[59], Puppet Governments[67], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE France, UK, Mexico, Angola | 53.08 | 6.00 | 76.25 | 0.00 | -24.00 | -0.60 | 0.00 | influence:France:15.55, access_touch:France, influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 2 | Special Relationship INFLUENCE UK, Angola | 42.88 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 3 | Puppet Governments INFLUENCE UK, Angola | 42.88 | 6.00 | 41.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:Angola:15.60, control_break:Angola, access_touch:Angola, non_coup_milops_penalty:4.57 |
| 4 | Warsaw Pact Formed INFLUENCE France, UK, Angola | 40.28 | 6.00 | 59.30 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:UK:14.15, control_break:UK, influence:Angola:15.60, control_break:Angola, access_touch:Angola, offside_ops_penalty, non_coup_milops_penalty:4.57 |
| 5 | Special Relationship COUP Mexico | 34.11 | 4.00 | 30.41 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4, milops_urgency:0.57, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Korean War[11], Independent Reds[22], Bear Trap[47], Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE France, Algeria | 37.12 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 2 | Willy Brandt INFLUENCE France, Algeria | 37.12 | 6.00 | 36.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, control_break:France, influence:Algeria:14.20, access_touch:Algeria, non_coup_milops_penalty:5.33 |
| 3 | Bear Trap INFLUENCE France, West Germany, Algeria | 33.12 | 6.00 | 52.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Korean War COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |
| 5 | Willy Brandt COUP Syria | 30.15 | 4.00 | 26.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Syria, milops_need:4, milops_urgency:0.67, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Special Relationship [37] as COUP`
- flags: `milops_shortfall:4`
- hand: `Fidel[8], Warsaw Pact Formed[16], Decolonization[30], Special Relationship[37], Allende[57], Puppet Governments[67], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship COUP Algeria | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 2 | Puppet Governments COUP Algeria | 33.65 | 4.00 | 29.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Algeria, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |
| 3 | Special Relationship INFLUENCE Algeria, South Africa | 33.37 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 4 | Puppet Governments INFLUENCE Algeria, South Africa | 33.37 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:5.33 |
| 5 | Special Relationship COUP Libya | 32.65 | 4.00 | 28.95 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Libya, battleground_coup, milops_need:4, milops_urgency:0.67, defcon_penalty:3, coup_access_open, expected_swing:1.5 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 49: T4 AR3 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Independent Reds[22], Bear Trap[47], Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE West Germany, Algeria | 34.65 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:6.40 |
| 2 | Bear Trap INFLUENCE East Germany, West Germany, Algeria | 30.05 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:6.40 |
| 3 | Willy Brandt COUP Saharan States | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 4 | Willy Brandt COUP Sudan | 19.95 | 4.00 | 16.25 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |
| 5 | Willy Brandt COUP Guatemala | 18.70 | 4.00 | 15.00 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:0.80, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Warsaw Pact Formed[16], Decolonization[30], Allende[57], Puppet Governments[67], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE Algeria, South Africa | 35.50 | 6.00 | 33.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, non_coup_milops_penalty:3.20 |
| 2 | Warsaw Pact Formed INFLUENCE Algeria, Congo/Zaire, South Africa | 31.55 | 6.00 | 49.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | Fidel INFLUENCE Algeria, South Africa | 19.50 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | Decolonization INFLUENCE Algeria, South Africa | 19.50 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | Colonial Rear Guards INFLUENCE Algeria, South Africa | 19.50 | 6.00 | 33.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Independent Reds[22], Bear Trap[47], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany, Algeria | 28.45 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 2 | Lone Gunman INFLUENCE Algeria | 17.05 | 6.00 | 19.20 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:8.00 |
| 3 | Independent Reds INFLUENCE West Germany, Algeria | 17.05 | 6.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Grain Sales to Soviets INFLUENCE West Germany, Algeria | 17.05 | 6.00 | 35.35 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Lone Gunman COUP Saharan States | 14.20 | 4.00 | 10.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.00, empty_coup_penalty, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Warsaw Pact Formed[16], Decolonization[30], Allende[57], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Congo/Zaire, Morocco, South Africa | 36.35 | 6.00 | 54.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, access_touch:Congo/Zaire, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | Fidel INFLUENCE Morocco, South Africa | 24.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | Decolonization INFLUENCE Morocco, South Africa | 24.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | Colonial Rear Guards INFLUENCE Morocco, South Africa | 24.30 | 6.00 | 38.60 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Allende INFLUENCE South Africa | 11.65 | 6.00 | 21.80 | 0.00 | -12.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Lone Gunman [109] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Independent Reds[22], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 1, DEFCON 2, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman COUP Saharan States | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 2 | Lone Gunman COUP Sudan | 15.20 | 4.00 | 11.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 3 | Lone Gunman COUP Guatemala | 13.95 | 4.00 | 10.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:4, milops_urgency:1.33, empty_coup_penalty, expected_swing:2.5 |
| 4 | Lone Gunman INFLUENCE West Germany | 11.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:10.67 |
| 5 | Independent Reds INFLUENCE East Germany, West Germany | 10.73 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 54: T4 AR5 US

- chosen: `Fidel [8] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Decolonization[30], Allende[57], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Decolonization COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Saharan States | 25.55 | 4.00 | 37.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 4 | Allende COUP Saharan States | 23.20 | 4.00 | 31.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 5 | Fidel INFLUENCE Congo/Zaire, South Africa | 20.37 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Independent Reds [22] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Independent Reds[22], Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 2, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds COUP Saharan States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Independent Reds COUP Sudan | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Saharan States | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets COUP Sudan | 6.05 | 4.00 | 18.35 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Independent Reds COUP Guatemala | 4.80 | 4.00 | 17.10 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:3, milops_urgency:1.50, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+1/A+0`

## Step 56: T4 AR6 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Decolonization[30], Allende[57], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Saharan States | 26.55 | 4.00 | 38.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | Allende COUP Saharan States | 24.20 | 4.00 | 32.35 | 0.00 | -12.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, coup_access_open, expected_swing:2.5, offside_ops_penalty |
| 4 | Decolonization INFLUENCE Congo/Zaire, South Africa | 11.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Colonial Rear Guards INFLUENCE Congo/Zaire, South Africa | 11.70 | 6.00 | 36.00 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Grain Sales to Soviets [68] as COUP`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Grain Sales to Soviets[68]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 2 | Grain Sales to Soviets COUP Sudan | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Grain Sales to Soviets COUP Guatemala | 6.30 | 4.00 | 18.60 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | -0.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |
| 5 | Grain Sales to Soviets COUP Tunisia | -2.85 | 4.00 | 9.45 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Tunisia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:1.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Colonial Rear Guards [110] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Allende[57], Colonial Rear Guards[110]`
- state: `VP 1, DEFCON 2, MilOps U2/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards COUP Colombia | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 2 | Colonial Rear Guards COUP Cameroon | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 3 | Colonial Rear Guards COUP Mozambique | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 4 | Colonial Rear Guards COUP Saharan States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |
| 5 | Colonial Rear Guards COUP SE African States | 7.55 | 4.00 | 19.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:SE African States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:3.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-2/A-2`

## Step 59: T5 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Vietnam Revolts[9], Captured Nazi Scientist[18], NATO[21], Red Scare/Purge[31], The Cambridge Five[36], Arms Race[42], Cultural Revolution[61], Sadat Expels Soviets[73]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Cultural Revolution EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Fidel EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Vietnam Revolts EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], De-Stalinization[33], SALT Negotiations[46], OPEC[64], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Panama Canal Returned EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Warsaw Pact Formed EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP -2, DEFCON -1, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Arms Race [42] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Fidel[8], Vietnam Revolts[9], Captured Nazi Scientist[18], NATO[21], The Cambridge Five[36], Arms Race[42], Cultural Revolution[61], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 2 | Cultural Revolution COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 3 | Arms Race INFLUENCE East Germany, France, West Germany | 47.09 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 4 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 47.09 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:5.71 |
| 5 | Fidel COUP Saharan States | 41.69 | 4.00 | 37.99 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+3/A+0`

## Step 62: T5 AR1 US

- chosen: `SALT Negotiations [46] as COUP`
- flags: `milops_shortfall:5`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], De-Stalinization[33], SALT Negotiations[46], OPEC[64], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations COUP Saharan States | 48.04 | 4.00 | 44.49 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5 |
| 2 | SALT Negotiations INFLUENCE Congo/Zaire, South Africa | 35.84 | 6.00 | 36.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, non_coup_milops_penalty:5.71 |
| 3 | Captured Nazi Scientist COUP Saharan States | 35.34 | 4.00 | 31.49 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 4 | Panama Canal Returned COUP Saharan States | 35.34 | 4.00 | 31.49 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:2.5 |
| 5 | Warsaw Pact Formed COUP Saharan States | 28.04 | 4.00 | 44.49 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:5, milops_urgency:0.71, coup_access_open, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+3`

## Step 63: T5 AR2 USSR

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Vietnam Revolts[9], Captured Nazi Scientist[18], NATO[21], The Cambridge Five[36], Cultural Revolution[61], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 50.13 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:2.67 |
| 2 | Cultural Revolution COUP Saharan States | 45.90 | 4.00 | 42.35 | 0.00 | 0.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:4.5 |
| 3 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 41.53 | 6.00 | 62.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | Fidel COUP Saharan States | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |
| 5 | Vietnam Revolts COUP Saharan States | 40.55 | 4.00 | 36.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.33, coup_access_open, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], Captured Nazi Scientist[18], De-Stalinization[33], OPEC[64], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Nigeria | 23.78 | 6.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:2.67 |
| 2 | Panama Canal Returned INFLUENCE Nigeria | 23.78 | 6.00 | 20.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, non_coup_milops_penalty:2.67 |
| 3 | Warsaw Pact Formed INFLUENCE Congo/Zaire, Nigeria | 22.68 | 6.00 | 39.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 4 | De Gaulle Leads France INFLUENCE Congo/Zaire, Nigeria | 22.68 | 6.00 | 39.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:2.67 |
| 5 | De-Stalinization INFLUENCE Congo/Zaire, Nigeria | 22.68 | 6.00 | 39.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:Nigeria:13.60, control_break:Nigeria, access_touch:Nigeria, offside_ops_penalty, non_coup_milops_penalty:2.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Vietnam Revolts[9], Captured Nazi Scientist[18], NATO[21], The Cambridge Five[36], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 41.00 | 6.00 | 62.80 | 0.00 | -24.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 2 | Fidel COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 3 | Vietnam Revolts COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Saharan States | 40.75 | 4.00 | 37.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:3.5 |
| 5 | Captured Nazi Scientist COUP Saharan States | 34.40 | 4.00 | 30.55 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.40, coup_access_open, expected_swing:2.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Panama Canal Returned [111] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], De-Stalinization[33], OPEC[64], Panama Canal Returned[111]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Panama Canal Returned INFLUENCE West Germany | 23.80 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:3.20 |
| 2 | Warsaw Pact Formed INFLUENCE West Germany, Congo/Zaire | 22.70 | 6.00 | 40.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 3 | De Gaulle Leads France INFLUENCE West Germany, Congo/Zaire | 22.70 | 6.00 | 40.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 4 | De-Stalinization INFLUENCE West Germany, Congo/Zaire | 22.70 | 6.00 | 40.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:3.20 |
| 5 | OPEC INFLUENCE West Germany, Congo/Zaire | 22.70 | 6.00 | 40.35 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:3.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Fidel [8] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Vietnam Revolts[9], Captured Nazi Scientist[18], The Cambridge Five[36], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 2 | Vietnam Revolts COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 3 | The Cambridge Five COUP Saharan States | 41.05 | 4.00 | 37.35 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:3.5 |
| 4 | Captured Nazi Scientist COUP Saharan States | 34.70 | 4.00 | 30.85 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.50, coup_access_open, expected_swing:2.5 |
| 5 | Fidel INFLUENCE East Germany, West Germany | 33.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], Warsaw Pact Formed[16], De Gaulle Leads France[17], De-Stalinization[33], OPEC[64]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE Congo/Zaire, South Africa | 17.55 | 6.00 | 36.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 2 | De Gaulle Leads France INFLUENCE Congo/Zaire, South Africa | 17.55 | 6.00 | 36.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 3 | De-Stalinization INFLUENCE Congo/Zaire, South Africa | 17.55 | 6.00 | 36.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 4 | OPEC INFLUENCE Congo/Zaire, South Africa | 17.55 | 6.00 | 36.00 | 0.00 | -20.00 | -0.45 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:4.00 |
| 5 | Arab-Israeli War INFLUENCE Congo/Zaire | 4.90 | 6.00 | 19.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:Congo/Zaire:14.20, control_break:Congo/Zaire, offside_ops_penalty, non_coup_milops_penalty:4.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], The Cambridge Five[36], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, North Korea | 35.32 | 6.00 | 34.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:North Korea:13.80, control_break:North Korea, non_coup_milops_penalty:5.33 |
| 2 | The Cambridge Five INFLUENCE West Germany, North Korea | 35.32 | 6.00 | 34.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:North Korea:13.80, control_break:North Korea, non_coup_milops_penalty:5.33 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, North Korea | 30.72 | 6.00 | 50.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:North Korea:13.80, control_break:North Korea, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Vietnam Revolts COUP Saharan States | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |
| 5 | Vietnam Revolts COUP Sudan | 19.55 | 4.00 | 15.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], De Gaulle Leads France[17], De-Stalinization[33], OPEC[64]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, South Africa | 18.17 | 6.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 2 | De-Stalinization INFLUENCE West Germany, South Africa | 18.17 | 6.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 3 | OPEC INFLUENCE West Germany, South Africa | 18.17 | 6.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 4 | Arab-Israeli War INFLUENCE West Germany | 5.52 | 6.00 | 21.15 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:5.33 |
| 5 | De Gaulle Leads France COUP Colombia | 4.90 | 4.00 | 21.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:0.67, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], The Cambridge Five[36], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, Algeria | 27.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:14.00 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Algeria | 22.45 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | The Cambridge Five COUP Saharan States | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 4 | The Cambridge Five COUP Sudan | 20.55 | 4.00 | 16.85 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |
| 5 | The Cambridge Five COUP Guatemala | 19.30 | 4.00 | 15.60 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:3.5 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], De-Stalinization[33], OPEC[64]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE West Germany, South Africa | 9.50 | 6.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | OPEC INFLUENCE West Germany, South Africa | 9.50 | 6.00 | 37.95 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | De-Stalinization COUP Colombia | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | De-Stalinization COUP Cameroon | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | De-Stalinization COUP Mozambique | 5.90 | 4.00 | 22.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:1.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Sadat Expels Soviets[73]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Saharan States | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 2 | Captured Nazi Scientist COUP Sudan | 17.20 | 4.00 | 13.35 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Sudan, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 3 | Captured Nazi Scientist COUP Guatemala | 15.95 | 4.00 | 12.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Guatemala, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 4 | Captured Nazi Scientist COUP Haiti | 15.95 | 4.00 | 12.10 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Haiti, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:2.5 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 10.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:22.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `OPEC [64] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Arab-Israeli War[13], OPEC[64]`
- state: `VP -1, DEFCON 2, MilOps U3/A3, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC COUP Saharan States | 30.90 | 4.00 | 47.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:4.5, offside_ops_penalty |
| 2 | Arab-Israeli War COUP Saharan States | 29.55 | 4.00 | 41.85 | 0.00 | -16.00 | -0.30 | 0.00 | coup_target:Saharan States, milops_need:2, milops_urgency:2.00, coup_access_open, expected_swing:3.5, offside_ops_penalty |
| 3 | OPEC COUP Colombia | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Colombia, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 4 | OPEC COUP Cameroon | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Cameroon, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |
| 5 | OPEC COUP Mozambique | 8.90 | 4.00 | 25.35 | 0.00 | -20.00 | -0.45 | 0.00 | coup_target:Mozambique, milops_need:2, milops_urgency:2.00, empty_coup_penalty, expected_swing:4.5, offside_ops_penalty |

- effects: `VP +0, DEFCON +1, MilOps U-3/A-3`

## Step 75: T6 AR0 USSR

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], Cuban Missile Crisis[43], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Ussuri River Skirmish[77]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Marshall Plan [23] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Marshall Plan[23], Red Scare/Purge[31], Nuclear Subs[44], ABM Treaty[60], Camp David Accords[66], Latin American Death Squads[70], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 4 | Nuclear Subs EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Ussuri River Skirmish[77]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, France, West Germany | 45.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 45.94 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 3 | Arab-Israeli War INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 4 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |
| 5 | Junta INFLUENCE East Germany, West Germany | 30.54 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Red Scare/Purge [31] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Red Scare/Purge[31], Nuclear Subs[44], ABM Treaty[60], Camp David Accords[66], Latin American Death Squads[70], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge INFLUENCE West Germany, Brazil, Venezuela, South Africa | 68.89 | 6.00 | 70.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 2 | ABM Treaty INFLUENCE West Germany, Brazil, Venezuela, South Africa | 68.89 | 6.00 | 70.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Brazil:14.20, access_touch:Brazil, influence:Venezuela:14.20, access_touch:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 3 | Nuclear Subs INFLUENCE West Germany, South Africa | 36.79 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 4 | Camp David Accords INFLUENCE West Germany, South Africa | 36.79 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |
| 5 | Latin American Death Squads INFLUENCE West Germany, South Africa | 36.79 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Africa:16.80, non_coup_milops_penalty:6.86 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], How I Learned to Stop Worrying[49], Junta[50], John Paul II Elected Pope[69], Shuttle Diplomacy[74], Ussuri River Skirmish[77]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Algeria | 48.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:8.00 |
| 2 | Arab-Israeli War INFLUENCE West Germany, Algeria | 33.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:8.00 |
| 3 | How I Learned to Stop Worrying INFLUENCE West Germany, Algeria | 33.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:8.00 |
| 4 | Junta INFLUENCE West Germany, Algeria | 33.05 | 6.00 | 35.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, non_coup_milops_penalty:8.00 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, Algeria | 28.45 | 6.00 | 50.90 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `ABM Treaty [60] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Nuclear Subs[44], ABM Treaty[60], Camp David Accords[66], Latin American Death Squads[70], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty INFLUENCE Argentina, Brazil, Venezuela, South Africa | 70.80 | 6.00 | 73.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Argentina:16.20, access_touch:Argentina, influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, influence:South Africa:16.80, non_coup_milops_penalty:8.00 |
| 2 | Nuclear Subs INFLUENCE Brazil, Venezuela | 36.10 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 3 | Camp David Accords INFLUENCE Brazil, Venezuela | 36.10 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 4 | Latin American Death Squads INFLUENCE Brazil, Venezuela | 36.10 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |
| 5 | Voice of America INFLUENCE Brazil, Venezuela | 36.10 | 6.00 | 38.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Brazil:14.20, control_break:Brazil, influence:Venezuela:14.20, control_break:Venezuela, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Arab-Israeli War[13], How I Learned to Stop Worrying[49], Junta[50], John Paul II Elected Pope[69], Shuttle Diplomacy[74]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 2 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 3 | Junta INFLUENCE East Germany, West Germany | 27.80 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.60 |
| 4 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 23.20 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.60 |
| 5 | Blockade INFLUENCE West Germany | 12.40 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Nuclear Subs[44], Camp David Accords[66], Latin American Death Squads[70], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE West Germany, Argentina | 38.45 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:9.60 |
| 2 | Camp David Accords INFLUENCE West Germany, Argentina | 38.45 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:9.60 |
| 3 | Latin American Death Squads INFLUENCE West Germany, Argentina | 38.45 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:9.60 |
| 4 | Voice of America INFLUENCE West Germany, Argentina | 38.45 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:9.60 |
| 5 | One Small Step INFLUENCE West Germany, Argentina | 38.45 | 6.00 | 42.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Argentina:16.20, control_break:Argentina, non_coup_milops_penalty:9.60 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], How I Learned to Stop Worrying[49], Junta[50], John Paul II Elected Pope[69], Shuttle Diplomacy[74]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 25.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 2 | Junta INFLUENCE East Germany, West Germany | 25.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 20.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Blockade INFLUENCE West Germany | 10.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:12.00 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 9.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Camp David Accords[66], Latin American Death Squads[70], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE West Germany, South Korea | 33.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Korea:13.80, control_break:South Korea, non_coup_milops_penalty:12.00 |
| 2 | Latin American Death Squads INFLUENCE West Germany, South Korea | 33.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Korea:13.80, control_break:South Korea, non_coup_milops_penalty:12.00 |
| 3 | Voice of America INFLUENCE West Germany, South Korea | 33.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Korea:13.80, control_break:South Korea, non_coup_milops_penalty:12.00 |
| 4 | One Small Step INFLUENCE West Germany, South Korea | 33.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Korea:13.80, control_break:South Korea, non_coup_milops_penalty:12.00 |
| 5 | Socialist Governments INFLUENCE West Germany, South Korea, Chile | 32.30 | 6.00 | 58.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:South Korea:13.80, control_break:South Korea, influence:Chile:16.80, access_touch:Chile, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Junta [50] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], Junta[50], John Paul II Elected Pope[69], Shuttle Diplomacy[74]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, West Germany | 21.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 16.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Blockade INFLUENCE West Germany | 6.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:16.00 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 5.40 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | John Paul II Elected Pope SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Latin American Death Squads[70], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, Chile | 29.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:16.00 |
| 2 | Voice of America INFLUENCE West Germany, Chile | 29.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:16.00 |
| 3 | One Small Step INFLUENCE West Germany, Chile | 29.65 | 6.00 | 39.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, access_touch:Chile, non_coup_milops_penalty:16.00 |
| 4 | Socialist Governments INFLUENCE West Germany, Chile, South Africa | 26.30 | 6.00 | 56.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, access_touch:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Socialist Governments SPACE | -8.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], John Paul II Elected Pope[69], Shuttle Diplomacy[74]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | -9.20 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 2 | Blockade INFLUENCE West Germany | -20.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:42.00 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -20.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | John Paul II Elected Pope SPACE | -34.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Shuttle Diplomacy SPACE | -34.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Voice of America[75], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, Chile | 1.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:42.00 |
| 2 | One Small Step INFLUENCE West Germany, Chile | 1.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:42.00 |
| 3 | Socialist Governments INFLUENCE West Germany, Chile, South Africa | -1.70 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 4 | Socialist Governments SPACE | -34.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:42.00 |
| 5 | Voice of America REALIGN Chile | -36.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:42.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Blockade[10], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | -44.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:66.00 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -44.60 | 6.00 | 31.70 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | John Paul II Elected Pope SPACE | -58.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | Blockade REALIGN Mexico | -60.93 | -1.00 | 6.22 | 0.00 | 0.00 | -0.15 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:66.00 |
| 5 | Blockade EVENT | -63.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 90: T6 AR7 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], One Small Step[81]`
- state: `VP -1, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE West Germany, Chile | -17.35 | 6.00 | 42.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, non_coup_milops_penalty:66.00 |
| 2 | Socialist Governments INFLUENCE West Germany, Chile, South Africa | -20.70 | 6.00 | 59.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, control_break:Chile, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 3 | Socialist Governments SPACE | -58.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:66.00 |
| 4 | One Small Step REALIGN Chile | -60.06 | -1.00 | 7.24 | 0.00 | 0.00 | -0.30 | 0.00 | defcon2_realign_window, non_coup_milops_penalty:66.00 |
| 5 | One Small Step EVENT | -63.80 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 0.00 | non_coup_milops_penalty:66.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 91: T7 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], UN Intervention[32], Nuclear Test Ban[34], Kitchen Debates[51], Portuguese Empire Crumbles[55], South African Unrest[56], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Alliance for Progress[79]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Portuguese Empire Crumbles EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Liberation Theology EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Missile Envy [52] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Decolonization[30], Brush War[39], Missile Envy[52], Brezhnev Doctrine[54], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 3, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Our Man in Tehran EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 4 | Brush War EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Brezhnev Doctrine EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +1, DEFCON +2, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], UN Intervention[32], Kitchen Debates[51], Portuguese Empire Crumbles[55], South African Unrest[56], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Alliance for Progress[79]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, Indonesia | 30.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:8.00 |
| 2 | South African Unrest INFLUENCE West Germany, Indonesia | 30.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:8.00 |
| 3 | Liberation Theology INFLUENCE West Germany, Indonesia | 30.95 | 6.00 | 33.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, non_coup_milops_penalty:8.00 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Indonesia | 26.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Alliance for Progress INFLUENCE East Germany, West Germany, Indonesia | 26.35 | 6.00 | 48.80 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Indonesia:12.10, control_break:Indonesia, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Decolonization[30], Brush War[39], Brezhnev Doctrine[54], Our Man in Tehran[84]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE West Germany, Chile | 35.65 | 6.00 | 37.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, non_coup_milops_penalty:8.00 |
| 2 | Brush War INFLUENCE West Germany, Chile, South Africa | 32.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 3 | Brezhnev Doctrine INFLUENCE West Germany, Chile, South Africa | 32.30 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 4 | Vietnam Revolts INFLUENCE West Germany, Chile | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |
| 5 | Decolonization INFLUENCE West Germany, Chile | 19.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:8.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], UN Intervention[32], Kitchen Debates[51], South African Unrest[56], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Alliance for Progress[79]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | 28.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 2 | Liberation Theology INFLUENCE East Germany, West Germany | 28.07 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:9.33 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 23.47 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 23.47 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | Blockade INFLUENCE West Germany | 12.67 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Decolonization[30], Brush War[39], Brezhnev Doctrine[54]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE West Germany, Chile, South Africa | 30.97 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 2 | Brezhnev Doctrine INFLUENCE West Germany, Chile, South Africa | 30.97 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 3 | Vietnam Revolts INFLUENCE West Germany, Chile | 18.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 4 | Decolonization INFLUENCE West Germany, Chile | 18.32 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:9.33 |
| 5 | CIA Created INFLUENCE West Germany | 17.67 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:9.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], UN Intervention[32], Kitchen Debates[51], Liberation Theology[76], Ask Not What Your Country Can Do For You[78], Alliance for Progress[79]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 26.20 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 21.60 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 21.60 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | Blockade INFLUENCE West Germany | 10.80 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:11.20 |
| 5 | UN Intervention INFLUENCE West Germany | 10.80 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Decolonization[30], Brezhnev Doctrine[54]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE West Germany, Chile, South Africa | 29.10 | 6.00 | 54.75 | 0.00 | -20.00 | -0.45 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, influence:South Africa:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 2 | Vietnam Revolts INFLUENCE West Germany, Chile | 16.45 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 3 | Decolonization INFLUENCE West Germany, Chile | 16.45 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:11.20 |
| 4 | CIA Created INFLUENCE West Germany | 15.80 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:11.20 |
| 5 | Romanian Abdication INFLUENCE West Germany | 3.80 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.20 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], UN Intervention[32], Kitchen Debates[51], Ask Not What Your Country Can Do For You[78], Alliance for Progress[79]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 18.80 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | Blockade INFLUENCE West Germany | 8.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 4 | UN Intervention INFLUENCE West Germany | 8.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:14.00 |
| 5 | Kitchen Debates INFLUENCE West Germany | -4.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], CIA Created[26], Decolonization[30]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, Chile | 13.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 2 | Decolonization INFLUENCE West Germany, Chile | 13.65 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 3 | CIA Created INFLUENCE West Germany | 13.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:14.00 |
| 4 | Romanian Abdication INFLUENCE West Germany | 1.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.00 |
| 5 | Vietnam Revolts SPACE | -6.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:14.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], UN Intervention[32], Kitchen Debates[51], Alliance for Progress[79]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 14.13 | 6.00 | 47.25 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | Blockade INFLUENCE West Germany | 3.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.67 |
| 3 | UN Intervention INFLUENCE West Germany | 3.33 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:18.67 |
| 4 | Kitchen Debates INFLUENCE West Germany | -8.67 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | Alliance for Progress SPACE | -11.12 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12], CIA Created[26], Decolonization[30]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, Chile | 8.98 | 6.00 | 37.95 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.15, control_break:West Germany, influence:Chile:16.80, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 2 | CIA Created INFLUENCE West Germany | 8.33 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:18.67 |
| 3 | Romanian Abdication INFLUENCE West Germany | -3.67 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 4 | Decolonization SPACE | -10.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.67 |
| 5 | CIA Created REALIGN Chile | -14.58 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:18.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Blockade [10] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], UN Intervention[32], Kitchen Debates[51]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | -27.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:49.00 |
| 2 | UN Intervention INFLUENCE West Germany | -27.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:49.00 |
| 3 | Kitchen Debates INFLUENCE West Germany | -39.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 4 | Blockade REALIGN West Germany | -45.27 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:49.00 |
| 5 | UN Intervention REALIGN West Germany | -45.27 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Romanian Abdication[12], CIA Created[26]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE West Germany | -22.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, non_coup_milops_penalty:49.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -34.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:49.00 |
| 3 | CIA Created REALIGN Chile | -44.91 | -1.00 | 5.24 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:49.00 |
| 4 | CIA Created EVENT | -46.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:49.00 |
| 5 | Romanian Abdication EVENT | -55.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:49.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `UN Intervention[32], Kitchen Debates[51]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | -55.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15, non_coup_milops_penalty:77.00 |
| 2 | Kitchen Debates INFLUENCE West Germany | -67.00 | 6.00 | 16.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 3 | UN Intervention REALIGN West Germany | -73.27 | -1.00 | 4.88 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:77.00 |
| 4 | UN Intervention EVENT | -74.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:77.00 |
| 5 | Kitchen Debates EVENT | -83.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Romanian Abdication[12]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | -62.00 | 6.00 | 21.15 | 0.00 | -12.00 | -0.15 | 0.00 | influence:West Germany:16.15, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:77.00 |
| 2 | Romanian Abdication EVENT | -83.15 | 0.00 | 0.00 | -3.00 | -3.00 | -0.15 | 0.00 | offside_event, non_coup_milops_penalty:77.00 |
| 3 | Romanian Abdication REALIGN Chile | -84.91 | -1.00 | 5.24 | 0.00 | -12.00 | -0.15 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:77.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 107: T8 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Containment[25], Red Scare/Purge[31], Summit[48], John Paul II Elected Pope[69], Alliance for Progress[79], AWACS Sale to Saudis[107]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Duck and Cover EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], Nuclear Test Ban[34], Ask Not What Your Country Can Do For You[78], The Iron Lady[86], Iran-Contra Scandal[96], Tear Down this Wall[99]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Tear Down this Wall EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Containment[25], Summit[48], John Paul II Elected Pope[69], Alliance for Progress[79], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 45.91 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 2 | Arab-Israeli War INFLUENCE East Germany, West Germany | 29.76 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:9.14 |
| 3 | Duck and Cover INFLUENCE East Germany, France, West Germany | 25.91 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 4 | Containment INFLUENCE East Germany, France, West Germany | 25.91 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |
| 5 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 25.91 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], Ask Not What Your Country Can Do For You[78], The Iron Lady[86], Iran-Contra Scandal[96], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany | 34.61 | 6.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 2 | The Iron Lady INFLUENCE East Germany, West Germany | 34.61 | 6.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 3 | Tear Down this Wall INFLUENCE East Germany, West Germany | 34.61 | 6.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 4 | Truman Doctrine INFLUENCE West Germany | 18.61 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |
| 5 | CIA Created INFLUENCE West Germany | 18.61 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:9.14 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Nasser[15], Containment[25], John Paul II Elected Pope[69], Alliance for Progress[79], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 28.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.67 |
| 2 | Duck and Cover INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 3 | Containment INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 4 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |
| 5 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 24.38 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], The Iron Lady[86], Iran-Contra Scandal[96], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, West Germany | 33.08 | 6.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 2 | Tear Down this Wall INFLUENCE East Germany, West Germany | 33.08 | 6.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 3 | Truman Doctrine INFLUENCE West Germany | 17.08 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 4 | CIA Created INFLUENCE West Germany | 17.08 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.67 |
| 5 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 13.08 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:10.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Containment[25], John Paul II Elected Pope[69], Alliance for Progress[79], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 2 | Containment INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 3 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 22.25 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 10.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Tear Down this Wall [99] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], Iran-Contra Scandal[96], Tear Down this Wall[99]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Tear Down this Wall INFLUENCE East Germany, West Germany | 30.95 | 6.00 | 38.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 2 | Truman Doctrine INFLUENCE West Germany | 14.95 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 3 | CIA Created INFLUENCE West Germany | 14.95 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.80 |
| 4 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 10.95 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |
| 5 | De-Stalinization INFLUENCE East Germany, West Germany | 10.95 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], Containment[25], John Paul II Elected Pope[69], Alliance for Progress[79], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 19.05 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Nasser INFLUENCE West Germany | 6.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], Truman Doctrine[19], CIA Created[26], De-Stalinization[33], Iran-Contra Scandal[96]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE West Germany | 11.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 2 | CIA Created INFLUENCE West Germany | 11.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 7.75 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | De-Stalinization INFLUENCE East Germany, West Germany | 7.75 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | Iran-Contra Scandal INFLUENCE West Germany | -4.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], John Paul II Elected Pope[69], Alliance for Progress[79], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 13.72 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 13.72 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 1.57 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | Nasser INFLUENCE West Germany | 1.42 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:21.33 |
| 5 | John Paul II Elected Pope SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `De Gaulle Leads France[17], CIA Created[26], De-Stalinization[33], Iran-Contra Scandal[96]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE West Germany | 6.42 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:21.33 |
| 2 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 2.42 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 3 | De-Stalinization INFLUENCE East Germany, West Germany | 2.42 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 4 | Iran-Contra Scandal INFLUENCE West Germany | -9.73 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:21.33 |
| 5 | Iran-Contra Scandal SPACE | -13.63 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:21.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], John Paul II Elected Pope[69], AWACS Sale to Saudis[107]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | -20.95 | 6.00 | 49.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -33.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | Nasser INFLUENCE West Germany | -33.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:56.00 |
| 4 | John Paul II Elected Pope SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | AWACS Sale to Saudis SPACE | -48.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `De Gaulle Leads France[17], De-Stalinization[33], Iran-Contra Scandal[96]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany | -32.25 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 2 | De-Stalinization INFLUENCE East Germany, West Germany | -32.25 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 3 | Iran-Contra Scandal INFLUENCE West Germany | -44.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 4 | Iran-Contra Scandal SPACE | -48.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |
| 5 | De Gaulle Leads France SPACE | -48.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:56.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Nasser[15], John Paul II Elected Pope[69]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -65.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | Nasser INFLUENCE West Germany | -65.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:88.00 |
| 3 | John Paul II Elected Pope SPACE | -80.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 4 | Nasser REALIGN West Germany | -83.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |
| 5 | Nasser EVENT | -85.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `De-Stalinization[33], Iran-Contra Scandal[96]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, West Germany | -64.25 | 6.00 | 38.20 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 2 | Iran-Contra Scandal INFLUENCE West Germany | -76.40 | 6.00 | 21.90 | 0.00 | -16.00 | -0.30 | 0.00 | influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 3 | Iran-Contra Scandal SPACE | -80.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 4 | De-Stalinization SPACE | -80.45 | 1.00 | 2.00 | 0.00 | 5.00 | -0.45 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:88.00 |
| 5 | Iran-Contra Scandal EVENT | -94.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:88.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Independent Reds[22], Suez Crisis[28], East European Unrest[29], UN Intervention[32], Arms Race[42], We Will Bury You[53], Grain Sales to Soviets[68], Yuri and Samantha[106]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Yuri and Samantha EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Romanian Abdication EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], Olympic Games[20], Special Relationship[37], South African Unrest[56], Sadat Expels Soviets[73], Alliance for Progress[79], An Evil Empire[100], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | An Evil Empire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +3, DEFCON -1, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Independent Reds[22], Suez Crisis[28], UN Intervention[32], Arms Race[42], Grain Sales to Soviets[68], Yuri and Samantha[106]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 2 | Arms Race INFLUENCE East Germany, France, West Germany | 44.76 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 3 | Yuri and Samantha INFLUENCE East Germany, West Germany | 28.61 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:10.29 |
| 4 | Independent Reds INFLUENCE East Germany, West Germany | 12.61 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 12.61 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Olympic Games[20], Special Relationship[37], South African Unrest[56], Sadat Expels Soviets[73], Alliance for Progress[79], An Evil Empire[100], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 49.76 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.29 |
| 2 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 49.76 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.29 |
| 3 | An Evil Empire INFLUENCE East Germany, France, West Germany | 49.76 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.29 |
| 4 | Olympic Games INFLUENCE East Germany, West Germany | 33.61 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.29 |
| 5 | Special Relationship INFLUENCE East Germany, West Germany | 33.61 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:10.29 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Independent Reds[22], UN Intervention[32], Arms Race[42], Grain Sales to Soviets[68], Yuri and Samantha[106]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 43.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 2 | Yuri and Samantha INFLUENCE East Germany, West Germany | 26.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:12.00 |
| 3 | Independent Reds INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 10.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:12.00 |
| 5 | Romanian Abdication INFLUENCE West Germany | 10.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Olympic Games[20], Special Relationship[37], South African Unrest[56], Alliance for Progress[79], An Evil Empire[100], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, France, West Germany | 48.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 2 | An Evil Empire INFLUENCE East Germany, France, West Germany | 48.05 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 3 | Olympic Games INFLUENCE East Germany, West Germany | 31.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 4 | Special Relationship INFLUENCE East Germany, West Germany | 31.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:12.00 |
| 5 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 28.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:12.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Yuri and Samantha [106] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], Independent Reds[22], UN Intervention[32], Grain Sales to Soviets[68], Yuri and Samantha[106]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Yuri and Samantha INFLUENCE East Germany, West Germany | 24.50 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 2 | Independent Reds INFLUENCE East Germany, West Germany | 8.50 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 8.50 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 4 | Romanian Abdication INFLUENCE West Germany | 8.35 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |
| 5 | UN Intervention INFLUENCE West Germany | 8.35 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `An Evil Empire [100] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Olympic Games[20], Special Relationship[37], South African Unrest[56], An Evil Empire[100], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | An Evil Empire INFLUENCE East Germany, France, West Germany | 45.65 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:14.40 |
| 2 | Olympic Games INFLUENCE East Germany, West Germany | 29.50 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:14.40 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | 29.50 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:14.40 |
| 4 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 25.65 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |
| 5 | South African Unrest INFLUENCE East Germany, West Germany | 13.50 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:14.40 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], Independent Reds[22], UN Intervention[32], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 4.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 2 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 4.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 3 | Romanian Abdication INFLUENCE West Germany | 4.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 4 | UN Intervention INFLUENCE West Germany | 4.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:18.00 |
| 5 | Independent Reds SPACE | -10.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Olympic Games[20], Special Relationship[37], South African Unrest[56], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 25.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:18.00 |
| 2 | Special Relationship INFLUENCE East Germany, West Germany | 25.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:18.00 |
| 3 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 22.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 9.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 9.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:18.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Romanian Abdication[12], UN Intervention[32], Grain Sales to Soviets[68]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | -1.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 2 | Romanian Abdication INFLUENCE West Germany | -1.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 3 | UN Intervention INFLUENCE West Germany | -1.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:24.00 |
| 4 | Grain Sales to Soviets SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | Romanian Abdication REALIGN Morocco | -21.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Special Relationship[37], South African Unrest[56], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 19.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:24.00 |
| 2 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | 16.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | 3.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 3.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:24.00 |
| 5 | South African Unrest SPACE | -16.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:24.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Romanian Abdication[12], UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | -40.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 2 | UN Intervention INFLUENCE West Germany | -40.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:63.00 |
| 3 | Romanian Abdication REALIGN Morocco | -60.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:63.00 |
| 4 | UN Intervention REALIGN Morocco | -60.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:63.00 |
| 5 | Romanian Abdication EVENT | -60.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Aldrich Ames Remix [101] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `South African Unrest[56], Aldrich Ames Remix[101], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Aldrich Ames Remix INFLUENCE East Germany, France, West Germany | -22.95 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | -35.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | -35.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 4 | South African Unrest SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |
| 5 | Colonial Rear Guards SPACE | -55.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:63.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `UN Intervention[32]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE West Germany | -76.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:99.00 |
| 2 | UN Intervention REALIGN Morocco | -96.01 | -1.00 | 4.14 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |
| 3 | UN Intervention EVENT | -96.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `South African Unrest[56], Colonial Rear Guards[110]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | -71.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 2 | Colonial Rear Guards INFLUENCE East Germany, West Germany | -71.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 3 | South African Unrest SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 4 | Colonial Rear Guards SPACE | -91.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:99.00 |
| 5 | South African Unrest EVENT | -105.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:99.00 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Warsaw Pact Formed[16], Nuclear Test Ban[34], Brezhnev Doctrine[54], Muslim Revolution[59], OPEC[64], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Marine Barracks Bombing[91]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Warsaw Pact Formed EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Five Year Plan[5], Korean War[11], Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], Cultural Revolution[61], Latin American Death Squads[70], Sadat Expels Soviets[73], Iran-Iraq War[105]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Warsaw Pact Formed[16], Brezhnev Doctrine[54], OPEC[64], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 3 | OPEC INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 43.62 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |
| 5 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 27.47 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], Cultural Revolution[61], Latin American Death Squads[70], Sadat Expels Soviets[73], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 48.62 | 6.00 | 54.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 2 | Latin American Death Squads INFLUENCE East Germany, West Germany | 32.47 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 3 | Iran-Iraq War INFLUENCE East Germany, West Germany | 32.47 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:11.43 |
| 4 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 28.62 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |
| 5 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 28.62 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:11.43 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Brezhnev Doctrine[54], OPEC[64], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 41.72 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 4 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 25.57 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:13.33 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 9.57 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], Cultural Revolution[61], Latin American Death Squads[70], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE East Germany, West Germany | 30.57 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.33 |
| 2 | Iran-Iraq War INFLUENCE East Germany, West Germany | 30.57 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:13.33 |
| 3 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 26.72 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 4 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 26.72 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |
| 5 | Korean War INFLUENCE East Germany, West Germany | 14.57 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:13.33 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `OPEC[64], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 39.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 39.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 3 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 22.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:16.00 |
| 4 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 6.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | John Paul II Elected Pope SPACE | -8.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Korean War[11], Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], Cultural Revolution[61], Iran-Iraq War[105]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, West Germany | 27.90 | 6.00 | 38.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:16.00 |
| 2 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 3 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 24.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 4 | Korean War INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |
| 5 | South African Unrest INFLUENCE East Germany, West Germany | 11.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:16.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `John Paul II Elected Pope[69], Ussuri River Skirmish[77], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 35.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 2 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 18.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:20.00 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 2.90 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | John Paul II Elected Pope SPACE | -12.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | Marine Barracks Bombing REALIGN West Germany | -16.00 | -1.00 | 5.29 | 0.00 | 0.00 | -0.30 | 0.00 | non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Warsaw Pact Formed [16] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Korean War[11], Warsaw Pact Formed[16], CIA Created[26], South African Unrest[56], Cultural Revolution[61]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Warsaw Pact Formed INFLUENCE East Germany, France, West Germany | 20.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 2 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 20.05 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 3 | Korean War INFLUENCE East Germany, West Germany | 7.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 4 | South African Unrest INFLUENCE East Germany, West Germany | 7.90 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:20.00 |
| 5 | CIA Created INFLUENCE West Germany | 7.75 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:20.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Marine Barracks Bombing [91] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `John Paul II Elected Pope[69], Marine Barracks Bombing[91]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marine Barracks Bombing INFLUENCE East Germany, West Germany | 12.23 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, non_coup_milops_penalty:26.67 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -3.77 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | John Paul II Elected Pope SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | Marine Barracks Bombing REALIGN West Germany | -22.67 | -1.00 | 5.29 | 0.00 | 0.00 | -0.30 | 0.00 | non_coup_milops_penalty:26.67 |
| 5 | Marine Barracks Bombing EVENT | -24.47 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 0.00 | non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Korean War[11], CIA Created[26], South African Unrest[56], Cultural Revolution[61]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE East Germany, France, West Germany | 13.38 | 6.00 | 54.50 | 0.00 | -20.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 2 | Korean War INFLUENCE East Germany, West Germany | 1.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 3 | South African Unrest INFLUENCE East Germany, West Germany | 1.23 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:26.67 |
| 4 | CIA Created INFLUENCE West Germany | 1.08 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:26.67 |
| 5 | Korean War SPACE | -18.97 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:26.67 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `John Paul II Elected Pope[69]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | -47.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | John Paul II Elected Pope SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | John Paul II Elected Pope EVENT | -76.30 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 0.00 | offside_event, non_coup_milops_penalty:70.00 |
| 4 | John Paul II Elected Pope REALIGN West Germany | -82.00 | -1.00 | 5.29 | 0.00 | -16.00 | -0.30 | 0.00 | offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Korean War[11], CIA Created[26], South African Unrest[56]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | -42.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 2 | South African Unrest INFLUENCE East Germany, West Germany | -42.10 | 6.00 | 38.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, control_break:West Germany, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 3 | CIA Created INFLUENCE West Germany | -42.25 | 6.00 | 21.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, control_break:West Germany, non_coup_milops_penalty:70.00 |
| 4 | Korean War SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |
| 5 | South African Unrest SPACE | -62.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:70.00 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `CIA Created[26], South African Unrest[56]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE East Germany, West Germany | -87.10 | 6.00 | 33.20 | 0.00 | -16.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 2 | CIA Created INFLUENCE West Germany | -87.25 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90, non_coup_milops_penalty:110.00 |
| 3 | South African Unrest SPACE | -102.30 | 1.00 | 2.00 | 0.00 | 5.00 | -0.30 | 0.00 | space_offside_disposal, offside_ops_penalty, non_coup_milops_penalty:110.00 |
| 4 | CIA Created REALIGN West Germany | -105.86 | -1.00 | 5.29 | 0.00 | 0.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |
| 5 | CIA Created EVENT | -107.65 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 0.00 | non_coup_milops_penalty:110.00 |

- effects: `VP -11, DEFCON +0, MilOps U+0/A+0`
