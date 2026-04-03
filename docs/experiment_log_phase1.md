# Self-Play Experimentation Log — Phase 1

Started: 2026-04-03

## Baseline Reference Models (corrected +2 bid benchmark, 500 games/side)

| Model | Data | Rows | USSR WR | US WR | Combined | Notes |
|-------|------|------|---------|-------|----------|-------|
| v23 | combined_v23 (heur+selfplay) | 1.33M | 28.6% | 1.2% | 14.8% | Best old-gen, lr=0.0012, ls=0.05, NO setup inf |
| v24 | similar | ~1.3M | 28.3% | 3.0% | 15.6% | NO setup inf |
| v25 | similar | ~1.3M | 26.0% | 2.6% | 14.3% | NO setup inf |
| v28 | similar | ~1.3M | 26.9% | 2.2% | 14.4% | NO setup inf |
| combined_bid2_h256 | heur+imit | 1.35M | 39.4% | 6.8% | 23.1% | Pure BC, NO setup inf in data |
| heuristic_repro_v1 | heur | 910k | 36.4% | 7.2% | 21.8% | Pure BC, MIXED setup inf |
| imitation_t1 | imit | 248k | 31.6% | 4.8% | 18.2% | Pure BC, NO setup inf |
| exp_baseline_h128 | heur+imit | 1.35M | 26.6% | 4.0% | 15.3% | h128 (half capacity) |
| exp_control_feat_h128 | heur+imit | 1.35M | 29.8% | 4.4% | 17.1% | h128 + region scoring features |
| exp_marginal_value_h128 | heur+imit | 1.35M | 12.2% | 2.4% | 7.3% | h128 + BCE country head (broken) |
| v88_setup | heur w/setup | 39k | 18.2% | 0.4% | 9.3% | Correct setup inf, too small |

### Key insight: combined_bid2_h256 is actually best at 23.1% combined (39.4% USSR!)
- This model was trained on data WITHOUT setup influence but benchmarked WITH setup
- It outperforms v23 because it has 1.35M rows of diverse heuristic data
- v23's self-play advantage was masked by the old benchmark (no setup)

### Learned-vs-Learned (v88 self-play)
- v88 vs v88 (500 games): USSR 87.0% | US 12.8% | Draw 0
- Massive USSR advantage mirrors the game's inherent asymmetry

## Hyperparams (v23-proven baseline)

```
lr=0.0012, batch_size=1024, epochs=60, weight_decay=1e-4,
label_smoothing=0.05, one_cycle=True, hidden_dim=256,
value_target=final_vp, dropout=0.1
```

---

## Phase 0: Pre-Self-Play Fixes

### 0a. Dirichlet noise in collection
- Status: DONE (already implemented in mcts.cpp:521-549, called at line 594)
- For non-MCTS collection: epsilon-greedy and temperature sampling are the mechanisms

### 0b. Canonical training targets
- Status: DONE (already canonical — accessible countries sorted at policies.cpp:676)

---

## Phase 1 Generations

### Gen 0 (v89) — DONE
- Started: 2026-04-03 01:18 UTC
- Data: heuristic_10k_setup_bid2_nash (787k) + heuristic_10k_setup_bid2_nash_b (1.35M)
  - Total: 2.13M rows, 20k games, ALL with correct setup influence
  - Verified: US inf at turn 1 ranges 17-57, mean ~27 (all >14)
- Hyperparams: v23 recipe (lr=0.0012, ls=0.05, bs=1024, ep=60, patience=15)
- val_loss: 3.8682, card_top1: 65.2%, mode_acc: 83.3%, country_top1: 34.8%
- **USSR WR: 37.2%** | **US WR: 7.2%** | **Combined: 22.2%**
- Notes: Matches combined_bid2_h256 (23.1%). Pure heuristic BC baseline replicated.

### Gen 0b (v89b) — DONE (batch size experiment)
- Data: Same as v89 (2.13M rows)
- Hyperparams: bs=8192, lr=0.0024 (2× base), rest same
- val_loss: 3.9164, card_top1: 65.0%, mode_acc: 83.1%, country_top1: 35.0%
- **USSR WR: 38.8%** | **US WR: 7.2%** | **Combined: 23.0%**
- Training time: ~10 min (vs ~27 min for v89). **2.8× speedup, same or better WR.**
- **DECISION: Use bs=8192, lr=0.0024 for all future training.**

### Gen 1 (v90) — IN PROGRESS
- Status: Collecting learned-vs-heuristic data
- Data: Gen 0 data + learned_v89b_vs_heuristic (2000 games each side)
- Hyperparams: bs=8192, lr=0.0024 (fast recipe)
- Notes: First self-play generation. Using v89b as base model.
