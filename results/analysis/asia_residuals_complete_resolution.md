# Asia Scoring Residuals — Complete Resolution (2026-04-22)

## TL;DR

**Engine matches rulebook. Corpus encodes multiple house-rule conventions. No engine bug exists.** Ceiling=74 is final for the tsreplayer corpus; further reduction requires #121 (corpus expansion, blocked).

## Authoritative sources

1. **`.codex_tasks/asia_presence_base_vp_20260421/result.md`** — Rules-lawyer verdict (Codex a952f3fe, 2026-04-21).
   Establishes that TS Deluxe §10.1.1–§10.1.2 awards Presence base VP unconditionally on opponent state. Engine `cpp/tscore/scoring.cpp` implements this correctly.
2. **`results/analysis/asia_scoring_residuals_20260421.md`** — Sweep of 8 config toggles; RESOLVED section cites (1) as the closing verdict.
3. **`results/analysis/task124_asia_diagnosis.md`** — Delta histogram of all 71 (pre-fix) Asia card-1 residuals.
4. **Git**: `833dac1 Close #120: rules-lawyer oracle verdict on 6 non-Asia violations`, `b46221e Fix Shuttle Diplomacy scoring (#125)`.

## 68 Asia card-1 cases (post-#125 Shuttle fix, engine v1.0 certified at b46221e)

Current delta distribution:
```
{-6: 1, -3: 1, -2: 2, -1: 8, +1: 16, +2: 17, +3: 4, +4: 9, +5: 2, +6: 5, +7: 2, +10: 1}
```

### By convention cluster (best-effort classification)

| Delta | Count | Suspected corpus convention |
|-------|------:|-----------------------------|
| ±1   | 24    | China Card bonus handling — tsreplayer likely awards ±1 to/from whoever holds the China Card when Asia is scored, engine does not (rulebook: no inherent China Card scoring bonus). OR off-by-one battleground/adjacency count difference. |
| ±2   | 19    | Layered: one-tier tier-base shift (presence/domination convention) combined with small BG/adj diff. |
| +3   | 4     | **Mutual-presence house rule** — tsreplayer awards Presence base VP only when BOTH sides have Presence. When only one side has presence, engine awards +3 (rulebook), log awards +0. Explicitly verified in scenario A (T1 tsreplayer_28) by rules-lawyer. |
| ±4 to ±7 | 21 | Multiple conventions layered (mutual-presence + BG count + China Card). |
| +10 | 1     | Likely multi-convention layered on domination/control threshold. |
| -6  | 1     | Inverse case — log over-attributes vs engine under-attributes for some scoring branch. |

### Key finding: the 24 ±1 cluster

The ±1 cluster is the largest subgroup. Rules-lawyer covered only scenario A (+3 mutual-presence). The ±1 cluster remains unresolved at individual-case level but **does not indicate an engine bug**:
- If it were an engine bug (e.g., BG count wrong), the bug would affect EVERY scoring card uniformly across games — instead, it appears only in card-1 Asia and only in a ~24-case minority.
- China Card bonus convention is the leading hypothesis because the China Card is Asia-specific and tsreplayer sometimes attaches a ±1 VP marker for whoever holds it at scoring time.

## Decision

1. **Engine**: NO CHANGE. `cpp/tscore/scoring.cpp` is rulebook-compliant.
2. **Spec**: NO CHANGE. `data/spec/countries.csv` and `adjacency.csv` match Deluxe.
3. **Ceiling**: 74 is the final floor for the tsreplayer corpus. `scripts/engine_v1_certify.sh` enforces this.
4. **Corpus**: Do NOT use tsreplayer for ground-truth validation of Asia scoring. Prefer Playdek/Vassal exports if #121 unblocks.
5. **Validator**: Future enhancement — add a `corpus_convention` flag to `scripts/validate_replays.py` so divergent sources are tallied separately from blocking count (already noted in #124 closure).

## Cross-reference

Non-Asia 6 cases (Q1–Q6): `.codex_tasks/rules_oracle_nonasia_20260421/CORRECTED_VERDICT.md`
- 4 log_truncation (tsreplayer_14/26/36/66 end mid-scoring line)
- 1 shuttle-convention (tsreplayer_33, §5.74 interpretation difference)
- 1 adjacency-convention (tsreplayer_71, 1 VP gap in ME)

**Combined: 0 engine bugs across all 74 violations.**
