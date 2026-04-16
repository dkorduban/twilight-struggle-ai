# Experimental Heuristic Stack

This directory owns the isolated heuristic-search baseline.

Local rules:
- Prefer additive work inside `cpp/experimental/` and `python/experimental/`.
- Do not modify existing `cpp/tscore` behavior to support this stack.
- Main autonomous rule: keep selecting the highest-ROI next step without asking
  for confirmation until the experimental heuristic meets the tiered end goal:
  1) beat MinimalHybrid decisively in isolated matchups across both seats, then
  2) restart the same read-plan-implement-benchmark loop against the reference
  learned policy until that matchup is also decisively winning. Do not stop on
  partial progress, transient regressions, or incomplete benchmarks; keep
  iterating until both tiers are met. After every benchmark:
  - if the current tier is not met, immediately re-read the prompt and traces,
    update the plan, implement the next highest-ROI change, and rerun
    benchmarks
  - do not pause on "good enough" parity, local speedups, or partial seat wins
- OODA loop:
  1) Observe:
     - re-read this `AGENTS.md` file before starting the new iteration, so the
       latest autonomy rules and cleanup discipline stay active
     - re-read `long-prompts/principled-heuristic.md` and the latest benchmark /
       trace output
     - extract dominant loss modes by seat, turn window, and terminal cause
  2) Orient:
     - update the roadmap if the highest-ROI step changed
     - reduce the problem to one seat, one failure family, and one metric
  3) Decide:
     - implement the single best strength-per-time or speed-per-time change
     - prefer proposal/eval fixes before deeper tree or belief work
  4) Act:
     - benchmark on meaningful samples using the active evidence ladder:
       - `50` games per seat: screening only
       - `200` games per seat: tentative candidate validation
       - `800` games per seat: baseline branch promotion / rejection
     - do not use any sample below `50` games per seat for ranking,
       promotion, or rejection
  5) Loop:
     - before restarting, re-read this policy again and confirm the current
       bottleneck and stop conditions have not changed
     - after each completed OODA iteration, re-read this policy before taking
       the next action, even if the next action is another benchmark or tuning
       run rather than a code change
     - if the current tier is not yet met, repeat from step 1 immediately
- Current loop priority:
  - the latest corrected `800+800` baseline is the authority:
    - `search` as USSR vs `minimal`: `450/800 = 56.25%`
    - `search` as US vs `minimal`: `98/800 = 12.25%`
  - the latest accepted working baseline on the newer Europe-support branch is:
    - `search` as USSR vs `minimal`: `31-19` on a clean explicit-seed `50`-game validation
    - `search` as US vs `minimal`: `7-43` on a clean explicit-seed `50`-game validation
    - that branch was accepted because it improved the USSR seat materially (`62%` vs `52%`) while preserving the US seat at the improved post-patch level (`14%` vs the earlier `10%` authority baseline)
    - its key change is a cheaper Europe non-battleground support / country-count pressure bonus in the proposal `PrepScoring` lane, now the default working baseline
  - corrected terminal-cause labeling matters:
    - earlier mid-turn `vp_threshold` wins were misclassified as
      `europe_control`
    - the active clean `800+800` baseline is the authority for terminal-cause
      diagnosis
  - a real experimental scoring-card bug was fixed:
    - when `must_play_scoring_card(...)` became true, proposal generation could
      still drop all scoring-card actions after shortlist truncation
    - that could fall through to a generic legal fallback and cause avoidable
      `scoring_card_held` losses
    - known failing US seed `448498040` no longer ends
      `scoring_card_held` after the fix
  - the active blocker is now generic scoring/play quality on the weak US seat:
    the corrected loss mix is mostly `vp` and `turn_limit`; the old
    `scoring_card_held` tail needs fresh post-fix measurement
  - the first generic country-count / non-BG broadening pass regressed both
    seats and should not be repeated blindly
  - the first targeted planner-side Europe-control-denial patch improved a tiny
    `10+10` probe but failed a larger `20+20` probe (`45%` USSR seat, `15%` US
    seat) and is rejected
  - widening the root to `search_candidate_limit=2` with `proposal_limit=12`
    is currently rejected on throughput under the old tighter budget, but can
    be reconsidered now that the active runtime budget is relaxed
  - keep exact region-score-delta proposal fixes, but reject any planner-side
    additions that push selfplay back above the target budget without a clear
    both-seat gain
  - the current highest-ROI loop is the fast exact-delta baseline plus cheap
    sequential both-seat tuning and lighter-weight proposal changes; only add
    new structural heuristics if they beat that tuned baseline, not just a
    hand-picked trace
  - the next highest-ROI loop from this baseline is:
    - first rerun the post-fix baseline on `200+200`, then `800+800`
    - then compare matched-seed candidates `proposal_limit_us=12` and
      `proposal_europe_support_pressure_bonus=0.0`
    - then continue US-side-only breadth and weight tuning for generic
      scoring/play quality
- Treat performance as a hard part of strength work:
  - prefer changes that improve both candidate quality and throughput
  - use all local CPU cores when running experimental benchmark or tuning jobs
  - the active runtime budget is now roughly `30s/game`; only prioritize speed
    work ahead of strength work when the candidate branch drifts materially
    above that budget or leaves straggler games that make 50-100 game
    evaluation impractical
  - current evaluation budgeting should assume:
    - `50` games per seat is cheap enough for screening
    - `200` games per seat is the minimum serious candidate check
    - `800` games per seat is the promotion gate for a new working baseline
- Host-process hygiene is mandatory:
  - remember that sandboxed sessions can hide still-running host-side CPU
    burners; always verify with host `ps` / `pgrep`, not just tool session state
  - before launching a new long benchmark or profiling batch, check for stale
    experimental workers and kill them if they are no longer needed
  - after any timeout, interrupted profile, or abandoned trace, run the cleanup
    recipe below
- Host cleanup recipe:
  - inspect: `ps -eo pid,etime,pcpu,pmem,args --sort=-pcpu | head -n 30`
  - narrow: `pgrep -af 'ts_experimental_(matchup|selfplay|spsa)'`
  - terminate specific stale workers: `kill -TERM <pid>...`
  - or pattern-kill abandoned experiments: `pkill -f 'ts_experimental_matchup ...'`
  - re-check with `ps` / `pgrep` until no unexpected experimental workers remain
- Use black-box tuning when the feature surface is ready:
  - prefer paired-seed, both-seat SPSA or nearby random search over ad hoc
    constant edits once key weights are exposed in `HeuristicConfig`
  - keep the best-so-far parameter vector, not just the latest candidate
- Reuse exact engine primitives from `cpp/tscore` for legality, state
  transitions, scoring, and data tables.
- Do not use `minimal_hybrid` as a policy, scorer, or proposal source here.
