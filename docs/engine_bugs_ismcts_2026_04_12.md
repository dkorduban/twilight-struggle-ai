# Engine Bugs: ISMCTS Audit 2026-04-12

Found during audit of 92.5% ISMCTS win rate result (results/analysis/ismcts_vs_model_v45_200g.md).
These bugs invalidate the benchmark — the wins are NOT genuine strategic superiority.

---

## Bug 1 — Perfect-Information Determinization [CRITICAL]

**File:** `cpp/tscore/ismcts.cpp`  
**Status:** Fixed 2026-04-12 — commit 7af5979 (cherry-pick of d73c224 from worktree)

### Description
`sample_determinization()` clones the full live `GameState`, which already contains the
opponent's true hand. Because `known_opp_count == opp_hand_size`, `hidden_needed = 0`
and no card resampling occurs. ISMCTS searches with **perfect knowledge of the opponent's
hidden hand** — equivalent to playing with open cards.

### Impact
This alone explains the near-100% win rates. ISMCTS can play exact trap lines because it
knows what the opponent will headline and which events they can play.

### Fix
In `sample_determinization()`: treat the opponent hand as fully unknown. Shuffle all
opponent hand cards back into the available pool, then resample `opp_hand_size` cards
uniformly. Only cards the opponent has **demonstrably played** should be excluded.

---

## Bug 2 — Headline DEFCON-1 Winner Inverted for First Resolver [MODERATE]

**File:** `cpp/tscore/game_loop.cpp` (headline resolution loop, ~line 852)  
**Status:** Fixed 2026-04-12 — commit a9dd071 (cherry-pick of db6cc13 from worktree)

### Description
The headline chooser loop (`game_loop.cpp:779`) iterates USSR then US, leaving
`gs.pub.phasing = Side::US`. The resolution loop then calls `apply_action_with_hands`
without resetting `pub.phasing` to `pending.side`.

Winner assignment in `step.cpp:1214`:
```cpp
if (pub.defcon <= 1) {
    return {true, other_side(pub.phasing)};  // phasing player LOSES
}
```

When the first-resolving headline (typically USSR's if higher ops) drops DEFCON to 1,
`pub.phasing` is still `US`, so `other_side(US) = USSR` is declared **winner** — but
USSR caused DEFCON-1 and should **lose**.

Note: headline order IS ops-determined (`std::sort` descending by ops, USSR wins ties).

### Fix
Add `gs.pub.phasing = pending.side;` immediately before `apply_action_with_hands` in
the headline resolution loop.

---

## Bug 3 — `apply_ops_randomly()` Wrong DEFCON Region Filter [MODERATE]

**File:** `cpp/tscore/game_loop.cpp` (lines 174–225)  
**Status:** Fixed 2026-04-12 — commit a9dd071 (same as Bug 2; also moved `is_defcon_restricted` out of anon namespace in legal_actions.cpp)

### Description
`apply_ops_randomly()` (used by Bear Trap, Quagmire, etc.) filters coup targets at
DEFCON ≤ 2 by `is_battleground` — but the real restriction is by **region** (see
`legal_actions.cpp:kDefconRegionThreshold`). Additionally, if the filtered list is
empty, it falls back to the full unfiltered `accessible` list, allowing coups that
should be blocked.

Correct thresholds (from `kDefconRegionThreshold`):
- Europe: restricted at DEFCON ≤ 3
- Asia: restricted at DEFCON ≤ 4  
- All others: restricted at DEFCON ≤ 1 or 2

### Fix
Replace the `is_battleground` filter with `is_defcon_restricted(cid, pub)` from
`legal_actions.cpp`. Remove the fallback that restores the unfiltered list — if no
valid coup target exists, fall back to `ActionMode::Influence` instead.

---

## Re-benchmark plan

After all 3 fixes are merged and built:
1. Re-run `benchmark_ismcts_vs_model` with v45, 200 games
2. Expected result: ISMCTS still better than raw policy (search IS valuable) but
   win rate should drop substantially from 92.5%
3. Log to `results/analysis/ismcts_vs_model_v45_post_fix.md`
