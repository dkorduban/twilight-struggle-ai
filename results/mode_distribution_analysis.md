# Per-Mode Play Statistics: Heuristic vs Learned Model (v106) vs MCTS

Generated: 2026-04-06  
Model: `data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt` (TSControlFeatGNNModel)  
MCTS data: `mcts_v99c_s7_ussr_vs_heuristic_2k.jsonl` (v99c, 400 sim; used as MCTS proxy)  
Sample sizes: 200 games per agent/side for v106; 2000 games for MCTS-v99c data

---

## 1. Overall Mode Distribution (% of decisions per side)

| Mode       | Heuristic USSR | Heuristic US | v106 Greedy USSR | v106 Greedy US | MCTS-v99c USSR |
|------------|---------------:|-------------:|-----------------:|---------------:|---------------:|
| Influence  |         72.0%  |       67.2%  |          40.6%   |        63.5%   |         52.1%  |
| Coup       |         15.7%  |       19.8%  |          39.3%   |         7.2%   |         24.0%  |
| Realign    |          0.0%  |        0.0%  |           0.0%   |         0.0%   |          7.9%  |
| Space Race |          0.1%  |        0.1%  |           0.0%   |         0.0%   |          0.6%  |
| Event      |         12.4%  |       12.9%  |          20.2%   |        29.3%   |         15.4%  |

Notes:
- "v106 Greedy" = argmax of model's mode_head logits; actual game execution falls back to the heuristic (mode choice only logged).
- MCTS-v99c data is from a different checkpoint (v99c, 400 sims). It is the best available proxy for MCTS behavior; v106 MCTS data would require step-trace extraction not currently supported by bindings.
- Heuristic data: 100 games heuristic vs heuristic using `play_traced_game`.

---

## 2. Era Breakdown

### Heuristic USSR (100 games, both sides heuristic)

| Era   | Influence | Coup  | Realign | Space | Event |
|-------|----------:|------:|--------:|------:|------:|
| Early |    73.6%  | 15.3% |   0.0%  |  0.0% | 11.1% |
| Mid   |    70.3%  | 16.1% |   0.0%  |  0.1% | 13.5% |
| Late  |    73.4%  | 13.8% |   0.0%  |  0.1% | 12.8% |

### Heuristic US (100 games, both sides heuristic)

| Era   | Influence | Coup  | Realign | Space | Event |
|-------|----------:|------:|--------:|------:|------:|
| Early |    73.2%  | 15.8% |   0.0%  |  0.0% | 11.1% |
| Mid   |    60.4%  | 25.0% |   0.0%  |  0.2% | 14.4% |
| Late  |    62.3%  | 24.5% |   0.0%  |  0.4% | 12.8% |

### v106 Greedy USSR (200 games)

| Era   | Influence | Coup  | Realign | Space | Event |
|-------|----------:|------:|--------:|------:|------:|
| Early |    47.6%  | 20.1% |   0.0%  |  0.0% | 32.3% |
| Mid   |    43.3%  | 40.8% |   0.0%  |  0.0% | 16.0% |
| Late  |    30.5%  | 54.5% |   0.0%  |  0.0% | 15.0% |

### v106 Greedy US (200 games)

| Era   | Influence | Coup  | Realign | Space | Event |
|-------|----------:|------:|--------:|------:|------:|
| Early |    50.2%  |  2.8% |   0.0%  |  0.0% | 47.0% |
| Mid   |    60.4%  | 12.2% |   0.0%  |  0.0% | 27.4% |
| Late  |    82.6%  |  3.9% |   0.0%  |  0.0% | 13.5% |

### MCTS-v99c USSR (2000 games, 400 sim)

| Era   | Influence | Coup  | Realign | Space | Event |
|-------|----------:|------:|--------:|------:|------:|
| Early |    44.7%  | 28.7% |   8.2%  |  1.2% | 17.3% |
| Mid   |    55.1%  | 21.7% |   8.3%  |  0.3% | 14.6% |
| Late  |    55.0%  | 22.8% |   7.2%  |  0.3% | 14.6% |

---

## 3. Key Discrepancies and Analysis

### 3.1 Realign: 0% everywhere except MCTS (+7.9%)

**What is happening:**  
The heuristic never realigns (it lacks this logic). The v106 greedy model also produces 0% Realign—its mode_head gives Realign near-zero probability (avg softmax ~1.2%). But MCTS-v99c realigns ~8% of the time, consistently across all eras.

**Why MCTS uses Realign:**  
MCTS can discover through tree search that Realign provides favorable expected value in specific board states (e.g., contesting a region where coup is expensive due to stability or DEFCON pressure). The policy prior discourages it; MCTS overrides the prior when rollouts support it. Realign is a tool the model has been trained to undervalue—it barely appears in the training data (heuristic data = 0%, greedy model = 0%), so the mode_head learns to assign it near-zero weight.

**Implication:**  
The model has a persistent Realign blind spot. Since greedy v106 never realigns, and training data comes from greedy/heuristic games, the mode_head has no positive signal for Realign. MCTS can partially compensate, but only when search depth is sufficient to discover its value. This blind spot will persist as long as training data excludes Realign actions.

**Fix:**  
Inject a small fraction of MCTS teacher data that contains Realign decisions, or add a Realign-specific data augmentation in the training pipeline.

### 3.2 Space Race: nearly 0% everywhere

**What is happening:**  
Heuristic uses Space ~0.1%. v106 Greedy: 0% (avg softmax 0.9-1.2%). MCTS-v99c: 0.6%.

**Why so low:**  
Space Race is a strategic one-time investment with diminishing returns if used too early. The heuristic rarely spaces; training data reflects this. The model has correctly learned that Space is niche. MCTS slightly elevates Space when it finds specific card+board combinations where the Space Race bonus outweighs alternative uses (e.g., burning a 4-op opponent card that would be dangerous as Event).

**Implication:**  
This is likely appropriate—Space Race is a situationally correct but rare play. If the model is losing because it cannot leverage Space bonuses, it is likely not the mode frequency that is wrong, but the card selection (which card to space).

### 3.3 Coup: v106 USSR is dramatically over-aggressive (39.3% vs heuristic 15.7%)

**What is happening:**  
The greedy model (USSR) chooses Coup nearly 40% of the time overall, and 54.5% in late war. The heuristic only Coups ~14-16%. MCTS (v99c) is intermediate at 24%.

**Why the model over-coups as USSR:**  
- Training data from heuristic games includes successful USSR coups (US is weak in many regions, especially early). The model has learned that Coup is often the highest-value action.
- The mode_head is not conditioned on whether the coup is legal at DEFCON 2 (DEFCON safety logic lives in the execution wrapper, not the mode head itself). The raw mode_head sees "Coup = high value" without accounting for marginal situations.
- Greedy argmax over mode_logits amplifies this: if Coup avg prob is 0.385 and Influence is 0.393, they are nearly tied, and small perturbations cause Coup to win.
- The late-war spike (54.5%) may reflect a spurious correlation: late war = less DEFCON margin for events, so Coup scores high on the mode_head as the non-Event alternative.

**Implication:**  
The MCTS intermediate value (24%) is probably closer to correct. MCTS's tree search penalizes excessive coups by discovering that they drain military ops, trigger opponent DEFCON plays, and often leave the USSR overextended. The greedy model has no such self-correction mechanism.

**Fix:**  
Add a training signal that penalizes over-couping. Options:
1. Increase value_weight for positions where excessive coup led to DEFCON loss.
2. Add MCTS teacher targets specifically for coup-heavy states, letting MCTS correct the mode prior.
3. Apply a mode calibration temperature at inference (T>1 for mode_head) to flatten the Coup/Influence distribution.

### 3.4 Event: v106 is over-aggressive on Events (especially early war)

**What is happening:**  
v106 Greedy US plays Events 47% of the time in early war (vs heuristic's 11%). v106 Greedy USSR plays Events 32.3% in early war (vs heuristic's 11.1%). The model dramatically over-plays Events.

**Why:**  
- The training data (nashc heuristic games) produces many early Events because Nash/heuristic uses Events situationally. The model learned that Events are valuable early.
- However, the greedy argmax amplifies this: if Event has 47% raw probability, it dominates Influence (50%) but barely wins. Any learned prior toward Event gets amplified by argmax selection.
- The US's high Event rate in early war (47%) may reflect a real asymmetry: US early-war events (NATO, Marshall Plan, Truman Doctrine) are very strong and playable in AR1-3. The model correctly learned this.
- USSR's 32% early-war Event rate may be a problem if it's playing opponent events (which trigger the opponent's event before Ops usage).

**Implication:**  
US early-war Event preference is plausible and may be correct. USSR early-war Event at 32% needs investigation: if USSR is playing Soviet events (good), this is correct; if it's playing US events as events (suicide move), this is a bug. The DEFCON safety logic should prevent the worst cases, but it does not prevent suboptimal event selection.

### 3.5 Influence: v106 USSR dramatically under-places influence (40.6% vs heuristic 72%)

**What is happening:**  
The model (USSR) places influence far less than the heuristic. MCTS is intermediate at 52%.

**Why:**  
This is a direct consequence of over-Coup and over-Event: if the model chooses Coup 39% and Event 20%, Influence must be ~40%. The heuristic's 72% Influence reflects that steady influence placement is the correct default for the USSR board position.

**Implication:**  
If the model is over-couping and the heuristic is more influence-heavy, the model may be winning games via DEFCON pressure tactics or Direct support rather than traditional influence control. This may explain Elo gains but could be fragile vs opponents who understand DEFCON discipline (human opponents, better MCTS).

### 3.6 US Coup vs Influence: the sides are correctly asymmetric, but magnitudes differ

**Heuristic:** US 19.8% Coup vs USSR 15.7% Coup. US coups more because it needs to challenge USSR influence in battleground countries (Southeast Asia, Central America) where early USSR flooding makes influence placement suboptimal.

**v106 Greedy:** US 7.2% Coup (too low) vs USSR 39.3% Coup (too high). The model has inverted the expected pattern—USSR over-coups while US under-coups. This is exactly backwards from what the board-control logic would suggest.

**Why:** The model learned from data where US side was the "winning side against heuristic" and winning US games tend to be influence-heavy (building NATO networks). US coups in early war often backfired vs heuristic in training data. The model over-generalized.

---

## 4. Summary Table: Actual vs Expected

| Issue | Observed | Expected (approx) | Fix Priority |
|-------|----------|-------------------|--------------|
| USSR Coup rate | 39% (greedy), 24% (MCTS) | 15-25% | HIGH: MCTS teacher targets |
| US Coup rate | 7% (greedy) | 15-25% | HIGH: data imbalance |
| Realign rate (any) | 0% (greedy), 8% (MCTS) | 5-10% | MED: MCTS teacher data |
| Space Race rate | 0% (greedy) | 1-3% | LOW: situationally correct |
| US early-war Event | 47% (greedy) | 20-35%? | MED: investigate card types |
| USSR late Coup | 54% (greedy) | 20-30% | HIGH: mode calibration |

---

## 5. Recommendations

1. **Mode temperature calibration at inference** (quick fix): Apply T=1.5-2.0 to mode_logits during greedy play to reduce mode concentration. This will lower Coup dominance and increase Influence/Realign without retraining.

2. **MCTS teacher data for mode correction** (medium fix): Collect 2-5k MCTS teacher games (400+ sim) and include them in the next training round. The MCTS-corrected mode distribution (Coup ~24%, Realign ~8%) is a better training signal than greedy mode choices.

3. **Realign signal injection** (targeted fix): Intentionally run 500-1000 games where Realign is forced occasionally (random epsilon exploration), then add those as training rows. The mode_head needs positive Realign examples to recover this latent capability.

4. **US Coup under-use**: Check if US training data is filtered to "wins only" (per standing policy). US wins with influence-dominant play may have starved the model of US coup signals. If US wins were predominantly influence-based, relax the filter or add US coup demonstrations from MCTS.

5. **Side-specific mode bias investigation**: Instrument future MCTS runs with mode logging (requires step-trace extraction in C++ bindings). The current analysis relied on v99c MCTS data; fresh v106 MCTS trace data would be more accurate.

---

## 6. Data Sources

| Source | Agent | Side | Games | n_decisions |
|--------|-------|------|-------|-------------|
| `play_traced_game` | Heuristic | Both | 100 | ~7400/side |
| `play_callback_matchup` | v106 Greedy | USSR | 200 | 15,213 |
| `play_callback_matchup` | v106 Greedy | US | 200 | 14,428 |
| `mcts_v99c_s7_ussr_vs_heuristic_2k.jsonl` | MCTS-v99c (400sim) | USSR | 2000 | 145,127 |
| `learned_v99c_s7_ussr_vs_heuristic_2k.jsonl` | Greedy-v99c | USSR | ~1000 | 73,208 |
