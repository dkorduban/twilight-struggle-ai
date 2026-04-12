# minimal_hybrid detailed rollout log

- seed: `20260410`
- winner: `USSR`
- final_vp: `1`
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

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Romanian Abdication[12], Indo-Pakistani War[24], US/Japan Mutual Defense Pact[27], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, South Korea, Thailand | 79.20 | 6.00 | 73.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand |
| 2 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Thailand, Thailand | 78.88 | 6.00 | 73.47 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand |
| 3 | US/Japan Mutual Defense Pact INFLUENCE Japan, South Korea, Thailand, Thailand | 78.78 | 6.00 | 73.38 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Thailand:20.45, access_touch:Thailand, influence:Thailand:10.22, control_break:Thailand, access_touch:Thailand |
| 4 | US/Japan Mutual Defense Pact INFLUENCE West Germany, Japan, Israel, Thailand | 78.55 | 6.00 | 73.15 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, access_touch:West Germany, influence:Japan:16.15, access_touch:Japan, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, access_touch:Thailand |
| 5 | US/Japan Mutual Defense Pact INFLUENCE Japan, South Korea, Israel, Thailand | 78.45 | 6.00 | 73.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, access_touch:Japan, influence:South Korea:15.55, access_touch:South Korea, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, access_touch:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 4: T1 AR1 US

- chosen: `COMECON [14] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], COMECON[14], Nasser[15], CIA Created[26], Suez Crisis[28], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Indonesia, Philippines | 66.00 | 6.00 | 60.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 2 | Suez Crisis INFLUENCE West Germany, Indonesia, Philippines | 66.00 | 6.00 | 60.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 3 | De-Stalinization INFLUENCE West Germany, Indonesia, Philippines | 66.00 | 6.00 | 60.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia, influence:Philippines:14.45, control_break:Philippines |
| 4 | COMECON INFLUENCE West Germany, Iran, Indonesia | 65.25 | 6.00 | 59.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |
| 5 | Suez Crisis INFLUENCE West Germany, Iran, Indonesia | 65.25 | 6.00 | 59.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, control_break:West Germany, influence:Iran:13.70, control_break:Iran, influence:Indonesia:13.85, control_break:Indonesia, access_touch:Indonesia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 5: T1 AR2 USSR

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1, offside_ops_play`
- hand: `Duck and Cover[4], Vietnam Revolts[9], Romanian Abdication[12], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE Japan, Israel, Thailand | 63.55 | 6.00 | 58.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 2 | Duck and Cover INFLUENCE Italy, Israel, Thailand | 63.35 | 6.00 | 57.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Israel:14.90, access_touch:Israel, influence:Thailand:20.45, control_break:Thailand |
| 3 | Duck and Cover INFLUENCE Israel, Philippines, Thailand | 63.35 | 6.00 | 57.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45, control_break:Thailand |
| 4 | Duck and Cover INFLUENCE Israel, Saudi Arabia, Thailand | 63.20 | 6.00 | 57.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Israel:14.90, access_touch:Israel, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45, control_break:Thailand |
| 5 | Duck and Cover INFLUENCE Italy, Japan, Thailand | 63.10 | 6.00 | 57.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Thailand:20.45, control_break:Thailand |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 6: T1 AR2 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], CIA Created[26], Suez Crisis[28], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE Turkey, North Korea, Iran | 58.75 | 6.00 | 53.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran |
| 2 | De-Stalinization INFLUENCE Turkey, North Korea, Iran | 58.75 | 6.00 | 53.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Turkey:12.45, control_break:Turkey, influence:North Korea:15.55, access_touch:North Korea, influence:Iran:13.70, control_break:Iran |
| 3 | Suez Crisis INFLUENCE East Germany, Turkey, Iran | 58.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:Iran:13.70, control_break:Iran |
| 4 | Suez Crisis INFLUENCE France, Turkey, Iran | 58.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Turkey:12.45, control_break:Turkey, influence:Iran:13.70, control_break:Iran |
| 5 | De-Stalinization INFLUENCE East Germany, Turkey, Iran | 58.25 | 6.00 | 52.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Turkey:12.45, control_break:Turkey, influence:Iran:13.70, control_break:Iran |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 7: T1 AR3 USSR

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Vietnam Revolts[9], Romanian Abdication[12], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 2 | Indo-Pakistani War INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE North Korea, Thailand | 46.70 | 6.00 | 41.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, control_break:North Korea, influence:Thailand:20.45 |
| 5 | Vietnam Revolts INFLUENCE Japan, North Korea | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, control_break:North Korea |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 8: T1 AR3 US

- chosen: `De-Stalinization [33] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], CIA Created[26], De-Stalinization[33]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization INFLUENCE East Germany, France, Pakistan | 55.10 | 6.00 | 49.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Pakistan:14.95, access_touch:Pakistan |
| 2 | De-Stalinization INFLUENCE East Germany, France, Panama | 54.85 | 6.00 | 49.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Panama:11.20, control_break:Panama |
| 3 | De-Stalinization INFLUENCE East Germany, France, Japan | 54.80 | 6.00 | 49.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:France:15.05, access_touch:France, influence:Japan:16.15 |
| 4 | De-Stalinization INFLUENCE East Germany, Pakistan, Panama | 54.75 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.05, access_touch:East Germany, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |
| 5 | De-Stalinization INFLUENCE France, Pakistan, Panama | 54.75 | 6.00 | 49.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.05, access_touch:France, influence:Pakistan:14.95, access_touch:Pakistan, influence:Panama:11.20, control_break:Panama |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 9: T1 AR4 USSR

- chosen: `Indo-Pakistani War [24] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Indo-Pakistani War[24], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Indo-Pakistani War INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 2 | Decolonization INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE East Germany, Thailand | 46.20 | 6.00 | 40.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.05, control_break:East Germany, influence:Thailand:20.45 |
| 4 | Indo-Pakistani War INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 5 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 10: T1 AR4 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Korean War[11], Arab-Israeli War[13], Nasser[15], CIA Created[26]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE India, Pakistan | 42.70 | 6.00 | 37.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan |
| 2 | Arab-Israeli War INFLUENCE India, Pakistan | 42.70 | 6.00 | 37.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, access_touch:India, influence:Pakistan:14.95, control_break:Pakistan |
| 3 | Korean War INFLUENCE Pakistan, Panama | 41.85 | 6.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Panama:11.20, control_break:Panama |
| 4 | Arab-Israeli War INFLUENCE Pakistan, Panama | 41.85 | 6.00 | 36.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Pakistan:14.95, control_break:Pakistan, influence:Panama:11.20, control_break:Panama |
| 5 | Korean War INFLUENCE Japan, Pakistan | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Pakistan:14.95, control_break:Pakistan |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 11: T1 AR5 USSR

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Decolonization INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |
| 4 | Decolonization INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 5 | The Cambridge Five INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 12: T1 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Arab-Israeli War[13], Nasser[15], CIA Created[26]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE Japan, Panama | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Panama:11.20, control_break:Panama |
| 2 | Arab-Israeli War INFLUENCE Italy, Panama | 37.85 | 6.00 | 32.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Panama:11.20, control_break:Panama |
| 3 | Arab-Israeli War INFLUENCE Italy, Japan | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15 |
| 4 | Arab-Israeli War INFLUENCE Iraq, Panama | 37.70 | 6.00 | 32.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:14.30, access_touch:Iraq, influence:Panama:11.20, control_break:Panama |
| 5 | Arab-Israeli War INFLUENCE Japan, Iraq | 37.65 | 6.00 | 31.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 13: T1 AR6 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:1`
- hand: `Romanian Abdication[12], The Cambridge Five[36]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | The Cambridge Five INFLUENCE Italy, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Thailand:20.45 |
| 3 | The Cambridge Five INFLUENCE Philippines, Thailand | 42.10 | 6.00 | 36.40 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 4 | The Cambridge Five INFLUENCE Saudi Arabia, Thailand | 41.95 | 6.00 | 36.25 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 5 | The Cambridge Five INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 14: T1 AR6 US

- chosen: `Nasser [15] as COUP`
- flags: `milops_shortfall:1, offside_ops_play`
- hand: `Nasser[15], CIA Created[26]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nasser COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1 |
| 2 | CIA Created COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:1 |
| 3 | Nasser COUP West Germany | 23.00 | 4.00 | 19.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:1 |
| 4 | CIA Created COUP West Germany | 23.00 | 4.00 | 19.15 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:1 |
| 5 | Nasser COUP India | 22.90 | 4.00 | 19.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:India, battleground_coup, milops_need:1 |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 15: T2 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:2`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Marshall Plan[23], UN Intervention[32], Nuclear Test Ban[34]`
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

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
- state: `VP -1, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NATO EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Truman Doctrine EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +3, DEFCON +0, MilOps U+0/A+0`

## Step 17: T2 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], Marshall Plan[23], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE Italy, Japan, Philippines, Thailand | 73.90 | 6.00 | 68.50 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 2 | Marshall Plan INFLUENCE Italy, Japan, Saudi Arabia, Thailand | 73.75 | 6.00 | 68.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 3 | Marshall Plan INFLUENCE Japan, Saudi Arabia, Philippines, Thailand | 73.75 | 6.00 | 68.35 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |
| 4 | Marshall Plan INFLUENCE Italy, West Germany, Japan, Thailand | 73.60 | 6.00 | 68.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 5 | Marshall Plan INFLUENCE West Germany, Japan, Philippines, Thailand | 73.60 | 6.00 | 68.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Philippines:14.45, access_touch:Philippines, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 18: T2 AR1 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Blockade[10], De Gaulle Leads France[17], Truman Doctrine[19], Containment[25], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE Italy, Japan, Philippines | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 2 | Containment INFLUENCE Italy, Japan, Philippines | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 3 | East European Unrest INFLUENCE Italy, Japan, Philippines | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 4 | NORAD INFLUENCE Italy, Japan, Philippines | 57.10 | 6.00 | 51.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.45, access_touch:Italy, influence:Japan:16.15, influence:Philippines:14.45, control_break:Philippines |
| 5 | De Gaulle Leads France INFLUENCE Japan, Iraq, Philippines | 56.95 | 6.00 | 51.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq, influence:Philippines:14.45, control_break:Philippines |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 19: T2 AR2 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Five Year Plan[5], Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 2 | Socialist Governments INFLUENCE Japan, Saudi Arabia, Thailand | 57.95 | 6.00 | 52.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia, influence:Thailand:20.45 |
| 3 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Socialist Governments INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 5 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 20: T2 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Truman Doctrine[19], Containment[25], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Japan, Iraq | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq |
| 2 | East European Unrest INFLUENCE West Germany, Japan, Iraq | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq |
| 3 | NORAD INFLUENCE West Germany, Japan, Iraq | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq |
| 4 | Containment INFLUENCE India, Japan, Iraq | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Iraq:14.30, access_touch:Iraq |
| 5 | Containment INFLUENCE Japan, North Korea, Iraq | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Iraq:14.30, access_touch:Iraq |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 21: T2 AR3 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Socialist Governments[7], Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE Japan, Iraq, Thailand | 61.45 | 6.00 | 55.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45 |
| 2 | Socialist Governments INFLUENCE West Germany, Iraq, Thailand | 60.95 | 6.00 | 55.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45 |
| 3 | Socialist Governments INFLUENCE North Korea, Iraq, Thailand | 60.85 | 6.00 | 55.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:North Korea:15.55, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45 |
| 4 | Socialist Governments INFLUENCE South Korea, Iraq, Thailand | 60.85 | 6.00 | 55.30 | 0.00 | 0.00 | -0.45 | 0.00 | influence:South Korea:15.55, influence:Iraq:14.30, control_break:Iraq, influence:Thailand:20.45 |
| 5 | Socialist Governments INFLUENCE Iraq, Indonesia, Thailand | 60.65 | 6.00 | 55.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Iraq:14.30, control_break:Iraq, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 22: T2 AR3 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Truman Doctrine[19], East European Unrest[29], NORAD[38]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan, Saudi Arabia | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 2 | NORAD INFLUENCE West Germany, Japan, Saudi Arabia | 53.15 | 6.00 | 47.60 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 3 | East European Unrest INFLUENCE India, Japan, Saudi Arabia | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 4 | East European Unrest INFLUENCE Japan, North Korea, Saudi Arabia | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |
| 5 | East European Unrest INFLUENCE Japan, South Korea, Saudi Arabia | 53.05 | 6.00 | 47.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Saudi Arabia:14.30, access_touch:Saudi Arabia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 23: T2 AR4 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], Olympic Games[20], Independent Reds[22], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Independent Reds INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Olympic Games INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 4 | Independent Reds INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 5 | Olympic Games INFLUENCE North Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 24: T2 AR4 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:2`
- hand: `Fidel[8], Blockade[10], Truman Doctrine[19], NORAD[38]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, India, Japan | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:India:15.55, influence:Japan:16.15 |
| 2 | NORAD INFLUENCE West Germany, Japan, North Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:North Korea:15.55 |
| 3 | NORAD INFLUENCE West Germany, Japan, South Korea | 52.90 | 6.00 | 47.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:South Korea:15.55 |
| 4 | NORAD INFLUENCE India, Japan, North Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:North Korea:15.55 |
| 5 | NORAD INFLUENCE India, Japan, South Korea | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 25: T2 AR5 USSR

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Independent Reds[22], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Independent Reds INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 3 | Independent Reds INFLUENCE North Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45 |
| 4 | Independent Reds INFLUENCE South Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, influence:Thailand:20.45 |
| 5 | Independent Reds INFLUENCE Indonesia, Thailand | 41.50 | 6.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 26: T2 AR5 US

- chosen: `Fidel [8] as INFLUENCE`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Fidel[8], Blockade[10], Truman Doctrine[19]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Fidel INFLUENCE India, Japan | 42.40 | 6.00 | 36.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Japan:16.15 |
| 2 | Fidel INFLUENCE West Germany, India | 41.90 | 6.00 | 36.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:India:15.55, control_break:India |
| 3 | Fidel INFLUENCE India, North Korea | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:North Korea:15.55 |
| 4 | Fidel INFLUENCE India, South Korea | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:South Korea:15.55 |
| 5 | Fidel INFLUENCE India, Egypt | 41.45 | 6.00 | 35.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:India:15.55, control_break:India, influence:Egypt:13.70, access_touch:Egypt |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 27: T2 AR6 USSR

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `holds_china, milops_shortfall:2`
- hand: `Captured Nazi Scientist[18], UN Intervention[32]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:2 |
| 2 | UN Intervention COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:2 |
| 3 | Captured Nazi Scientist INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 4 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | Captured Nazi Scientist COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 28: T2 AR6 US

- chosen: `Blockade [10] as COUP`
- flags: `milops_shortfall:2, offside_ops_play`
- hand: `Blockade[10], Truman Doctrine[19]`
- state: `VP 2, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2 |
| 2 | Truman Doctrine COUP Japan | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Japan, battleground_coup, milops_need:2 |
| 3 | Blockade COUP India | 22.90 | 4.00 | 19.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:India, battleground_coup, milops_need:2 |
| 4 | Blockade COUP North Korea | 22.90 | 4.00 | 19.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:2 |
| 5 | Blockade COUP South Korea | 22.90 | 4.00 | 19.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:2 |

- effects: `VP +0, DEFCON +0, MilOps U-1/A+0`

## Step 29: T3 AR0 USSR

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `holds_china, milops_shortfall:3`
- hand: `Five Year Plan[5], Blockade[10], COMECON[14], CIA Created[26], Suez Crisis[28], Red Scare/Purge[31], UN Intervention[32], Special Relationship[37]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Blockade EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | UN Intervention EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 30: T3 AR0 US

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Containment[25], East European Unrest[29], Decolonization[30], Nuclear Test Ban[34], The Cambridge Five[36], NORAD[38]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |

- effects: `VP -2, DEFCON +1, MilOps U+0/A+0`

## Step 31: T3 AR1 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Five Year Plan[5], Blockade[10], COMECON[14], CIA Created[26], Suez Crisis[28], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | COMECON INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 4 | Five Year Plan INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 5 | Five Year Plan INFLUENCE Japan, South Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 32: T3 AR1 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Containment[25], East European Unrest[29], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | Containment INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | East European Unrest INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 4 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 5 | Duck and Cover INFLUENCE India, Japan | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 33: T3 AR2 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], COMECON[14], CIA Created[26], Suez Crisis[28], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 3 | COMECON INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 4 | COMECON INFLUENCE Japan, South Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |
| 5 | Suez Crisis INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 34: T3 AR2 US

- chosen: `Containment [25] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Containment[25], East European Unrest[29], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | East European Unrest INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 4 | Containment INFLUENCE India, Japan | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15 |
| 5 | Containment INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 35: T3 AR3 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], CIA Created[26], Suez Crisis[28], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Japan, Thailand | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Suez Crisis INFLUENCE Japan, North Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55, influence:Thailand:20.45 |
| 3 | Suez Crisis INFLUENCE Japan, South Korea, Thailand | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55, influence:Thailand:20.45 |
| 4 | Suez Crisis INFLUENCE Japan, Indonesia, Thailand | 57.50 | 6.00 | 51.95 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |
| 5 | Suez Crisis INFLUENCE Japan, Egypt, Thailand | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 36: T3 AR3 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 3 | East European Unrest INFLUENCE India, Japan | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15 |
| 4 | East European Unrest INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |
| 5 | East European Unrest INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 37: T3 AR4 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Blockade[10], CIA Created[26], UN Intervention[32], Special Relationship[37]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE Japan, Thailand | 42.30 | 6.00 | 36.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15, influence:Thailand:20.45 |
| 2 | Special Relationship INFLUENCE West Germany, Thailand | 41.80 | 6.00 | 36.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:15.65, influence:Thailand:20.45 |
| 3 | Special Relationship INFLUENCE North Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:North Korea:15.55, influence:Thailand:20.45 |
| 4 | Special Relationship INFLUENCE South Korea, Thailand | 41.70 | 6.00 | 36.00 | 0.00 | 0.00 | -0.30 | 0.00 | influence:South Korea:15.55, influence:Thailand:20.45 |
| 5 | Special Relationship INFLUENCE Indonesia, Thailand | 41.50 | 6.00 | 35.80 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Indonesia:13.85, access_touch:Indonesia, influence:Thailand:20.45 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 38: T3 AR4 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:3`
- hand: `Captured Nazi Scientist[18], Decolonization[30], The Cambridge Five[36], NORAD[38]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE West Germany, Japan | 37.35 | 6.00 | 31.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:15.65, influence:Japan:16.15 |
| 2 | NORAD INFLUENCE India, Japan | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:India:15.55, influence:Japan:16.15 |
| 3 | NORAD INFLUENCE Japan, North Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:North Korea:15.55 |
| 4 | NORAD INFLUENCE Japan, South Korea | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:South Korea:15.55 |
| 5 | NORAD INFLUENCE Japan, Egypt | 36.90 | 6.00 | 31.35 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Japan:16.15, influence:Egypt:13.70, access_touch:Egypt |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 39: T3 AR5 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:3`
- hand: `Blockade[10], CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:3 |
| 2 | CIA Created COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:3 |
| 3 | UN Intervention COUP Thailand | 27.80 | 4.00 | 23.95 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Thailand, battleground_coup, milops_need:3 |
| 4 | Blockade INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 5 | CIA Created INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 40: T3 AR5 US

- chosen: `Decolonization [30] as COUP`
- flags: `milops_shortfall:3, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Decolonization[30], The Cambridge Five[36]`
- state: `VP 0, DEFCON 4, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP Japan | 24.35 | 4.00 | 20.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3 |
| 2 | The Cambridge Five COUP Japan | 24.35 | 4.00 | 20.65 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Japan, battleground_coup, milops_need:3 |
| 3 | Decolonization COUP India | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:India, battleground_coup, milops_need:3 |
| 4 | Decolonization COUP North Korea | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:North Korea, battleground_coup, milops_need:3 |
| 5 | Decolonization COUP South Korea | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:South Korea, battleground_coup, milops_need:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+2`

## Step 41: T3 AR6 USSR

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `holds_china, milops_shortfall:2, offside_ops_play`
- hand: `CIA Created[26], UN Intervention[32]`
- state: `VP 0, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 2 | UN Intervention INFLUENCE Thailand | 26.30 | 6.00 | 20.45 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Thailand:20.45 |
| 3 | CIA Created INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 4 | UN Intervention INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 5 | CIA Created INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 42: T3 AR6 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:1`
- hand: `Captured Nazi Scientist[18], The Cambridge Five[36]`
- state: `VP 0, DEFCON 3, MilOps U1/A2, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE Japan | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:Japan:16.15 |
| 2 | The Cambridge Five INFLUENCE Japan | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Japan:16.15 |
| 3 | Captured Nazi Scientist INFLUENCE West Germany | 21.50 | 6.00 | 15.65 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:15.65 |
| 4 | Captured Nazi Scientist INFLUENCE India | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:India:15.55 |
| 5 | Captured Nazi Scientist INFLUENCE North Korea | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:North Korea:15.55 |

- effects: `VP -1, DEFCON +1, MilOps U-1/A-2`

## Step 43: T4 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Marshall Plan[23], Suez Crisis[28], Summit[48], Missile Envy[52], Willy Brandt[58], Muslim Revolution[59], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Suez Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Arab-Israeli War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 44: T4 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Suez Crisis[28], East European Unrest[29], Kitchen Debates[51], We Will Bury You[53], ABM Treaty[60], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 45: T4 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], Marshall Plan[23], Suez Crisis[28], Summit[48], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE UK, West Germany, Mexico, Algeria | 69.35 | 6.00 | 63.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria |
| 2 | Marshall Plan INFLUENCE East Germany, West Germany, Mexico, Algeria | 69.25 | 6.00 | 63.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria |
| 3 | Marshall Plan INFLUENCE France, West Germany, Mexico, Algeria | 69.25 | 6.00 | 63.85 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria |
| 4 | Marshall Plan INFLUENCE East Germany, UK, West Germany, Mexico | 69.20 | 6.00 | 63.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico |
| 5 | Marshall Plan INFLUENCE France, UK, West Germany, Mexico | 69.20 | 6.00 | 63.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:UK:14.15, access_touch:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 46: T4 AR1 US

- chosen: `We Will Bury You [53] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Suez Crisis[28], East European Unrest[29], Kitchen Debates[51], We Will Bury You[53], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You INFLUENCE UK, West Germany, Mexico, South Africa | 73.95 | 6.00 | 68.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80 |
| 2 | We Will Bury You INFLUENCE UK, Mexico, Algeria, South Africa | 73.50 | 6.00 | 68.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |
| 3 | We Will Bury You INFLUENCE East Germany, UK, Mexico, South Africa | 73.35 | 6.00 | 67.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80 |
| 4 | We Will Bury You INFLUENCE France, UK, Mexico, South Africa | 73.35 | 6.00 | 67.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:15.55, influence:UK:14.15, control_break:UK, influence:Mexico:14.95, access_touch:Mexico, influence:South Africa:16.80 |
| 5 | We Will Bury You INFLUENCE UK, West Germany, Algeria, South Africa | 73.20 | 6.00 | 67.80 | 0.00 | 0.00 | -0.60 | 0.00 | influence:UK:14.15, control_break:UK, influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 47: T4 AR2 USSR

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Suez Crisis[28], Summit[48], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Algeria, Morocco | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco |
| 2 | Summit INFLUENCE West Germany, Algeria, Morocco | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco |
| 3 | Sadat Expels Soviets INFLUENCE West Germany, Algeria, Morocco | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco |
| 4 | Suez Crisis INFLUENCE East Germany, Algeria, Morocco | 56.60 | 6.00 | 51.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco |
| 5 | Suez Crisis INFLUENCE France, Algeria, Morocco | 56.60 | 6.00 | 51.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Algeria:14.20, control_break:Algeria, influence:Morocco:14.80, access_touch:Morocco |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 48: T4 AR2 US

- chosen: `Duck and Cover [4] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Duck and Cover[4], Captured Nazi Scientist[18], Suez Crisis[28], East European Unrest[29], Kitchen Debates[51], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover INFLUENCE West Germany, Algeria, South Africa | 59.20 | 6.00 | 53.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa |
| 2 | Suez Crisis INFLUENCE West Germany, Algeria, South Africa | 59.20 | 6.00 | 53.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa |
| 3 | East European Unrest INFLUENCE West Germany, Algeria, South Africa | 59.20 | 6.00 | 53.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Algeria:14.20, access_touch:Algeria, influence:South Africa:16.80, control_break:South Africa |
| 4 | Duck and Cover INFLUENCE East Germany, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |
| 5 | Duck and Cover INFLUENCE France, West Germany, South Africa | 59.05 | 6.00 | 53.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80, control_break:South Africa |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 49: T4 AR3 USSR

- chosen: `Summit [48] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Summit[48], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria |
| 2 | Summit INFLUENCE France, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria |
| 4 | Sadat Expels Soviets INFLUENCE France, West Germany, Algeria | 56.45 | 6.00 | 50.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Algeria:14.20, control_break:Algeria |
| 5 | Summit INFLUENCE West Germany, Cuba, Algeria | 55.95 | 6.00 | 50.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:Algeria:14.20, control_break:Algeria |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 50: T4 AR3 US

- chosen: `Suez Crisis [28] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Suez Crisis[28], East European Unrest[29], Kitchen Debates[51], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Suez Crisis INFLUENCE West Germany, Morocco, South Africa | 54.80 | 6.00 | 49.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 2 | East European Unrest INFLUENCE West Germany, Morocco, South Africa | 54.80 | 6.00 | 49.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 3 | Suez Crisis INFLUENCE East Germany, Morocco, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 4 | Suez Crisis INFLUENCE France, Morocco, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |
| 5 | East European Unrest INFLUENCE East Germany, Morocco, South Africa | 54.20 | 6.00 | 48.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Morocco:14.80, access_touch:Morocco, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 51: T4 AR4 USSR

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4, offside_ops_play`
- hand: `Arab-Israeli War[13], Missile Envy[52], Willy Brandt[58], Sadat Expels Soviets[73], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba |
| 3 | Sadat Expels Soviets INFLUENCE France, West Germany, Cuba | 52.30 | 6.00 | 46.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba |
| 4 | Sadat Expels Soviets INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15 |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 52: T4 AR4 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], East European Unrest[29], Kitchen Debates[51], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | East European Unrest INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | East European Unrest INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 4 | East European Unrest INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | East European Unrest INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 53: T4 AR5 USSR

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Arab-Israeli War[13], Missile Envy[52], Willy Brandt[58], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Arab-Israeli War INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | Missile Envy INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | Missile Envy INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 54: T4 AR5 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:4, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Kitchen Debates[51], Flower Power[62], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Flower Power INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Flower Power INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 55: T4 AR6 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Missile Envy[52], Willy Brandt[58], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Missile Envy INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | Willy Brandt INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 56: T4 AR6 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], Kitchen Debates[51], John Paul II Elected Pope[69]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | John Paul II Elected Pope INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | John Paul II Elected Pope INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | John Paul II Elected Pope INFLUENCE Iraq, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 5 | John Paul II Elected Pope INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 57: T4 AR7 USSR

- chosen: `Willy Brandt [58] as INFLUENCE`
- flags: `holds_china, milops_shortfall:4`
- hand: `Willy Brandt[58], Colonial Rear Guards[110]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Willy Brandt INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Willy Brandt INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | Colonial Rear Guards INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | Colonial Rear Guards INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | Willy Brandt INFLUENCE West Germany, Cuba | 36.90 | 6.00 | 31.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 58: T4 AR7 US

- chosen: `Captured Nazi Scientist [18] as COUP`
- flags: `milops_shortfall:4`
- hand: `Captured Nazi Scientist[18], Kitchen Debates[51]`
- state: `VP -2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 2 | Kitchen Debates COUP South Africa | 24.15 | 4.00 | 20.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:4 |
| 3 | Captured Nazi Scientist COUP West Germany | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:4 |
| 4 | Kitchen Debates COUP West Germany | 23.50 | 4.00 | 19.65 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:West Germany, battleground_coup, milops_need:4 |
| 5 | Captured Nazi Scientist COUP East Germany | 22.90 | 4.00 | 19.05 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:East Germany, battleground_coup, milops_need:4 |

- effects: `VP -1, DEFCON +0, MilOps U+0/A+0`

## Step 59: T5 AR0 USSR

- chosen: `COMECON [14] as EVENT`
- flags: `holds_china, milops_shortfall:5`
- hand: `Five Year Plan[5], COMECON[14], De Gaulle Leads France[17], Decolonization[30], Nuclear Subs[44], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63], Lone Gunman[109]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | U2 Incident EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Decolonization EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 60: T5 AR0 US

- chosen: `Red Scare/Purge [31] as EVENT`
- flags: `milops_shortfall:5`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Red Scare/Purge[31], Special Relationship[37], Bear Trap[47], South African Unrest[56], OAS Founded[71]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Red Scare/Purge EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Special Relationship EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Captured Nazi Scientist EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |
| 5 | CIA Created EVENT | 5.10 | 0.00 | 0.00 | 1.50 | 1.00 | -0.15 | 2.75 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 61: T5 AR1 USSR

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5, offside_ops_play`
- hand: `Five Year Plan[5], De Gaulle Leads France[17], Decolonization[30], Nuclear Subs[44], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63], Lone Gunman[109]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE East Germany, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Five Year Plan INFLUENCE France, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | De Gaulle Leads France INFLUENCE France, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | U2 Incident INFLUENCE East Germany, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 62: T5 AR1 US

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Socialist Governments[7], Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Special Relationship[37], Bear Trap[47], South African Unrest[56], OAS Founded[71]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Socialist Governments INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Bear Trap INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Socialist Governments INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 63: T5 AR2 USSR

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `De Gaulle Leads France[17], Decolonization[30], Nuclear Subs[44], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63], Lone Gunman[109]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | De Gaulle Leads France INFLUENCE France, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | U2 Incident INFLUENCE East Germany, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | U2 Incident INFLUENCE France, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | De Gaulle Leads France INFLUENCE West Germany, Cuba | 36.75 | 6.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 64: T5 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Special Relationship[37], Bear Trap[47], South African Unrest[56], OAS Founded[71]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Bear Trap INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Bear Trap INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 4 | Bear Trap INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Bear Trap INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 65: T5 AR3 USSR

- chosen: `U2 Incident [63] as INFLUENCE`
- flags: `holds_china, milops_shortfall:5`
- hand: `Decolonization[30], Nuclear Subs[44], How I Learned to Stop Worrying[49], Junta[50], U2 Incident[63], Lone Gunman[109]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | U2 Incident INFLUENCE East Germany, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | U2 Incident INFLUENCE France, West Germany | 37.25 | 6.00 | 31.70 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | U2 Incident INFLUENCE West Germany, Cuba | 36.75 | 6.00 | 31.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba |
| 4 | U2 Incident INFLUENCE East Germany, France | 36.65 | 6.00 | 31.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55 |
| 5 | U2 Incident INFLUENCE Italy, West Germany | 36.65 | 6.00 | 31.10 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 66: T5 AR3 US

- chosen: `Vietnam Revolts [9] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Vietnam Revolts[9], Captured Nazi Scientist[18], CIA Created[26], Special Relationship[37], South African Unrest[56], OAS Founded[71]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Vietnam Revolts INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Special Relationship INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | South African Unrest INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Vietnam Revolts INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | Vietnam Revolts INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 67: T5 AR4 USSR

- chosen: `Decolonization [30] as COUP`
- flags: `holds_china, milops_shortfall:5`
- hand: `Decolonization[30], Nuclear Subs[44], How I Learned to Stop Worrying[49], Junta[50], Lone Gunman[109]`
- state: `VP -3, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization COUP East Germany | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:East Germany, battleground_coup, milops_need:5 |
| 2 | Decolonization COUP France | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:France, battleground_coup, milops_need:5 |
| 3 | Nuclear Subs COUP East Germany | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:East Germany, battleground_coup, milops_need:5 |
| 4 | Nuclear Subs COUP France | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:France, battleground_coup, milops_need:5 |
| 5 | How I Learned to Stop Worrying COUP East Germany | 23.75 | 4.00 | 20.05 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:East Germany, battleground_coup, milops_need:5 |

- effects: `VP +0, DEFCON -1, MilOps U+2/A+0`

## Step 68: T5 AR4 US

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], CIA Created[26], Special Relationship[37], South African Unrest[56], OAS Founded[71]`
- state: `VP -3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | South African Unrest INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Special Relationship INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Special Relationship INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | South African Unrest INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 69: T5 AR5 USSR

- chosen: `Nuclear Subs [44] as COUP`
- flags: `holds_china, milops_shortfall:3, offside_ops_play`
- hand: `Nuclear Subs[44], How I Learned to Stop Worrying[49], Junta[50], Lone Gunman[109]`
- state: `VP -3, DEFCON 4, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs COUP Mexico | 23.15 | 4.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3 |
| 2 | How I Learned to Stop Worrying COUP Mexico | 23.15 | 4.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3 |
| 3 | Junta COUP Mexico | 23.15 | 4.00 | 19.45 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:3 |
| 4 | Nuclear Subs COUP Morocco | 23.00 | 4.00 | 19.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:3 |
| 5 | How I Learned to Stop Worrying COUP Morocco | 23.00 | 4.00 | 19.30 | 0.00 | 0.00 | -0.30 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:3 |

- effects: `VP +0, DEFCON -1, MilOps U+0/A+0`

## Step 70: T5 AR5 US

- chosen: `South African Unrest [56] as INFLUENCE`
- flags: `milops_shortfall:5, offside_ops_play`
- hand: `Captured Nazi Scientist[18], CIA Created[26], South African Unrest[56], OAS Founded[71]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | South African Unrest INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | South African Unrest INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | South African Unrest INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | South African Unrest INFLUENCE Iraq, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 5 | South African Unrest INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 71: T5 AR6 USSR

- chosen: `Lone Gunman [109] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `How I Learned to Stop Worrying[49], Junta[50], Lone Gunman[109]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lone Gunman INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 2 | How I Learned to Stop Worrying INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15 |
| 3 | Junta INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15 |
| 4 | Lone Gunman INFLUENCE East Germany | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:15.55 |
| 5 | Lone Gunman INFLUENCE France | 21.40 | 6.00 | 15.55 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 72: T5 AR6 US

- chosen: `Captured Nazi Scientist [18] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `Captured Nazi Scientist[18], CIA Created[26], OAS Founded[71]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Captured Nazi Scientist INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 2 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 3 | OAS Founded INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 4 | Captured Nazi Scientist INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 5 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 73: T5 AR7 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:3`
- hand: `How I Learned to Stop Worrying[49], Junta[50]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15 |
| 2 | Junta INFLUENCE West Germany | 21.85 | 6.00 | 16.15 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55 |
| 4 | How I Learned to Stop Worrying INFLUENCE France | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55 |
| 5 | Junta INFLUENCE East Germany | 21.25 | 6.00 | 15.55 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 74: T5 AR7 US

- chosen: `CIA Created [26] as INFLUENCE`
- flags: `milops_shortfall:5`
- hand: `CIA Created[26], OAS Founded[71]`
- state: `VP -3, DEFCON 3, MilOps U2/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | CIA Created INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 2 | OAS Founded INFLUENCE South Africa | 22.65 | 6.00 | 16.80 | 0.00 | 0.00 | -0.15 | 0.00 | influence:South Africa:16.80 |
| 3 | CIA Created INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 4 | OAS Founded INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |
| 5 | CIA Created COUP South Africa | 21.65 | 4.00 | 17.80 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:South Africa, battleground_coup, milops_need:5, defcon_penalty:3 |

- effects: `VP +2, DEFCON +1, MilOps U-2/A+0`

## Step 75: T6 AR0 USSR

- chosen: `Nuclear Test Ban [34] as EVENT`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], COMECON[14], CIA Created[26], US/Japan Mutual Defense Pact[27], Nuclear Test Ban[34], The Cambridge Five[36], Quagmire[45], Brezhnev Doctrine[54]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Test Ban EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | COMECON EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Brezhnev Doctrine EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Korean War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 76: T6 AR0 US

- chosen: `Duck and Cover [4] as EVENT`
- flags: `milops_shortfall:6`
- hand: `Duck and Cover[4], Truman Doctrine[19], Independent Reds[22], NORAD[38], Arms Race[42], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP -1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Duck and Cover EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Arms Race EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Independent Reds EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Puppet Governments EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON +0, MilOps U+0/A+0`

## Step 77: T6 AR1 USSR

- chosen: `US/Japan Mutual Defense Pact [27] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6, offside_ops_play`
- hand: `Korean War[11], Romanian Abdication[12], COMECON[14], CIA Created[26], US/Japan Mutual Defense Pact[27], The Cambridge Five[36], Quagmire[45], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Cuba | 67.70 | 6.00 | 62.30 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba |
| 2 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Mexico | 67.60 | 6.00 | 62.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95 |
| 3 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, Italy, West Germany | 67.60 | 6.00 | 62.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15 |
| 4 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Morocco | 67.45 | 6.00 | 62.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Morocco:14.80 |
| 5 | US/Japan Mutual Defense Pact INFLUENCE East Germany, France, West Germany, Egypt | 67.35 | 6.00 | 61.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15, influence:Egypt:13.20, access_touch:Egypt |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 78: T6 AR1 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Independent Reds[22], NORAD[38], Arms Race[42], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | NORAD INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Arms Race INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Arms Race INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | NORAD INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 79: T6 AR2 USSR

- chosen: `COMECON [14] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], COMECON[14], CIA Created[26], The Cambridge Five[36], Quagmire[45], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | COMECON INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15 |
| 2 | Quagmire INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 57.80 | 6.00 | 52.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, control_break:France, influence:West Germany:16.15 |
| 4 | COMECON INFLUENCE France, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Mexico:14.95 |
| 5 | Quagmire INFLUENCE France, West Germany, Mexico | 57.20 | 6.00 | 51.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, control_break:France, influence:West Germany:16.15, influence:Mexico:14.95 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 80: T6 AR2 US

- chosen: `Arms Race [42] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Independent Reds[22], Arms Race[42], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arms Race INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Arms Race INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Arms Race INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 4 | Arms Race INFLUENCE Poland, West Germany, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Arms Race INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 81: T6 AR3 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], The Cambridge Five[36], Quagmire[45], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 3 | Quagmire INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15 |
| 4 | Quagmire INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95 |
| 5 | Quagmire INFLUENCE France, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 82: T6 AR3 US

- chosen: `Independent Reds [22] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Independent Reds[22], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Independent Reds INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Puppet Governments INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Liberation Theology INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 83: T6 AR4 USSR

- chosen: `Brezhnev Doctrine [54] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], The Cambridge Five[36], Brezhnev Doctrine[54]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brezhnev Doctrine INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 2 | Brezhnev Doctrine INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15 |
| 3 | Brezhnev Doctrine INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95 |
| 4 | Brezhnev Doctrine INFLUENCE France, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:Italy:14.95, influence:West Germany:16.15 |
| 5 | Brezhnev Doctrine INFLUENCE France, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Mexico:14.95 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 84: T6 AR4 US

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Puppet Governments[67], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Liberation Theology INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Puppet Governments INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 85: T6 AR5 USSR

- chosen: `Korean War [11] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Korean War[11], Romanian Abdication[12], CIA Created[26], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Korean War INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | The Cambridge Five INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | Korean War INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 86: T6 AR5 US

- chosen: `Grain Sales to Soviets [68] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Grain Sales to Soviets[68], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Grain Sales to Soviets INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Liberation Theology INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Grain Sales to Soviets INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | Grain Sales to Soviets INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 87: T6 AR6 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:6`
- hand: `Romanian Abdication[12], CIA Created[26], The Cambridge Five[36]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | The Cambridge Five INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55 |
| 4 | The Cambridge Five INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15 |
| 5 | The Cambridge Five INFLUENCE West Germany, Mexico | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Mexico:14.95 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 88: T6 AR6 US

- chosen: `Nixon Plays the China Card [72] as INFLUENCE`
- flags: `milops_shortfall:6`
- hand: `Truman Doctrine[19], Nixon Plays the China Card[72], Liberation Theology[76]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nixon Plays the China Card INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Liberation Theology INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Nixon Plays the China Card INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Nixon Plays the China Card INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Liberation Theology INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 89: T6 AR7 USSR

- chosen: `Romanian Abdication [12] as COUP`
- flags: `holds_china, milops_shortfall:6`
- hand: `Romanian Abdication[12], CIA Created[26]`
- state: `VP 1, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Romanian Abdication COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6 |
| 2 | CIA Created COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:6 |
| 3 | Romanian Abdication COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:6 |
| 4 | CIA Created COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:6 |
| 5 | Romanian Abdication INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 90: T6 AR7 US

- chosen: `Liberation Theology [76] as INFLUENCE`
- flags: `milops_shortfall:6, offside_ops_play`
- hand: `Truman Doctrine[19], Liberation Theology[76]`
- state: `VP 1, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Liberation Theology INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Liberation Theology INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Liberation Theology INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Liberation Theology INFLUENCE Iraq, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 5 | Liberation Theology INFLUENCE Poland, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Poland:13.55, access_touch:Poland, influence:South Africa:16.80 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 91: T7 AR0 USSR

- chosen: `De-Stalinization [33] as EVENT`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Olympic Games[20], Containment[25], De-Stalinization[33], Special Relationship[37], Cuban Missile Crisis[43], SALT Negotiations[46], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De-Stalinization EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Cuban Missile Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | SALT Negotiations EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Olympic Games EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 92: T7 AR0 US

- chosen: `East European Unrest [29] as EVENT`
- flags: `milops_shortfall:7`
- hand: `East European Unrest[29], Decolonization[30], The Cambridge Five[36], Brush War[39], Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Ask Not What Your Country Can Do For You EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Lonely Hearts Club Band EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 4 | Brush War EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |
| 5 | Che EVENT | -4.20 | 0.00 | 0.00 | -3.00 | -3.00 | -0.45 | 2.25 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 93: T7 AR1 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Olympic Games[20], Containment[25], Special Relationship[37], Cuban Missile Crisis[43], SALT Negotiations[46], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE West Germany, Israel, Ethiopia | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia |
| 2 | Cuban Missile Crisis INFLUENCE West Germany, Israel, Ethiopia | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia |
| 3 | SALT Negotiations INFLUENCE West Germany, Israel, Ethiopia | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia |
| 4 | Ussuri River Skirmish INFLUENCE West Germany, Israel, Ethiopia | 57.70 | 6.00 | 52.15 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Israel:14.40, access_touch:Israel, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia |
| 5 | Containment INFLUENCE East Germany, West Germany, Ethiopia | 57.35 | 6.00 | 51.80 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Ethiopia:13.60, control_break:Ethiopia, access_touch:Ethiopia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 94: T7 AR1 US

- chosen: `Brush War [39] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Brush War[39], Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Brush War INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Che INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 95: T7 AR2 USSR

- chosen: `Cuban Missile Crisis [43] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Olympic Games[20], Special Relationship[37], Cuban Missile Crisis[43], SALT Negotiations[46], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Cuban Missile Crisis INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 2 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 3 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 4 | Cuban Missile Crisis INFLUENCE East Germany, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |
| 5 | Cuban Missile Crisis INFLUENCE France, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 96: T7 AR2 US

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Decolonization[30], The Cambridge Five[36], Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65], Ask Not What Your Country Can Do For You[78], Che[83]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Che INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Che INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Ask Not What Your Country Can Do For You INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 97: T7 AR3 USSR

- chosen: `SALT Negotiations [46] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Olympic Games[20], Special Relationship[37], SALT Negotiations[46], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | SALT Negotiations INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 3 | SALT Negotiations INFLUENCE East Germany, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |
| 4 | SALT Negotiations INFLUENCE France, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 98: T7 AR3 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65], Che[83]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Che INFLUENCE France, West Germany, South Africa | 54.05 | 6.00 | 48.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Che INFLUENCE West Germany, Iraq, South Africa | 53.80 | 6.00 | 48.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 4 | Che INFLUENCE West Germany, Cuba, South Africa | 53.55 | 6.00 | 48.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:West Germany:16.15, influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |
| 5 | Che INFLUENCE East Germany, France, South Africa | 53.45 | 6.00 | 47.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 99: T7 AR4 USSR

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Olympic Games[20], Special Relationship[37], Ussuri River Skirmish[77], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 52.80 | 6.00 | 47.25 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:France:15.55, influence:West Germany:16.15 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |
| 3 | Ussuri River Skirmish INFLUENCE France, West Germany, Saudi Arabia | 52.55 | 6.00 | 47.00 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:15.55, influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:Italy:14.95, influence:West Germany:16.15 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Mexico | 52.20 | 6.00 | 46.65 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15, influence:Mexico:14.95 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 100: T7 AR4 US

- chosen: `Decolonization [30] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Decolonization[30], The Cambridge Five[36], Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Decolonization INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | The Cambridge Five INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 5 | Decolonization INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 101: T7 AR5 USSR

- chosen: `Olympic Games [20] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Olympic Games[20], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Olympic Games INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Olympic Games INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | Special Relationship INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 4 | Special Relationship INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 5 | Olympic Games INFLUENCE West Germany, Saudi Arabia | 37.15 | 6.00 | 31.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 102: T7 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `The Cambridge Five[36], Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 4 | The Cambridge Five INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 5 | The Cambridge Five INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 103: T7 AR6 USSR

- chosen: `Special Relationship [37] as INFLUENCE`
- flags: `holds_china, milops_shortfall:7, offside_ops_play`
- hand: `Blockade[10], Special Relationship[37], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Special Relationship INFLUENCE East Germany, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:West Germany:16.15 |
| 2 | Special Relationship INFLUENCE France, West Germany | 37.40 | 6.00 | 31.70 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:West Germany:16.15 |
| 3 | Special Relationship INFLUENCE West Germany, Saudi Arabia | 37.15 | 6.00 | 31.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:Saudi Arabia:13.80, access_touch:Saudi Arabia |
| 4 | Special Relationship INFLUENCE East Germany, France | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:France:15.55 |
| 5 | Special Relationship INFLUENCE Italy, West Germany | 36.80 | 6.00 | 31.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:14.95, influence:West Germany:16.15 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 104: T7 AR6 US

- chosen: `Portuguese Empire Crumbles [55] as INFLUENCE`
- flags: `milops_shortfall:7, offside_ops_play`
- hand: `Portuguese Empire Crumbles[55], Allende[57], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Portuguese Empire Crumbles INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 3 | Portuguese Empire Crumbles INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 4 | Portuguese Empire Crumbles INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 5 | Lonely Hearts Club Band INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 105: T7 AR7 USSR

- chosen: `Blockade [10] as COUP`
- flags: `holds_china, milops_shortfall:7`
- hand: `Blockade[10], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Blockade COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7 |
| 2 | Panama Canal Returned COUP Mexico | 22.30 | 4.00 | 18.45 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Mexico, battleground_coup, milops_need:7 |
| 3 | Blockade COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:7 |
| 4 | Panama Canal Returned COUP Morocco | 22.15 | 4.00 | 18.30 | 0.00 | 0.00 | -0.15 | 0.00 | coup_target:Morocco, battleground_coup, milops_need:7 |
| 5 | Blockade INFLUENCE West Germany | 22.00 | 6.00 | 16.15 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.15 |

- effects: `VP +0, DEFCON -1, MilOps U+1/A+0`

## Step 106: T7 AR7 US

- chosen: `Lonely Hearts Club Band [65] as INFLUENCE`
- flags: `milops_shortfall:7`
- hand: `Allende[57], Lonely Hearts Club Band[65]`
- state: `VP 2, DEFCON 3, MilOps U1/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Lonely Hearts Club Band INFLUENCE West Germany, South Africa | 38.65 | 6.00 | 32.95 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.15, influence:South Africa:16.80 |
| 2 | Lonely Hearts Club Band INFLUENCE East Germany, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:15.55, influence:South Africa:16.80 |
| 3 | Lonely Hearts Club Band INFLUENCE France, South Africa | 38.05 | 6.00 | 32.35 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:15.55, influence:South Africa:16.80 |
| 4 | Lonely Hearts Club Band INFLUENCE Iraq, South Africa | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Iraq:13.80, access_touch:Iraq, influence:South Africa:16.80 |
| 5 | Lonely Hearts Club Band INFLUENCE Cuba, South Africa | 37.55 | 6.00 | 31.85 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Cuba:13.55, access_touch:Cuba, influence:South Africa:16.80 |

- effects: `VP +1, DEFCON +1, MilOps U-1/A+0`

## Step 107: T8 AR0 USSR

- chosen: `De Gaulle Leads France [17] as EVENT`
- flags: `holds_china, milops_shortfall:8`
- hand: `De Gaulle Leads France[17], The Cambridge Five[36], Nuclear Subs[44], Quagmire[45], How I Learned to Stop Worrying[49], OPEC[64], Camp David Accords[66], Shuttle Diplomacy[74], AWACS Sale to Saudis[107]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | Quagmire EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | OPEC EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | The Cambridge Five EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | How I Learned to Stop Worrying EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 108: T8 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Korean War[11], De Gaulle Leads France[17], NORAD[38], Muslim Revolution[59], ABM Treaty[60], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Solidarity[104]`
- state: `VP 3, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | NORAD EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Ussuri River Skirmish EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | John Paul II Elected Pope EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Solidarity EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP -1, DEFCON +1, MilOps U+0/A+0`

## Step 109: T8 AR1 USSR

- chosen: `Quagmire [45] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `The Cambridge Five[36], Nuclear Subs[44], Quagmire[45], How I Learned to Stop Worrying[49], OPEC[64], Camp David Accords[66], Shuttle Diplomacy[74], AWACS Sale to Saudis[107]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Quagmire INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 5 | Quagmire INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 110: T8 AR1 US

- chosen: `Muslim Revolution [59] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Korean War[11], De Gaulle Leads France[17], NORAD[38], Muslim Revolution[59], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution INFLUENCE East Germany, France, Italy, West Germany | 72.10 | 6.00 | 66.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Cuba | 71.95 | 6.00 | 66.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 3 | Muslim Revolution INFLUENCE East Germany, France, West Germany, Iraq | 71.45 | 6.00 | 66.05 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:West Germany:16.90, influence:Iraq:13.55, access_touch:Iraq |
| 4 | Muslim Revolution INFLUENCE France, Italy, West Germany, Cuba | 71.35 | 6.00 | 65.95 | 0.00 | 0.00 | -0.60 | 0.00 | influence:France:16.30, access_touch:France, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Muslim Revolution INFLUENCE East Germany, France, UK, West Germany | 71.30 | 6.00 | 65.90 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, access_touch:France, influence:UK:14.90, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 111: T8 AR2 USSR

- chosen: `OPEC [64] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `The Cambridge Five[36], Nuclear Subs[44], How I Learned to Stop Worrying[49], OPEC[64], Camp David Accords[66], Shuttle Diplomacy[74], AWACS Sale to Saudis[107]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OPEC INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | OPEC INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | OPEC INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 112: T8 AR2 US

- chosen: `De Gaulle Leads France [17] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Korean War[11], De Gaulle Leads France[17], NORAD[38], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | De Gaulle Leads France INFLUENCE East Germany, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |
| 2 | De Gaulle Leads France INFLUENCE France, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |
| 3 | NORAD INFLUENCE East Germany, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |
| 4 | NORAD INFLUENCE France, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 59.45 | 6.00 | 53.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 113: T8 AR3 USSR

- chosen: `Shuttle Diplomacy [74] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `The Cambridge Five[36], Nuclear Subs[44], How I Learned to Stop Worrying[49], Camp David Accords[66], Shuttle Diplomacy[74], AWACS Sale to Saudis[107]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Shuttle Diplomacy INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Shuttle Diplomacy INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Shuttle Diplomacy INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | AWACS Sale to Saudis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 114: T8 AR3 US

- chosen: `NORAD [38] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Korean War[11], NORAD[38], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | NORAD INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | NORAD INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | NORAD INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 115: T8 AR4 USSR

- chosen: `AWACS Sale to Saudis [107] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `The Cambridge Five[36], Nuclear Subs[44], How I Learned to Stop Worrying[49], Camp David Accords[66], AWACS Sale to Saudis[107]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | AWACS Sale to Saudis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | AWACS Sale to Saudis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | AWACS Sale to Saudis INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | AWACS Sale to Saudis INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |
| 5 | AWACS Sale to Saudis INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 116: T8 AR4 US

- chosen: `Ussuri River Skirmish [77] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Korean War[11], John Paul II Elected Pope[69], Ussuri River Skirmish[77], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ussuri River Skirmish INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ussuri River Skirmish INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Ussuri River Skirmish INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Ussuri River Skirmish INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Ussuri River Skirmish INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 117: T8 AR5 USSR

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `The Cambridge Five[36], Nuclear Subs[44], How I Learned to Stop Worrying[49], Camp David Accords[66]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Nuclear Subs INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Nuclear Subs INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 118: T8 AR5 US

- chosen: `Korean War [11] as INFLUENCE`
- flags: `milops_shortfall:8, offside_ops_play`
- hand: `Blockade[10], Korean War[11], John Paul II Elected Pope[69], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Korean War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Korean War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | John Paul II Elected Pope INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 119: T8 AR6 USSR

- chosen: `Nuclear Subs [44] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8, offside_ops_play`
- hand: `Nuclear Subs[44], How I Learned to Stop Worrying[49], Camp David Accords[66]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Nuclear Subs INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Nuclear Subs INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Camp David Accords INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 120: T8 AR6 US

- chosen: `John Paul II Elected Pope [69] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], John Paul II Elected Pope[69], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | John Paul II Elected Pope INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | John Paul II Elected Pope INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Solidarity INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | John Paul II Elected Pope INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 121: T8 AR7 USSR

- chosen: `How I Learned to Stop Worrying [49] as INFLUENCE`
- flags: `holds_china, milops_shortfall:8`
- hand: `How I Learned to Stop Worrying[49], Camp David Accords[66]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | How I Learned to Stop Worrying INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | How I Learned to Stop Worrying INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Camp David Accords INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Camp David Accords INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | How I Learned to Stop Worrying INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 122: T8 AR7 US

- chosen: `Solidarity [104] as INFLUENCE`
- flags: `milops_shortfall:8`
- hand: `Blockade[10], Solidarity[104]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Solidarity INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Solidarity INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Solidarity INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 4 | Solidarity INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Solidarity INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 123: T9 AR0 USSR

- chosen: `We Will Bury You [53] as EVENT`
- flags: `holds_china, milops_shortfall:9`
- hand: `Socialist Governments[7], Marshall Plan[23], Containment[25], Missile Envy[52], We Will Bury You[53], OAS Founded[71], Ask Not What Your Country Can Do For You[78], Iranian Hostage Crisis[85], Panama Canal Returned[111]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | We Will Bury You EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Socialist Governments EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Iranian Hostage Crisis EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Missile Envy EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Marshall Plan EVENT | -3.60 | 0.00 | 0.00 | -3.00 | -3.00 | -0.60 | 3.00 | offside_event, headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 124: T9 AR0 US

- chosen: `ABM Treaty [60] as EVENT`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], The Cambridge Five[36], Bear Trap[47], ABM Treaty[60], Flower Power[62], One Small Step[81], The Iron Lady[86], The Reformer[90], Lone Gunman[109]`
- state: `VP 2, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ABM Treaty EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Five Year Plan EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Bear Trap EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | The Iron Lady EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | One Small Step EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +2, DEFCON -1, MilOps U+0/A+0`

## Step 125: T9 AR1 USSR

- chosen: `Marshall Plan [23] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Socialist Governments[7], Marshall Plan[23], Containment[25], Missile Envy[52], OAS Founded[71], Ask Not What Your Country Can Do For You[78], Iranian Hostage Crisis[85], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Marshall Plan INFLUENCE East Germany, France, Italy, West Germany | 70.60 | 6.00 | 65.20 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Marshall Plan INFLUENCE East Germany, France, Turkey, West Germany | 70.10 | 6.00 | 64.70 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |
| 3 | Marshall Plan INFLUENCE East Germany, France, West Germany, Saudi Arabia | 69.95 | 6.00 | 64.55 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Saudi Arabia:13.55, access_touch:Saudi Arabia |
| 4 | Marshall Plan INFLUENCE East Germany, France, UK, West Germany | 69.80 | 6.00 | 64.40 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:UK:14.90, influence:West Germany:16.90 |
| 5 | Marshall Plan INFLUENCE East Germany, Italy, Turkey, West Germany | 69.50 | 6.00 | 64.10 | 0.00 | 0.00 | -0.60 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 126: T9 AR1 US

- chosen: `Five Year Plan [5] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `Five Year Plan[5], The Cambridge Five[36], Bear Trap[47], Flower Power[62], One Small Step[81], The Iron Lady[86], The Reformer[90], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Five Year Plan INFLUENCE Italy, West Germany, Mexico | 61.60 | 6.00 | 56.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico |
| 2 | Bear Trap INFLUENCE Italy, West Germany, Mexico | 61.60 | 6.00 | 56.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico |
| 3 | The Iron Lady INFLUENCE Italy, West Germany, Mexico | 61.60 | 6.00 | 56.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico |
| 4 | The Reformer INFLUENCE Italy, West Germany, Mexico | 61.60 | 6.00 | 56.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:Italy:15.70, control_break:Italy, influence:West Germany:16.90, influence:Mexico:13.45, control_break:Mexico |
| 5 | Five Year Plan INFLUENCE East Germany, Italy, Mexico | 61.00 | 6.00 | 55.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, control_break:Italy, influence:Mexico:13.45, control_break:Mexico |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 127: T9 AR2 USSR

- chosen: `Socialist Governments [7] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Socialist Governments[7], Containment[25], Missile Envy[52], OAS Founded[71], Ask Not What Your Country Can Do For You[78], Iranian Hostage Crisis[85], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Socialist Governments INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Containment INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 5 | Socialist Governments INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 128: T9 AR2 US

- chosen: `Bear Trap [47] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `The Cambridge Five[36], Bear Trap[47], Flower Power[62], One Small Step[81], The Iron Lady[86], The Reformer[90], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Bear Trap INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | The Iron Lady INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | The Reformer INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | Bear Trap INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Bear Trap INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 129: T9 AR3 USSR

- chosen: `Containment [25] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Containment[25], Missile Envy[52], OAS Founded[71], Ask Not What Your Country Can Do For You[78], Iranian Hostage Crisis[85], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | Containment INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Containment INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 130: T9 AR3 US

- chosen: `The Iron Lady [86] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `The Cambridge Five[36], Flower Power[62], One Small Step[81], The Iron Lady[86], The Reformer[90], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Iron Lady INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | The Reformer INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | The Iron Lady INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | The Iron Lady INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | The Reformer INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 131: T9 AR4 USSR

- chosen: `Ask Not What Your Country Can Do For You [78] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `Missile Envy[52], OAS Founded[71], Ask Not What Your Country Can Do For You[78], Iranian Hostage Crisis[85], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Ask Not What Your Country Can Do For You INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Ask Not What Your Country Can Do For You INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Iranian Hostage Crisis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 132: T9 AR4 US

- chosen: `The Reformer [90] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `The Cambridge Five[36], Flower Power[62], One Small Step[81], The Reformer[90], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Reformer INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | The Reformer INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | The Reformer INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | The Reformer INFLUENCE East Germany, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | The Reformer INFLUENCE France, West Germany, Cuba | 54.30 | 6.00 | 48.75 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 133: T9 AR5 USSR

- chosen: `Iranian Hostage Crisis [85] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Missile Envy[52], OAS Founded[71], Iranian Hostage Crisis[85], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iranian Hostage Crisis INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Iranian Hostage Crisis INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Iranian Hostage Crisis INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Iranian Hostage Crisis INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |
| 5 | Iranian Hostage Crisis INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 134: T9 AR5 US

- chosen: `The Cambridge Five [36] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `The Cambridge Five[36], Flower Power[62], One Small Step[81], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | The Cambridge Five INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | The Cambridge Five INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Flower Power INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Flower Power INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 135: T9 AR6 USSR

- chosen: `Missile Envy [52] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9`
- hand: `Missile Envy[52], OAS Founded[71], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Missile Envy INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Missile Envy INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Missile Envy INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 4 | Missile Envy INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Missile Envy INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 136: T9 AR6 US

- chosen: `Flower Power [62] as INFLUENCE`
- flags: `milops_shortfall:9, offside_ops_play`
- hand: `Flower Power[62], One Small Step[81], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Flower Power INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Flower Power INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Flower Power INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 137: T9 AR7 USSR

- chosen: `OAS Founded [71] as INFLUENCE`
- flags: `holds_china, milops_shortfall:9, offside_ops_play`
- hand: `OAS Founded[71], Panama Canal Returned[111]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | OAS Founded INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 2 | Panama Canal Returned INFLUENCE West Germany | 22.75 | 6.00 | 16.90 | 0.00 | 0.00 | -0.15 | 0.00 | influence:West Germany:16.90 |
| 3 | OAS Founded INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |
| 4 | OAS Founded INFLUENCE France | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:France:16.30 |
| 5 | Panama Canal Returned INFLUENCE East Germany | 22.15 | 6.00 | 16.30 | 0.00 | 0.00 | -0.15 | 0.00 | influence:East Germany:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 138: T9 AR7 US

- chosen: `One Small Step [81] as INFLUENCE`
- flags: `milops_shortfall:9`
- hand: `One Small Step[81], Lone Gunman[109]`
- state: `VP 4, DEFCON 4, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | One Small Step INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | One Small Step INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | One Small Step INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 4 | One Small Step INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | One Small Step INFLUENCE West Germany, Cuba | 38.15 | 6.00 | 32.45 | 0.00 | 0.00 | -0.30 | 0.00 | influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +1, MilOps U+0/A+0`

## Step 139: T10 AR0 USSR

- chosen: `Muslim Revolution [59] as EVENT`
- flags: `holds_china, milops_shortfall:10`
- hand: `Captured Nazi Scientist[18], Brush War[39], Muslim Revolution[59], Puppet Governments[67], Che[83], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Muslim Revolution EVENT | 6.90 | 0.00 | 0.00 | 1.50 | 1.00 | -0.60 | 5.00 | headline_context |
| 2 | Brush War EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Che EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Latin American Debt Crisis EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |
| 5 | Iran-Iraq War EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 140: T10 AR0 US

- chosen: `Containment [25] as EVENT`
- flags: `milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Containment[25], East European Unrest[29], Summit[48], Junta[50], Sadat Expels Soviets[73], Che[83], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Containment EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 2 | East European Unrest EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 3 | Summit EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 4 | Sadat Expels Soviets EVENT | 6.30 | 0.00 | 0.00 | 1.50 | 1.00 | -0.45 | 4.25 | headline_context |
| 5 | Junta EVENT | 5.70 | 0.00 | 0.00 | 1.50 | 1.00 | -0.30 | 3.50 | headline_context |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 141: T10 AR1 USSR

- chosen: `Brush War [39] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Captured Nazi Scientist[18], Brush War[39], Puppet Governments[67], Che[83], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Brush War INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Che INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | North Sea Oil INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | Brush War INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Brush War INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 142: T10 AR1 US

- chosen: `East European Unrest [29] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], East European Unrest[29], Summit[48], Junta[50], Sadat Expels Soviets[73], Che[83], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | East European Unrest INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Summit INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Che INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | East European Unrest INFLUENCE East Germany, France, West Germany, Cuba | 70.60 | 6.00 | 65.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 143: T10 AR2 USSR

- chosen: `Che [83] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Captured Nazi Scientist[18], Puppet Governments[67], Che[83], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | North Sea Oil INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Che INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Che INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | North Sea Oil INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 144: T10 AR2 US

- chosen: `Summit [48] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Summit[48], Junta[50], Sadat Expels Soviets[73], Che[83], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Summit INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Sadat Expels Soviets INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Che INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Summit INFLUENCE East Germany, France, West Germany, Cuba | 70.60 | 6.00 | 65.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany, Cuba | 70.60 | 6.00 | 65.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 145: T10 AR3 USSR

- chosen: `North Sea Oil [89] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Puppet Governments[67], Our Man in Tehran[84], North Sea Oil[89], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | North Sea Oil INFLUENCE East Germany, France, West Germany | 55.05 | 6.00 | 49.50 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | North Sea Oil INFLUENCE East Germany, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | North Sea Oil INFLUENCE France, Italy, West Germany | 54.45 | 6.00 | 48.90 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | North Sea Oil INFLUENCE East Germany, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |
| 5 | North Sea Oil INFLUENCE France, Turkey, West Germany | 53.95 | 6.00 | 48.40 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 146: T10 AR3 US

- chosen: `Sadat Expels Soviets [73] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Junta[50], Sadat Expels Soviets[73], Che[83], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Sadat Expels Soviets INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Che INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany, Cuba | 70.60 | 6.00 | 65.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 4 | Che INFLUENCE East Germany, France, West Germany, Cuba | 70.60 | 6.00 | 65.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Sadat Expels Soviets INFLUENCE East Germany, France, West Germany, Iraq | 70.10 | 6.00 | 64.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Iraq:13.55, access_touch:Iraq |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 147: T10 AR4 USSR

- chosen: `Puppet Governments [67] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Puppet Governments[67], Our Man in Tehran[84], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Puppet Governments INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Puppet Governments INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Our Man in Tehran INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Our Man in Tehran INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 148: T10 AR4 US

- chosen: `Che [83] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Junta[50], Che[83], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Che INFLUENCE East Germany, France, Italy, West Germany | 70.75 | 6.00 | 65.20 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 2 | Che INFLUENCE East Germany, France, West Germany, Cuba | 70.60 | 6.00 | 65.05 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 3 | Che INFLUENCE East Germany, France, West Germany, Iraq | 70.10 | 6.00 | 64.55 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90, influence:Iraq:13.55, access_touch:Iraq |
| 4 | Che INFLUENCE East Germany, Italy, West Germany, Cuba | 70.00 | 6.00 | 64.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Che INFLUENCE France, Italy, West Germany, Cuba | 70.00 | 6.00 | 64.45 | 0.00 | 0.00 | -0.45 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 149: T10 AR5 USSR

- chosen: `Our Man in Tehran [84] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10, offside_ops_play`
- hand: `Captured Nazi Scientist[18], Our Man in Tehran[84], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Our Man in Tehran INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Our Man in Tehran INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Latin American Debt Crisis INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 150: T10 AR5 US

- chosen: `Arab-Israeli War [13] as INFLUENCE`
- flags: `milops_shortfall:10, offside_ops_play`
- hand: `Arab-Israeli War[13], Truman Doctrine[19], Junta[50], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Arab-Israeli War INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Junta INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Star Wars INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 4 | Arab-Israeli War INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Arab-Israeli War INFLUENCE France, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 151: T10 AR6 USSR

- chosen: `Latin American Debt Crisis [98] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Captured Nazi Scientist[18], Latin American Debt Crisis[98], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Latin American Debt Crisis INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Latin American Debt Crisis INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 4 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 5 | Latin American Debt Crisis INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 152: T10 AR6 US

- chosen: `Junta [50] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Truman Doctrine[19], Junta[50], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Junta INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Star Wars INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 3 | Junta INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Junta INFLUENCE France, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Star Wars INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 153: T10 AR7 USSR

- chosen: `Iran-Iraq War [105] as INFLUENCE`
- flags: `holds_china, milops_shortfall:10`
- hand: `Captured Nazi Scientist[18], Iran-Iraq War[105]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Iran-Iraq War INFLUENCE East Germany, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90 |
| 2 | Iran-Iraq War INFLUENCE France, West Germany | 38.90 | 6.00 | 33.20 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90 |
| 3 | Iran-Iraq War INFLUENCE East Germany, France | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30 |
| 4 | Iran-Iraq War INFLUENCE Italy, West Germany | 38.30 | 6.00 | 32.60 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Italy:15.70, influence:West Germany:16.90 |
| 5 | Iran-Iraq War INFLUENCE Turkey, West Germany | 37.80 | 6.00 | 32.10 | 0.00 | 0.00 | -0.30 | 0.00 | influence:Turkey:13.70, access_touch:Turkey, influence:West Germany:16.90 |

- effects: `VP +0, DEFCON +0, MilOps U+0/A+0`

## Step 154: T10 AR7 US

- chosen: `Star Wars [88] as INFLUENCE`
- flags: `milops_shortfall:10`
- hand: `Truman Doctrine[19], Star Wars[88]`
- state: `VP 4, DEFCON 5, MilOps U0/A0, Space U0/A0, China USSR (up)`

| Rank | Action | Total | Mode | Detail | Event | Bias | Ops | Headline | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Star Wars INFLUENCE East Germany, France, West Germany | 55.20 | 6.00 | 49.50 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:France:16.30, influence:West Germany:16.90 |
| 2 | Star Wars INFLUENCE East Germany, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 3 | Star Wars INFLUENCE France, Italy, West Germany | 54.60 | 6.00 | 48.90 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:Italy:15.70, influence:West Germany:16.90 |
| 4 | Star Wars INFLUENCE East Germany, West Germany, Cuba | 54.45 | 6.00 | 48.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:East Germany:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |
| 5 | Star Wars INFLUENCE France, West Germany, Cuba | 54.45 | 6.00 | 48.75 | 0.00 | 0.00 | -0.30 | 0.00 | influence:France:16.30, influence:West Germany:16.90, influence:Cuba:14.05, access_touch:Cuba |

- effects: `VP -3, DEFCON +0, MilOps U+0/A+0`
