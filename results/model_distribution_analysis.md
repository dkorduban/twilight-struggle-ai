# Model Country Distribution Analysis: v106_cf_gnn_s42

## Overview

- **Model**: `TSControlFeatGNNModel` (2-round GNN over 86-country adjacency graph)
- **Checkpoint**: `data/checkpoints/v106_cf_gnn_s42/baseline_best_scripted.pt`
- **Country head**: mixture-of-4-softmaxes (4 strategies x 86 countries)
- **Performance**: ~35% Nash combined win rate as USSR vs heuristic

Analysis performed on heuristic-vs-heuristic traced games (seeds: 42,100,200,300,500,700,900,1100,1300,1500),
feeding each game state through the model to observe country distributions at different phases.
Note: The model was trained on self-play data where the heuristic is the opponent,
so these states represent the distribution of positions the model would encounter in evaluation.

## Early War (Turns 1-3)

Sample size: 30 decision points


USSR decisions: 15, US decisions: 15
Average value (USSR perspective): 0.364

### Strategy Mixing Weights

| Strategy | Avg Weight |
|----------|-----------|
| Strategy 0 | 0.146 |
| Strategy 1 | 0.235 |
| Strategy 2 | 0.354 |
| Strategy 3 | 0.265 |

### Top-15 Countries (Mixed Distribution, Both Sides Averaged)

| Rank | Country | Prob | Region | BG? |
|------|---------|------|--------|-----|
| 1 | Thailand | 0.3253 | SoutheastAsia | Yes |
| 2 | Japan | 0.0952 | Asia | Yes |
| 3 | Indonesia | 0.0683 | SoutheastAsia | Yes |
| 4 | Iran | 0.0502 | MiddleEast | Yes |
| 5 | Egypt | 0.0442 | MiddleEast | Yes |
| 6 | Angola | 0.0424 | Africa | Yes |
| 7 | Vietnam | 0.0405 | SoutheastAsia | Yes |
| 8 | Turkey | 0.0377 | Europe | Yes |
| 9 | North Korea | 0.0367 | Asia | Yes |
| 10 | West Germany | 0.0312 | Europe | Yes |
| 11 | Philippines | 0.0295 | SoutheastAsia | Yes |
| 12 | Ethiopia | 0.0292 | Africa | Yes |
| 13 | France | 0.0183 | Europe | Yes |
| 14 | India | 0.0161 | Asia | Yes |
| 15 | Lebanon | 0.0156 | MiddleEast | No |

### Bottom-10 Countries (Lowest Probability)

| Rank | Country | Prob | Region | BG? |
|------|---------|------|--------|-----|
| 77 | Bulgaria | 0.0000 | Europe | No |
| 78 | Benelux | 0.0000 | Europe | No |
| 79 | USA | 0.0000 | ? | No |
| 80 | Yugoslavia | 0.0000 | Europe | No |
| 81 | Taiwan | 0.0000 | Asia | No |
| 82 | Norway | 0.0000 | Europe | No |
| 83 | USSR | 0.0000 | ? | No |
| 84 | Greece | 0.0000 | Europe | No |
| 85 | Afghanistan | 0.0000 | Asia | No |
| 86 | Denmark | 0.0000 | Europe | No |

### Per-Strategy Country Top-10

**Strategy 0** (avg weight: 0.146)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | Thailand | 0.7993 | SoutheastAsia |
| 2 | Indonesia | 0.0963 | SoutheastAsia |
| 3 | Vietnam | 0.0328 | SoutheastAsia |
| 4 | India | 0.0291 | Asia |
| 5 | Egypt | 0.0256 | MiddleEast |
| 6 | Nigeria | 0.0064 | Africa |
| 7 | France | 0.0056 | Europe |
| 8 | Ethiopia | 0.0022 | Africa |
| 9 | Philippines | 0.0007 | SoutheastAsia |
| 10 | South Africa | 0.0007 | Africa |

**Strategy 1** (avg weight: 0.235)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | Thailand | 0.4050 | SoutheastAsia |
| 2 | Japan | 0.2147 | Asia |
| 3 | Egypt | 0.0870 | MiddleEast |
| 4 | North Korea | 0.0717 | Asia |
| 5 | Turkey | 0.0555 | Europe |
| 6 | Indonesia | 0.0361 | SoutheastAsia |
| 7 | Libya | 0.0342 | MiddleEast |
| 8 | Iran | 0.0331 | MiddleEast |
| 9 | France | 0.0280 | Europe |
| 10 | Vietnam | 0.0155 | SoutheastAsia |

**Strategy 2** (avg weight: 0.354)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | Thailand | 0.4723 | SoutheastAsia |
| 2 | Angola | 0.0655 | Africa |
| 3 | North Korea | 0.0602 | Asia |
| 4 | Turkey | 0.0558 | Europe |
| 5 | Ethiopia | 0.0477 | Africa |
| 6 | Indonesia | 0.0398 | SoutheastAsia |
| 7 | Philippines | 0.0384 | SoutheastAsia |
| 8 | West Germany | 0.0358 | Europe |
| 9 | Iran | 0.0355 | MiddleEast |
| 10 | Vietnam | 0.0289 | SoutheastAsia |

**Strategy 3** (avg weight: 0.265)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | Thailand | 0.2047 | SoutheastAsia |
| 2 | Japan | 0.1563 | Asia |
| 3 | West Germany | 0.1028 | Europe |
| 4 | Vietnam | 0.0871 | SoutheastAsia |
| 5 | Indonesia | 0.0781 | SoutheastAsia |
| 6 | France | 0.0694 | Europe |
| 7 | Lebanon | 0.0651 | MiddleEast |
| 8 | Philippines | 0.0400 | SoutheastAsia |
| 9 | Angola | 0.0337 | Africa |
| 10 | Israel | 0.0273 | MiddleEast |

### Region Aggregate Probabilities

| Region | Total Prob | BG Prob | Non-BG Prob |
|--------|-----------|---------|-------------|
| Europe | 0.1173 | 0.1173 | 0.0000 |
| Asia | 0.1733 | 0.1733 | 0.0000 |
| MiddleEast | 0.1630 | 0.1473 | 0.0157 |
| CentralAmerica | 0.0013 | 0.0006 | 0.0007 |
| SouthAmerica | 0.0002 | 0.0001 | 0.0001 |
| Africa | 0.0815 | 0.0815 | 0.0000 |
| SoutheastAsia | 0.4635 | 0.4634 | 0.0001 |

## Mid War (Turns 4-7)

Sample size: 30 decision points

USSR decisions: 13, US decisions: 17
Average value (USSR perspective): 0.680

### Strategy Mixing Weights

| Strategy | Avg Weight |
|----------|-----------|
| Strategy 0 | 0.157 |
| Strategy 1 | 0.381 |
| Strategy 2 | 0.359 |
| Strategy 3 | 0.102 |

### Top-15 Countries (Mixed Distribution, Both Sides Averaged)

| Rank | Country | Prob | Region | BG? |
|------|---------|------|--------|-----|
| 1 | Chile | 0.2419 | SouthAmerica | Yes |
| 2 | South Africa | 0.1479 | Africa | Yes |
| 3 | Mozambique | 0.0978 | Africa | No |
| 4 | Ethiopia | 0.0806 | Africa | Yes |
| 5 | Argentina | 0.0654 | SouthAmerica | Yes |
| 6 | Mexico | 0.0515 | CentralAmerica | Yes |
| 7 | Angola | 0.0495 | Africa | Yes |
| 8 | Brazil | 0.0422 | SouthAmerica | Yes |
| 9 | Nigeria | 0.0341 | Africa | Yes |
| 10 | North Korea | 0.0298 | Asia | Yes |
| 11 | Egypt | 0.0280 | MiddleEast | Yes |
| 12 | Morocco | 0.0172 | Africa | Yes |
| 13 | Cameroon | 0.0160 | Africa | No |
| 14 | Indonesia | 0.0145 | SoutheastAsia | Yes |
| 15 | Panama | 0.0142 | CentralAmerica | Yes |

### Bottom-10 Countries (Lowest Probability)

| Rank | Country | Prob | Region | BG? |
|------|---------|------|--------|-----|
| 77 | Czechoslovakia | 0.0000 | Europe | No |
| 78 | ID=64 | 0.0000 | Africa | No |
| 79 | Canada | 0.0000 | Europe | No |
| 80 | Taiwan | 0.0000 | Asia | No |
| 81 | Yugoslavia | 0.0000 | Europe | No |
| 82 | Denmark | 0.0000 | Europe | No |
| 83 | Bulgaria | 0.0000 | Europe | No |
| 84 | Benelux | 0.0000 | Europe | No |
| 85 | Afghanistan | 0.0000 | Asia | No |
| 86 | USSR | 0.0000 | ? | No |

### Per-Strategy Country Top-10

**Strategy 0** (avg weight: 0.157)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | Chile | 0.7718 | SouthAmerica |
| 2 | South Africa | 0.1011 | Africa |
| 3 | Indonesia | 0.0439 | SoutheastAsia |
| 4 | Nigeria | 0.0334 | Africa |
| 5 | Ethiopia | 0.0231 | Africa |
| 6 | West Germany | 0.0131 | Europe |
| 7 | Japan | 0.0038 | Asia |
| 8 | Vietnam | 0.0033 | SoutheastAsia |
| 9 | Panama | 0.0017 | CentralAmerica |
| 10 | Brazil | 0.0015 | SouthAmerica |

**Strategy 1** (avg weight: 0.381)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | South Africa | 0.1593 | Africa |
| 2 | Argentina | 0.1468 | SouthAmerica |
| 3 | Brazil | 0.0991 | SouthAmerica |
| 4 | Angola | 0.0659 | Africa |
| 5 | Mexico | 0.0624 | CentralAmerica |
| 6 | North Korea | 0.0594 | Asia |
| 7 | Mozambique | 0.0580 | Africa |
| 8 | Nigeria | 0.0516 | Africa |
| 9 | Chile | 0.0507 | SouthAmerica |
| 10 | Ethiopia | 0.0399 | Africa |

**Strategy 2** (avg weight: 0.359)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | Chile | 0.3669 | SouthAmerica |
| 2 | South Africa | 0.3140 | Africa |
| 3 | Mozambique | 0.1015 | Africa |
| 4 | Ethiopia | 0.0785 | Africa |
| 5 | Angola | 0.0381 | Africa |
| 6 | Nigeria | 0.0336 | Africa |
| 7 | Egypt | 0.0208 | MiddleEast |
| 8 | Japan | 0.0138 | Asia |
| 9 | Jordan | 0.0133 | MiddleEast |
| 10 | Syria | 0.0046 | MiddleEast |

**Strategy 3** (avg weight: 0.102)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | South Africa | 0.5829 | Africa |
| 2 | Cameroon | 0.0665 | Africa |
| 3 | Panama | 0.0573 | CentralAmerica |
| 4 | Mexico | 0.0448 | CentralAmerica |
| 5 | West Germany | 0.0445 | Europe |
| 6 | Indonesia | 0.0363 | SoutheastAsia |
| 7 | Morocco | 0.0347 | Africa |
| 8 | Ethiopia | 0.0331 | Africa |
| 9 | France | 0.0326 | Europe |
| 10 | UK | 0.0288 | Europe |

### Region Aggregate Probabilities

| Region | Total Prob | BG Prob | Non-BG Prob |
|--------|-----------|---------|-------------|
| Europe | 0.0196 | 0.0196 | 0.0000 |
| Asia | 0.0321 | 0.0321 | 0.0000 |
| MiddleEast | 0.0358 | 0.0321 | 0.0037 |
| CentralAmerica | 0.0659 | 0.0658 | 0.0001 |
| SouthAmerica | 0.3750 | 0.3629 | 0.0121 |
| Africa | 0.4561 | 0.3353 | 0.1207 |
| SoutheastAsia | 0.0155 | 0.0155 | 0.0000 |

## Late War (Turns 8-10)

Sample size: 30 decision points

USSR decisions: 15, US decisions: 15
Average value (USSR perspective): 0.307

### Strategy Mixing Weights

| Strategy | Avg Weight |
|----------|-----------|
| Strategy 0 | 0.137 |
| Strategy 1 | 0.089 |
| Strategy 2 | 0.700 |
| Strategy 3 | 0.074 |

### Top-15 Countries (Mixed Distribution, Both Sides Averaged)

| Rank | Country | Prob | Region | BG? |
|------|---------|------|--------|-----|
| 1 | West Germany | 0.2127 | Europe | Yes |
| 2 | Cuba | 0.1806 | CentralAmerica | Yes |
| 3 | East Germany | 0.1776 | Europe | Yes |
| 4 | Congo/Zaire | 0.1029 | Africa | Yes |
| 5 | Algeria | 0.0846 | Africa | Yes |
| 6 | Ethiopia | 0.0832 | Africa | Yes |
| 7 | Angola | 0.0668 | Africa | Yes |
| 8 | France | 0.0563 | Europe | Yes |
| 9 | Argentina | 0.0173 | SouthAmerica | Yes |
| 10 | Chile | 0.0061 | SouthAmerica | Yes |
| 11 | South Africa | 0.0025 | Africa | Yes |
| 12 | Mexico | 0.0023 | CentralAmerica | Yes |
| 13 | Morocco | 0.0018 | Africa | Yes |
| 14 | UK | 0.0015 | Europe | Yes |
| 15 | Venezuela | 0.0011 | SouthAmerica | Yes |

### Bottom-10 Countries (Lowest Probability)

| Rank | Country | Prob | Region | BG? |
|------|---------|------|--------|-----|
| 77 | Denmark | 0.0000 | Europe | No |
| 78 | Romania | 0.0000 | Europe | No |
| 79 | Afghanistan | 0.0000 | Asia | No |
| 80 | Canada | 0.0000 | Europe | No |
| 81 | Malaysia | 0.0000 | SoutheastAsia | No |
| 82 | Yugoslavia | 0.0000 | Europe | No |
| 83 | Czechoslovakia | 0.0000 | Europe | No |
| 84 | Burma | 0.0000 | SoutheastAsia | No |
| 85 | Benelux | 0.0000 | Europe | No |
| 86 | Hungary | 0.0000 | Europe | No |

### Per-Strategy Country Top-10

**Strategy 0** (avg weight: 0.137)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | West Germany | 0.4814 | Europe |
| 2 | Mexico | 0.1703 | CentralAmerica |
| 3 | East Germany | 0.1290 | Europe |
| 4 | Ethiopia | 0.0811 | Africa |
| 5 | France | 0.0369 | Europe |
| 6 | Congo/Zaire | 0.0366 | Africa |
| 7 | Chile | 0.0163 | SouthAmerica |
| 8 | Italy | 0.0147 | Europe |
| 9 | Syria | 0.0102 | MiddleEast |
| 10 | Argentina | 0.0080 | SouthAmerica |

**Strategy 1** (avg weight: 0.089)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | West Germany | 0.6099 | Europe |
| 2 | Congo/Zaire | 0.2454 | Africa |
| 3 | East Germany | 0.0580 | Europe |
| 4 | Iran | 0.0323 | MiddleEast |
| 5 | Algeria | 0.0311 | Africa |
| 6 | UK | 0.0080 | Europe |
| 7 | France | 0.0039 | Europe |
| 8 | Angola | 0.0021 | Africa |
| 9 | Ethiopia | 0.0019 | Africa |
| 10 | Venezuela | 0.0017 | SouthAmerica |

**Strategy 2** (avg weight: 0.700)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | East Germany | 0.2764 | Europe |
| 2 | Cuba | 0.1810 | CentralAmerica |
| 3 | West Germany | 0.1153 | Europe |
| 4 | Ethiopia | 0.0980 | Africa |
| 5 | France | 0.0946 | Europe |
| 6 | Algeria | 0.0867 | Africa |
| 7 | Congo/Zaire | 0.0814 | Africa |
| 8 | Angola | 0.0420 | Africa |
| 9 | Argentina | 0.0174 | SouthAmerica |
| 10 | UK | 0.0028 | Europe |

**Strategy 3** (avg weight: 0.074)

| Rank | Country | Prob | Region |
|------|---------|------|--------|
| 1 | West Germany | 0.4175 | Europe |
| 2 | Cuba | 0.1568 | CentralAmerica |
| 3 | Congo/Zaire | 0.1180 | Africa |
| 4 | Angola | 0.0970 | Africa |
| 5 | South Africa | 0.0654 | Africa |
| 6 | Algeria | 0.0590 | Africa |
| 7 | France | 0.0507 | Europe |
| 8 | Morocco | 0.0311 | Africa |
| 9 | Ethiopia | 0.0019 | Africa |
| 10 | Iran | 0.0009 | MiddleEast |

### Region Aggregate Probabilities

| Region | Total Prob | BG Prob | Non-BG Prob |
|--------|-----------|---------|-------------|
| Europe | 0.4495 | 0.4495 | 0.0000 |
| Asia | 0.0000 | 0.0000 | 0.0000 |
| MiddleEast | 0.0004 | 0.0003 | 0.0001 |
| CentralAmerica | 0.1830 | 0.1830 | 0.0000 |
| SouthAmerica | 0.0252 | 0.0252 | 0.0000 |
| Africa | 0.3419 | 0.3419 | 0.0000 |
| SoutheastAsia | 0.0000 | 0.0000 | 0.0000 |

---

## Strategy Guide Comparison

### Key Principles from Strategy Guides

From `classic.md` (TwilightStrategy.com adaptation):
- Default to Ops over events; events must earn their keep
- Asia/Thailand highest early war priority
- Africa/South America highest mid war priority
- Europe is emergency/static, not routine sink
- Iran coup T1AR1 as USSR
- China Card for Asia, not generic ops

From `sankt.md` (Sankt/Aragorn collected musings):
- Evaluate ops by expected VP/tempo/persistence, not raw influence count
- France + Italy + Europe control get special weight
- Battlegrounds first; non-BGs for access/domination fillers only
- Asia is "good enough at parity"; don't pour ops into Asian black hole
- Score cards on latest safe slot, not auto-fired first chance
- Space race is a real VP race ("7th region")

From `minimal_hybrid.md` (heuristic policy logic):
- Region weights: Asia=1.35, SEA=1.25, ME=1.10, Europe=0.85 (early)
- Region weights: SA=1.20, Africa=1.20, CA=0.95, Europe=0.95 (mid)
- Thailand +6.0 bonus in early war
- BG countries +7.0 base, non-BG +1.0
- France/Italy/W.Germany/E.Germany +2.0 bonus

### Early War Alignment

| Country | Model Prob | Rank/86 | Strategy Importance | Assessment |
|---------|-----------|---------|-------------------|------------|
| Thailand | 0.3253 | 1 | Critical | GOOD |
| Japan | 0.0952 | 2 | Medium | rank 2 |
| Iran | 0.0502 | 4 | High | GOOD |
| Egypt | 0.0442 | 5 | High | GOOD |
| North Korea | 0.0367 | 9 | Low | rank 9 |
| West Germany | 0.0312 | 10 | High | GOOD |
| France | 0.0183 | 13 | High | GOOD |
| India | 0.0161 | 14 | Critical | Adequate |
| Libya | 0.0151 | 17 | High | Adequate |
| Pakistan | 0.0138 | 18 | Critical | Adequate |
| South Korea | 0.0115 | 20 | Medium | rank 20 |
| Italy | 0.0114 | 21 | High | Adequate |
| East Germany | 0.0107 | 22 | Medium-High | rank 22 |
| Israel | 0.0101 | 23 | Medium-High | rank 23 |
| Afghanistan | 0.0000 | 85 | Low-Med | rank 85 |

### Mid War Alignment

| Country | Model Prob | Rank/86 | Strategy Importance | Assessment |
|---------|-----------|---------|-------------------|------------|
| Chile | 0.2419 | 1 | High (SA) | GOOD |
| South Africa | 0.1479 | 2 | High (Africa) | GOOD |
| Argentina | 0.0654 | 5 | High (SA) | GOOD |
| Mexico | 0.0515 | 6 | High (CA) | GOOD |
| Angola | 0.0495 | 7 | High (Africa) | GOOD |
| Brazil | 0.0422 | 8 | High (SA) | GOOD |
| Nigeria | 0.0341 | 9 | High (Africa) | GOOD |
| Morocco | 0.0172 | 12 | High (Africa) | GOOD |
| Indonesia | 0.0145 | 14 | Medium | rank 14 |
| Panama | 0.0142 | 15 | High (CA) | GOOD |
| Venezuela | 0.0134 | 16 | High (SA) | Adequate |
| France | 0.0057 | 19 | Med (Europe) | rank 19 |
| Algeria | 0.0038 | 21 | High (Africa) | Adequate |
| Congo/Zaire | 0.0023 | 25 | High (Africa) | Adequate |
| Thailand | 0.0008 | 31 | Medium | rank 31 |
| Italy | 0.0004 | 34 | Med (Europe) | rank 34 |
| Cuba | 0.0001 | 42 | High (CA) | BLIND SPOT |
| Pakistan | 0.0000 | 45 | Medium | rank 45 |
| India | 0.0000 | 48 | Medium | rank 48 |

---

## Strategy Decomposition Analysis

The model uses mixture-of-4-softmaxes for country selection.
Each strategy should ideally represent a distinct tactical plan.
We analyze whether the 4 strategies are meaningfully different or redundant.

### Early War Strategy Differentiation

**Inter-strategy KL divergences** (higher = more differentiated):

|  | S0 | S1 | S2 | S3 |
|--|----|----|----|----|
| S0 | - | 0.763 | 0.553 | 1.880 |
| S1 | 3.558 | - | 1.743 | 2.817 |
| S2 | 2.943 | 1.348 | - | 1.882 |
| S3 | 5.165 | 2.714 | 2.806 | - |

**Strategy regional focus** (top-3 regions by probability mass):

- **Strategy 0** (weight 0.146): SoutheastAsia=0.929, Asia=0.029, MiddleEast=0.026 | Top country: Thailand (0.799)
- **Strategy 1** (weight 0.235): SoutheastAsia=0.457, Asia=0.289, MiddleEast=0.155 | Top country: Thailand (0.405)
- **Strategy 2** (weight 0.354): SoutheastAsia=0.579, Africa=0.129, Asia=0.119 | Top country: Thailand (0.472)
- **Strategy 3** (weight 0.265): SoutheastAsia=0.410, Europe=0.219, Asia=0.178 | Top country: Thailand (0.205)

### Mid War Strategy Differentiation

**Inter-strategy KL divergences** (higher = more differentiated):

|  | S0 | S1 | S2 | S3 |
|--|----|----|----|----|
| S0 | - | 2.285 | 0.748 | 14.087 |
| S1 | 7.196 | - | 4.443 | 5.348 |
| S2 | 2.816 | 1.152 | - | 8.990 |
| S3 | 3.214 | 1.878 | 3.685 | - |

**Strategy regional focus** (top-3 regions by probability mass):

- **Strategy 0** (weight 0.157): SouthAmerica=0.773, Africa=0.159, SoutheastAsia=0.047 | Top country: Chile (0.772)
- **Strategy 1** (weight 0.381): Africa=0.443, SouthAmerica=0.362, CentralAmerica=0.071 | Top country: South Africa (0.159)
- **Strategy 2** (weight 0.359): Africa=0.572, SouthAmerica=0.370, MiddleEast=0.039 | Top country: Chile (0.367)
- **Strategy 3** (weight 0.102): Africa=0.723, Europe=0.108, CentralAmerica=0.104 | Top country: South Africa (0.583)

### Late War Strategy Differentiation

**Inter-strategy KL divergences** (higher = more differentiated):

|  | S0 | S1 | S2 | S3 |
|--|----|----|----|----|
| S0 | - | 1.797 | 1.703 | 3.353 |
| S1 | 0.860 | - | 1.666 | 0.883 |
| S2 | 2.416 | 3.766 | - | 2.436 |
| S3 | 3.426 | 3.031 | 1.301 | - |

**Strategy regional focus** (top-3 regions by probability mass):

- **Strategy 0** (weight 0.137): Europe=0.665, CentralAmerica=0.171, Africa=0.125 | Top country: West Germany (0.481)
- **Strategy 1** (weight 0.089): Europe=0.681, Africa=0.281, MiddleEast=0.034 | Top country: West Germany (0.610)
- **Strategy 2** (weight 0.700): Europe=0.490, Africa=0.309, CentralAmerica=0.182 | Top country: East Germany (0.276)
- **Strategy 3** (weight 0.074): Europe=0.469, Africa=0.373, CentralAmerica=0.157 | Top country: West Germany (0.417)

---

## Identified Weaknesses and Blind Spots

1. **Pakistan under-prioritized in Early War** (rank 18/86). Strategy guides identify it as a top early-war target.

2. **Strategy concentration in Late War**: Strategy 2 has weight 0.700 (min=0.074). The mixture may not be learning distinct plans.

---

## Concrete Suggestions for Improvement

1. **Increase Asia/SEA emphasis in early-war training data**: The heuristic opponent
   may not contest Asia enough. Consider data augmentation with contested Asia states.

2. **Add region-phase auxiliary losses**: A small auxiliary loss encouraging the model
   to match expected regional probability mass per game phase could calibrate targeting.

3. **Encourage strategy diversity**: Add entropy bonus on strategy mixing weights,
   or KL divergence penalty between strategy distributions, to prevent collapse.

4. **Battleground focus loss**: Weight BG countries higher in country head loss,
   since BG control is the primary VP mechanism in scoring.

5. **Phase-conditional country targets**: Consider adding game-phase embedding to the
   country head so strategies can be phase-aware (different in early vs mid vs late war).

6. **Stronger opponents in training**: Self-play or play against a mix of opponent strengths
   would force the model to learn contested positions where country targeting matters most.

