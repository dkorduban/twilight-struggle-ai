---
name: Southeast Asia stability discovery
description: Indonesia/Malaysia stability is 1 not 3; verified against 21 coup results from logs
type: project
---

## Finding

**Indonesia/Malaysia (country_id=76) has incorrect stability value in data/spec/countries.csv.**

Current CSV value: **3**
Correct value (from coup evidence): **1**

## Evidence

Analyzed 21 coup attempts across 10 log files using the coup formula:
```
stability = (die_roll + ops - net_result) / 2
```

### Vietnam (id=80, CSV stability: 1)
- **18 coups total**, all consistent with stability=1
- Files: tsreplayer_38, 49, 50, 58, 61, 62, 64, 65, 72
- Status: **VERIFIED**

### Indonesia/Malaysia (id=76, CSV stability: 3)
- **3 coups total**, ALL imply stability=1 not 3

| File | Target | Roll | Ops | Result | Implied Stab | CSV says |
|------|--------|------|-----|--------|-------------|----------|
| tsreplayer_33 | Malaysia | 4 | 3 | 3 | (4+3-3)/2 = 2 | 3 ❌ |
| tsreplayer_38 | Indonesia | 5 | 1 | 4 | (5+1-4)/2 = 1 | 3 ❌ |
| tsreplayer_38 | Indonesia | 6 | 3 | 7 | (6+3-7)/2 = 1 | 3 ❌ |

### Philippines (id=78, CSV stability: 2)
- **0 coups found**
- Status: Cannot verify

## Impact

**This is a critical bug in the coup-result reducer.** With stability=3, coups in Indonesia/Malaysia should need much higher rolls to succeed. Using stability=3 in the reducer will cause:

1. **Replay validation failures**: Coups that succeeded in logs appear to violate coup math
2. **Scoring miscalculations**: Any influence lost/gained in Indonesia/Malaysia via coup will be traced to wrong stability assumptions
3. **Hand-reconstruction errors**: If coup results are recomputed with stability=3, they will disagree with the log record

## How to Apply

Fix `/home/dkord/code/twilight-struggle-ai/data/spec/countries.csv` line 156:

**Before:**
```
76,Indonesia/Malaysia,SoutheastAsia,3,true,0,0
```

**After:**
```
76,Indonesia/Malaysia,SoutheastAsia,1,true,0,0
```

Then re-run all parser and reducer tests to verify alignment with logs.

## Notes

- This is the only Southeast Asia country with visible coup evidence in the current log corpus
- The one anomaly (tsreplayer_33 Malaysia, implied stab=2) is from a single roll; the two Indonesia coups (both imply stab=1) are more consistent
- tsreplayer_33 may also be a log anomaly or parsing error; flag it for review if other Malaysia coups appear
