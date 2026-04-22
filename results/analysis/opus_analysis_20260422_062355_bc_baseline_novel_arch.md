# Opus Analysis: BC baseline + novel architecture
Date: 2026-04-22 06:23:55 UTC
Question: (1) How do we train a BC baseline that consumes the upcoming sub-frame JSONL schema, mixing autoregressive and one-shot sub-decisions correctly, and clears the ≥ 0.5 combined gate against heuristic? (2) Conditional on that gate, what concrete novel architecture (GNN + multi-headed attention + CLS pool + card/country cross-attention + two aux heads) should supersede `TSCountryAttnSideModel`?

## Executive Summary
We design a BC baseline (`TSCountryAttnSubframeModel`) that ingests both top-level AR rows and the new sub-frame JSONL rows from `.claude/plan/subframe-row-emission.md` and routes them to the right policy head by `frame_kind`. Top-level ARs train all four heads (card / mode / country / value); sub-frames train the relevant head only (card, country, or SmallChoice) and carry value as a gradient-stopped aux. At inference, the design adopts the user-specified split: multi-pass / autoregressive for realigns, card-select, and SmallChoice sub-frames, but **single-shot** for influence placement (train per-row, infer one allocation) — matching the engine's atomic influence step and the DP decoder already in `CountryAllocHead`. The gate is ≥ 0.5 combined WR vs heuristic at +2 bid, single seeds 50000 / 50500 × 500 games per side. Part B proposes a new architecture `TSNovelModel` with a GNN country encoder (2 MP rounds, ablated over {1, 2, 3}), a self-attention layer with optional regional-local masking, a learned CLS pool token that cross-attends across countries, a card × country cross-attention encoder, card self-attention, and two auxiliary losses (state-diff prediction and opponent belief). Given the 0.003 adv_card spread seen in prior arch sweeps, we explicitly identify the aux heads — not the encoder — as the primary novel value; the encoder ablations are structured so a null encoder result still leaves the aux heads as a distinct contribution. Ablation matrix collapsed from 48 → 14 runs via one-factor-at-a-time plus a single aux × best-arch cross.

## Part A — BC Baseline

### User-specified Part A requirements (verbatim, then addressed)
> - Consumes BOTH top-level AR rows and new sub-frame rows (schema in .claude/plan/subframe-row-emission.md) as supervised targets.
> - MUST emit partial actions AUTOREGRESSIVELY for sequenced sub-decisions (e.g. do several realigns as several separate forward passes, each conditioned on the updated state).
> - BUT influence placement / removal is a SINGLE inference call producing the whole allocation at once (not autoregressive per country). This matches the engine's one-shot influence step and avoids ballooning inference cost.
> - Benchmark: ≥0.5 combined vs heuristic on +2 bid; 500 games USSR + 500 games US, canonical seeds 50000 / 50500 via `tscore.benchmark_batched`.
> - GATE: do NOT proceed to Part B until baseline clears 0.5 combined. If below, iterate data/hparams/target encoding first.

Addressed in §A.1–A.6 below.

### A.1 Data pipeline

**Upstream assumption.** The sub-frame JSONL schema is described in `.claude/plan/subframe-row-emission.md` (lines 197–214 of that file): each sub-frame row inherits all top-level AR scalar fields (turn, ar, phasing, VP, DEFCON, MilOps, Space, influence, hands, etc.) plus the new fields `row_kind` ∈ {"ar", "subframe"}, `frame_kind`, `source_card`, `parent_card`, `step_index`, `total_steps`, `budget_remaining`, `stack_depth`, `criteria_bits`, `eligible_cards`, `eligible_countries`, `eligible_n`, `chosen_option_index`, `chosen_card`, `chosen_country`. **This BC baseline work is gated on the sub-frame collector landing first.** The DAG in §C.2 makes that dependency explicit.

**JSONL → Parquet conversion (recommended).** The existing `TS_SelfPlayDataset` in `python/tsrl/policies/dataset.py` reads Parquet via `_read_slim` (lines 222–226). `.jsonl/.ndjson` support already exists for teacher targets (`python/tsrl/policies/dataset.py:80`). We extend the existing `selfplay_jsonl_to_parquet.py` converter (or whatever tool maps collector output today) to:
- Add a `row_kind` string column.
- Include all sub-frame-specific columns listed above. Set them to default values on top-level-AR rows (`row_kind="ar"`, `frame_kind=0`, `source_card=0`, etc.). Keeping a uniform schema is cheaper than two parallel tables.
- Store `eligible_cards` as `List(Int32)` (bitset-expanded) of length ≤ 112; `eligible_countries` as `List(Int32)` of length ≤ 86. Use `List(Int32)` for consistency with existing list columns (see `_LIST_COLS` on `python/tsrl/policies/dataset.py:242`).

**Dataset class.** Extend `TS_SelfPlayDataset` → `TS_SubframeDataset` (subclass or flag) that:
1. Loads all rows (AR + subframe) into the existing tensor stores.
2. Adds the following new tensor columns:
   - `row_kind: int8` (0 = AR, 1 = subframe).
   - `frame_kind: int8` (enum `FrameKind` in `cpp/tscore/decision_frame.hpp`, values 0–10).
   - `source_card: int16`, `parent_card: int16`, `step_index: int8`, `total_steps: int8`, `budget_remaining: int16`, `criteria_bits: int16`.
   - `eligible_cards_mask: uint8[112]`, `eligible_countries_mask: uint8[86]` — densified bitsets, stored as uint8 (4× less RAM than float32).
   - `chosen_option_index: int8`, `chosen_card: int16`, `chosen_country: int16`.
3. Derives a per-row `target_head` id ∈ {card, mode+country+value, country, small_choice} (§A.2 table) stored as `int8` at load time.
4. `__getitems__` returns the existing fields plus the new tensors. Single dataloader; no dual-pipeline complexity.

**Frame-context scalars.** The existing `FrameContextScalarEncoder` already takes an 8-dim `frame_ctx` block at scalar indices [32:40] (see `python/tsrl/policies/dataset.py:38`). For sub-frame rows we populate `frame_ctx` as a richer condition:
- `frame_ctx[0] = frame_kind / 10.0`
- `frame_ctx[1] = step_index / max(1, total_steps)`
- `frame_ctx[2] = total_steps / 16.0`
- `frame_ctx[3] = budget_remaining / 4.0`
- `frame_ctx[4] = stack_depth / 4.0`
- `frame_ctx[5] = source_card / 112.0`
- `frame_ctx[6] = (criteria_bits & 0xFF) / 255.0`
- `frame_ctx[7] = is_top_level` — already used by the existing encoder for backward compat; set to 1 for `row_kind=ar`, 0 for `row_kind=subframe`.

This mirrors the `frame_ctx` conventions already shipped in `dataset.py:348-349` and requires no model surgery for the BC baseline — the existing 40-dim scalar vector is reused.

**Collate.** Reuse `TS_SelfPlayDataset.passthrough_collate`. No dynamic-padding complexity.

### A.2 Model architecture

The BC baseline is a **derivative of `TSCountryAttnSideModel`** (see `python/tsrl/policies/model.py:1799-1908`) with three surgical additions, no encoder rewrite:

```python
class TSCountryAttnSubframeModel(TSCountryAttnSideModel):
    """BC baseline: v32 architecture + sub-frame heads and routing."""

    def __init__(self, dropout=0.1, hidden_dim=TRUNK_HIDDEN):
        super().__init__(dropout=dropout, hidden_dim=hidden_dim)
        # (1) New single-country CE head for sub-frame country picks.
        #     country_logits from the existing strategy mixture is a
        #     probability-weighted mixture, NOT a clean per-country CE
        #     distribution. For CountryPick/FreeOpsInfluence/NoradInfluence/
        #     SetupPlacement sub-frames we add a dedicated logit head.
        self.country_pick_head = nn.Linear(hidden_dim, NUM_COUNTRIES)
        # (2) Option-index head: the existing small_choice_head (size 8)
        #     already covers SmallChoice/CancelChoice/DeferredOps. Reused.
        # (3) Per-card head for CardSelect/ForcedDiscard/Headline sub-frames
        #     is the existing card_head (size 111). Reused.

    def forward(self, influence, cards, scalars,
                eligible_cards_mask=None, eligible_countries_mask=None):
        out = super().forward(influence, cards, scalars)
        out["country_pick_logits"] = self.country_pick_head(  # (B, 86)
            self._last_hidden  # cache hidden in super() for reuse
        )
        # Legal-action masking: caller may pass masks for inference.
        if eligible_cards_mask is not None:
            out["card_logits"] = _mask_logits(out["card_logits"], eligible_cards_mask)
        if eligible_countries_mask is not None:
            out["country_pick_logits"] = _mask_logits(
                out["country_pick_logits"], eligible_countries_mask)
        return out
```

(In practice, we break out `TSCountryAttnSideModel.forward` so `_last_hidden` is exposed instead of recomputing — that change is two lines in the superclass and kept back-compat by returning the same dict.)

**Per-head target routing.** Each row carries a `target_head` enum set at dataset load time:

| row_kind | frame_kind | Head trained | Target column | Loss |
|---|---|---|---|---|
| ar | TopLevelAR | card + mode + country + value | `action_card_id`, `action_mode`, `action_targets`, `winner_side` | existing v32 loss unchanged |
| subframe | SmallChoice / CancelChoice / DeferredOps | `small_choice_head` | `chosen_option_index` | CE(8) masked to `eligible_n` |
| subframe | CountryPick / FreeOpsInfluence / NoradInfluence / SetupPlacement | `country_pick_head` | `chosen_country` | CE(86) masked to `eligible_countries_mask` |
| subframe | CardSelect / ForcedDiscard | `card_head` (reused) | `chosen_card` (− 1) | CE(111) masked to `eligible_cards_mask` |
| subframe | Headline | `card_head` + implicit `mode_head` = Event | `chosen_card`; mode supervised as 4 | CE(111) + CE(mode=Event) |

**Design choice called out: country pick head is a new dedicated head, not a repurposed strategy.**  The existing `country_logits` comes from a softmax-mixed strategy distribution (`python/tsrl/policies/model.py:1887-1891`) that outputs per-country *probabilities* not raw logits, designed for op-count allocation. For sub-frame single-country picks we need a proper cross-entropy target with `chosen_country` as the class. Reusing one of the 4 strategies would (a) break the mixture semantics at top-level AR, (b) require gradient-stop surgery, and (c) tie two unrelated heads to the same parameters. The +86 × 256 = 22K-parameter dedicated head is negligible.

### A.3 Training procedure

Reuse validated v23/v32 BC hparams (see `scripts/bc_v32_fixed_engine.sh`) with adjustments for the richer loss:

```python
# Config (mirrors scripts/bc_v32_fixed_engine.sh except where noted)
epochs           = 30                      # same as v32 fix
batch_size       = 1024                    # same
lr               = 1e-4                    # same
one_cycle        = True                    # same (OneCycleLR)
weight_decay     = 1e-4                    # same
label_smoothing  = 0.05                    # same
hidden_dim       = 256                     # same
val_fraction     = 0.10                    # same
split            = "deterministic_by_game" # same (prevents leakage)
num_strategies   = 4                       # same
dropout          = 0.1                     # same
```

**Loss composition.**

```
L = L_ar + L_sub + α_value · L_value_ar
L_ar  = CE(card) + CE(mode) + L_country_mixture        # exactly v32 loss
L_sub = 1[CountryPick ∨ FreeOps ∨ ...] · CE(country_pick)
      + 1[CardSelect ∨ ForcedDiscard ∨ Headline] · CE(card, masked)
      + 1[SmallChoice ∨ Cancel ∨ Deferred] · CE(small_choice, masked)
      + 1[Headline] · CE(mode=Event)
L_value_ar = MSE(value_pred, winner_side)             # only on ar rows
α_value    = 0.5                                     # v32 default
```

**Sub-frame weight balancing.** Self-play rows are dominated by free-ops country picks (one per op spent). Left uncorrected, `L_country_pick` will swamp the other sub-frame heads. Apply inverse-frequency class weights per `target_head`, normalised so the total sub-frame loss has the same expected magnitude as `L_ar`:

```python
w_head[h] = N_ar / max(1, count(h))           # per-head weight
w_head    = clamp(w_head, 0.1, 10.0)          # anti-pathology
```

Compute `w_head` once at dataset construction. This keeps BC training targeting roughly the same effective gradient signal per head.

**Optimiser / schedule.** Adam (already in `scripts/train_ppo.py:3232`, `scripts/train_baseline.py`). OneCycleLR over 30 epochs.

**Warm-start.** Start from the current best v32 checkpoint (`results/ppo_v32_continue/ppo_best.pt` or the current-head v33/v35 best). The new `country_pick_head` is initialised zero-bias, Xavier weights, same as the other linear heads. `--reset-optimizer` should be used because the optimizer state is v32-specific (see `feedback_bc_before_ppo.md` and the behavior in `scripts/train_ppo.py:3235`).

**Precision.** bf16 autocast during forward (existing convention on RTX 3050 4GB; see `feedback_cuda_wsl.md`).

### A.4 Inference procedure

This is the part the user called out explicitly: some sub-decisions are autoregressive (one forward pass per sub-frame, each conditioned on the updated state), but **influence placement is a single inference call that emits a full allocation**.

**State machine (per top-level AR):**

```
┌──────────────────────────────────────────────────────────────────┐
│                      Top-level AR begins                         │
│                                                                  │
│  1. Forward pass on current PublicState + hand features          │
│     → card_logits, mode_logits, country_logits (mixture),        │
│       country_strategy_logits, strategy_logits, value.           │
│  2. Mask illegal cards / illegal modes via legal_actions API.   │
│  3. Sample card ∼ card_probs, then mode ∼ mode_probs | card.    │
│  4. Dispatch on mode:                                            │
│                                                                  │
│  ├── INFLUENCE  (mode=0, OpsFirst with Influence, Headline-BC):  │
│  │    ONE-SHOT. Call CountryAllocHead.forward(                  │
│  │      country_features = trunk hidden expanded per-country,   │
│  │      budget = ops_available)                                 │
│  │    → returns (86,) allocation counts via DP decoder.         │
│  │    Apply the whole allocation atomically through the         │
│  │    engine's single influence-step API.                       │
│  │    (Training asymmetry: the BC dataset gives us one sub-     │
│  │     frame row per op spent; we still train per-row because   │
│  │     each row is a clean supervised signal. At inference we   │
│  │     collapse to one DP call to save 3-4× inference cost.)    │
│  │                                                              │
│  ├── REALIGN  (mode=2):                                         │
│  │    AUTOREGRESSIVE. For i = 1..n_realigns:                    │
│  │      s_i = engine.public_state_after(prev_realigns)          │
│  │      forward_pass(s_i) → country_pick_logits                 │
│  │      mask to DEFCON-legal countries (exclude                 │
│  │        DEFCON-restricted regions; see decode_helpers.hpp)    │
│  │      argmax / sample → country_i                             │
│  │      commit realign, advance state.                          │
│  │                                                              │
│  ├── COUP  (mode=1):                                            │
│  │    ONE-SHOT. Single country pick. Call forward_pass on       │
│  │    current state, country_pick_logits, mask to coup-legal    │
│  │    (BGs only if DEFCON=2, etc.), sample country, commit.     │
│  │    Coup is one atomic decision; no autoreg.                  │
│  │                                                              │
│  ├── SPACE  (mode=3):                                           │
│  │    ONE-SHOT. No country picking; engine resolves.            │
│  │                                                              │
│  ├── EVENT  (mode=4) and OPSFIRST  (mode=5):                    │
│  │    EVENT-DRIVEN AUTOREG SUBFRAMES.                           │
│  │    Trigger the event via engine.apply_action; any            │
│  │    DecisionFrame pushed by the event (CardSelect,            │
│  │    ForcedDiscard, SmallChoice, CountryPick, CancelChoice,    │
│  │    DeferredOps) is resolved by a fresh forward pass with     │
│  │    frame_ctx populated from the DecisionFrame fields,        │
│  │    the eligible_* masks applied to the relevant head.        │
│  │    OpsFirst additionally triggers a subsequent Ops-sub-      │
│  │    action (Influence/Coup/Realign) which itself follows      │
│  │    the branching above.                                      │
│  └── HEADLINE  (only at headline phase):                        │
│       One forward pass per side (simultaneous in engine, but    │
│       collector emits two separate Headline sub-frames).        │
│       Each is a card selection: card_logits masked to hand ∩    │
│       non-scoring, mode implicitly Event.                       │
└──────────────────────────────────────────────────────────────────┘
```

**The influence training/inference asymmetry must be explicit.** During training, every free-ops country-placement row contributes gradient to `country_pick_head`. During inference we bypass `country_pick_head` entirely for influence and instead use the **existing** `CountryAllocHead` DP decoder (see `python/tsrl/policies/model.py:405-473`) which outputs a whole-budget allocation in one forward pass. This is the design choice the user specified: train the single-country head on per-row data (for generalisation), but at inference emit the whole allocation at once (for cost and engine-atomic-step alignment).

**Concretely, which scores feed the DP decoder?** The existing `CountryAllocHead.score_head` takes `(B, n_countries, hidden_dim)` and returns marginal per-op-count scores. In v32 this is fed by the attention encoder's per-country tokens. The BC baseline inherits this pipeline unchanged — nothing in Part A changes how influence allocation happens at inference.

**Implementation touchpoint.** The Python side already has an `nn_policy.py`-style wrapper that translates model outputs into engine actions. For sub-frame inference we need either:
- **(Recommended) C++ side.** Implement `PolicyCallbackFn` as specified in `.claude/plan/subframe-row-emission.md` §6, calling a TorchScript-exported `TSCountryAttnSubframeModel` via `tscore`'s existing batched inference. This is the same route `base_policy` already uses for top-level ARs.
- **(Alternative) Python side.** For BC benchmark-only purposes we can stay in Python by using `tscore.benchmark_batched` with a Python callback. But the user's benchmark command goes through `tscore.benchmark_batched` which expects a scripted checkpoint. Export via `cpp/tools/export_baseline_to_torchscript.py` (already modified in current `git status`).

### A.5 Benchmark protocol

Single-seed per side, 500 games each, per user spec:

```bash
# Export the BC checkpoint to TorchScript for the C++ benchmark harness.
uv run python cpp/tools/export_baseline_to_torchscript.py \
    --checkpoint results/bc_subframe_v1/baseline_best.pt \
    --model-type country_attn_subframe \
    --out results/bc_subframe_v1/baseline_best_scripted.pt

# Run the authoritative gate benchmark.
uv run python - <<'PY'
import os; os.environ["OMP_NUM_THREADS"] = "1"
import sys; sys.path.insert(0, "build-ninja/bindings")
import torch; torch.set_num_threads(1)
import tscore
CKPT = "results/bc_subframe_v1/baseline_best_scripted.pt"
N = 500

# Per-user-spec: USSR side uses seed 50000, US side uses seed 50500.
ussr = tscore.benchmark_batched(CKPT, tscore.Side.USSR, N, pool_size=32, seed=50000)
us   = tscore.benchmark_batched(CKPT, tscore.Side.US,   N, pool_size=32, seed=50500)
wr_ussr = sum(1 for x in ussr if x.winner == tscore.Side.USSR) / N
wr_us   = sum(1 for x in us   if x.winner == tscore.Side.US)   / N
combined = 0.5 * (wr_ussr + wr_us)
print(f"USSR {wr_ussr:.3f}  US {wr_us:.3f}  combined {combined:.3f}")
PY
```

Notes:
- `benchmark_batched` defaults: `nash_temperatures=True`, `+2 bid`, heuristic opponent. Leave defaults. See `feedback_benchmark_api.md` on using `sum(1 for x if ...)` not `.count()`.
- `pool_size=32` for RTX 3050 4GB (existing convention in `bench_bc_v32_fixed_multiseed.py:51`).
- `OMP_NUM_THREADS=1` and `torch.set_num_threads(1)` are mandatory in-proc (shared with engine threads).

**Optional robustness check (not the gate):** after passing the single-seed gate, run the 5-seed multi-grid from `bench_bc_v32_fixed_multiseed.py` (seeds {50000, 60000, 70000, 80000, 90000} USSR and {50500, 60500, 70500, 80500, 90500} US) to confirm the gate result is not single-seed noise. This is only cited as "nice to have"; it is not required by the spec.

### A.6 Success gate

- **combined ≥ 0.5** on the single-seed gate above → proceed to Part B.
- **combined < 0.5** → do NOT proceed to Part B. Iterate in this order, one change at a time:
  1. Target encoding for sub-frames (e.g. smooth CE vs hard CE for small-choice; verify `country_pick_head` masks are correct via a zero-illegal-rate assertion).
  2. Per-head loss weights `w_head`: start with inverse-frequency, try uniform, try 2× upweight on `country_pick` sub-frames.
  3. Data coverage: confirm sub-frame collector emitted non-degenerate distributions (no frame_kind with <1% of rows, no frame_kind at 99%).
  4. Hparams: only after (1)-(3), try lr ∈ {5e-5, 2e-4} and epochs = 50.
  5. As a last resort, gate the sub-frame loss off (`L_sub = 0`) and verify the model still clears v32's historical 0.483–0.55 combined band. That pins whether the regression is in sub-frame training vs architecture plumbing.

## Part B — Novel Architecture

### User-specified Part B requirements (verbatim)
> Country encoder:
>   - GNN message passing over country adjacency graph. Start with 2 rounds. Ablation target: {1, 2, 3}.
>   - Multi-headed self-attention over countries.
>     - Ablation: full attention vs attention masked to "same region + 1-hop neighbors" (regional-local attention).
>   - Pooling beyond sum + per-region: include a LEARNED "pool token" (CLS-style) that cross-attends to every country embedding; its output serves as a global state embedding fed to heads. Keep sum + per-region as baseline aux features.
>
> Card encoder:
>   - Cards cross-attend to country embeddings (cards = query; countries = key/value).
>   - Cards self-attend 1-2 layers — lets the model learn combos and anti-event plays.
>
> Feature inputs:
>   - Sub-frame features from the new schema: frame_kind, source_card, step_index, total_steps, budget_remaining, criteria_bits, eligible_cards_mask, eligible_countries_mask. These condition the policy head at sub-frame rows.
>   - Region scoring scalars (already 42-dim in v32).
>   - Country state features (influence, adjacency, scoring-value).
>
> Heads:
>   - Existing: card head, mode head, country allocation head, option_index head (for sub-frames), value head.
>   - AUX HEAD 1: State-diff prediction. Given (s, a), predict s' = T(s, a) as a DELTA. Scope: per-country influence delta, VP delta, DEFCON delta, MilOps delta. Unsupervised regularizer: model must understand action semantics to predict next state. Training data is free (s, a, s') from every self-play row.
>   - AUX HEAD 2: Belief head. Predict P(opponent_card_i ∈ opponent_hand | public_state, public_history). Cross-entropy against known ground truth from self-play telemetry (opponent hand is observable in self-play). Gives the model a representation of opponent capability that improves policy at inference.

Addressed in §B.1–B.7 below.

### B.1 Country encoder (`CountryGNNAttnCLSEncoder`)

```python
class CountryGNNAttnCLSEncoder(nn.Module):
    """
    Country tokens: 86 learned embeddings + dynamic features.
    Pipeline:
      (1) Input projection:   (B, 86, 13)  →  (B, 86, D)     D = 128
      (2) GNN message passing: n_mp ∈ {0, 1, 2, 3} rounds
          h_i ← h_i + MLP( [h_i, Σ_{j ∈ N(i)} W · h_j / deg(i)] )
      (3) Multi-headed self-attention (1 layer, 4 heads):
            mask ∈ {full, regional-local}
            regional-local: j attends to i iff region(j) == region(i)
                            OR j ∈ N(i) (1-hop)
      (4) CLS pool token: learned (D,) token cross-attends to all 86
          country tokens (one cross-attn layer, 4 heads).
          → pool_embed (B, D).
      (5) Baseline aux features: sum-pool and per-region mean-pool
          over the post-MP tokens (7 regions).
      (6) Final out: concat [pool_embed, sum_pool, *region_pools]  → (B, 8*D)
          project to INFLUENCE_HIDDEN = 128.
    """

    _EMBED_DIM   = 128    # matches INFLUENCE_HIDDEN
    _NUM_HEADS   = 4
    _NUM_REGIONS = 7
    _NUM_COUNTRIES = NUM_COUNTRIES  # 86

    def __init__(self, n_mp: int = 2, attn_mask_mode: str = "full",
                 use_cls: bool = True):
        super().__init__()
        self.n_mp = n_mp
        self.attn_mask_mode = attn_mask_mode   # "full" | "regional_local"
        self.use_cls = use_cls

        # Static + dynamic country features (same 13 dims as v32).
        self.register_buffer("country_static", _COUNTRY_FEATS.clone())     # (86, 11)
        self.register_buffer("region_masks",
                             torch.stack([m.clone() for m in _REGION_MASKS]))  # (7, 86)
        self.register_buffer("adjacency",  _COUNTRY_ADJACENCY.clone())     # (86, 86) row-normalised
        self.register_buffer("attn_mask",  self._build_attn_mask())        # (86, 86) bool

        self.country_proj = nn.Linear(_COUNTRY_FEAT_DIM + 2, self._EMBED_DIM)

        # GNN: stacked MLP message passers
        self.mp_layers = nn.ModuleList([
            GNNMessagePasser(self._EMBED_DIM) for _ in range(n_mp)
        ])

        # Self-attention (single layer, 4 heads)
        self.qkv_proj = nn.Linear(self._EMBED_DIM, 3 * self._EMBED_DIM)
        self.attn_out = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.attn_ln  = nn.LayerNorm(self._EMBED_DIM)

        # CLS pool token + cross-attention
        if use_cls:
            self.cls_token   = nn.Parameter(torch.zeros(1, 1, self._EMBED_DIM))
            nn.init.normal_(self.cls_token, std=0.02)
            self.cls_q_proj  = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
            self.cls_kv_proj = nn.Linear(self._EMBED_DIM, 2 * self._EMBED_DIM)
            self.cls_out     = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
            self.cls_ln      = nn.LayerNorm(self._EMBED_DIM)

        # Final projection: [pool_embed, sum_pool, 7 × region_pool]
        n_pool_components = (1 if use_cls else 0) + 1 + self._NUM_REGIONS
        self.out_proj = nn.Linear(n_pool_components * self._EMBED_DIM, INFLUENCE_HIDDEN)

    def forward(self, influence):
        # influence: (B, 172). Build per-country tokens exactly as v32.
        B = influence.shape[0]
        tokens = self._build_tokens(influence)           # (B, 86, D)
        for layer in self.mp_layers:
            tokens = layer(tokens, self.adjacency)       # message passing
        tokens = tokens + self._attn(tokens)             # residual self-attn
        tokens = self.attn_ln(tokens)

        sum_pool   = tokens.mean(dim=1)                  # (B, D)
        region_ps  = [ _masked_mean_pool(tokens, self.region_masks[i])
                       for i in range(self._NUM_REGIONS) ]  # each (B, D)

        parts = []
        if self.use_cls:
            cls = self.cls_token.expand(B, -1, -1)       # (B, 1, D)
            cls_out = self._cls_cross_attn(cls, tokens)  # (B, D)
            parts.append(cls_out)
        parts.append(sum_pool)
        parts.extend(region_ps)
        concat = torch.cat(parts, dim=-1)                # (B, n_pool_components*D)
        return torch.relu(self.out_proj(concat)), tokens # (B, 128), (B, 86, D)
```

Notes:
- Message passer `GNNMessagePasser` is a standard mean-aggregator:
  `h_i ← ReLU(h_i + Linear([h_i || Σ_j A_ij h_j]))`. `A` is the row-normalised adjacency already built in `python/tsrl/policies/model.py:219` (`_COUNTRY_ADJACENCY`). No learned edge weights in v1; keep the inductive bias clean.
- Regional-local attention mask: `M[i, j] = 1` iff `region(i) == region(j)` OR adjacency[i, j] > 0, OR `i == j`. Pre-computed as a boolean buffer.
- Per-token residual wiring: `tokens = tokens + attn_out(softmax(QK^T / sqrt(d)) V)` with `F.scaled_dot_product_attention(..., attn_mask=self.attn_mask)` to stay in the fast kernel path (see v32's manual QKV pattern on `model.py:678-707`).
- CLS cross-attn is a single-layer cross-attention: Q = cls_token projected, K/V = tokens. No self-attn on CLS (unnecessary; it's 1 token).
- Return **both** the pooled global embedding and the per-country token map. The card encoder needs the per-country tokens for cross-attention; the allocation / country-pick heads also need them.

**Parameter count.** At D=128, n_mp=2: 86×13 proj ≈ 1.6K + 2 × (128×128 + 128×128) ≈ 65K (GNN) + 3×128² ≈ 50K (attn) + 128×(7+1+1)×128 ≈ 147K (out_proj) ≈ **260K params** for the country encoder alone. Compare v32's `CountryAttnEncoder`: ~42K + out_proj 128×(1+7)×128 = 131K → ~175K total. Net +85K — modest.

### B.2 Card encoder (`CardCrossAttnEncoder`)

```python
class CardCrossAttnEncoder(nn.Module):
    """
    Cards cross-attend to country tokens, then 1-2 self-attn layers.

    Input:
      - cards: (B, 448) — 4 one-hot-ish vectors (known_in, possible, discard, removed)
               Reshape into 112 card tokens each with a 4-dim status vector plus
               8-dim static card features (_CARD_FEATS).
      - country_tokens: (B, 86, D) from CountryGNNAttnCLSEncoder.

    Output:
      - card_hidden: (B, CARD_HIDDEN=128) — pooled over cards with one learned
                     card-pool token OR mean over playable cards.
      - card_tokens: (B, 112, D) — per-card token (for belief aux head in §B.4).
    """
    _EMBED_DIM   = 128
    _NUM_HEADS   = 4
    _NUM_CARDS   = 112
    _NUM_SELF_ATTN = 2   # ablate: {1, 2}

    def __init__(self, n_self_attn: int = 2):
        super().__init__()
        self.register_buffer("card_static", _CARD_FEATS.clone())   # (112, 8)
        # per-card input dims: 4 (status) + 8 (static) = 12
        self.card_proj = nn.Linear(12, self._EMBED_DIM)

        # Cross-attn: card queries, country keys/values
        self.cross_q   = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.cross_kv  = nn.Linear(self._EMBED_DIM, 2 * self._EMBED_DIM)
        self.cross_out = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.cross_ln  = nn.LayerNorm(self._EMBED_DIM)

        # Self-attn stack (1-2 layers)
        self.self_attn = nn.ModuleList([
            SelfAttnBlock(self._EMBED_DIM, self._NUM_HEADS)
            for _ in range(n_self_attn)
        ])

        # Pool: learned card pool token cross-attending over card_tokens.
        self.card_pool_token = nn.Parameter(torch.zeros(1, 1, self._EMBED_DIM))
        nn.init.normal_(self.card_pool_token, std=0.02)
        self.pool_q   = nn.Linear(self._EMBED_DIM, self._EMBED_DIM)
        self.pool_kv  = nn.Linear(self._EMBED_DIM, 2 * self._EMBED_DIM)
        self.pool_out = nn.Linear(self._EMBED_DIM, CARD_HIDDEN)

    def forward(self, cards, country_tokens):
        B = cards.shape[0]
        status = cards.view(B, 4, self._NUM_CARDS).permute(0, 2, 1)  # (B, 112, 4)
        stat   = self.card_static.unsqueeze(0).expand(B, -1, -1)     # (B, 112, 8)
        per_card = torch.cat([status, stat], dim=-1)                  # (B, 112, 12)
        tokens   = torch.relu(self.card_proj(per_card))               # (B, 112, D)

        # Cross-attn: cards attend over countries.
        tokens = tokens + self._cross_attn(tokens, country_tokens)    # residual
        tokens = self.cross_ln(tokens)

        for blk in self.self_attn:
            tokens = blk(tokens)

        # Pool: learned token over cards.
        q  = self.pool_q(self.card_pool_token.expand(B, -1, -1))      # (B, 1, D)
        kv = self.pool_kv(tokens).chunk(2, dim=-1)
        k, v = kv
        pooled = F.scaled_dot_product_attention(
            q.view(B, 1, self._NUM_HEADS, self._EMBED_DIM // self._NUM_HEADS).transpose(1,2),
            k.view(B, 112, self._NUM_HEADS, self._EMBED_DIM // self._NUM_HEADS).transpose(1,2),
            v.view(B, 112, self._NUM_HEADS, self._EMBED_DIM // self._NUM_HEADS).transpose(1,2),
        ).transpose(1,2).contiguous().view(B, 1, self._EMBED_DIM).squeeze(1)  # (B, D)
        card_hidden = torch.relu(self.pool_out(pooled))  # (B, CARD_HIDDEN)
        return card_hidden, tokens                        # (B, 128), (B, 112, D)
```

Shapes:
- Input `cards`: (B, 448) — existing contract from `TSCountryAttnSideModel`.
- `country_tokens`: (B, 86, 128) from the country encoder.
- `card_hidden`: (B, 128) for the trunk.
- `card_tokens`: (B, 112, 128) for the belief aux head (§B.4).

Param count at D=128, n_self_attn=2: ~12×128 + (cross: 3·128²) + 2 × (self-attn block ≈ 130K) + pool ≈ 380K. Compared to v32's card encoder (a single `nn.Linear(448, 128)` ≈ 57K), this is +320K params. Still well below a Transformer-encoder blowup.

### B.3 Feature inputs

| Input | Where it enters | Shape |
|---|---|---|
| **Per-country dynamic** — USSR influence, US influence | `CountryGNNAttnCLSEncoder._build_tokens` | 2 per country, concat with 11 static |
| **Per-country static** — stability, is_bg, 7-region onehot, us_start/3, ussr_start/3 | `country_static` buffer | (86, 11), reused from v32 |
| **Country adjacency** — row-normalised | `adjacency` buffer, used by GNN message passers and attention mask | (86, 86), reused from v32 |
| **Region scoring scalars** — inherited from v32 (already 42-dim per `project_v32_region_scalars.md`) | `FrameContextScalarEncoder` input via `ControlFeatGNNEncoder` (as in v32) | (B, 42) appended to SCALAR_DIM scalars |
| **Global scalars** — VP, DEFCON, MilOps, Space, turn, AR, phasing, active effects, Chernobyl, ops modifier | Existing 32-dim block | (B, 32) scalar input |
| **Per-card static** — ops, side_ussr, side_us, era_{early,mid,late}, is_scoring, is_starred | `CardCrossAttnEncoder.card_static` | (112, 8), reused from v32 |
| **Per-card dynamic** — actor_known_in, actor_possible, discard, removed | Reshape of `cards` input (112, 4) | inside card encoder |
| **Sub-frame features** — `frame_kind`, `source_card`, `step_index`, `total_steps`, `budget_remaining`, `criteria_bits`, `eligible_cards_mask`, `eligible_countries_mask` | `frame_ctx` block of scalar input (§A.1) for frame_kind, source_card, step_index, total_steps, budget_remaining, criteria_bits. The two masks are *applied at the output heads*, not fed as input features — this avoids the 112+86 = 198-dim feature inflation and is semantically correct (masks constrain the action space, not the state). | (B, 8) for scalars; (B, 112) and (B, 86) for masks at head |

**Callouts:**
- Region scoring scalars are *already* 42-dim in v32 per `memory/project_v32_region_scalars.md`. They are inherited, not a novel input.
- `criteria_bits` is packed as `(criteria_bits & 0xFF) / 255.0` in frame_ctx[6]. This is lossy (bit 9+ is dropped) but simple; loss of higher bits is marginal for the bits actually used by sub-frame kinds.
- `eligible_cards_mask` and `eligible_countries_mask` enter **at legal-action masking time** at the heads, not as encoder input. Feeding a 198-dim dynamic mask as input would be duplicative (the model must learn "if mask=0, output 0" which is exactly what the mask already enforces).

### B.4 Heads

**Existing heads (reused from v32, adjusted in/out):**

| Head | Input | Output | Loss |
|---|---|---|---|
| `card_head` | trunk hidden (B, H) | (B, 111) | masked CE on AR rows + CardSelect/ForcedDiscard/Headline sub-frames |
| `mode_head` | trunk hidden | (B, 6) | masked CE on AR rows + Headline (mode=Event) |
| `strategy_heads` / `strategy_mixer` → `country_logits` | trunk hidden | (B, 4, 86), (B, 4) → mixture (B, 86) | ops-weighted log-mixture CE on AR influence/coup/realign rows (unchanged) |
| `country_pick_head` (new in BC baseline, carried forward) | trunk hidden | (B, 86) | masked CE on sub-frame country picks |
| `small_choice_head` | trunk hidden | (B, 8) | masked CE on SmallChoice/Cancel/Deferred sub-frames |
| `value_head_{ussr,us}` | trunk hidden | (B, 1) | MSE on AR rows (skip sub-frame rows for value — no additional signal there) |

**New aux heads:**

**Aux head 1: state-diff (`TransitionDiffHead`).**

Given per-country tokens `T ∈ (B, 86, D)` and an action-conditioning vector `a ∈ (B, D_a)` (see below), predict:
- Per-country influence deltas: `Δinfluence_c ∈ R^2` (USSR delta, US delta) for each country.
- VP delta: `ΔVP ∈ R` (typically in [-5, +5]).
- DEFCON delta: `ΔDEFCON ∈ R` (typically in {-1, 0, +1, +2}).
- MilOps delta per side: `ΔMilOps ∈ R^2` (bounded [0, +6]).

```python
class TransitionDiffHead(nn.Module):
    def __init__(self, D=128, D_a=64, hidden=128):
        super().__init__()
        # Action conditioning vector built from card, mode, country_pick, small_choice.
        self.action_enc = nn.Linear(111 + 6 + 86 + 8, D_a)
        # Per-country head: input is [T_c || a] per country.
        self.per_country_mlp = nn.Sequential(
            nn.Linear(D + D_a, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 2),  # Δinfluence_c
        )
        # Global diffs (VP, DEFCON, MilOps_ussr, MilOps_us)
        self.global_mlp = nn.Sequential(
            nn.Linear(D + D_a, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 4),
        )

    def forward(self, country_tokens, trunk_hidden, a_one_hot):
        # country_tokens: (B, 86, D); trunk_hidden: (B, H); a_one_hot: (B, 111+6+86+8)
        B = country_tokens.shape[0]
        a = torch.relu(self.action_enc(a_one_hot))               # (B, D_a)
        a_c = a.unsqueeze(1).expand(-1, 86, -1)                   # (B, 86, D_a)
        per_c = torch.cat([country_tokens, a_c], dim=-1)          # (B, 86, D+D_a)
        d_influence = self.per_country_mlp(per_c)                 # (B, 86, 2)
        pooled = country_tokens.mean(dim=1)                       # (B, D)
        global_in = torch.cat([pooled, a], dim=-1)                # (B, D+D_a)
        d_global = self.global_mlp(global_in)                     # (B, 4)
        return {"d_influence": d_influence, "d_global": d_global}
```

**Loss.** MSE for all 4 quantities. Training data is free: for each self-play row, the next row of the same game (or the post-action state snapshot already in `StepTrace`) gives us `s' = T(s, a)` directly.

```
L_state_diff = MSE(pred.d_influence, s'.influence - s.influence)
             + 0.5 · MSE(pred.d_global, [s'.vp - s.vp,
                                          s'.defcon - s.defcon,
                                          s'.milops_ussr - s.milops_ussr,
                                          s'.milops_us - s.milops_us])
```

Terminal rows (no `s'`): zero out the loss via a `has_next` mask.

**Aux head 2: belief (`OpponentBeliefHead`).**

Given the trunk hidden and per-card tokens, predict for each card `c` the probability `P(c ∈ opponent_hand | public_state)`.

```python
class OpponentBeliefHead(nn.Module):
    def __init__(self, D=128, hidden=64):
        super().__init__()
        # Per-card MLP: input is card_token_c. Outputs one logit per card.
        self.per_card_mlp = nn.Sequential(
            nn.Linear(D, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 1),
        )

    def forward(self, card_tokens):
        # card_tokens: (B, 112, D)
        return self.per_card_mlp(card_tokens).squeeze(-1)   # (B, 112)
```

**Loss.**

```
L_belief = BCE_with_logits(belief_logits, opp_hand_indicator)
        * (1 - public_reveal_mask)     # zero out where card is publicly known
```

where `opp_hand_indicator[c] = 1 iff card c is in opponent's hand at this row`, and `public_reveal_mask[c] = 1 iff card c is public (discard, removed, own-hand, China-card on opposite owner, publicly revealed)`. Public-reveal-mask rules out trivial classes — the belief head is not credited for predicting what is already known.

Ground truth is available at collection time: `opp_hand_snapshot` already exists in `StepTrace` (see `cpp/tscore/game_loop.hpp:133` from the spec file). The collector writes it to `opp_known_in` / `opp_possible` — but these are the *actor's* causal beliefs, not ground truth. For the belief loss we need the actual opponent hand. Add a new `opp_hand_truth` column to the collector schema (it is already accessible in-engine at collection time; use only at train-time, never fed back into inference inputs).

**Legal masking** for all heads stays the same pattern as v32:
```python
logits = logits.clone()
logits[~legal_mask] = float("-inf")
probs = torch.softmax(logits, dim=-1)
```

### B.5 Training loss composition

```
L_total = L_policy + α · L_value + β · L_state_diff + γ · L_belief
```

where:
- `L_policy = L_ar + L_sub` from §A.3 (identical).
- `L_value = MSE(value_pred, value_target)` with the v32 2× weight on US-win states (per `memory/feedback_us_win_value_weighting.md`).
- `L_state_diff` as defined in §B.4.
- `L_belief` as defined in §B.4.

**Starting weights (v1):**
- α = 0.5 (v32 default)
- β = 0.1 — aux is regulariser, not primary signal
- γ = 0.1 — same

**Tuning protocol.** In the first training run, log each loss term to W&B with the keys `train/{policy, value, state_diff, belief}_loss` and their validation counterparts. If `L_state_diff` or `L_belief` dominates policy loss by > 3× after epoch 5, halve β or γ. The aux heads are not fair-weighted by default because they have more dimensions (86 × 2 country deltas vs a single card class); start lower and grow if saturation is high.

**Stop-gradient on trunk from aux?** No. The whole point of the aux heads is to inject extra gradient into the trunk for representation-learning. Only stop gradient on the **input** to the aux heads if you want to *post-train* a linear probe; at training time the aux gradient flows.

**Action conditioning for state-diff.** The `a_one_hot` fed to the transition-diff head is the ground-truth action at this row (card + mode + country + small_choice), not the model's predicted action. Using the predicted action would create a chicken-and-egg where wrong policy predictions corrupt state-diff loss; using the ground-truth action keeps state-diff as a pure world-model signal and lets policy gradient flow through `L_policy`.

### B.6 Ablation matrix

Full 3×2×2×4 = 48 is infeasible; the prior arch sweep (`results/analysis/opus_analysis_20260417_arch_sweep_update.md`) saw 0.003 adv_card spread across radically different architectures. Use a **one-factor-at-a-time design with a single aux cross**, 14 runs total:

| Run | MP rounds | Attention | CLS | Aux | Purpose |
|---|---|---|---|---|---|
| 0 (baseline) | 2 | full | on | none | Reference |
| 1 | 0 (no MP) | full | on | none | MP-necessity |
| 2 | 1 | full | on | none | MP-1 |
| 3 | 3 | full | on | none | MP-saturation |
| 4 | 2 | regional-local | on | none | Mask effect |
| 5 | 2 | full | off | none | CLS effect |
| 6 | 2 | full | on | state-diff only | Aux-1 isolated |
| 7 | 2 | full | on | belief only | Aux-2 isolated |
| 8 | 2 | full | on | both | Aux-combined |
| 9 | best-MP | best-attn | best-CLS | none | Best encoder, no aux |
| 10 | best-MP | best-attn | best-CLS | state-diff only | Best encoder + aux-1 |
| 11 | best-MP | best-attn | best-CLS | belief only | Best encoder + aux-2 |
| 12 | best-MP | best-attn | best-CLS | both | Final candidate |
| 13 | 2 | full | on | none (PPO warm-start) | Sanity: matches v32 baseline |

**Justification for collapse:**
- Runs 0–3 isolate MP rounds.
- Runs 0, 4 isolate attention mask mode.
- Runs 0, 5 isolate CLS token.
- Runs 0, 6, 7, 8 isolate aux heads.
- Runs 9–12 recombine the best encoder (picked from 0–5) with all 4 aux settings.
- Run 13 is a regression guard: if "best encoder, no aux" ≠ "v32 + subframe heads", something is off.

If runs 0–5 are all within 0.003 adv_card of each other (likely, per the 2026-04-17 analysis), **skip runs 9–12 for encoder sweeping and go straight to run 8 as the novel architecture candidate**. In that case, runs 6, 7, 8 are the primary contribution.

### B.7 Validation protocol

Each retained ablation run:
1. **BC training** on the same sub-frame dataset as Part A. 30 epochs, same hparams, 3 seeds (42, 43, 44 — per the prior arch sweep convention).
2. **Primary offline metric:** advantage-weighted card accuracy (adv_card), same as prior arch sweeps. Secondary: unweighted card_acc, policy_loss, value_loss, state_diff_mse, belief_bce.
3. **Online benchmark:** 500 games × 2 sides vs heuristic at +2 bid, seeds 50000 / 50500. Report USSR WR, US WR, combined.
4. **Elo placement:** if combined ≥ 0.5, run a 50-game match against the BC baseline (Part A) and against the current v32 production checkpoint. Add to the `results/elo/elo_full_ladder.json` ladder.
5. **Go/no-go for promotion to PPO:** adv_card ≥ BC baseline + 0.005 AND combined WR ≥ BC baseline − 0.02. The adv_card bar must be a real improvement; the combined WR must not regress significantly.

## Part C — Execution plan

### C.1 File list

**Part A — BC baseline:**

Files to create:
- `scripts/train_bc_subframe.py` — wrapper around `scripts/train_baseline.py` that sets `--model-type country_attn_subframe`, configures the per-head loss weights, and enables sub-frame row ingestion.
- `scripts/bench_bc_subframe_gate.py` — exact single-seed gate benchmark (§A.5) that writes `results/bench_bc_subframe_gate.json`. Returns exit code 0 iff combined ≥ 0.5.
- `results/bc_subframe_v1/` — training artefact directory.
- `tests/python/test_bc_subframe_dataset.py` — unit test: load a tiny parquet with 3 AR + 5 sub-frame rows, verify per-head target routing matches the table in §A.2.
- `tests/python/test_bc_subframe_model_forward.py` — unit test: forward pass returns all expected keys including `country_pick_logits`.

Files to modify:
- `python/tsrl/policies/dataset.py` — add `TS_SubframeDataset` subclass (or `subframe_mode` flag on `TS_SelfPlayDataset`); extend `_NEEDED_COLS` with the sub-frame columns; add per-row `target_head` derivation.
- `python/tsrl/policies/model.py` — add `TSCountryAttnSubframeModel` class (section A.2) after line 1908.
- `python/tsrl/constants.py` — register `"country_attn_subframe": TSCountryAttnSubframeModel` in `_LazyModelRegistry`.
- `scripts/train_baseline.py` — extend the loss branch in `train_one_epoch` to dispatch per-head loss by `target_head`; add the `--model-type country_attn_subframe` path.
- `cpp/tools/export_baseline_to_torchscript.py` — add `"country_attn_subframe"` to the model-type whitelist; verify TorchScript traces the new `country_pick_head` and the masked-inference path.
- `cpp/tools/collect_selfplay_rows_jsonl.cpp` — already covered by the sub-frame collector spec; no BC-specific changes here, but verify the Parquet converter (or add one) emits the sub-frame columns BC needs.
- `python/tsrl/etl/` — add or extend the JSONL→Parquet converter to carry the sub-frame columns; add `row_kind` as a string column. (Check existing converter; if the ETL tooling already flows the top-level JSONL → Parquet and just needs schema extension, this is a 1-day change.)

**Part B — Novel architecture:**

Files to create:
- `python/tsrl/policies/novel_encoder.py` — `CountryGNNAttnCLSEncoder`, `CardCrossAttnEncoder`, `GNNMessagePasser`, `SelfAttnBlock`, helpers. Keep these separate from `model.py` to contain churn.
- `python/tsrl/policies/aux_heads.py` — `TransitionDiffHead`, `OpponentBeliefHead`.
- `scripts/train_novel_arch.py` — orchestrates the 14-cell ablation matrix, with a `--ablation-cell` int arg mapping to the table in §B.6.
- `scripts/bench_novel_arch_ablations.py` — runs the §B.7 benchmark + Elo insertion for each completed cell.
- `results/novel_arch_v1/` — training artefact directory, one subdir per cell.
- `tests/python/test_novel_encoder.py` — unit tests: output shapes match contract, attention mask shapes are correct for "regional_local", GNN message-passing zero rounds is identity, CLS-off works.
- `tests/python/test_aux_heads.py` — shape tests + a "learns identity transition on synthetic data" smoke test.

Files to modify:
- `python/tsrl/policies/model.py` — add `TSNovelModel` class composing the new encoders + heads + aux heads.
- `python/tsrl/constants.py` — register `"novel_gnn_attn_cls": TSNovelModel`.
- `scripts/train_baseline.py` — extend loss-composition block to route `L_state_diff` and `L_belief` when the model exposes aux outputs (guard with `outputs.get("state_diff_pred") is not None`).
- `scripts/train_ppo.py` — no change required for the encoder swap itself; only needed if we want to add aux losses to PPO too (out of scope for v1).
- `cpp/tools/export_baseline_to_torchscript.py` — add `"novel_gnn_attn_cls"` and ensure aux heads are either elided (eval-only inference) or exported.

### C.2 Task ordering DAG

```
                     ┌──────────────────────────────────────────────────────┐
                     │  [EXT] Sub-frame collector lands (.claude/plan/       │
                     │        subframe-row-emission.md, 3 commits)           │
                     └───────────────┬───────────────────────────────────────┘
                                     │
                                     ▼
                     ┌──────────────────────────────────────────────────────┐
                     │  A0. JSONL → Parquet schema extension + row_kind     │
                     │      column.                                         │
                     └───────────────┬──────────────────────────────────────┘
                                     │
                                     ▼
     ┌─────────────────────────────────────────────────┐
     │  A1. TS_SubframeDataset (Python, unit tests).   │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  A2. TSCountryAttnSubframeModel + per-head      │
     │      target routing in train_baseline.py.       │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  A3. BC train 30 epochs, export TorchScript.    │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  A4. GATE benchmark: single-seed 500×2 heur.    │
     │      combined ≥ 0.5 ?                           │
     └─────────┬───────────────────┬───────────────────┘
               │ pass               │ fail
               ▼                    │
     ┌─────────────────────┐        │
     │  B0. Wire aux data: │        ▼
     │    s' columns,      │  ┌─────────────────────┐
     │    opp_hand_truth.  │  │  Iterate A per §A.6 │
     └─────────┬───────────┘  └─────────────────────┘
               │
               ▼
     ┌─────────────────────────────────────────────────┐
     │  B1. novel_encoder.py + aux_heads.py + tests.   │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  B2. Run ablation cells 0–5 (encoder sweep),    │
     │      3 seeds each.                              │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  B3. Ablation cells 6–8 (aux sweep, fixed base).│
     │      If encoder sweep null, go straight to B4.  │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  B4. Cells 9–12: best encoder × 4 aux configs.  │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  B5. Online bench + Elo insertion for winner.   │
     │      Promotion gate: adv_card ≥ BC + 0.005 AND   │
     │      combined WR ≥ BC − 0.02.                   │
     └───────────────┬─────────────────────────────────┘
                     │
                     ▼
     ┌─────────────────────────────────────────────────┐
     │  B6. PPO warm-start from novel BC winner.       │
     └─────────────────────────────────────────────────┘
```

### C.3 Go/no-go criteria (explicit gates)

| Gate | Pass condition | Fail action |
|---|---|---|
| A0 → A1 | Sub-frame collector emits correct JSONL on a short game (spec acceptance tests green) | Block until sub-frame commits land |
| A1 → A2 | `test_bc_subframe_dataset.py` green; dataset loads ≥ 100K rows without schema errors | Fix schema map |
| A2 → A3 | Forward pass returns all expected keys; per-head loss terms are all non-NaN after 1 epoch | Fix forward path |
| A3 → A4 | Val loss decreasing for ≥ 20/30 epochs; no NaN; checkpoint exports to TorchScript cleanly | Retrain with lower lr or smaller loss weights |
| A4 → B0 | **combined ≥ 0.5** on single-seed 500×2 heuristic benchmark | Iterate per §A.6; do NOT start Part B |
| B0 → B1 | `opp_hand_truth` and s' columns present in ≥ 95% of rows; remainder properly masked | Fix collector / ETL |
| B1 → B2 | Novel encoder unit tests green; forward pass shape-checks pass | Fix shapes / masks |
| B2 → B3 | At least one encoder config matches the BC baseline combined WR within ±0.02 | If all regress, stop and revisit encoder design |
| B3 → B4 | Aux sweep shows either aux-1 or aux-2 gives adv_card ≥ baseline + 0.002 with 3-seed agreement | Skip aux heads, just keep encoder wins |
| B4 → B5 | Final combo candidate combined WR ≥ BC baseline − 0.02 | Reject candidate |
| B5 → B6 | Novel BC winner promoted to PPO warm-start only if it clears adv_card ≥ BC + 0.005 AND online WR not regressed | Archive as "neutral" and continue v32 PPO chain |

## Conclusions

1. **Part A is primarily an I/O + routing exercise**, not an architecture exercise. The v32 encoder stays; the dataset, per-head target routing table, loss composition, and inference state machine are the deliverables. The new `country_pick_head` is the only architectural addition in Part A.

2. **The "autoregressive for realigns, one-shot for influence" rule creates a deliberate training/inference asymmetry.** Training sees one sub-frame row per influence op; inference collapses them into one DP-decoded allocation. Document this in code comments at every touchpoint so future contributors do not "fix" the asymmetry.

3. **The country pick head is a new dedicated CE head**, not a reuse of the strategy mixture. The existing `country_logits` outputs mixture probabilities designed for ops-count allocation and cannot be used as raw logits for single-country cross-entropy without breaking the AR influence loss.

4. **The gate is 0.5 combined, not 0.55**, and uses a single seed per side, not the 5-seed multi-grid. The existing `bench_bc_v32_fixed_multiseed.py` uses different constants — do not copy its thresholds or seed list into the gate protocol.

5. **Part B's novel value is the aux heads, not the encoder.** Prior arch sweeps (`results/analysis/opus_analysis_20260417_arch_sweep_update.md`) showed a 0.003 adv_card spread across fundamentally different encoders. Structure the ablation matrix so that a null encoder result still leaves `L_state_diff` and `L_belief` as a distinct, defensible contribution.

6. **Ablation matrix collapsed 48 → 14** via one-factor-at-a-time plus a best-encoder × aux cross. If the encoder sweep is null (likely), skip directly to cells 6–8 as the primary experiment.

7. **Aux heads consume free data**: `s'` comes from the next row of the same game; `opp_hand_truth` already exists in `StepTrace.opp_hand_snapshot`. The only collection change is to surface `opp_hand_truth` into the Parquet schema (and never feed it back into inference).

8. **Promotion to PPO is gated on BOTH adv_card improvement AND online WR non-regression.** Single-metric promotion has previously led to collapse (`memory/project_policy_collapse.md`); keep both gates.

## Recommendations

1. **Block Part B until the sub-frame collector lands.** The spec in `.claude/plan/subframe-row-emission.md` is the authoritative source; do not design against speculative fields.

2. **Do Part A in exactly two PRs:** (a) dataset + model class + train script (no new benchmarks, internal smoke test only), (b) gate benchmark + acceptance. Small PRs reduce the blast radius if the per-head routing has a bug.

3. **Warm-start BC from v32 best, with `--reset-optimizer`.** The new `country_pick_head` has no correspondent in v32; the old optimizer state is not compatible. Per `memory/feedback_bc_before_ppo.md`, BC before PPO is standard for architecture changes.

4. **Run Part B encoder ablations (cells 0–5) in parallel with GPU time permitting; run the aux-head ablations (cells 6–8) with a fixed encoder=baseline.** This is cheaper than a factorial design and answers the aux question independently.

5. **Log all four loss terms (`L_policy`, `L_value`, `L_state_diff`, `L_belief`) to W&B from the first run** so weight balancing is visible and easy to tune without rerunning. Use the `train/` and `val/` prefix convention already in `scripts/train_ppo.py:3853`.

6. **Before any Part B training, add a `opp_hand_truth` column to the collector schema and Parquet converter.** This is a 1-commit change and is a hard dependency on `L_belief`. Without it, cells 7, 8, 11, 12 cannot run.

7. **If Part A fails the gate**, the first iteration to try is *weighting the sub-frame loss down*, not *up*. The dominant failure mode is the sub-frame country-pick loss dominating training and degrading AR influence policy. Try `w_head[country_pick] = 0.3` before any hparam sweep.

8. **Do not reuse the existing `TS_SelfPlayDataset` directly for sub-frame rows without the `row_kind` filter on the training path.** A bug where AR-only code reads sub-frame rows (or vice versa) will silently break loss dispatch. Put a `_raise_on_row_kind_mismatch` assertion in `TSCountryAttnSubframeModel.forward` for the first few training steps and remove once validated.

## Open Questions

1. **Should influence-placement sub-frame rows be trained at all, given inference bypasses `country_pick_head` for that frame kind?** Yes by default (the head is still needed for CountryPick, NoradInfluence, etc.), and the free-ops rows are useful for generalisation — but if per-head balancing proves unstable, dropping free-ops rows from `country_pick_head` training and training only on the non-free-ops country picks is a valid fallback. Decide empirically.

2. **Does the belief head need the public-history as input?** The spec says "P(opp_card_i ∈ opp_hand | public_state, public_history)". The current model sees the current public state only (via cards and scalars); there is no sequence history. For v1 we rely on `actor_known_not_in`, `actor_possible`, `discard_mask`, `removed_mask`, which together encode the full public history as a flattened state. If this is insufficient, consider adding a small GRU over recent ARs in a future revision — out of scope for v1.

3. **Should `L_state_diff` use MSE or categorical (discretized) loss for DEFCON?** DEFCON deltas are integer-valued in {−1, 0, +1, +2}. MSE works but is noisy; one-hot CE on 4 classes would be cleaner. v1 uses MSE for simplicity; revisit if DEFCON delta prediction error stays > 0.5 after epoch 10.

4. **How do we TorchScript-export aux heads?** The policy-callback inference path does not need the aux heads (they are training-only). We either (a) export them but zero their weights in the scripted artefact, or (b) gate them behind a `self.training` check. Option (b) is cleaner but requires testing TorchScript compatibility with conditional branching. Default: option (b), verify on first export.

5. **Is the CLS token order-invariant over the 86 countries?** In principle yes (attention is permutation-equivariant). In practice, the positional information lives in the static features (`region_onehot`, `is_bg`, starting influence) and the adjacency buffer. We should verify via a permutation-invariance smoke test: shuffle country indices in a validation batch and check outputs match within numerical tolerance.

6. **Single dataset vs two datasets for AR and sub-frame?** v1 uses one dataset with a `row_kind` column. If collate-time shape polymorphism (the sub-frame masks are only meaningful on sub-frame rows) causes issues, split into two datasets and use a sampler that draws AR and sub-frame rows in the correct ratio. Decide after first training pass.
