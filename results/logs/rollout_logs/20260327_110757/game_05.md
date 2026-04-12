# minimal_hybrid detailed rollout log

- seed: `20260414`
- winner: `USSR`
- final_vp: `6`
- end_turn: `10`
- end_reason: `turn_limit`

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

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15], Captured Nazi Scientist[18], Marshall Plan[23], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, Japan, South Korea, Thailand | 79.20 | 6.00 | 73.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, Thailand, Thailand | 78.88 | 6.00 | 73.47 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand |
| 3 | Marshall Plan INFLUENCE Japan, South Korea, Thailand, Thailand | 78.78 | 6.00 | 73.38 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand |
| 4 | Marshall Plan INFLUENCE West Germany, Japan, Israel, Thailand | 78.55 | 6.00 | 73.15 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, access_touch:Thailand |
| 5 | Marshall Plan INFLUENCE Japan, South Korea, Israel, Thailand | 78.45 | 6.00 | 73.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 4: T1 AR1 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], De Gaulle Leads France[17], Indo-Pakistani War[24], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE West Germany, Iran, Indonesia, Philippines | 84.70 | 6.00 | 79.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 2 | De-Stalinization INFLUENCE West Germany, Iran, Indonesia, Philippines | 84.70 | 6.00 | 79.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 3 | De Gaulle Leads France INFLUENCE Turkey, West Germany, Indonesia, Philippines | 83.45 | 6.00 | 77.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 4 | De-Stalinization INFLUENCE Turkey, West Germany, Indonesia, Philippines | 83.45 | 6.00 | 77.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 5 | De Gaulle Leads France INFLUENCE West Germany, North Korea, Indonesia, Philippines | 83.05 | 6.00 | 77.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55, access_touch:North Korea, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15], Captured Nazi Scientist[18], East European Unrest[29], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE Japan, Israel, Thailand | 63.55 | 6.00 | 58.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 2 | NORAD INFLUENCE Japan, Israel, Thailand | 63.55 | 6.00 | 58.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 3 | East European Unrest INFLUENCE Italy, Israel, Thailand | 63.35 | 6.00 | 57.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 4 | East European Unrest INFLUENCE Israel, Philippines, Thailand | 63.35 | 6.00 | 57.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, control_break:Thailand |
| 5 | NORAD INFLUENCE Italy, Israel, Thailand | 63.35 | 6.00 | 57.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], De-Stalinization[33], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, Turkey, North Korea | 73.15 | 6.00 | 67.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea |
| 2 | De-Stalinization INFLUENCE East Germany, Turkey, North Korea, Pakistan | 73.05 | 6.00 | 67.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Pakistan:14.95, access_touch:Pakistan |
| 3 | De-Stalinization INFLUENCE France, Turkey, North Korea, Pakistan | 73.05 | 6.00 | 67.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Pakistan:14.95, access_touch:Pakistan |
| 4 | De-Stalinization INFLUENCE East Germany, Turkey, North Korea, Panama | 72.80 | 6.00 | 67.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama |
| 5 | De-Stalinization INFLUENCE France, Turkey, North Korea, Panama | 72.80 | 6.00 | 67.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Panama:11.20, control_break:Panama |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `NORAD [38] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Vietnam Revolts[9], Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, North Korea, Thailand | 66.60 | 6.00 | 61.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 2 | NORAD INFLUENCE Japan, North Korea, Thailand | 62.70 | 6.00 | 57.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 3 | NORAD INFLUENCE Italy, North Korea, Thailand | 62.50 | 6.00 | 56.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 4 | NORAD INFLUENCE North Korea, Philippines, Thailand | 62.50 | 6.00 | 56.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 5 | NORAD INFLUENCE North Korea, Saudi Arabia, Thailand | 62.35 | 6.00 | 56.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Pakistan, Panama | 54.50 | 6.00 | 48.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |
| 2 | Indo-Pakistani War INFLUENCE Japan, Pakistan, Panama | 54.50 | 6.00 | 48.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |
| 3 | Special Relationship INFLUENCE Japan, Pakistan, Panama | 54.50 | 6.00 | 48.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |
| 4 | Arab-Israeli War INFLUENCE Italy, Pakistan, Panama | 54.30 | 6.00 | 48.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |
| 5 | Indo-Pakistani War INFLUENCE Italy, Pakistan, Panama | 54.30 | 6.00 | 48.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Formosan Resolution INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Vietnam Revolts INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |
| 4 | Vietnam Revolts INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 5 | Formosan Resolution INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Indo-Pakistani War[24], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE India, Japan, Pakistan | 58.85 | 6.00 | 53.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan |
| 2 | Special Relationship INFLUENCE India, Japan, Pakistan | 58.85 | 6.00 | 53.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan |
| 3 | Indo-Pakistani War INFLUENCE Italy, India, Pakistan | 58.65 | 6.00 | 52.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan |
| 4 | Special Relationship INFLUENCE Italy, India, Pakistan | 58.65 | 6.00 | 52.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan |
| 5 | Indo-Pakistani War INFLUENCE India, Pakistan, Iraq | 58.50 | 6.00 | 52.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan, influence:Iraq:14.30, access_touch:Iraq |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], Captured Nazi Scientist[18], Formosan Resolution[35]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Formosan Resolution INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |
| 3 | Formosan Resolution INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 4 | Formosan Resolution INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 5 | Formosan Resolution INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Blockade[10], Romanian Abdication[12], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Italy, Japan, Iraq | 53.60 | 6.00 | 47.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq |
| 2 | Special Relationship INFLUENCE Italy, West Germany, Japan | 53.45 | 6.00 | 47.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | Special Relationship INFLUENCE Italy, India, Japan | 53.35 | 6.00 | 47.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:India:15.55, influence:Japan:16.15 |
| 4 | Special Relationship INFLUENCE Italy, Japan, North Korea | 53.35 | 6.00 | 47.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:North Korea:15.55 |
| 5 | Special Relationship INFLUENCE Italy, Japan, South Korea | 53.35 | 6.00 | 47.65 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:1`
- hand: `Nasser[15], Captured Nazi Scientist[18]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:1 |
| 2 | Captured Nazi Scientist COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:1 |
| 3 | Nasser INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | Nasser INFLUENCE Iraq | 25.15 | 6.00 | 19.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Iraq:14.30, control_break:Iraq |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 14: T1 AR6 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12]`
- state: `VP 0, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE Italy, Japan | 41.45 | 6.00 | 35.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15 |
| 2 | Romanian Abdication INFLUENCE Italy, Japan | 41.45 | 6.00 | 35.60 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15 |
| 3 | Blockade INFLUENCE Italy, Saudi Arabia | 41.10 | 6.00 | 35.25 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 4 | Romanian Abdication INFLUENCE Italy, Saudi Arabia | 41.10 | 6.00 | 35.25 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | Blockade INFLUENCE Italy, West Germany | 40.95 | 6.00 | 35.10 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], Red Scare/Purge[31], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP 1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], US/Japan Mutual Defense Pact[27], Decolonization[30], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE Japan, Iraq, Philippines, Thailand | 77.25 | 6.00 | 71.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 2 | Nuclear Test Ban INFLUENCE Japan, Iraq, Philippines, Thailand | 77.25 | 6.00 | 71.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE Italy, Japan, Iraq, Thailand | 77.25 | 6.00 | 71.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45 |
| 4 | Nuclear Test Ban INFLUENCE Italy, Japan, Iraq, Thailand | 77.25 | 6.00 | 71.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE Japan, Iraq, Saudi Arabia, Thailand | 77.10 | 6.00 | 71.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Five Year Plan[5], COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Philippines | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 2 | COMECON INFLUENCE Japan, Philippines | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 3 | Suez Crisis INFLUENCE Japan, Philippines | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 4 | Five Year Plan INFLUENCE Saudi Arabia, Philippines | 40.80 | 6.00 | 35.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines |
| 5 | COMECON INFLUENCE Saudi Arabia, Philippines | 40.80 | 6.00 | 35.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, control_break:Philippines |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Nuclear Test Ban [34] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], Decolonization[30], Nuclear Test Ban[34], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban INFLUENCE Italy, Japan, Saudi Arabia, Thailand | 73.75 | 6.00 | 68.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 2 | Nuclear Test Ban INFLUENCE Italy, West Germany, Japan, Thailand | 73.60 | 6.00 | 68.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Nuclear Test Ban INFLUENCE Italy, Japan, North Korea, Thailand | 73.50 | 6.00 | 68.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 4 | Nuclear Test Ban INFLUENCE Italy, Japan, South Korea, Thailand | 73.50 | 6.00 | 68.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |
| 5 | Nuclear Test Ban INFLUENCE West Germany, Japan, Saudi Arabia, Thailand | 73.45 | 6.00 | 68.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `COMECON[14], Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE Italy, Japan | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15 |
| 2 | Suez Crisis INFLUENCE Italy, Japan | 41.15 | 6.00 | 35.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Japan:16.15 |
| 3 | COMECON INFLUENCE Italy, Saudi Arabia | 40.80 | 6.00 | 35.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 4 | Suez Crisis INFLUENCE Italy, Saudi Arabia | 40.80 | 6.00 | 35.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | COMECON INFLUENCE Italy, West Germany | 40.65 | 6.00 | 35.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, control_break:Italy, influence:West Germany:15.65 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Fidel[8], Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Socialist Governments INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 3 | Socialist Governments INFLUENCE Japan, South Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |
| 4 | Socialist Governments INFLUENCE Japan, Indonesia, Thailand | 57.50 | 6.00 | 51.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |
| 5 | Socialist Governments INFLUENCE Japan, Egypt, Thailand | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Truman Doctrine[19], Olympic Games[20], Independent Reds[22], Suez Crisis[28], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan | 42.35 | 6.00 | 36.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Japan:16.15 |
| 2 | Suez Crisis INFLUENCE West Germany, Saudi Arabia | 42.00 | 6.00 | 36.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 3 | Suez Crisis INFLUENCE West Germany, India | 41.75 | 6.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:India:15.55 |
| 4 | Suez Crisis INFLUENCE West Germany, North Korea | 41.75 | 6.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:North Korea:15.55 |
| 5 | Suez Crisis INFLUENCE West Germany, South Korea | 41.75 | 6.00 | 36.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Fidel [8] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Fidel[8], Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 5 | Fidel INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `Olympic Games [20] as COUP`
- flags: `milops_shortfall:2`
- hand: `Truman Doctrine[19], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games COUP Japan | 24.35 | 4.00 | 20.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2 |
| 2 | Independent Reds COUP Japan | 24.35 | 4.00 | 20.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2 |
| 3 | Olympic Games COUP India | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:India, battleground_coup, milops_need:2 |
| 4 | Olympic Games COUP North Korea | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2 |
| 5 | Olympic Games COUP South Korea | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:2 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 25: T2 AR5 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Korean War[11], Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Korean War INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 5 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Truman Doctrine [19] as INFLUENCE`
- flags: `none`
- hand: `Truman Doctrine[19], Independent Reds[22], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Truman Doctrine INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 3 | Independent Reds INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 4 | Truman Doctrine INFLUENCE Saudi Arabia | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | UN Intervention INFLUENCE Saudi Arabia | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Decolonization[30], The Cambridge Five[36]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 5 | Decolonization INFLUENCE North Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 28: T2 AR6 US

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `none`
- hand: `Independent Reds[22], UN Intervention[32]`
- state: `VP 1, DEFCON 3, MilOps U0/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | Independent Reds INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 3 | UN Intervention INFLUENCE Saudi Arabia | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 4 | Independent Reds INFLUENCE Saudi Arabia | 21.50 | 6.00 | 15.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | UN Intervention INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65 |

- effects: `VP -2, DEFCON +1, MilOps U+0/A-2`

## Step 29: T3 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Olympic Games[20], NATO[21], Independent Reds[22], Marshall Plan[23], CIA Created[26], Decolonization[30], De-Stalinization[33]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | NATO EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `US/Japan Mutual Defense Pact [27] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Socialist Governments[7], COMECON[14], Captured Nazi Scientist[18], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Formosan Resolution EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], NATO[21], Independent Reds[22], Marshall Plan[23], CIA Created[26], Decolonization[30]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE Italy, Japan, Saudi Arabia, Thailand | 73.75 | 6.00 | 68.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 2 | Marshall Plan INFLUENCE Italy, Japan, Saudi Arabia, Thailand | 73.75 | 6.00 | 68.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 3 | NATO INFLUENCE Italy, West Germany, Japan, Thailand | 73.60 | 6.00 | 68.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Marshall Plan INFLUENCE Italy, West Germany, Japan, Thailand | 73.60 | 6.00 | 68.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 5 | NATO INFLUENCE Italy, Japan, North Korea, Thailand | 73.50 | 6.00 | 68.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Socialist Governments[7], COMECON[14], Captured Nazi Scientist[18], Indo-Pakistani War[24], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE West Germany, Japan, Saudi Arabia | 58.15 | 6.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 2 | COMECON INFLUENCE West Germany, Japan, Saudi Arabia | 58.15 | 6.00 | 52.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 3 | Socialist Governments INFLUENCE India, Japan, Saudi Arabia | 58.05 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, control_break:Japan, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 4 | Socialist Governments INFLUENCE Japan, North Korea, Saudi Arabia | 58.05 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | Socialist Governments INFLUENCE Japan, South Korea, Saudi Arabia | 58.05 | 6.00 | 52.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], Independent Reds[22], Marshall Plan[23], CIA Created[26], Decolonization[30]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, Japan, North Korea, Thailand | 73.20 | 6.00 | 67.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 2 | Marshall Plan INFLUENCE West Germany, Japan, South Korea, Thailand | 73.20 | 6.00 | 67.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |
| 3 | Marshall Plan INFLUENCE Japan, North Korea, South Korea, Thailand | 73.10 | 6.00 | 67.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:South Korea:15.55, influence:Thailand:20.45 |
| 4 | Marshall Plan INFLUENCE West Germany, Japan, Indonesia, Thailand | 73.00 | 6.00 | 67.60 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |
| 5 | Marshall Plan INFLUENCE Japan, North Korea, Indonesia, Thailand | 72.90 | 6.00 | 67.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `COMECON[14], Captured Nazi Scientist[18], Indo-Pakistani War[24], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, India, Japan | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15, control_break:Japan |
| 2 | COMECON INFLUENCE West Germany, Japan, North Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55 |
| 3 | COMECON INFLUENCE West Germany, Japan, South Korea | 57.90 | 6.00 | 52.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55 |
| 4 | COMECON INFLUENCE India, Japan, North Korea | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55 |
| 5 | COMECON INFLUENCE India, Japan, South Korea | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Olympic Games[20], Independent Reds[22], CIA Created[26], Decolonization[30]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 3 | Five Year Plan INFLUENCE Japan, South Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |
| 4 | Five Year Plan INFLUENCE Japan, Indonesia, Thailand | 57.50 | 6.00 | 51.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |
| 5 | Five Year Plan INFLUENCE Japan, Egypt, Thailand | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Indo-Pakistani War[24], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE India, Japan | 47.40 | 6.00 | 41.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, control_break:Japan |
| 2 | Formosan Resolution INFLUENCE India, Japan | 47.40 | 6.00 | 41.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, control_break:Japan |
| 3 | Special Relationship INFLUENCE India, Japan | 47.40 | 6.00 | 41.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15, control_break:Japan |
| 4 | Indo-Pakistani War INFLUENCE West Germany, Japan | 42.50 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan |
| 5 | Formosan Resolution INFLUENCE West Germany, Japan | 42.50 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Olympic Games[20], Independent Reds[22], CIA Created[26], Decolonization[30]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Independent Reds INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Olympic Games INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 5 | Independent Reds INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], Formosan Resolution[35], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, Japan | 42.50 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan |
| 2 | Special Relationship INFLUENCE West Germany, Japan | 42.50 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan |
| 3 | Formosan Resolution INFLUENCE India, Japan | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, influence:Japan:16.15, control_break:Japan |
| 4 | Formosan Resolution INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55 |
| 5 | Formosan Resolution INFLUENCE Japan, South Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Independent Reds[22], CIA Created[26], Decolonization[30]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Independent Reds INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 4 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 5 | Independent Reds INFLUENCE North Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 40: T3 AR5 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], UN Intervention[32], Special Relationship[37]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, Japan | 42.50 | 6.00 | 36.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, control_break:Japan |
| 2 | Special Relationship INFLUENCE India, Japan | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, influence:Japan:16.15, control_break:Japan |
| 3 | Special Relationship INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:North Korea:15.55 |
| 4 | Special Relationship INFLUENCE Japan, South Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:South Korea:15.55 |
| 5 | Special Relationship INFLUENCE Japan, Egypt | 42.05 | 6.00 | 36.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, control_break:Japan, influence:Egypt:13.70, access_touch:Egypt |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 41: T3 AR6 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `CIA Created[26], Decolonization[30]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE North Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45 |
| 4 | Decolonization INFLUENCE South Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, influence:Thailand:20.45 |
| 5 | Decolonization INFLUENCE Indonesia, Thailand | 41.50 | 6.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Japan | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 2 | UN Intervention INFLUENCE Japan | 27.00 | 6.00 | 21.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15, control_break:Japan |
| 3 | Captured Nazi Scientist COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3 |
| 4 | UN Intervention COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3 |
| 5 | Captured Nazi Scientist COUP India | 22.90 | 4.00 | 19.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:India, battleground_coup, milops_need:3 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 43: T4 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Duck and Cover[4], COMECON[14], Nasser[15], Marshall Plan[23], Decolonization[30], Arms Race[42], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Nasser EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `NATO [21] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], NATO[21], Independent Reds[22], CIA Created[26], SALT Negotiations[46], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Latin American Death Squads EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Marshall Plan[23], Decolonization[30], Arms Race[42], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE West Germany, Mexico, Algeria, South Africa | 72.00 | 6.00 | 66.60 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, access_touch:South Africa |
| 2 | Marshall Plan INFLUENCE UK, West Germany, Mexico, South Africa | 71.95 | 6.00 | 66.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, access_touch:South Africa |
| 3 | Marshall Plan INFLUENCE East Germany, West Germany, Mexico, South Africa | 71.85 | 6.00 | 66.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, access_touch:South Africa |
| 4 | Marshall Plan INFLUENCE France, West Germany, Mexico, South Africa | 71.85 | 6.00 | 66.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80, access_touch:South Africa |
| 5 | Marshall Plan INFLUENCE UK, Mexico, Algeria, South Africa | 71.50 | 6.00 | 66.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, access_touch:South Africa |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Korean War[11], Romanian Abdication[12], Independent Reds[22], CIA Created[26], SALT Negotiations[46], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE West Germany, Mexico, South Africa | 54.95 | 6.00 | 49.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80 |
| 2 | SALT Negotiations INFLUENCE Mexico, Algeria, South Africa | 54.50 | 6.00 | 48.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 3 | SALT Negotiations INFLUENCE East Germany, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80 |
| 4 | SALT Negotiations INFLUENCE France, Mexico, South Africa | 54.35 | 6.00 | 48.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80 |
| 5 | SALT Negotiations INFLUENCE West Germany, Algeria, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Nasser[15], Decolonization[30], Arms Race[42], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Algeria, Morocco, South Africa | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 2 | Arms Race INFLUENCE Algeria, Morocco, South Africa | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 3 | Bear Trap INFLUENCE Algeria, Morocco, South Africa | 57.85 | 6.00 | 52.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 4 | Duck and Cover INFLUENCE West Germany, Algeria, South Africa | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |
| 5 | Arms Race INFLUENCE West Germany, Algeria, South Africa | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], Independent Reds[22], CIA Created[26], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Latin American Death Squads INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Korean War INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Decolonization[30], Arms Race[42], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE UK, West Germany, South Africa | 54.15 | 6.00 | 48.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Bear Trap INFLUENCE UK, West Germany, South Africa | 54.15 | 6.00 | 48.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Arms Race INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Arms Race INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], Independent Reds[22], CIA Created[26], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80 |
| 2 | Latin American Death Squads INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80 |
| 3 | Colonial Rear Guards INFLUENCE UK, South Africa | 41.65 | 6.00 | 35.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:South Africa:16.80 |
| 4 | Independent Reds INFLUENCE UK, West Germany | 41.00 | 6.00 | 35.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15 |
| 5 | Latin American Death Squads INFLUENCE UK, West Germany | 41.00 | 6.00 | 35.30 | 0.00 | 0.00 | -0.30 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Decolonization[30], Bear Trap[47], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Bear Trap INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Bear Trap INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 4 | Bear Trap INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |
| 5 | Bear Trap INFLUENCE Italy, West Germany, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `Latin American Death Squads [70] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Romanian Abdication[12], CIA Created[26], Allende[57], Latin American Death Squads[70], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Death Squads INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Latin American Death Squads INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 4 | Colonial Rear Guards INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 5 | Latin American Death Squads INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Decolonization[30], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Decolonization INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Decolonization INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], CIA Created[26], Allende[57], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Colonial Rear Guards INFLUENCE Algeria, South Africa | 38.20 | 6.00 | 32.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Colonial Rear Guards INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Colonial Rear Guards INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Nasser[15], Kitchen Debates[51], Lonely Hearts Club Band[65]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Lonely Hearts Club Band INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Lonely Hearts Club Band INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Lonely Hearts Club Band INFLUENCE Italy, South Africa | 37.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `Romanian Abdication [12] as COUP`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Romanian Abdication[12], CIA Created[26], Allende[57]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 2 | CIA Created COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 3 | Allende COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 4 | Romanian Abdication COUP West Germany | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:4 |
| 5 | CIA Created COUP West Germany | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:4 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+1`

## Step 57: T4 AR7 USSR

- chosen: `Nasser [15] as COUP`
- flags: `holds_china, milops_shortfall:4`
- hand: `Nasser[15], Kitchen Debates[51]`
- state: `VP -1, DEFCON 4, MilOps U0/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 2 | Kitchen Debates COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 3 | Nasser INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 4 | Kitchen Debates INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 5 | Nasser COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:4 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 58: T4 AR7 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `CIA Created[26], Allende[57]`
- state: `VP -1, DEFCON 3, MilOps U1/A1, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 2 | Allende INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 3 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 4 | Allende INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 5 | CIA Created COUP South Africa | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:3, defcon_penalty:3 |

- effects: `VP +0, DEFCON +1, MilOps U-1/A-1`

## Step 59: T5 AR0 USSR

- chosen: `Brush War [39] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `NATO[21], Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Brush War[39], Cuban Missile Crisis[43], Brezhnev Doctrine[54], Puppet Governments[67], Our Man in Tehran[84]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Five Year Plan [5] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Five Year Plan[5], Fidel[8], Arab-Israeli War[13], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Suez Crisis[28], Cultural Revolution[61], OPEC[64]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | Suez Crisis EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `NATO[21], Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Cuban Missile Crisis[43], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, France, West Germany, South Africa | 69.45 | 6.00 | 64.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | NATO INFLUENCE East Germany, West Germany, Cuba, South Africa | 68.95 | 6.00 | 63.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 3 | NATO INFLUENCE France, West Germany, Cuba, South Africa | 68.95 | 6.00 | 63.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 4 | NATO INFLUENCE East Germany, Italy, West Germany, South Africa | 68.85 | 6.00 | 63.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | NATO INFLUENCE East Germany, West Germany, Mexico, South Africa | 68.85 | 6.00 | 63.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Suez Crisis[28], Cultural Revolution[61], OPEC[64]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Algeria, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 2 | Cultural Revolution INFLUENCE West Germany, Algeria, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 3 | OPEC INFLUENCE West Germany, Algeria, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 4 | Suez Crisis INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Suez Crisis INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Cuban Missile Crisis[43], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE West Germany, Algeria, South Africa | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |
| 2 | Brezhnev Doctrine INFLUENCE West Germany, Algeria, South Africa | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |
| 3 | Cuban Missile Crisis INFLUENCE East Germany, Algeria, South Africa | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |
| 4 | Cuban Missile Crisis INFLUENCE France, Algeria, South Africa | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |
| 5 | Brezhnev Doctrine INFLUENCE East Germany, Algeria, South Africa | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Cultural Revolution [61] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Cultural Revolution[61], OPEC[64]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cultural Revolution INFLUENCE West Germany, Morocco, South Africa | 54.80 | 6.00 | 49.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 2 | OPEC INFLUENCE West Germany, Morocco, South Africa | 54.80 | 6.00 | 49.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 3 | Cultural Revolution INFLUENCE East Germany, Morocco, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 4 | Cultural Revolution INFLUENCE France, Morocco, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 5 | OPEC INFLUENCE East Germany, Morocco, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Brezhnev Doctrine[54], Puppet Governments[67]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Brezhnev Doctrine INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Brezhnev Doctrine INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 4 | Brezhnev Doctrine INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |
| 5 | Brezhnev Doctrine INFLUENCE Italy, West Germany, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `OPEC [64] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], OPEC[64]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | OPEC INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | OPEC INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | OPEC INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | OPEC INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Indo-Pakistani War[24], UN Intervention[32], The Cambridge Five[36], Puppet Governments[67]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | The Cambridge Five INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Puppet Governments INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Indo-Pakistani War INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | Indo-Pakistani War INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 68: T5 AR4 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Fidel[8], Arab-Israeli War[13], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Arab-Israeli War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Olympic Games INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Fidel INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `UN Intervention[32], The Cambridge Five[36], Puppet Governments[67]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Puppet Governments INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | The Cambridge Five INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | The Cambridge Five INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Puppet Governments INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Olympic Games INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Arab-Israeli War INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | Arab-Israeli War INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `UN Intervention[32], Puppet Governments[67]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Puppet Governments INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Puppet Governments INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Puppet Governments INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Puppet Governments INFLUENCE Italy, South Africa | 37.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Olympic Games INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Olympic Games INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Independent Reds INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `UN Intervention [32] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `UN Intervention[32]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5 |
| 2 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 3 | UN Intervention COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:5 |
| 4 | UN Intervention COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:5 |
| 5 | UN Intervention INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 74: T5 AR7 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], Independent Reds[22]`
- state: `VP -1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Independent Reds INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Independent Reds INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Independent Reds INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |
| 5 | Independent Reds INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 75: T6 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Quagmire[45], We Will Bury You[53], Muslim Revolution[59], Voice of America[75], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Blockade[10], Nuclear Test Ban[34], Junta[50], Willy Brandt[58], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79]`
- state: `VP 0, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Alliance for Progress EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Camp David Accords EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | OAS Founded EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +1, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Marshall Plan[23], Quagmire[45], Muslim Revolution[59], Voice of America[75], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, West Germany, South Africa | 69.45 | 6.00 | 64.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Muslim Revolution INFLUENCE East Germany, France, West Germany, South Africa | 69.45 | 6.00 | 64.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Marshall Plan INFLUENCE East Germany, West Germany, Cuba, South Africa | 68.95 | 6.00 | 63.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 4 | Marshall Plan INFLUENCE France, West Germany, Cuba, South Africa | 68.95 | 6.00 | 63.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Muslim Revolution INFLUENCE East Germany, West Germany, Cuba, South Africa | 68.95 | 6.00 | 63.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Blockade[10], Junta[50], Willy Brandt[58], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Socialist Governments INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Socialist Governments INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Quagmire[45], Muslim Revolution[59], Voice of America[75], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, West Germany, South Africa | 74.45 | 6.00 | 69.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Muslim Revolution INFLUENCE France, West Germany, Cuba, South Africa | 73.95 | 6.00 | 68.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 3 | Muslim Revolution INFLUENCE France, Italy, West Germany, South Africa | 73.85 | 6.00 | 68.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, control_break:France, influence:Italy:14.95, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Muslim Revolution INFLUENCE France, West Germany, Mexico, South Africa | 73.85 | 6.00 | 68.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Mexico:14.95, influence:South Africa:16.80 |
| 5 | Muslim Revolution INFLUENCE France, West Germany, Morocco, South Africa | 73.70 | 6.00 | 68.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Morocco:14.80, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Alliance for Progress [79] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Vietnam Revolts[9], Blockade[10], Junta[50], Willy Brandt[58], Camp David Accords[66], OAS Founded[71], Alliance for Progress[79]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Alliance for Progress INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Alliance for Progress INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Alliance for Progress INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Alliance for Progress INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Alliance for Progress INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Quagmire[45], Voice of America[75], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Quagmire INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Ussuri River Skirmish INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Quagmire INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], Junta[50], Willy Brandt[58], Camp David Accords[66], OAS Founded[71]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Junta INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Willy Brandt INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Camp David Accords INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Vietnam Revolts INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Voice of America[75], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Ussuri River Skirmish INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Ussuri River Skirmish INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |
| 5 | Ussuri River Skirmish INFLUENCE Italy, West Germany, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Junta[50], Willy Brandt[58], Camp David Accords[66], OAS Founded[71]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Willy Brandt INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Camp David Accords INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Junta INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | Junta INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Olympic Games INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Olympic Games INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], Willy Brandt[58], Camp David Accords[66], OAS Founded[71]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Camp David Accords INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Willy Brandt INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Willy Brandt INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Camp David Accords INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `Voice of America [75] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Voice of America[75], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Voice of America INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Voice of America INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Voice of America INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Voice of America INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Voice of America INFLUENCE Italy, South Africa | 37.45 | 6.00 | 31.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Camp David Accords [66] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Blockade[10], Camp David Accords[66], OAS Founded[71]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Camp David Accords INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Camp David Accords INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Camp David Accords INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Camp David Accords INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |
| 5 | Camp David Accords INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Captured Nazi Scientist[18], Panama Canal Returned[111]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:6 |
| 2 | Panama Canal Returned COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:6 |
| 3 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 4 | Panama Canal Returned INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 5 | Captured Nazi Scientist COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 90: T6 AR7 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Blockade[10], OAS Founded[71]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE South Africa | 27.65 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa |
| 2 | OAS Founded INFLUENCE South Africa | 27.65 | 6.00 | 21.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80, control_break:South Africa |
| 3 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 4 | OAS Founded INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 5 | Blockade COUP South Africa | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:6, defcon_penalty:3 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 91: T7 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], Decolonization[30], UN Intervention[32], Special Relationship[37], Nuclear Subs[44], Summit[48], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | South African Unrest EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:7`
- hand: `Indo-Pakistani War[24], Red Scare/Purge[31], Formosan Resolution[35], NORAD[38], Flower Power[62], U2 Incident[63], Sadat Expels Soviets[73], Shuttle Diplomacy[74], Lone Gunman[109]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Shuttle Diplomacy EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Indo-Pakistani War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Five Year Plan[5], Decolonization[30], UN Intervention[32], Special Relationship[37], Nuclear Subs[44], Summit[48], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Summit INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Five Year Plan INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Five Year Plan INFLUENCE France, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Summit INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Indo-Pakistani War[24], Formosan Resolution[35], NORAD[38], Flower Power[62], U2 Incident[63], Sadat Expels Soviets[73], Shuttle Diplomacy[74], Lone Gunman[109]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE France, West Germany, South Africa | 60.55 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 2 | U2 Incident INFLUENCE France, West Germany, South Africa | 60.55 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 3 | Sadat Expels Soviets INFLUENCE France, West Germany, South Africa | 60.55 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 4 | Shuttle Diplomacy INFLUENCE France, West Germany, South Africa | 60.55 | 6.00 | 55.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, access_touch:France, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 5 | NORAD INFLUENCE East Germany, France, South Africa | 59.95 | 6.00 | 54.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, access_touch:France, influence:South Africa:16.80, control_break:South Africa |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Decolonization[30], UN Intervention[32], Special Relationship[37], Nuclear Subs[44], Summit[48], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE West Germany, South Africa | 38.50 | 6.00 | 32.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Summit INFLUENCE East Germany, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Summit INFLUENCE France, South Africa | 37.90 | 6.00 | 32.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Summit INFLUENCE Cuba, South Africa | 37.40 | 6.00 | 31.85 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Summit INFLUENCE Italy, South Africa | 37.30 | 6.00 | 31.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Indo-Pakistani War[24], Formosan Resolution[35], Flower Power[62], U2 Incident[63], Sadat Expels Soviets[73], Shuttle Diplomacy[74], Lone Gunman[109]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 2 | U2 Incident INFLUENCE France, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 4 | Sadat Expels Soviets INFLUENCE France, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Decolonization[30], UN Intervention[32], Special Relationship[37], Nuclear Subs[44], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP South Africa | 25.00 | 4.00 | 21.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:7 |
| 2 | Special Relationship COUP South Africa | 25.00 | 4.00 | 21.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:7 |
| 3 | Nuclear Subs COUP South Africa | 25.00 | 4.00 | 21.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:7 |
| 4 | South African Unrest COUP South Africa | 25.00 | 4.00 | 21.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:7 |
| 5 | Nixon Plays the China Card COUP South Africa | 25.00 | 4.00 | 21.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:7 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 98: T7 AR3 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Indo-Pakistani War[24], Formosan Resolution[35], Flower Power[62], Sadat Expels Soviets[73], Shuttle Diplomacy[74], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Sadat Expels Soviets INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Shuttle Diplomacy INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Sadat Expels Soviets INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `UN Intervention [32] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `UN Intervention[32], Special Relationship[37], Nuclear Subs[44], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | UN Intervention INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 2 | Special Relationship INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 3 | Nuclear Subs INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 4 | South African Unrest INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 5 | Nixon Plays the China Card INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Indo-Pakistani War[24], Formosan Resolution[35], Flower Power[62], Shuttle Diplomacy[74], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Shuttle Diplomacy INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Shuttle Diplomacy INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Shuttle Diplomacy INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Shuttle Diplomacy INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Special Relationship[37], Nuclear Subs[44], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 2 | Nuclear Subs INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 3 | South African Unrest INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 4 | Nixon Plays the China Card INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 5 | Special Relationship COUP South Africa | 22.50 | 4.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Indo-Pakistani War[24], Formosan Resolution[35], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Formosan Resolution INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Flower Power INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Indo-Pakistani War INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | Indo-Pakistani War INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Nuclear Subs[44], South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 2 | South African Unrest INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 3 | Nixon Plays the China Card INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 4 | Nuclear Subs COUP South Africa | 22.50 | 4.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5, defcon_penalty:3 |
| 5 | South African Unrest COUP South Africa | 22.50 | 4.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5, defcon_penalty:3 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Formosan Resolution [35] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Formosan Resolution[35], Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Formosan Resolution INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Flower Power INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Formosan Resolution INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Formosan Resolution INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Flower Power INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `South African Unrest[56], Nixon Plays the China Card[72]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 2 | Nixon Plays the China Card INFLUENCE South Africa | 22.50 | 6.00 | 16.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Africa:16.80 |
| 3 | South African Unrest COUP South Africa | 22.50 | 4.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5, defcon_penalty:3 |
| 4 | Nixon Plays the China Card COUP South Africa | 22.50 | 4.00 | 18.80 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5, defcon_penalty:3 |
| 5 | South African Unrest INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 106: T7 AR7 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Flower Power[62], Lone Gunman[109]`
- state: `VP 2, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Flower Power INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Flower Power INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Flower Power INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |
| 5 | Flower Power INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 107: T8 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `Olympic Games[20], NATO[21], East European Unrest[29], Decolonization[30], Arms Race[42], Willy Brandt[58], Muslim Revolution[59], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Willy Brandt EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `Junta [50] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Junta[50], Allende[57], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 2 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 3 | Vietnam Revolts EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |
| 4 | Arab-Israeli War EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |
| 5 | Colonial Rear Guards EVENT | -4.80 | 0.00 | 0.00 | -3.00 | -3.00 | -0.30 | 1.50 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `NATO [21] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Olympic Games[20], NATO[21], East European Unrest[29], Decolonization[30], Arms Race[42], Willy Brandt[58], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO INFLUENCE East Germany, France, Italy, West Germany | 70.60 | 6.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | NATO INFLUENCE East Germany, France, West Germany, Cuba | 70.45 | 6.00 | 65.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 3 | NATO INFLUENCE East Germany, France, Turkey, West Germany | 70.10 | 6.00 | 64.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |
| 4 | NATO INFLUENCE East Germany, Italy, West Germany, Cuba | 69.85 | 6.00 | 64.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | NATO INFLUENCE France, Italy, West Germany, Cuba | 69.85 | 6.00 | 64.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Vietnam Revolts[9], Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Allende[57], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE Italy, South Africa | 45.20 | 6.00 | 39.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:South Africa:13.80, control_break:South Africa |
| 2 | Arab-Israeli War INFLUENCE Italy, South Africa | 45.20 | 6.00 | 39.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:South Africa:13.80, control_break:South Africa |
| 3 | Iran-Iraq War INFLUENCE Italy, South Africa | 45.20 | 6.00 | 39.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:South Africa:13.80, control_break:South Africa |
| 4 | Colonial Rear Guards INFLUENCE Italy, South Africa | 45.20 | 6.00 | 39.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:South Africa:13.80, control_break:South Africa |
| 5 | Vietnam Revolts INFLUENCE Italy, West Germany | 43.30 | 6.00 | 37.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Olympic Games[20], East European Unrest[29], Decolonization[30], Arms Race[42], Willy Brandt[58], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Arms Race INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | East European Unrest INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | East European Unrest INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Arab-Israeli War[13], Allende[57], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Olympic Games[20], Decolonization[30], Arms Race[42], Willy Brandt[58], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Arms Race INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Arms Race INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Romanian Abdication[12], Allende[57], Iran-Iraq War[105], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Iran-Iraq War INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Olympic Games[20], Decolonization[30], Willy Brandt[58], Latin American Death Squads[70], Ask Not What Your Country Can Do For You[78]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Allende[57], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Colonial Rear Guards INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 5 | Colonial Rear Guards INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Olympic Games[20], Decolonization[30], Willy Brandt[58], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Olympic Games INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Decolonization INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Decolonization INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Blockade [10] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Romanian Abdication[12], Allende[57]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 2 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 3 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 4 | Blockade INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |
| 5 | Blockade INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Decolonization[30], Willy Brandt[58], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Decolonization INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Willy Brandt INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Latin American Death Squads INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `Romanian Abdication [12] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Romanian Abdication[12], Allende[57]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 2 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 3 | Romanian Abdication INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |
| 4 | Romanian Abdication INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30 |
| 5 | Allende INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `Willy Brandt[58], Latin American Death Squads[70]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Willy Brandt INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Latin American Death Squads INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Latin American Death Squads INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Willy Brandt INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Allende [57] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Allende[57]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Allende INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 2 | Allende INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |
| 3 | Allende INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30 |
| 4 | Allende INFLUENCE Poland | 21.65 | 6.00 | 15.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Poland:14.30, access_touch:Poland |
| 5 | Allende INFLUENCE Italy | 21.55 | 6.00 | 15.70 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Italy:15.70 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `Suez Crisis [28] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Captured Nazi Scientist[18], Suez Crisis[28], Brush War[39], Quagmire[45], OPEC[64], Nixon Plays the China Card[72]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], ABM Treaty[60], Flower Power[62], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], North Sea Oil[89], AWACS Sale to Saudis[107], Colonial Rear Guards[110]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | North Sea Oil EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | AWACS Sale to Saudis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Duck and Cover[4], Arab-Israeli War[13], Captured Nazi Scientist[18], Brush War[39], Quagmire[45], OPEC[64], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE East Germany, West Germany, Algeria | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria |
| 2 | Duck and Cover INFLUENCE France, West Germany, Algeria | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria |
| 3 | Brush War INFLUENCE East Germany, West Germany, Algeria | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria |
| 4 | Brush War INFLUENCE France, West Germany, Algeria | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria |
| 5 | Quagmire INFLUENCE East Germany, West Germany, Algeria | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Algeria:13.20, control_break:Algeria |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], Flower Power[62], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], North Sea Oil[89], AWACS Sale to Saudis[107], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 56.55 | 6.00 | 51.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 56.55 | 6.00 | 51.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90 |
| 3 | North Sea Oil INFLUENCE France, Poland, West Germany | 56.05 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | AWACS Sale to Saudis INFLUENCE France, Poland, West Germany | 56.05 | 6.00 | 50.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 5 | North Sea Oil INFLUENCE France, Italy, West Germany | 55.95 | 6.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, access_touch:France, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Brush War[39], Quagmire[45], OPEC[64], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Quagmire INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | Brush War INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Brush War INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Fidel[8], Flower Power[62], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], AWACS Sale to Saudis[107], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 3 | AWACS Sale to Saudis INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | AWACS Sale to Saudis INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Quagmire[45], OPEC[64], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Quagmire INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Quagmire INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | OPEC INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Fidel[8], Flower Power[62], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Fidel INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Flower Power INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], OPEC[64], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | OPEC INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | OPEC INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | OPEC INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | OPEC INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Flower Power[62], Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Flower Power INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Lonely Hearts Club Band INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Arab-Israeli War[13], Captured Nazi Scientist[18], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Nixon Plays the China Card INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Arab-Israeli War INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Lonely Hearts Club Band[65], John Paul II Elected Pope[69], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Lonely Hearts Club Band INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | John Paul II Elected Pope INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Nixon Plays the China Card[72]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Nixon Plays the China Card INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 4 | Nixon Plays the China Card INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Nixon Plays the China Card INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `John Paul II Elected Pope[69], Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | John Paul II Elected Pope INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | John Paul II Elected Pope INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:9`
- hand: `Captured Nazi Scientist[18]`
- state: `VP 3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP East Germany | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:East Germany, battleground_coup, milops_need:9 |
| 2 | Captured Nazi Scientist COUP France | 23.65 | 4.00 | 19.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:France, battleground_coup, milops_need:9 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 4 | Captured Nazi Scientist COUP UK | 22.25 | 4.00 | 18.40 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:UK, battleground_coup, milops_need:9 |
| 5 | Captured Nazi Scientist INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 138: T9 AR7 US

- chosen: `Colonial Rear Guards [110] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Colonial Rear Guards[110]`
- state: `VP 3, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Colonial Rear Guards INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Colonial Rear Guards INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | Colonial Rear Guards INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 5 | Colonial Rear Guards INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Glasnost [93] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Independent Reds[22], The Cambridge Five[36], Summit[48], Liberation Theology[76], Ussuri River Skirmish[77], Glasnost[93], Wargames[103], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Glasnost EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Wargames EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Cuban Missile Crisis [43] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], The Cambridge Five[36], Cuban Missile Crisis[43], Bear Trap[47], Willy Brandt[58], Muslim Revolution[59], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Grain Sales to Soviets EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON -3, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Wargames [103] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Independent Reds[22], The Cambridge Five[36], Summit[48], Liberation Theology[76], Ussuri River Skirmish[77], Wargames[103], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Wargames INFLUENCE East Germany, France, Italy, West Germany | 70.60 | 6.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Wargames INFLUENCE East Germany, France, West Germany, Cuba | 70.45 | 6.00 | 65.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 3 | Wargames INFLUENCE East Germany, France, Turkey, West Germany | 70.10 | 6.00 | 64.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |
| 4 | Wargames INFLUENCE East Germany, Italy, West Germany, Cuba | 69.85 | 6.00 | 64.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Wargames INFLUENCE France, Italy, West Germany, Cuba | 69.85 | 6.00 | 64.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Olympic Games[20], The Cambridge Five[36], Bear Trap[47], Willy Brandt[58], Muslim Revolution[59], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Italy, West Germany | 75.60 | 6.00 | 70.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |
| 2 | Muslim Revolution INFLUENCE East Germany, Italy, Poland, West Germany | 75.10 | 6.00 | 69.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, control_break:Italy, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 3 | Muslim Revolution INFLUENCE France, Italy, Poland, West Germany | 75.10 | 6.00 | 69.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, control_break:Italy, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | Muslim Revolution INFLUENCE East Germany, Italy, West Germany, Cuba | 74.85 | 6.00 | 69.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Muslim Revolution INFLUENCE France, Italy, West Germany, Cuba | 74.85 | 6.00 | 69.45 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Independent Reds[22], The Cambridge Five[36], Summit[48], Liberation Theology[76], Ussuri River Skirmish[77], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Summit INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Summit INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], The Cambridge Five[36], Bear Trap[47], Willy Brandt[58], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Bear Trap INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | Bear Trap INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Independent Reds[22], The Cambridge Five[36], Liberation Theology[76], Ussuri River Skirmish[77], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Ussuri River Skirmish INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Ussuri River Skirmish INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Sadat Expels Soviets[73], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 3 | Sadat Expels Soviets INFLUENCE France, Poland, West Germany | 54.55 | 6.00 | 49.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Sadat Expels Soviets INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Independent Reds[22], The Cambridge Five[36], Liberation Theology[76], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Independent Reds INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Olympic Games[20], The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Olympic Games INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `The Cambridge Five[36], Liberation Theology[76], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Liberation Theology INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `The Cambridge Five[36], Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Willy Brandt INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Liberation Theology[76], Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Liberation Theology INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Solidarity INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Liberation Theology INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Willy Brandt[58], Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Willy Brandt INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Grain Sales to Soviets INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Willy Brandt INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Solidarity [104] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Solidarity[104], Panama Canal Returned[111]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Solidarity INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Solidarity INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 4 | Solidarity INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Solidarity INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Grain Sales to Soviets[68], Lone Gunman[109]`
- state: `VP 6, DEFCON 2, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Grain Sales to Soviets INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Grain Sales to Soviets INFLUENCE Poland, West Germany | 38.40 | 6.00 | 32.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:14.30, access_touch:Poland, influence:West Germany:16.90 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 5 | Grain Sales to Soviets INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`
