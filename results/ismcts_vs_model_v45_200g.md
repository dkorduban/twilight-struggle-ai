# ISMCTS vs Raw Policy Benchmark — v45
Date: 2026-04-11 01:15 UTC
Config: 16 determinizations × 100 simulations, pool_size=16, max_pending=4, device=cuda
Games: 200 (100/side)
Duration: 1649.6s (8.2s/game)

## Results

| Side (search) | Wins | Win Rate |
|---------------|------|----------|
| USSR          | 87/100 | 87% |
| US            | 98/100 | 98% |
| **Combined**  | **185/200** | **92.5%** |

## End Reasons

### USSR (search side)
- defcon1: 75 (75%)
- turn_limit: 22 (22%)
- vp: 2 (2%)
- vp_threshold: 1 (1%)
- VP range: [-34, 12], mean=-1.4
- Turn range: [1, 10], mean=4.2

### US (search side)
- defcon1: 100 (100%)
- VP range: [-7, 13], mean=1.4
- Turn range: [1, 9], mean=1.8

## Analysis

1. **Search adds massive value**: 92.5% combined vs same-model raw policy
2. **DEFCON-1 exploitation dominates**: 87.5% of all games end in DEFCON-1
3. **US search is devastating**: mean turn 1.8 — finds DEFCON traps almost immediately
4. **USSR search is strong but less so**: takes longer (mean turn 4.2) but still wins 87%
5. **Raw policy is DEFCON-vulnerable**: The model doesn't defend against DEFCON-1 traps
   that search discovers via lookahead

## Implications

- ISMCTS with even modest sim counts (100) provides enormous strength boost
- DEFCON defense should be a priority — model needs to learn to avoid/exploit traps
- The PolicyCallback + SmallChoiceHead work (pragmatic heads) becomes more valuable
  since search needs good event decisions during determinization rollouts
- At 8.2s/game, ISMCTS is viable for evaluation but too slow for training data generation
