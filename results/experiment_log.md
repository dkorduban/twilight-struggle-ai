# Experiment Log

Running record of data collection, training, and benchmark runs.
Newest entries at top.

---

## 2026-04-02: Combined bid2 training (60 epochs)

**Tag:** `combined_bid2_15k_60ep`
**Status:** Complete

**Data:**
| Source | Rows | Config |
|---|---|---|
| `heuristic_10k_bid2_t05_t20.parquet` | 1,100,000 | USSR T=0.5, US T=2.0, bid+2, human openings (Iran+1) |
| `imitation_5k_t1_t1_bid2.parquet` | 248,049 | USSR T=1.0, US T=1.0, bid+2, human openings (Iran+1) |
| **Total** | **1,348,049** | |

Note: The 10k source parquet has 1,507,847 rows but the copy in `data/combined_bid2_15k/`
was made from an earlier truncated conversion (1,100,000 rows). Accepted as-is.

**Hyperparameters:**
- epochs: 60, batch_size: 1024, lr: 5e-4, OneCycleLR
- hidden_dim: 256, dropout: 0.1, weight_decay: 1e-4
- value_target: final_vp, value_weight: 1.0
- advantage_weight: 0.0 (pure BC), model_type: baseline
- bench-after-train: 500 games

**Results:**
- Val card_top1: 71.9%, card_top3: 84.1%, mode_acc: 95.3%, best val_loss: 2.4306 (epoch 58)
- Learned as USSR vs greedy heuristic: **36.4%** WR (177/500, 14 draws)
- Marginal gain over T=1 baseline (+1.3 pp), still below heuristic_repro_v1 (40.3%)
- No overfitting detected (train_loss ~ val_loss at convergence)

**Checkpoint dir:** `data/checkpoints/combined_bid2_15k_60ep/`
**W&B:** auto-logged

---

## 2026-04-02: Imitation learning T=1 baseline

**Tag:** `imitation_t1_baseline`

**Data:**
| Source | Rows | Config |
|---|---|---|
| `imitation_5k_t1_t1_bid2.parquet` | 248,049 | 5k games, USSR T=1.0, US T=1.0, bid+2, human openings |

**Hyperparameters:**
- epochs: 20, batch_size: 256, lr: 3e-4, OneCycleLR
- hidden_dim: 256, dropout: 0.1, weight_decay: 0.0
- value_target: final_vp, value_weight: 1.0
- advantage_weight: 0.0 (pure BC)

**Results:**
- Val card_top1: 69.8%, mode_acc: 93.9%, best val_loss: 2.9461
- Learned as USSR vs heuristic T=1: **35.1%** WR
- Learned as US vs heuristic T=1: **13.4%** WR
- Conclusion: pure BC on noisy T=1 data underperforms the teacher significantly

**Checkpoint dir:** `data/checkpoints/imitation_t1_baseline/`

---

## 2026-04-02: Temperature matrix sweep (6x6, bid+2)

**Tag:** `heuristic-temp-matrix-bid2`

**Config:** 1000 games/cell, bid+2, human openings (Iran+1), temps [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
**W&B:** https://wandb.ai/korduban-ai/twilight-struggle-ai/runs/p6nf1e0x

**USSR WR matrix:**
```
           us=0.5  us=1.0  us=1.5  us=2.0  us=3.0  us=5.0
ussr=0.5    70.5    68.3    67.8    65.0    67.6    65.9
ussr=1.0    71.8    66.9    64.9    66.8    67.2    68.0
ussr=1.5    71.2    67.7    69.9    63.6    65.7    67.1
ussr=2.0    69.3    69.5    67.2    64.3    62.0    68.1
ussr=3.0    68.1    67.9    65.5    66.5    63.5    65.5
ussr=5.0    64.9    64.3    63.2    62.1    61.6    64.4
```

**Nash equilibrium (mixed strategy):**
- USSR: T=0.5 (34.0%), T=1.0 (32.3%), T=3.0 (33.7%)
- US: T=1.5 (37.8%), T=2.0 (61.1%), T=3.0 (1.2%)
- Game value: USSR 66.09%, US 33.91%

Hardcoded as `kNashUSSRTemps` / `kNashUSTemps` in `cpp/tscore/human_openings.hpp`.
Available via `--nash-temperatures` flag on benchmark and collection binaries.

---

## 2026-04-02: 1D temperature sweep (bid+2)

**Tag:** `heuristic-temp-sweep-human-openings-bid2`

**Config:** 1000 games/matchup, bid+2, human openings (Iran+1)
**W&B:** https://wandb.ai/korduban-ai/twilight-struggle-ai/runs/frjg92l6

**Key findings:**
- USSR sweep (vs greedy US): peaks at T=1.0 (73.4% WR), collapses at T=10 (41.4%)
- US sweep (vs greedy USSR): peaks at T=5.0 (38.1% US WR), collapses at T=10 (23.0%)

---

## 2026-04-02: Human openings correction

Fixed `kHumanUSOpeningsBid2` in `human_openings.hpp` — extracted from 58 human games.
Previous version incorrectly added +2 to Italy; real data shows bid goes to Iran+1.

**USSR openings (58 games):**
- 50.0%: Austria+1, EG+1, Poland+4
- 41.4%: EG+1, Poland+4, Yugoslavia+1
- 8.6%: EG+1, Poland+5

**US openings (58 games, bid+2 = 9 total):**
- 75.9%: Italy+4, WG+4, Iran+1
- 10.3%: France+3, Italy+2, WG+3, Iran+1
- 8.6%: France+2, Italy+3, WG+3, Iran+1
- 1.7%: Canada+1, Italy+3, Turkey+1, WG+3, Iran+1
- 1.7%: France+1, Italy+3, WG+4, Iran+1
- 1.7%: Italy+3, WG+4 (no bid game)

---

## 2026-04-02: 10k heuristic data collection (bid+2)

**Output:** `data/selfplay/heuristic_10k_bid2_t05_t20/` (79 JSONL chunks)
**Parquet:** `data/selfplay/heuristic_10k_bid2_t05_t20.parquet` (1,507,847 rows, 177MB)
**Config:** 10k games, USSR T=0.5, US T=2.0, bid+2, human openings, seed=50000

---

## 2026-04-02: 5k imitation data collection (T=1/1)

**Output:** `data/selfplay/imitation_5k_t1_t1_bid2/` (13 JSONL chunks)
**Parquet:** `data/selfplay/imitation_5k_t1_t1_bid2.parquet` (248,049 rows)
**Config:** 5k games, USSR T=1.0, US T=1.0, bid+2, human openings, seed=70000

---

## Pre-2026-04-02: Historical context

- **Golden era (v23-v33):** Trained on pure vs-heuristic data, NO setup influence, NO bid.
  Best was v28 at 30.6% WR (USSR vs greedy heuristic).
- **heuristic_repro_v1:** 867k rows (413k v4 anchor + 454k T=0.5/2.0), NO bid, NO setup.
  Achieved 40.3% WR — beat golden era. But used old setup (no free influence phase).
- All models from v23-v88 used no-bid, no-setup configuration.
- Starting 2026-04-02: all new experiments use bid+2, human openings, correct Iran+1.
