# Opus Analysis: ELO Ladder Cleanup
Date: 2026-04-10T22:38:09Z
Question: Should we remove corrupted-era models (v27-v43) from the ELO tournament? How?

## Executive Summary

**Yes, remove them. The cost of keeping v27-v41 in the tournament is large and growing; the benefit is negligible.**

The corrupted-era models (v27-v41, all trained with the hard-argmax log_prob bug) occupy the bottom of the ladder at Elo 1690-1892, well below even v8 (1931). They add **345 match slots** per round-robin tournament update (74% of all 465 pairs), of which only 15 new matches matter when adding a new model (v44+). Every future tournament update wastes ~15 extra match-runs per new model on corrupted-era opponents that provide zero useful signal about the frontier. The match cache means old results are reused, but the BayesElo solver still processes all 465 results, and the match discovery loop iterates over 31 models instead of 16.

The **recommended approach is Option B+D**: rename the scripted_for_elo files for v27-v41 so they stop being auto-discovered, then manually reset the ladder JSON to contain only clean models. The match cache files in results/matches/ are left untouched as a historical archive. This is safe, reversible, and requires no code changes.

## Findings

### Current Ladder State

31 models total. Sorted by Elo:
- **Clean era (v8-v22):** 15 models, Elo range 1931-2089. These are the real training lineage.
- **Corrupted era (v27-v41):** 15 models, Elo range 1690-1892. All below v8.
- **Heuristic:** Elo 1652 (anchor floor).
- **v23-v26:** Have scripted_for_elo files but are NOT in the ladder (possibly skipped during transition).

465 total match results in the ladder. Of these:
- 105 are purely between corrupted-era models (useless).
- 240 are corrupted-vs-clean cross matches (marginally useful for anchoring heuristic floor, but not needed).
- 120 are clean-era pairs (the only ones that matter going forward).

### Are Bad Models Being Added to Future Tournaments?

**Yes.** The dynamic model discovery in `ppo_loop_step.sh` (lines 91-115) scans `data/checkpoints/scripted_for_elo/*_scripted.pt` and includes any model with version >= 8. Since v27-v41 all have scripted files in that directory, they are included in every future tournament `--models` list.

When v44 finishes, `ppo_loop_step.sh` will build a `--models` list containing all ~35 models (heuristic + v8-v41 + v44), generating a round-robin schedule of ~595 pairs. Of the 31 new matches needed for v44, 15 will be against corrupted-era models that cluster 200+ Elo below the frontier -- pure waste.

### Match Cache Impact

The match cache (`results/matches/`) stores one JSON per pair. There are ~134 cached files involving v27-v41. These files are:
- **Read by** `run_elo_tournament.py` during the cache-loading phase (lines 404-416): it loads ALL `*.json` files from `--match-cache-dir`.
- **Only used** if both models appear in the `--models` list AND form a scheduled pair. If a model is not in `--models`, its cached matches are loaded but never matched to any scheduled pair, so they are harmlessly ignored.

Therefore: removing v27-v41 from the `--models` list is sufficient. Their cache files can stay. They won't be read into the match list or affect BayesElo fitting.

**However**, there is a subtle issue: the cache loading loop (lines 406-416) reads ALL files in results/matches/. With 134+ corrupted-era files, this is a minor I/O overhead but not a bottleneck.

### Removal Options Analysis

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: Edit ladder JSON** | Remove v27-v41 from ratings dict and matches list, re-run BayesElo on remaining | Clean JSON immediately | Must also prevent re-discovery, or they come back next tournament |
| **B: Don't add to --models** | Raise `MIN_SCRIPTED_VERSION` or add exclusion logic | No file edits, code-driven | They still have scripted files, could confuse manual runs |
| **C: Mark as "retired"** | Add a `retired` flag in ladder JSON | Preserves history | Requires code changes to `run_elo_tournament.py` to skip retired models |
| **D: Rename scripted files** | Move `v{27..41}_scripted.pt` to `v{27..41}_scripted.pt.retired` | Simple, reversible, no code changes | Slightly ad-hoc naming |
| **B+D (recommended)** | Rename scripted files AND reset ladder JSON | Clean discovery + clean ladder | Two manual steps instead of one |

**Option B alone (MIN_SCRIPTED_VERSION) is fragile** because v44+ will eventually pass v41, and the version cutoff would need to be a range exclusion rather than a minimum. Better to remove the files from discovery entirely.

**Option D alone works** because `ppo_loop_step.sh` globs for `*_scripted.pt` -- renaming to `.pt.retired` removes them from discovery. Combined with resetting the ladder JSON, this gives a clean state.

## Conclusions

1. **The corrupted-era models are pure deadweight.** They are 200+ Elo below the frontier, will never be relevant again, and cost ~15 wasted match-runs per tournament update (roughly 15 minutes of CPU time per new generation).

2. **They are actively being included** in every tournament via the scripted_for_elo auto-discovery. This is the main problem to fix.

3. **The safest, simplest cleanup is Option B+D**: rename the scripted files to stop discovery, then regenerate the ladder from cached clean-era matches only. No code changes needed. Fully reversible (just rename back).

4. **Match cache files should be left alone.** They are inert when the models aren't in the --models list, and serve as historical record.

5. **v23-v26 should also be examined.** They have scripted files but aren't in the ladder -- they may or may not be corrupted. If they are pre-bug (v23-v26 trained before the bug was introduced at v27), they should stay. If they are also corrupted, rename them too.

## Recommendations (with exact commands/edits)

### Step 1: Rename corrupted-era scripted files

```bash
cd /home/dkord/code/twilight-struggle-ai
for v in $(seq 27 41); do
  f="data/checkpoints/scripted_for_elo/v${v}_scripted.pt"
  [ -f "$f" ] && mv "$f" "${f}.retired"
done
```

### Step 2: Regenerate ladder from clean models only

```bash
# Build clean model list (v8-v22 + heuristic)
uv run python scripts/run_elo_tournament.py \
  --models heuristic \
    v8:data/checkpoints/scripted_for_elo/v8_scripted.pt \
    v9:data/checkpoints/scripted_for_elo/v9_scripted.pt \
    v10:data/checkpoints/scripted_for_elo/v10_scripted.pt \
    v11:data/checkpoints/scripted_for_elo/v11_scripted.pt \
    v12:data/checkpoints/scripted_for_elo/v12_scripted.pt \
    v13:data/checkpoints/scripted_for_elo/v13_scripted.pt \
    v14:data/checkpoints/scripted_for_elo/v14_scripted.pt \
    v15:data/checkpoints/scripted_for_elo/v15_scripted.pt \
    v16:data/checkpoints/scripted_for_elo/v16_scripted.pt \
    v17:data/checkpoints/scripted_for_elo/v17_scripted.pt \
    v18:data/checkpoints/scripted_for_elo/v18_scripted.pt \
    v19:data/checkpoints/scripted_for_elo/v19_scripted.pt \
    v20:data/checkpoints/scripted_for_elo/v20_scripted.pt \
    v21:data/checkpoints/scripted_for_elo/v21_scripted.pt \
    v22:data/checkpoints/scripted_for_elo/v22_scripted.pt \
  --games 400 --anchor v12 --anchor-elo 2001 \
  --schedule round_robin \
  --match-cache-dir results/matches \
  --out results/elo_full_ladder.json
```

This will reuse all 120 clean-era cached match results (zero new games needed) and refit BayesElo on only clean models + heuristic. The corrupted-era matches in the cache are ignored because those models aren't in --models.

### Step 3 (optional): Archive the old ladder

```bash
cp results/elo_full_ladder.json results/archive/elo_full_ladder_with_corrupted_era.json
```

### Step 4: Verify v23-v26 status

Check whether v23-v26 were trained with or without the bug. If corrupted, also rename their scripted files. If clean, they can be added to the ladder or left out (they were apparently skipped and don't appear in the current ladder anyway).

## Open Questions

1. **Were v23-v26 corrupted?** They have scripted files but aren't in the ladder. Need to check which version introduced the hard-argmax bug. If v27 was the first corrupted version, v23-v26 are clean and could optionally be added back.

2. **Should we also clean the match cache?** Not necessary for correctness, but `results/matches/` currently has ~134 files involving v27-v41. Moving them to `results/matches/archive/` would reduce the cache-loading I/O slightly. Low priority.

3. **Should we prune v8-v10 eventually?** These early models (Elo 1931-1956) are getting far from the frontier (2089). They still provide useful anchoring and floor calibration, but as v44+ pushes higher, the bottom of the clean ladder may also become uninformative. Revisit when the frontier exceeds v22 by 100+ Elo.
