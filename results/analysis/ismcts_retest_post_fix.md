# ISMCTS Re-benchmark — Post Engine Fix
Date: 2026-04-12
Config: 16 determinizations × 100 simulations, pool_size=16, max_pending=4, device=cuda
Games: 200 (100/side)
Duration: 1137.1s (5.7s/game)
Model: data/checkpoints/scripted_for_elo/v45_scripted.pt

Fixes since previous benchmark (ismcts_vs_model_v45_200g.md, 2026-04-11):
- a9dd071: Headline DEFCON-1 phasing bug (headline phase could trigger DEFCON-1 win incorrectly)
- a9dd071: apply_ops_randomly illegal coup targets (ops could coup a country with 0 influence)
- 7af5979: ISMCTS determinization: resample opponent hand correctly

## Results

| Side (search) | Wins | Win Rate |
|---------------|------|----------|
| USSR          | 90/100 | 90.0% ±3.0% |
| US            | 99/100 | 99.0% ±1.0% |
| **Combined**  | **189/200** | **94.5% ±1.6%** |

## End Reasons

### USSR (search side)
- defcon1: 87 (87%)
- turn_limit: 11 (11%)
- europe_control: 1 (1%)
- vp_threshold: 1 (1%)
- VP range: [-24, 11], mean=-0.4
- Turn range: [1, 10], mean=3.2

### US (search side)
- defcon1: 98 (98%)
- turn_limit: 2 (2%)
- VP range: [-14, 18], mean=1.3
- Turn range: [1, 10], mean=1.8

## Comparison with Previous Benchmark (2026-04-11)

| Metric | Before fixes | After fixes | Delta |
|--------|-------------|-------------|-------|
| USSR win rate | 87% | 90% ±3% | +3pp |
| US win rate | 98% | 99% ±1% | +1pp |
| Combined win rate | 92.5% | 94.5% ±1.6% | +2pp |
| **DEFCON-1 rate** | **87.5%** | **92.5%** | **+5pp** |
| Mean game length USSR | turn 4.2 | turn 3.2 | -1.0 turn |
| Speed | 8.2s/game | 5.7s/game | 1.44× faster |

## Analysis

1. **Engine fixes did not reduce DEFCON-1 rate**: The DEFCON-1 rate actually increased from 87.5% to 92.5%. The headline phasing bug fix and illegal coup target fix did not reduce search's ability to exploit DEFCON traps — if anything, the correct engine may offer more DEFCON-exploiting lines.

2. **USSR side improved somewhat**: 87% → 90% win rate, and mean game length dropped from 4.2 to 3.2 turns. This may reflect the corrected ISMCTS determinization resampling (7af5979) giving search better information about opponent hands.

3. **Speed improved significantly**: 8.2s → 5.7s per game (1.44× faster). This is likely because the US side is now faster (470s vs the first time showing similar overhead), possibly due to the engine correctness fixes removing some slow error-handling paths or redundant work.

4. **US side remains catastrophically dominant**: 99% win rate with mean turn 1.8 — DEFCON-1 trap exploitation via search remains nearly perfect on the US side. The headline phasing fix did not meaningfully affect this.

5. **Raw policy is still very DEFCON-vulnerable**: The model needs to learn to recognize and defend against DEFCON-1 threats that search discovers via lookahead. The corrected hand resampling (7af5979) likely makes search more accurate, not less.

## Conclusions

The engine bug fixes did **not** reduce the DEFCON-1 rate — the root cause of the 87.5% DEFCON-1 rate in the original benchmark was not a false positive from engine bugs. The DEFCON exploitation is real: ISMCTS genuinely finds DEFCON-1 traps that the raw policy cannot defend against.

The corrected hand resampling in determinization (7af5979) may have slightly improved search quality (USSR: +3pp), but the fundamental conclusion remains: the raw policy is DEFCON-vulnerable and ISMCTS exploits this systematically.

**Next steps** to reduce DEFCON-1 exploitation as a training signal concern:
- Train with DEFCON-awareness: include DEFCON-defense positions in supervised data
- Use ISMCTS self-play to generate DEFCON-threat positions for policy improvement
- Or accept that DEFCON exploitation is a real strength gap and use it as a training signal (match ISMCTS targets)
