# A/B Test: Cold-Start vs Warm-Start — v73

**Date:** 2026-04-01
**Dataset:** data/combined_v73 (11 files: heuristic_anchor + v67-68,70-72 vsh_filtered + v67-68,70-72 selfplay)
**Benchmark:** 200 games vs heuristic, seed=9999, C++ engine (ts_collect_selfplay_rows_jsonl), USSR side

---

## Summary Table

| Model          | Checkpoint                         | Best val_loss | Best epoch | Epochs run | Win% vs heuristic |
|----------------|------------------------------------|--------------|------------|------------|-------------------|
| v72 (cold)     | data/checkpoints/retrain_v72/      | 1.6729       | 120        | 120        | 8.2%              |
| v73 cold-start | data/checkpoints/retrain_v73/      | 1.6621       | 117        | 120        | 11.7%             |
| v73 warm-start | data/checkpoints/retrain_v73_warm/ | 1.5766       | 2          | 10         | 9.7%              |

---

## Training Details

### v72 (baseline, cold-start, 120 epochs max)
- **val_loss:** 1.6729 at epoch 120 (kept improving throughout, no early stop triggered)
- **val_card_top1:** 0.945, val_mode_acc: 0.969, val_country_ce: 0.5820
- **Win%:** 8.2% (16/194 decisive, 6 draws, 200 games)
- **Notes:** Full 120-epoch run with slow continued improvement; crashed after training on teacher_search step

### v73 cold-start (same config as v72: 120 epochs max, patience=12, lr=2.4e-3)
- **val_loss:** 1.6621 at epoch 117
- **val_card_top1:** 0.945, val_mode_acc: 0.969, val_country_ce: 0.5788
- **Win%:** 11.7% (23/196 decisive, 4 draws, 200 games)
- **Improvement vs v72:** -0.0108 val_loss, +3.5pp win rate
- **Notes:** Trained on new v72 data (vs_heuristic + vs_v71 selfplay); win rate improvement substantial (+43% relative)

### v73 warm-start (init from v72 checkpoint, 60 epochs max, patience=8, lr=2.4e-3)
- **val_loss:** 1.5766 at epoch 2
- **val_card_top1:** 0.954, val_mode_acc: 0.975, val_country_ce: 0.5212
- **Win%:** 9.7% (19/195 decisive, 5 draws, 200 games)
- **Early stop:** Epoch 10 (8 epochs no improvement after epoch 2)
- **Improvement vs v72 cold:** -0.0963 val_loss (-5.7% relative)
- **Improvement vs v73 cold:** -0.0855 val_loss (-5.1% relative)
- **Training time:** ~10 epochs (~5 min) vs 120 epochs (~35 min) for cold-start (~7x faster)
- **Notes:** Starts at val_loss=1.5771 on epoch 1 — already beats cold-start's final best of 1.6621

---

## Detailed Warm-Start Epoch Progression

| Epoch | val_loss | card_top1 | card_nll | mode_acc | val_value_mse |
|-------|----------|-----------|----------|----------|---------------|
| 1     | 1.5771   | 0.955     | 0.1778   | 0.975    | 0.1788        |
| 2 (best) | 1.5766 | 0.954   | 0.1781   | 0.976    | 0.1774        |
| 3     | 1.5796   | 0.953     | 0.1803   | 0.975    | 0.1760        |
| 10 (stop) | ~1.63 | ~0.943  | ~0.193   | ~0.972   | ~0.169        |

---

## Historical Win Rate Context (selected gens)

| Version | Win% vs heuristic | Notes |
|---------|-------------------|-------|
| v60     | 17.9%             |       |
| v61     | 18.5%             | peak  |
| v64     | 16.8%             |       |
| v65     | 17.4%             |       |
| v66     | 15.5%             |       |
| v68     | 15.7%             |       |
| v69     | 8.7%              | DEGRADED — excluded from training |
| v70     | 13.7%             |       |
| v71     | 12.5%             |       |
| v72     | 8.2%              |       |
| v73 cold | 11.7%            |       |
| v73 warm | 9.7%             |       |

---

## Key Findings

### val_loss winner: warm-start (by a large margin)
- Warm-start achieves val_loss=1.5766 vs cold-start's 1.6621 — **-5.1% improvement**
- Warm-start reaches its best in 2 epochs; cold-start needs 117 epochs
- Warm-start is ~7x faster to converge
- All supervised metrics favor warm-start: card_top1 (0.954 vs 0.945), mode_acc (0.975 vs 0.969), country_ce (0.521 vs 0.579)

### win-rate winner: cold-start (marginally)
- Cold-start wins 11.7%, warm-start wins 9.7% — a 2pp gap favoring cold-start
- With 200 games at ~10% win rate, the 95% CI is approximately ±4.3pp — this gap is within noise
- The result is not statistically significant at p<0.05

### Interpretation
The val_loss gap clearly favors warm-start (better imitation of training distribution), but the win rate does not follow. Possible explanations:

1. **OneCycleLR with warm-start may cause suboptimal game behavior**: the LR peaks early when the model is already near a good basin, potentially causing overshoot and then early convergence to a local minimum with good loss but suboptimal exploration
2. **Sample variance dominates at n=200**: a 2pp difference is noise; both models are likely within 1-2pp of each other in expectation
3. **v72 weights encode game-play priors that don't match v73 data distribution**: the warm-start may be fitting v73 data to a v72 prior that's slightly miscalibrated

### Data quality note
Both v72 and v73 show lower win rates (8-12%) than the v60-v68 era (14-18%). The rolling window now excludes degraded v69 data but the recovery is incomplete. The training mix includes v67-68 data from a lower-quality era; as newer gens cycle in, win rates should recover.

---

## Recommendations

1. **Use cold-start v73 as the production checkpoint** (higher win rate, 11.7%)
2. **Warm-start is promising but needs a lower LR**: try max_lr=1.0e-3 instead of 2.4e-3 for warm-start; the high LR may cause the early-epoch burst followed by stagnation
3. **Extend patience to 12 for warm-start** to give value head more time to adapt to new data distribution
4. **Run 500-game benchmark** before drawing strong conclusions — 200 games is insufficient for 2pp differences
5. **Fix the pipeline teacher_search crash**: positions from C++ vsh collection lack full state_dict (hands/deck/flags); teacher_search.py should gracefully skip unvalidatable positions rather than hard-exiting, or use a `--skip-validation` flag

---

## Pipeline Notes

- combined_v72 was reconstructed from combined_v71 rolling window (dropped v65 as too old, dropped v69 as degraded)
- Pipeline crashed on teacher_search.py validation error (partial state_dict in C++ collection output)
- filter_bad_games.py, combined_v73 assembly, and v73 pipeline launch were done manually
- DEFCON-1 rate for v72 collection: 8.7% (within target range of <25%)

---

## File Locations

- Cold-start checkpoint: `data/checkpoints/retrain_v73/baseline_best.pt`
- Warm-start checkpoint: `data/checkpoints/retrain_v73_warm/baseline_best.pt`
- Cold benchmark JSON: `results/bench_v73_cold.json`
- Warm benchmark JSON: `results/bench_v73_warm.json`
- v72 benchmark JSON: `results/bench_v72.json`
- Cold training log: `logs/train_v73.log`
- Warm training log: `logs/train_v73_warm.log`
- Combined v73 data: `data/combined_v73/` (11 files)
