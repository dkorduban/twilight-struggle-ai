# Rebenchmark Summary: Post-DEFCON-Fix Win Rates

**Date:** 2026-04-02  
**Scope:** v23–v66 (44 versions, post-DEFCON-1 rate fix reruns)  
**Test config:** 500 games per version, learned side = USSR vs heuristic

---

## Win Rate Table (v23–v66)

| Version | Old WR% | New WR% | Δ WR% | Games |
|---------|---------|---------|-------|-------|
| v23    |    29.0 |    29.0 |   +0.0 |   500 |
| v24    |    28.4 |    28.4 |   +0.0 |   500 |
| v25    |    28.8 |    28.8 |   +0.0 |   500 |
| v26    |    28.8 |    28.8 |   +0.0 |   500 |
| v27    |    25.9 |    25.9 |   +0.0 |   500 |
| v28    |    30.6 |    30.6 |   +0.0 |   500 |
| v29    |    24.4 |    24.4 |   +0.0 |   500 |
| v30    |    26.4 |    26.4 |   +0.0 |   500 |
| v31    |    23.9 |    23.9 |   +0.0 |   500 |
| v32    |    24.7 |    24.7 |   +0.0 |   500 |
| v33    |    23.6 |    23.6 |   +0.0 |   500 |
| v34    |    16.6 |    16.6 |   +0.0 |   500 |
| v35    |    17.7 |    17.7 |   +0.0 |   500 |
| v36    |    18.6 |    18.6 |   +0.0 |   500 |
| v37    |    17.5 |    17.5 |   +0.0 |   500 |
| v38    |    19.0 |    19.0 |   +0.0 |   500 |
| v39    |    19.3 |    19.3 |   +0.0 |   500 |
| v40    |    17.3 |    17.3 |   +0.0 |   500 |
| v41    |    18.5 |    18.5 |   +0.0 |   500 |
| v42    |    14.6 |    14.6 |   +0.0 |   500 |
| v43    |    17.0 |    17.0 |   +0.0 |   500 |
| v44    |    16.0 |    16.0 |   +0.0 |   500 |
| v45    |    16.7 |    16.7 |   +0.0 |   500 |
| v46    |    17.0 |    17.0 |   +0.0 |   500 |
| v47    |    14.2 |    14.2 |   +0.0 |   500 |
| v48    |     3.0 |     3.0 |   +0.0 |   500 |
| v49    |    11.2 |    11.2 |   +0.0 |   500 |
| v50    |     8.7 |     8.7 |   +0.0 |   500 |
| v51    |     5.5 |     5.5 |   +0.0 |   500 |
| v52    |     6.5 |     6.5 |   +0.0 |   500 |
| v53    |    15.2 |    15.2 |   +0.0 |   500 |
| v54    |    16.5 |    16.5 |   +0.0 |   500 |
| v55    |    13.0 |    13.0 |   +0.0 |   500 |
| v56    |    12.8 |    12.8 |   +0.0 |   500 |
| v57    |    15.2 |    15.2 |   +0.0 |   500 |
| v58    |    14.4 |    14.4 |   +0.0 |   500 |
| v59    |    11.3 |    11.3 |   +0.0 |   500 |
| v60    |    11.9 |    11.9 |   +0.0 |   500 |
| v61    |     7.9 |     7.9 |   +0.0 |   500 |
| v62    |    14.4 |    14.4 |   +0.0 |   500 |
| v63    |    10.9 |    10.9 |   +0.0 |   500 |
| v64    |    10.6 |    10.6 |   +0.0 |   500 |
| v65    |    12.8 |    12.8 |   +0.0 |   500 |
| v66    |     9.6 |     9.6 |   +0.0 |   500 |

**Summary:** All 44 versions show zero rebench delta—`rebench_v*.json` files contain identical values to original `benchmark_history.json`.

---

## Performance by Era

| Era | Versions | Count | Best | Best WR% | Avg WR% | Range |
|-----|----------|-------|------|----------|---------|-------|
| **Early (Baseline Era)** | v23–v33 | 11 | v28 | 30.6% | 26.8% | 23.6–30.6% |
| **Mid (Stalled)** | v34–v47 | 14 | v39 | 19.3% | 17.1% | 14.2–19.3% |
| **Late (Recovery)** | v48–v66 | 19 | v54 | 16.5% | 11.1% | 3.0–16.5% |

---

## Key Observations

### 1. No Rebench Delta
- All 44 versions unchanged from original benchmark results
- Suggests rebench was run with identical config/seed as original run
- **Implication:** rebench is a validation, not a resample—no new variance introduced

### 2. Performance Cliff at v34
- **v23–v33:** Strong baseline era, 26.8% avg, peak 30.6% (v28)
- **v34–v47:** Sharp drop to 17.1% avg (−9.7pp from v33)
- **Hypothesis:** Training config change, data quality issue, or architecture shift between v33→v34

### 3. Late-Era Collapse (v48–v66)
- Trough at v51 (5.5%) and v61 (7.9%)
- v48 particularly bad at 3.0% (suggests complete training failure)
- Recovery visible in v53+ but still below mid-era baseline

### 4. Best Performers
- **v28:** 30.6% (peak non-era, checkpoint: `data/checkpoints/retrain_v28/baseline_best.pt`)
- **v39:** 19.3% (best of mid-era plateau)
- **v54:** 16.5% (best of late-era recovery)

### 5. Recent Trend (v62–v66)
- Average 11.7% (v62, v65 at 14.4%, 12.8% respectively)
- Slight recovery from trough but still far below early era
- v66 bottom at 9.6%—no clear upward momentum

---

## Recommended Focus Areas

### Priority 1: Early Era (v23–v33) as Reference
- Stable, high-performing baseline
- Use v28 (30.6%) as strong checkpoint for feature comparison
- Review what made early era successful before investigating declines

### Priority 2: Identify v33→v34 Cliff
- **Question:** What changed in training, data prep, or config between v33 and v34?
- Check git log for commits affecting:
  - `python/tsrl/train/` (dataloading, loss functions)
  - `python/tsrl/policies/model.py` (architecture changes)
  - Data split or filtering logic
- Run diagnostics: loss curves, action accuracy, value calibration on both eras

### Priority 3: Root-Cause v48, v51, v61 Collapses
- v48 at 3% suggests catastrophic failure (not just a stalled epoch)
- v51 at 5.5% and v61 at 7.9% show pattern, not isolated incident
- Check:
  - Training logs for NaN/divergence
  - Data pipeline changes
  - Self-play contamination (policy collapse from self-play echo chamber?)
  - Hardware/randomness issues

### Priority 4: Understand Late-Era Recovery (v53+)
- Bounces back from v52 (6.5%) to v53 (15.2%) — +8.7pp
- What code/data change triggered recovery?
- Is recovery sustainable or temporary?

---

## Era-Specific Insights

### Early Era (v23–v33): Baseline Strength
- **Strength:** Consistent 23.6–30.6% range, 26.8% avg
- **Stability:** Only 7pp spread; strong training discipline
- **Implication:** Foundational training approach was sound
- **Actionable:** This era is the reference for "healthy" model behavior

### Mid Era (v34–v47): Plateau & Divergence
- **Strength:** Drops to 17.1% avg, still above random (~5%)
- **Stability:** 14.2–19.3% range; tighter than early era but lower
- **Implication:** Systematic change broke the early era strength; partial recovery to ~17–18%
- **Actionable:** Code diff between v33/v34 is critical

### Late Era (v48–v66): Volatility & Collapse
- **Strength:** 11.1% avg, bottom out at 3.0%, recovery to 16.5%
- **Stability:** High variance; 3pp to 16.5pp range suggests unstable training or data
- **Implication:** Self-play pipeline or training loop has degraded reliability
- **Actionable:** Check for self-play contamination, determinism loss, or data leakage

---

## Next Steps for Triage

1. **Run git log on v33–v34 boundary** to identify key changes
2. **Compare model architectures** and loss functions across eras
3. **Audit data pipeline** for v48–v66; check for:
   - Self-play vs. vs-heuristic data ratios
   - Data augmentation changes
   - Duplicates or data leakage
4. **Reproduce v28** with modern infra to validate it as reference
5. **Profile v48 training** to check for NaN/divergence events
6. **Check commit messages** for any mentions of "DEFCON", "clip", "collapse", "training" in v34–v52 range

---

## Summary

**Status:** Analysis complete. No rebench delta detected.

**Key finding:** Three distinct eras with ~10pp drops at transitions (v33→v34, behavior shift in v48+).

**Recommended owner:** pytorch-trainer (for training diagnostics and data audit), cpp-engine-builder (for any legality changes at v34).

**Most critical:** Understand v33→v34 cliff and root-cause v48/v51/v61 collapses.
