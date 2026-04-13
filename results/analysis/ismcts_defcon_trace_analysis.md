# ISMCTS DEFCON Trace Analysis

## Scope

- Raw greedy baseline checkpoint: `data/checkpoints/scripted_for_elo/v79_sc_scripted.pt`
- Direct traced ISMCTS-vs-model play is not exposed in the Python bindings. The bindings expose `benchmark_ismcts*` result-only APIs, but no traced ISMCTS policy hook.
- This report therefore uses two evidence sources:
  1. fresh near-greedy raw-policy self-play via `rollout_self_play_batched` (binding requires `temperature > 0`, so this uses `temperature=1e-06`; `n=64`)
  2. existing search-trace JSONL files in `data/selfplay/` as the closest available step-level proxy
- Detailed last-10-step DEFCON-1 windows were written to `results/analysis/ismcts_defcon_trace_windows.jsonl`.

## Dataset Summary

| dataset | source_kind | games | defcon1_games | defcon1_rate | avg_turn_defcon1 |
|---|---|---:|---:|---:|---:|
| v79_sc_scripted.pt @ T=1e-06 | raw_policy | 64 | 14 | 21.9% | 7.07 |
| mcts_v106_ussr_400sim_1k.jsonl | search_proxy | 1000 | 98 | 9.8% | 7.43 |
| mcts_v99c_s7_ussr_vs_heuristic_2k.jsonl | search_proxy | 2000 | 187 | 9.3% | 6.66 |

## Main Findings

- Raw greedy traced baseline ended by DEFCON-1 in 14/64 games (21.9%).
- Search-proxy traces contributed 285 DEFCON-1 games across 3000 recorded games.
- Average turn of terminal DEFCON-1 in search-proxy traces: 6.93.
- Average turn of terminal DEFCON-1 in raw traced baseline: 7.07.
- These rates are not a like-for-like reproduction of the 2026-04-12 v45 benchmark in `results/analysis/ismcts_retest_post_fix.md`. This script follows the task instruction to use the highest available scripted checkpoint for the raw baseline (`v79_sc_scripted.pt`), and the search trace proxies come from older recorded MCTS corpora (`v99c` / `v106`) rather than traced ISMCTS-vs-raw-policy matches.
- The fatal action is not only a `coup` problem. In the search-proxy traces, terminal DEFCON-1 drops split mostly between `event` and `ops`; the `ops` bucket is dominated by DEFCON-lowering cards such as `Duck and Cover` played for ops where the opponent event still fires and collapses DEFCON from 2 to 1.
- Repeated headline/setup motifs show up in the last three steps: `Duck and Cover`, `Che`, `How I Learned to Stop Worrying`, `Brush War`, `We Will Bury You`, and `Cuban Missile Crisis`.

## Confirmed Bug

- Bug name: `Headline card selection uses non-headline legality mask`.
- The code confirms this is not just a plausible hypothesis. Headline choices are queued with `is_headline=true` in `advance_until_search_or_done(...)` (`cpp/tscore/ismcts.cpp:1390-1405`), but selection still uses ordinary card/mode legality, then headline commit forcibly converts the chosen action to `Event` in `commit_selected_action(...)` (`cpp/tscore/ismcts.cpp:1049-1089`).
- There is no dedicated `legal_headline_cards(...)` or other headline-only legality helper in `cpp/tscore/legal_actions.cpp` or `cpp/tscore/legal_actions.hpp`. `legal_modes(...)` (`cpp/tscore/legal_actions.cpp:136-190`) has no headline-context parameter at all.

### Affected Paths

- Raw-policy opponent path:
  - `resolve_model_decision(...)` calls `greedy_action_from_model(...)`.
  - `greedy_action_from_model(...)` uses `legal_cards(...)` at `cpp/tscore/ismcts.cpp:1168` and `legal_modes(...)` at `cpp/tscore/ismcts.cpp:1203`.
  - It has no `is_headline` parameter and therefore no headline-only legality handling.
- ISMCTS search side:
  - `collect_card_drafts(...)` (`cpp/tscore/ismcts.cpp:371-449`) uses the same `legal_cards(...)` plus `is_card_blocked_by_defcon(...)` filter, then adds generic modes such as `Influence`, `Coup`, `Realign`, and `Space`.
  - That means the search tree also evaluates headline candidates using non-headline legality before headline commit forces the result to `Event`.
- Parallel batched search path:
  - `mcts_batched.cpp` shows the same structure: headline decisions are queued with `is_headline=true` (`cpp/tscore/mcts_batched.cpp:2424-2435`) and committed by forcing `action.mode = ActionMode::Event` (`cpp/tscore/mcts_batched.cpp:2752-2754`).
  - Its draft generation also adds generic modes before separately adding `Event` (`cpp/tscore/mcts_batched.cpp:651-678`), so the same class of bug exists there too.

### Mechanism

- `is_card_blocked_by_defcon(...)` (`cpp/tscore/ismcts.cpp:178-197`) blocks:
  - opponent DEFCON-lowering cards at `DEFCON <= 2`
  - opponent DEFCON-lowering cards at headline when `DEFCON == 3`
  - neutral DEFCON-lowering cards at headline when `DEFCON <= 3`
- It does **not** block own DEFCON-lowering cards in headline context.
- During headline selection, both the raw-policy path and the search path can therefore retain an own DEFCON-lowering card because non-event modes look legal during selection.
- `commit_selected_action(...)` then rewrites the selected headline action to `ActionMode::Event`, so the event fires even if selection effectively treated the card like an ops/influence/space candidate.

### Impact

- At `DEFCON=2`, own DEFCON-lowering cards can be selected as headlines and then immediately lose the game when their event fires and drops DEFCON to 1.
- The concrete risk set includes the DEFCON-lowering cards already recurring in the traces and benchmark context:
  - `Duck and Cover`
  - `We Will Bury You`
  - `How I Learned to Stop Worrying`
  - `Brush War`
  - `Che`
  - `Cuban Missile Crisis`
- `Duck and Cover` is the clearest example because the owning side can keep card 4 in the candidate set during selection, then headline commit forces it to `Event`.

### Fix

- The safest fix is to make headline legality event-only at selection time rather than at commit time.
- Two equivalent implementation directions:
  - extend `is_card_blocked_by_defcon(...)` with headline context and, when `is_headline=true` and `DEFCON <= 2`, block **all** DEFCON-lowering cards regardless of side because all headlines resolve as events
  - or add a dedicated helper such as `is_card_blocked_by_defcon_headline(card_id, pub)` / `legal_headline_cards(...)` and use it consistently in both `greedy_action_from_model(...)` and `collect_card_drafts(...)`
- Any fix needs to cover both:
  - the raw-policy opponent path
  - the learned-side search path

## Search Proxy: Cards/Modes In Final 3 Steps Before DEFCON-1

| card | side | mode_id | mode | count | pct_of_top_bucket |
|---|---|---:|---|---:|---:|
| Che | USSR | 1 | event | 43 | 14.7% |
| Duck and Cover | USSR | 0 | ops | 39 | 13.4% |
| How I Learned to Stop Worrying | US | 1 | event | 30 | 10.3% |
| Brush War | US | 1 | event | 29 | 9.9% |
| Che | US | 0 | ops | 28 | 9.6% |
| Che | US | 4 | coup | 21 | 7.2% |
| We Will Bury You | USSR | 1 | event | 19 | 6.5% |
| Five Year Plan | USSR | 0 | ops | 19 | 6.5% |
| Soviets Shoot Down KAL 007 | USSR | 0 | ops | 18 | 6.2% |
| Cuban Missile Crisis | US | 1 | event | 16 | 5.5% |
| We Will Bury You | US | 1 | event | 15 | 5.1% |
| We Will Bury You | US | 0 | ops | 15 | 5.1% |

### Search Proxy: Terminal DEFCON-1 Drop Mode

| value | count | pct |
|---|---:|---:|
| event | 126 | 44.2% |
| ops | 121 | 42.5% |
| coup | 35 | 12.3% |
| realignment | 2 | 0.7% |
| space | 1 | 0.4% |

### Search Proxy: Terminal DEFCON-1 Drop Side

| value | count | pct |
|---|---:|---:|
| USSR | 164 | 57.5% |
| US | 121 | 42.5% |

## Raw Greedy Baseline: Cards/Modes In Final 3 Steps Before DEFCON-1

| card | side | mode_id | mode | count | pct_of_top_bucket |
|---|---|---:|---|---:|---:|
| Che | USSR | 1 | event | 2 | 15.4% |
| Liberation Theology | US | 0 | ops | 1 | 7.7% |
| Duck and Cover | US | 1 | event | 1 | 7.7% |
| Colonial Rear Guards | USSR | 0 | ops | 1 | 7.7% |
| Cuban Missile Crisis | US | 1 | event | 1 | 7.7% |
| Shuttle Diplomacy | USSR | 0 | ops | 1 | 7.7% |
| SALT Negotiations | USSR | 0 | ops | 1 | 7.7% |
| Cuban Missile Crisis | US | 0 | ops | 1 | 7.7% |
| Alliance for Progress | USSR | 0 | ops | 1 | 7.7% |
| Summit | USSR | 0 | ops | 1 | 7.7% |
| Special Relationship | US | 0 | ops | 1 | 7.7% |
| Arab-Israeli War | USSR | 0 | ops | 1 | 7.7% |

### Raw Baseline: Terminal DEFCON-1 Drop Mode

| value | count | pct |
|---|---:|---:|
| ops | 11 | 78.6% |
| event | 3 | 21.4% |

### Raw Baseline: Terminal DEFCON-1 Drop Side

| value | count | pct |
|---|---:|---:|
| USSR | 8 | 57.1% |
| US | 6 | 42.9% |

## Example Windows

The appendix below shows a small sample of the recorded last-10-step windows. The full set is in the JSONL artifact.

### search_proxy | mcts_v106_ussr_400sim_1k.jsonl | mcts_v106_ussr_80000_0001 | end_turn=7

| turn | ar | side | card | mode_id | mode | DEFCON before | DEFCON after |
|---|---:|---|---|---:|---|---:|---:|
| 7 | 2 | US | East European Unrest (29) | 0 | ops | 2 | 2 |
| 7 | 3 | USSR | Korean War (11) | 0 | ops | 2 | 2 |
| 7 | 3 | US | Sadat Expels Soviets (73) | 4 | coup | 2 | 2 |
| 7 | 4 | USSR | OPEC (64) | 0 | ops | 2 | 2 |
| 7 | 4 | US | UN Intervention (32) | 4 | coup | 2 | 2 |
| 7 | 5 | USSR | Portuguese Empire Crumbles (55) | 0 | ops | 2 | 2 |
| 7 | 5 | US | CIA Created (26) | 4 | coup | 2 | 2 |
| 7 | 6 | USSR | Puppet Governments (67) | 0 | ops | 2 | 2 |
| 7 | 6 | US | Cultural Revolution (61) | 4 | coup | 2 | 2 |
| 7 | 7 | USSR | Duck and Cover (4) | 0 | ops | 2 | 1 |

### search_proxy | mcts_v106_ussr_400sim_1k.jsonl | mcts_v106_ussr_80000_0046 | end_turn=6

| turn | ar | side | card | mode_id | mode | DEFCON before | DEFCON after |
|---|---:|---|---|---:|---|---:|---:|
| 5 | 4 | USSR | Nuclear Subs (44) | 0 | ops | 3 | 3 |
| 5 | 4 | US | Lonely Hearts Club Band (65) | 4 | coup | 3 | 3 |
| 5 | 5 | USSR | Lone Gunman (109) | 4 | coup | 3 | 3 |
| 5 | 5 | US | Missile Envy (52) | 4 | coup | 3 | 3 |
| 5 | 6 | USSR | Nixon Plays the China Card (72) | 4 | coup | 3 | 3 |
| 5 | 6 | US | Camp David Accords (66) | 4 | coup | 3 | 3 |
| 5 | 7 | USSR | OAS Founded (71) | 4 | coup | 3 | 3 |
| 5 | 7 | US | Latin American Death Squads (70) | 4 | coup | 3 | 4 |
| 6 | 0 | US | Cuban Missile Crisis (43) | 1 | event | 4 | 2 |
| 6 | 0 | USSR | Duck and Cover (4) | 1 | event | 2 | 1 |

### search_proxy | mcts_v106_ussr_400sim_1k.jsonl | mcts_v106_ussr_80000_0060 | end_turn=7

| turn | ar | side | card | mode_id | mode | DEFCON before | DEFCON after |
|---|---:|---|---|---:|---|---:|---:|
| 7 | 2 | US | Nuclear Test Ban (34) | 0 | ops | 2 | 2 |
| 7 | 3 | USSR | Warsaw Pact Formed (16) | 0 | ops | 2 | 2 |
| 7 | 3 | US | Cuban Missile Crisis (43) | 4 | coup | 2 | 2 |
| 7 | 4 | USSR | One Small Step (81) | 0 | ops | 2 | 2 |
| 7 | 4 | US | East European Unrest (29) | 4 | coup | 2 | 2 |
| 7 | 5 | USSR | Five Year Plan (5) | 0 | ops | 2 | 2 |
| 7 | 5 | US | Latin American Death Squads (70) | 4 | coup | 2 | 2 |
| 7 | 6 | USSR | Puppet Governments (67) | 0 | ops | 2 | 2 |
| 7 | 6 | US | South African Unrest (56) | 4 | coup | 2 | 2 |
| 7 | 7 | USSR | Duck and Cover (4) | 0 | ops | 2 | 1 |

### raw_policy | v79_sc_scripted.pt | raw_rollout_024000_0007 | end_turn=7

| turn | ar | side | card | mode_id | mode | DEFCON before | DEFCON after |
|---|---:|---|---|---:|---|---:|---:|
| 6 | 4 | USSR | SALT Negotiations (46) | 2 | space | 2 | 2 |
| 6 | 4 | US | Formosan Resolution (35) | 1 | event | 2 | 2 |
| 6 | 5 | USSR | OAS Founded (71) | 0 | ops | 2 | 2 |
| 6 | 5 | US | Missile Envy (52) | 1 | event | 2 | 2 |
| 6 | 6 | USSR | Colonial Rear Guards (110) | 0 | ops | 2 | 2 |
| 6 | 6 | US | Kitchen Debates (51) | 1 | event | 2 | 2 |
| 6 | 7 | USSR | Nixon Plays the China Card (72) | 0 | ops | 2 | 2 |
| 6 | 7 | US | Liberation Theology (76) | 0 | ops | 2 | 3 |
| 7 | 0 | USSR | Che (83) | 1 | event | 3 | 3 |
| 7 | 0 | US | Duck and Cover (4) | 1 | event | 3 | 1 |

### raw_policy | v79_sc_scripted.pt | raw_rollout_024000_0012 | end_turn=4

| turn | ar | side | card | mode_id | mode | DEFCON before | DEFCON after |
|---|---:|---|---|---:|---|---:|---:|
| 4 | 1 | US | Muslim Revolution (59) | 1 | event | 2 | 2 |
| 4 | 2 | USSR | OAS Founded (71) | 2 | space | 2 | 2 |
| 4 | 2 | US | How I Learned to Stop Worrying (49) | 0 | ops | 2 | 2 |
| 4 | 3 | USSR | Latin American Death Squads (70) | 0 | ops | 2 | 2 |
| 4 | 3 | US | Our Man in Tehran (84) | 1 | event | 2 | 2 |
| 4 | 4 | USSR | Missile Envy (52) | 0 | ops | 2 | 2 |
| 4 | 4 | US | U2 Incident (63) | 1 | event | 2 | 2 |
| 4 | 5 | USSR | Colonial Rear Guards (110) | 0 | ops | 2 | 2 |
| 4 | 5 | US | Cuban Missile Crisis (43) | 1 | event | 2 | 2 |
| 4 | 6 | USSR | Shuttle Diplomacy (74) | 0 | ops | 2 | 1 |
