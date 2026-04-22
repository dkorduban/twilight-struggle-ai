# Opus Analysis: Heuristic vs Heuristic US Bias
Date: 2026-04-20
Question: Why does greedy heuristic get 72% US WR vs heuristic, and was a bid used?

## Executive Summary
The "US wins 72%, USSR wins 28%" report is **label-inverted**. The actual 2000-game JSONL artifact (`/tmp/heur_vs_heur.jsonl`, seed=70000, greedy minimal_hybrid both sides) shows the opposite: **USSR wins ~70%, US wins ~30%, avg final_vp = +7.86** (USSR-dominant). This matches the historical bid=2 heuristic-vs-heuristic baselines in `results/archive/heuristic_temperature_sweep_human_openings_bid2.json` (USSR 68.1% at t=0.0, USSR 72.2% at t=0.1). The run did use a bid — effectively +2, injected via the hardcoded `use_atomic_setup = true` in `cpp/tools/collect_selfplay_rows_jsonl.cpp` which always places the 9-influence `kHumanUSOpeningsBid2` opening regardless of the `--bid` flag. No engine bug, no heuristic asymmetry bug — the "USSR ~70%" is the expected behavior of greedy minimal_hybrid at competitive bid+2 setup.

## Findings

### 1. Ground truth from the actual JSONL artifact
`/tmp/heur_vs_heur.jsonl` (1.16 GB, last modified 2026-04-20 16:48, 257,253 rows across 2000 games, `game_id` prefix `selfplay_70000_*`):

| Convention | USSR wins | US wins | Draws |
|---|---|---|---|
| `final_vp > 0 / < 0 / == 0` (side-absolute, unambiguous) | 1385 (69.25%) | 582 (29.10%) | 33 (1.65%) |
| `winner_side == +1 / -1 / 0` (emitter convention) | 1439 (71.95%) | 561 (28.05%) | 0 |
| **Among decisive (by `final_vp`)** | **70.41%** | **29.59%** | — |

- `avg_final_vp = +7.86` (sign says USSR-dominant; TS convention is `+vp = USSR` and `-vp = US`).
- End-reason histogram: `turn_limit=975, europe_control=662, vp_threshold=204, defcon1=88, vp=58, scoring_card_held=7, wargames=6` — healthy distribution, no suspicious end-state spike.

Therefore the user's "US wins 72%, USSR wins 28%" is the same 72/28 split with the labels flipped. The 72/28 figure is almost an exact match to the archived bid=2 baseline (`heuristic_temperature_sweep_human_openings_bid2.json:34-39`, `ussr_wins=706/us_wins=272, ussr_wr=72.19` for `ussr_temperature=0.1`).

### 2. Convention check — `winner_side` is side-absolute, not actor-relative
`cpp/tools/collect_selfplay_rows_jsonl.cpp:39-44`:
```cpp
int winner_side_int(const std::optional<ts::Side>& winner) {
    if (!winner.has_value()) return 0;
    return *winner == ts::Side::USSR ? 1 : -1;
}
```
USSR = +1, US = -1, draw = 0. This is side-absolute. **But**: `scripts/bench_cpp.sh:150-154` carries a stale/incorrect comment claiming `winner_side` is actor-relative ("`1=actor won, -1=actor lost`"). Anyone pattern-matching on that comment and interpreting `winner_side == -1` as "actor lost = opponent (US) won" would mislabel the 72/28 split as a US win rate. The `bench_cpp.sh` code itself then disregards `winner_side` and uses `final_vp` anyway, so the stale comment was silent — but it looks like the source of the reporting confusion.

There is no ambiguity in the VP sign: game_loop.cpp:3509–3524 and 3617–3624 set `winner = Side::USSR if vp > 0`, `Side::US if vp < 0`. The 33 "draws" in the `final_vp` tally become USSR-labeled wins in `winner_side` because line 3518 makes USSR the default for `vp == 0` at turn limit. Either way, US is the minority side.

### 3. Was a bid applied? Yes, effectively +2, via atomic setup
`cpp/tools/collect_selfplay_rows_jsonl.cpp:235, 279-280, 343-347`:
- `us_bid = 0` is the default.
- `GameLoopConfig` is constructed with `.us_bid_extra = us_bid` AND `.use_atomic_setup = true` (hardcoded; comment: "always use atomic setup with kHumanUSOpeningsBid2").

`cpp/tscore/game_loop.cpp:3438-3467` (atomic setup branch):
- Line 3438-3440: if `us_bid_extra > 0`, top up `setup_influence_remaining[US]`. With default `--bid 0`, this is a no-op.
- Line 3448-3467: When `use_atomic_setup` is true, iterate `{USSR, US}` and place the full opening from the table.
  - USSR table: `kHumanUSSROpenings` — all three entries total 6 influence.
  - US table: `kHumanUSOpeningsBid2` — five of six entries total **9 influence** (7 setup + 2 bid), and one entry (the "no bid game", weight 1/58 = 1.7%) totals 7.
- Line 3467: `setup_influence_remaining = {0, 0}` regardless of what the table placed.

Net effect: with `--bid 0` and atomic setup on (the only mode `collect_selfplay_rows_jsonl` ever uses), the US gets `~8.97` influence on average (`5*9 + 1*7, weighted /58 ≈ 8.966`) — **effectively a +2 bid is baked in.** Passing `--bid 2` on the CLI would double-compensate (add 2 to `setup_influence_remaining[US]`, then the atomic branch overwrites it and places the Bid2 table anyway), so the CLI flag is largely cosmetic in this tool.

Contrast with `cpp/tools/benchmark_matchup.cpp`: it sets only `us_bid_extra = us_bid` and does NOT set `use_atomic_setup=true` (GameLoopConfig default is false). That tool uses the policy-driven setup loop at `game_loop.cpp:3362-3420`, where each side's policy is called once per influence point. `scripts/run_temperature_sweep.py` uses `ts_benchmark_matchup --bid 2`, which gives the US 7+2=9 via policy placement + bid top-up (different code path, but same 9-vs-6 balance on the board). That is why the archive sweep at `bid=2` yields essentially the same 68–72% USSR WR as `collect_selfplay_rows_jsonl` at `--bid 0` — both setups converge to 9 US vs 6 USSR influence.

### 4. Heuristic symmetry check
`cpp/tscore/policies.cpp` / `cpp/tscore/heuristic*` / `python/tsrl/policies/minimal_hybrid.py` — both the C++ and Python minimal_hybrid policies are side-parametric: the same scoring functions apply with role of phasing side swapped. No asymmetric magic numbers found that would favor one side. The `kNashUSSRTemps` / `kNashUSTemps` are Nash-mixed strategies derived from the 6×6 temperature matrix (greedy USSR beats greedy US ~66/34 per `human_openings.hpp:94-95`), which is again USSR-dominant. The heuristic favors USSR because the game, at +2 bid with competitive play, favors USSR; this is the widely accepted meta. Bid+2 is the competitive baseline precisely because +0 bid would be even more USSR-dominant.

### 5. Is 70% USSR plausible for greedy minimal_hybrid at bid+2?
Yes — this is the known ceiling of the heuristic's asymmetry and matches multiple historical baselines:
- `results/archive/heuristic_temperature_sweep_human_openings_bid2.json`: 68.1% (t=0,0), 72.2% (t=0.1,0), 70.8% (t=0.25,0), 71.2% (t=0.5,0)
- `results/archive/heuristic_temperature_sweep_no_setup.json`: 65.5% (t=0,0) — slightly lower but same direction
- `human_openings.hpp:94-95`: "Game value: USSR 66.09%, US 33.91%" — the Nash game-value ceiling over the temperature matrix.
- Competitive human TS is typically USSR-favored pre-bid; +2 bid brings expert human play to roughly 50/50. Machine heuristic is weaker than expert humans so the +2 bid is not large enough to equalize; USSR keeps a 65–72% edge against a greedy heuristic US.

### 6. What recent engine changes could plausibly have shifted bias?
Scanned git log for commits touching `game_loop.cpp`, `policies.cpp`, `collect_selfplay_rows_jsonl.cpp`:
- DEFCON-1 fixes (2026-04-13, commits `f6800e3`, `eedd07a`, `55e792a`, etc.) hardened the heuristic against self-destructive coups. Net effect: fewer defcon1-ended games, USSR retains control of nuclear risk.
- Tier-1 + Tier-2 card fixes (2026-04-19, commits through `530118a`) corrected cards 7/20/50/68/75/16/28/33/60/76/77/95/98. Many of these hurt the USSR-exploitable openings (e.g., Decolonization 4-stack into Angola) — would, if anything, REDUCE USSR WR, not increase it. Post-fix panel-vs-heuristic WRs crashed from ~83% (pre-fix) to ~41–45% (post-fix) per `opus_analysis_20260419_230000_postfix_elo_investigation.md:60` — but that is *learned-vs-heuristic*, not heuristic-vs-heuristic.
- The heuristic-vs-heuristic symmetry at ~70% USSR has been stable across the archive (pre- and post- many of these fixes), so no engine regression is in evidence.

### 7. Summary of the data path
```
user request: 2000 games greedy minimal_hybrid both sides
  -> scripts/collect_cpp.sh (probably) OR direct ts_collect_selfplay_rows_jsonl invocation
  -> build-ninja/cpp/tools/ts_collect_selfplay_rows_jsonl --out /tmp/heur_vs_heur.jsonl --games 2000 --seed 70000 [--bid 0 default] [--ussr-policy minimal_hybrid] [--us-policy minimal_hybrid]
  -> GameLoopConfig { us_bid_extra=0, use_atomic_setup=true }  [HARDCODED atomic]
  -> atomic setup places 9 US influence + 6 USSR influence from kHumanUS{SR,}Openings
  -> play 80 turns of AR, emit per-step row with winner_side=+1/-1/0 and final_vp
  -> 2000 game records, 1385 USSR wins by final_vp, 582 US wins, 33 draws
  -> reporter read winner_side assuming actor-relative encoding or inverted labels
  -> "US wins 72%" (actually USSR wins 72%)
```

## Conclusions
1. **The reported 72% US / 28% USSR is a label inversion**, not a real signal. The raw `/tmp/heur_vs_heur.jsonl` shows USSR 69–72% depending on which field you read (`final_vp` sign vs. `winner_side` int), both pointing the same direction.
2. **A bid was applied**, effectively +2, whether or not `--bid 2` was on the CLI. `collect_selfplay_rows_jsonl.cpp` hardcodes `use_atomic_setup = true`, which always draws from the `kHumanUSOpeningsBid2` table (9-influence US openings). The `--bid` CLI flag is nearly cosmetic in this tool.
3. **`winner_side` convention in `collect_selfplay_rows_jsonl.cpp` is side-absolute**: USSR=+1, US=-1, draw=0. `bench_cpp.sh:150-154` has a stale comment claiming actor-relative encoding; that comment is the most likely source of the reporter's confusion. It should be deleted or corrected.
4. **No engine or heuristic bug is implicated.** The ~70% USSR WR at bid+2 is consistent with archived baselines (2026-04-02 temperature sweep results) and with the Nash game-value 66.09% USSR announced in `human_openings.hpp:94-95`.
5. **The heuristic is symmetric** — no side-specific code path favors US. The bias is in the game's intrinsic balance with a +2 bid, not in the policy.
6. **The run used seed=70000**, which is the historical "imitation / human-openings dataset" seed (`results/experiment_log.md` ties seed=70000 to bid+2 + human openings config).

## Recommendations
1. **Re-report the result with correct labels**: USSR wins ~70%, US wins ~30%, avg final_vp = +7.86, end-reason histogram includes `turn_limit=975, europe_control=662, vp_threshold=262 (vp+vp_threshold), defcon1=88`. This is not a red flag — it is expected and matches bid+2 baselines.
2. **Fix or remove the stale `bench_cpp.sh:150-154` comment** that asserts `winner_side` is actor-relative. Option A: change the comment to the correct convention (`winner_side=+1 → USSR won, -1 → US won, 0 → draw`). Option B: delete the note since the code already uses `final_vp` and never touches `winner_side`. I recommend Option A plus a matching assertion in the downstream summarizer if any code still reads `winner_side`.
3. **Add a loud warning in `collect_selfplay_rows_jsonl.cpp`** documenting that `use_atomic_setup=true` is hardcoded and that `--bid 0` does NOT disable the +2 bid — the US always receives the `kHumanUSOpeningsBid2` opening (~9 influence). If a true "no bid" heuristic self-play is ever needed, a `--no-atomic-setup` flag would be required.
4. **Consider a sanity-check script** (e.g., `scripts/validate_heur_selfplay_winrate.py`) that compares a fresh run's USSR/US WR against a stored baseline (68–72% USSR at bid+2) and fails loudly if the delta exceeds ~5 pp. This would catch real regressions (e.g., if a rule fix actually flipped balance) and also catch label-inversion reporting bugs at the source.
5. **For heuristic-vs-heuristic as a benchmark baseline**: prefer reporting `final_vp_mean` (no sign-convention ambiguity across codepaths) in addition to WR. A +7.86 average VP is a very clean signal that USSR is ahead.

## Open Questions
1. What script or pipeline produced the user's "72% US" report? I did not find the CLI invocation in `results/autonomous_decisions.log`. If the caller was a shell script that parsed `winner_side` rather than `final_vp`, the label-inversion culprit can be pinpointed and fixed. Candidates to audit: any summarizer using `winner_side == -1` as the US-win predicate, any grep/awk chain that swapped stdout columns.
2. Is the `use_atomic_setup = true` hardcoding in `collect_selfplay_rows_jsonl.cpp` intentional for dataset-generation consistency, or a leftover from the human-openings imitation experiment? The flag should probably be exposed as a CLI option with clear documentation.
3. Do any downstream Parquet/training pipelines read `winner_side` directly (vs. `final_vp`)? If so, their side-vs-actor convention should be audited. `bench_cpp.sh` already avoids `winner_side`, but other consumers may not.
