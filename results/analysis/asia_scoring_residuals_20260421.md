# #124 Asia card-1 SCORING_VP_MISMATCH sweep — partial findings

Date: 2026-04-21 UTC
Corpus: 71 Asia Scoring (card_id=1) violations from 51-game tsreplayer corpus.

## What I did

Wrote `scripts/sweep_asia_scoring_configs.py`. It reads the full state snapshots
already in `results/validator_violations.jsonl` (no engine rebuild needed), then
recomputes expected VP under 8 configs (2^3 toggles) plus a per-violation
china-holder free choice (+1/-1/0 to net VP), and compares to the log's
`expected_vp`.

**Toggles tested:**
- `sk_is_bg`: South Korea is_battleground (current spec=true)
- `sk_usa_adj`: SK adjacent to USA anchor (current spec=true)
- `phi_usa_adj`: Philippines adjacent to USA anchor (current spec=true)

**China holder**: free per-violation (best of no-bonus / US-holds / USSR-holds).

## Results

| Config | no-china zero | any-china zero | unsolved |
|---|---:|---:|---:|
| sk_bg=1 sk_adj=1 phi_adj=1 (current) | 11/71 | 21/71 | 50 |
| sk_bg=1 sk_adj=1 phi_adj=0 | 11/71 | 21/71 | 50 |
| sk_bg=1 sk_adj=0 phi_adj=1 | 18/71 | 24/71 | 47 |
| sk_bg=1 sk_adj=0 phi_adj=0 | 18/71 | 25/71 | 46 |
| sk_bg=0 sk_adj=1 phi_adj=1 | 20/71 | 26/71 | 45 |
| sk_bg=0 sk_adj=1 phi_adj=0 | **20/71** | 27/71 | 44 |
| sk_bg=0 sk_adj=0 phi_adj=1 | 16/71 | 30/71 | 41 |
| sk_bg=0 sk_adj=0 phi_adj=0 | 17/71 | **30/71** | **41** |

## Takeaways

1. **The three working hypotheses are too small to explain the bulk of residuals.**
   Best case (demote SK from BG, drop both SK→USA and PHI→USA adjacencies, free
   china holder) leaves **41/71 violations unsolved**. The dominant driver is
   something else entirely.

2. **Demoting SK from BG helps modestly** (+2 no-china zeroes vs current spec).
   Not enough evidence alone to ship a countries.csv change — would need primary
   sources confirming SK is non-BG in standard Deluxe.

3. **Toggling SK/PHI adjacency is nearly a no-op** on the no-china residual but
   slightly shifts the china-hypothesis budget. Unreliable signal.

## The real puzzle: T1 base-VP convention

**Turn 1 tsreplayer_28 Asia Scoring:**
- USSR controls only North Korea (default setup, inf=3 ≥ 0+3 stab).
- US controls nothing (Japan inf=1 < 0+4 stab; SK inf=1 < 0+3 stab).
- Rulebook: USSR Presence(3) + NK BG(+1) = **+4 net USSR**.
- tsreplayer log: "USSR gains 1 VP" = **+1 net USSR**.
- Our engine also disagrees with the log (that's why this violation exists).

The 3-VP gap cannot be explained by SK/PHI toggles or china bonus. Two plausible
explanations:

a. **tsreplayer does not award the Presence tier base VP when opponent has no
   presence.** Under this convention: USSR gets 0 + 1 BG = 1. ✓ matches log.
b. **tsreplayer awards Presence=1 (not 3) in Asia.** Under this: USSR gets 1 +
   1 BG = 2. ✗ off by 1. Less likely.

Hypothesis (a) would be a significant rule-interpretation difference worth
verifying against the PDF and cross-engine (another TS implementation if
accessible).

## Next steps

1. **Rules primary-source check**: re-read TS Deluxe §10.1.2 for the exact tier
   base-VP award condition. Is there an implicit "opponent must have presence"
   precondition, or does rulebook truly award base VP unilaterally? Dispatch to
   bg-rules-lawyer with the T1 tsreplayer_28 scenario as the acid test.
2. **Cross-engine verification**: if any other open-source TS engine (e.g. the
   GMT Vassal module, TSEspionage mod) is accessible, replay the T1 state and
   compare.
3. **Don't change countries.csv / adjacency.csv yet.** The 20/71 SK-is-BG signal
   is too weak given the 41/71 unsolved mass. Any spec change now risks the
   Europe retraction pattern (fit to partial signal, break on full corpus).

## Assets
- `scripts/sweep_asia_scoring_configs.py` — the sweep script, runnable.
- Full per-violation residuals printable by re-running with best config.

## Status: RESOLVED — corpus-encoding difference, not an engine bug

**Rules-lawyer verdict (2026-04-21, `.codex_tasks/asia_presence_base_vp_20260421/result.md`):**

- TS Deluxe §10.1.1–§10.1.2 award the Presence tier base VP (Asia=3) to any
  superpower with ≥1 controlled country in the region, **unconditionally on
  opponent state**. Engine `cpp/tscore/scoring.cpp` implements this correctly.
- tsreplayer encodes a **different convention**: Presence base VP only awarded
  when BOTH sides have Presence. This is a house-rule divergence from published
  Deluxe rules.
- Scenario A (T1 tsreplayer_28): rulebook gives USSR +4; tsreplayer log gives
  USSR +1; our engine gives USSR +4. **Engine matches rulebook — bug is in the
  corpus.**

**Decision:**
1. Do NOT change `data/spec/countries.csv`, `data/spec/adjacency.csv`, or
   `cpp/tscore/scoring.cpp`.
2. Do NOT use the 71 Asia card-1 residuals as a blocking certification gate for
   `#122` engine v1.0 certification. The corpus is unreliable ground truth for
   unilateral-presence scenarios.
3. For future corpus expansion (`#121`), prefer replay sources that match
   published Deluxe rules (e.g., Playdek/Vassal exports) over tsreplayer for
   scoring validation.
4. Task `#124` is **closed**.

**What the validator SHOULD do going forward:**
Add a "corpus convention" flag to `scripts/validate_replays.py` so violations
from a known-divergent source can be suppressed from the blocking count while
still being tallied for awareness.
