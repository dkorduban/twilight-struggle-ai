# Experimental Python Wrappers

This directory mirrors the isolated native heuristic stack.

Local rules:
- Keep wrapper and smoke code isolated here.
- Prefer direct access to the experimental native module over touching legacy
  `tsrl` APIs.
- Main autonomous rule: keep selecting the highest-ROI next step without asking
  for confirmation until the experimental heuristic meets the tiered goal:
  1) decisively beat MinimalHybrid, then
  2) restart the same loop and keep iterating until it decisively beats the
  reference learned policy too.
  Work in a loop: re-read prompt and current results, update plan, implement,
  benchmark, analyze failures, and repeat until the goal is met. After every
  benchmark, if the current tier is not satisfied, immediately start the next
  loop rather than stopping on partial progress.
- OODA loop:
  1) Observe:
     - re-read this `AGENTS.md` file before starting the new iteration so the
       latest autonomy and cleanup rules are in force
     - re-read the prompt and current benchmark / trace outputs
     - extract the dominant failure modes by seat and terminal cause
  2) Orient:
     - update the roadmap / exposed config if the bottleneck changed
     - reduce the problem to one seat and one failure family
  3) Decide:
     - expose or support the single highest-ROI native change or benchmark flow
  4) Act:
     - run the benchmark / tuning pass needed to validate that change using the
       active evidence ladder:
       - `50` games per seat: screening only
       - `200` games per seat: tentative candidate validation
       - `800` games per seat: baseline promotion / rejection
     - do not use any sample below `50` games per seat for ranking,
       promotion, or rejection
  5) Loop:
     - before restarting, re-read this policy again and confirm the active
       bottleneck and stop conditions are still current
     - after each completed OODA iteration, re-read this policy before the
       next benchmark, tuning run, or code change so the latest loop rules stay
       active
     - if the current tier is still unmet, restart immediately
- Current loop priority:
  - corrected cause labels are mandatory before using loss-mode analytics:
    earlier mid-turn `vp_threshold` wins were misclassified as
    `europe_control`
  - the latest corrected `800+800` baseline is now the authority:
    - `search` as USSR vs `minimal`: `450/800 = 56.25%`
    - `search` as US vs `minimal`: `98/800 = 12.25%`
  - the latest accepted working baseline on the newer Europe-support branch is
    `31-19` on a clean explicit-seed `50`-game USSR-seat validation and `7-43`
    on the matching US-seat validation; that branch is accepted because it
    lifts the USSR seat to `62%` while preserving the post-patch US-side gain
    at `14%`
  - that accepted branch is now the default working baseline and comes from a
    cheap Europe non-battleground support / country-count pressure bonus in the
    native proposal `PrepScoring` lane
  - a real experimental scoring-card bug is now fixed:
    - must-play scoring cards could be dropped by shortlist truncation and then
      bypassed by fallback action selection
    - known failing US seed `448498040` no longer ends
      `scoring_card_held` after the fix
  - the first generic non-BG broadening pass regressed both seats, so do not
    optimize the wrapper around that direction
  - the first targeted planner-side Europe-denial patch also failed its larger
    `20+20` probe and should stay rejected
  - the wider-root config (`proposal_limit=12`, `search_candidate_limit=2`) is
    too slow for the old tighter budget; with the new `~30s/game` budget it may
    be reconsidered if it materially improves both-seat strength
  - favor wrapper/config and benchmark support that improves generic
    scoring/play quality first, because the corrected weak-seat loss mix is
    dominated by `vp` and `turn_limit`, not `europe_control`; remeasure the
    old `scoring_card_held` tail on the post-fix baseline before using it for
    prioritization
  - next wrapper/benchmark support priority:
    - rerun post-fix `200+200`, then `800+800`
    - compare matched-seed candidates `proposal_limit_us=12` and
      `proposal_europe_support_pressure_bonus=0.0`
    - then continue US-side-only breadth and weight tuning
- Performance and tuning are part of the same loop:
  - move wrapper/config support forward whenever it unlocks 50-100 game
    benchmark runs, parallel evaluation, or SPSA-style tuning
  - prefer exposing native `HeuristicConfig` fields over duplicating logic in
    Python
- Remember the host/sandbox split:
  - a finished or missing sandbox session does not prove the host process died
  - before or after long native runs, verify host-side workers with `ps` /
    `pgrep`
  - cleanup recipe for stale experimental workers:
    `ps -eo pid,etime,pcpu,pmem,args --sort=-pcpu | head -n 30`
    `pgrep -af 'ts_experimental_(matchup|selfplay|spsa)'`
    `kill -TERM <pid>...` or `pkill -f 'ts_experimental_matchup ...'`
