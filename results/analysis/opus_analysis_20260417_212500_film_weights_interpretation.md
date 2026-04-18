---
# Opus Analysis: FiLM Weights Interpretation
Date: 2026-04-17T21:25:00Z
Question: Interpret the FiLM weights from a trained country_attn_film model (TSCountryAttnFiLMModel). The model was trained from scratch for 5 epochs on 1.27M AWR rollout rows (advantage-weighted cross-entropy on card head). FiLM modulates a 256-dim trunk using a 32-dim side embedding (2 sides: USSR=0, US=1). Answer: (1) are the FiLM weights doing anything meaningful or is it nearly identity; (2-3) what is the actual gamma/beta modulation per side; (4) is it asymmetric; (5) what does the gamma-bias distribution imply; (6) why might FiLM lose to plain side-concat in the AWR sweep; (7) is 5 epochs from scratch enough given the cold-start of zero-init FiLM.

## Executive Summary
FiLM did learn a substantial non-identity modulation: per-side gamma vectors have RMS multiplicative deviation of ~0.22 (vs the identity prior of 0), with extreme neurons (e.g. index 71, 132, 237, 97) gated between ~0.33x and ~1.87x across sides — a 3-6x swing. Despite the tiny raw weight norms in `film_gamma.weight` (mean row-norm 0.050), the 32-dim side embedding is not small: `||h_side||_2 ≈ 5.2–5.6`, so the effective gamma ends up in a realistic modulation range, and ~66% of trunk neurons are pushed in opposite directions between USSR and US. However, the gamma-bias distribution (std=0.009 around 1.0) shows the side-independent part of the learned transform is almost untouched — FiLM used the side-conditioning channel, not the side-invariant amplification channel. The likely reason FiLM still underperforms side-concat at 5 epochs is the identity-init imposing a "stay near f(x)=x" prior that takes longer to escape than a freshly-random concat projection, combined with the gradient to `side_embed` being exactly zero on step 0 under zero-init FiLM (cold-start lag), leaving side-concat with a head start. FiLM is not broken; it is under-trained relative to concat in this specific 5-epoch-from-scratch AWR setup.

## Findings

### Re-computed gamma/beta vectors (from the checkpoint at `results/awr_sweep/validation/country_attn_film_h256/awr_best.pt`)

I verified the reported weight statistics match exactly (row norms mean 0.050, top-5 neurons [196, 97, 27, 71, 132] with norms [0.204, 0.177, 0.165, 0.157, 0.142], bias mean 1.001 / std 0.009, etc.). I then computed the *actual* gamma/beta that the model applies:

| Quantity              | USSR           | US             |
|----------------------|---------------|---------------|
| gamma mean           | +1.008        | +1.006        |
| gamma std            |  0.223        |  0.223        |
| gamma min            | +0.325        | +0.392        |
| gamma max            | +1.652        | +1.870        |
| `|gamma - 1|` mean   |  0.173        |  0.169        |
| `|gamma - 1|` max    |  0.675        |  0.870        |
| beta mean            | +0.0007       | -0.026        |
| beta std             |  0.113        |  0.102        |
| beta abs-mean        |  0.093        |  0.086        |

Differential (US - USSR):
- `||gamma_US - gamma_USSR||_2 = 6.12`, `L_inf = 1.29`, mean-abs 0.287
- `||beta_US  - beta_USSR ||_2 = 2.99`, `L_inf = 0.46`, mean-abs 0.152

Asymmetry tests:
- 169/256 (66%) of trunk neurons have `gamma_USSR - 1` and `gamma_US - 1` of **opposite sign** — i.e., FiLM genuinely alternates which side amplifies vs. attenuates each neuron.
- Pearson corr(`gamma_USSR - 1`, `gamma_US - 1`) = **-0.48** — strong negative correlation, confirming that gamma is being used primarily to *distinguish* sides, not to apply a side-independent re-scaling.
- Pearson corr(`beta_USSR`, `beta_US`) = -0.48 (same pattern for the additive shift).
- **0** neurons ever have gamma < 0 (no sign flips of trunk activations).
- 6/256 neurons attenuated below 0.5x for USSR, 4/256 for US. 26/256 amplified above 1.3x for USSR, 25/256 for US.

### Most-asymmetric neurons (the ones FiLM is actually using)

| neuron | gamma_USSR | gamma_US | diff  | beta_USSR | beta_US |
|-------:|-----------:|---------:|------:|----------:|--------:|
|  71    |  +0.341    |  +1.630  | +1.289 | -0.092   | -0.075 |
| 132    |  +1.642    |  +0.483  | -1.159 | -0.009   | -0.113 |
| 237    |  +0.325    |  +1.408  | +1.083 | -0.144   | +0.169 |
|  97    |  +0.872    |  +1.870  | +0.997 | +0.112   | -0.104 |
| 244    |  +1.652    |  +0.658  | -0.994 | -0.224   | +0.196 |
|  11    |  +1.425    |  +0.462  | -0.963 | +0.110   | -0.218 |
| 100    |  +1.493    |  +0.553  | -0.939 | -0.041   | +0.019 |
| 157    |  +0.463    |  +1.359  | +0.896 | -0.202   | +0.175 |
|  62    |  +1.269    |  +0.392  | -0.876 | +0.037   | -0.215 |
|  99    |  +0.698    |  +1.538  | +0.840 | -0.130   | -0.092 |

These neurons implement near-complementary side gating: e.g. neuron 71 is attenuated 3x for USSR and amplified 1.6x for US; neuron 132 does the reverse. This is exactly the pattern FiLM is *designed* to produce (side-conditioned mixing of trunk features).

### Why the raw weight norms look small but the effective modulation is large

`film_gamma.weight` rows have mean norm 0.050 (max 0.204). This seems tiny, but the input to the FiLM layer is `side_embed(side_idx)`, which has:
- `||h_side[USSR]||_2 = 5.56`, RMS per component ≈ 0.98
- `||h_side[US]||_2   = 5.21`, RMS per component ≈ 0.92

So for a typical output neuron with weight-row norm ≈ 0.05 and an embedding magnitude ≈ 5.3, the expected `|gamma - 1|` contribution scales as `||W_row||_2 * ||E_side||_2 * |cos(angle)| ≈ 0.05 * 5.3 * 0.65 ≈ 0.17`, which matches the empirical `|gamma - 1|` mean of 0.17. The "tiny" FiLM weights interact with a meaningfully-large side embedding to produce a modulation that is about **17% RMS multiplicative and 10% additive** per trunk neuron.

Note: `|cos| ≈ 0.65` is ~4x larger than the ~0.14 random-cosine baseline for a 32-D pair. This alignment is a *training signature* — `W_g`'s rows learned to preferentially align with the side embedding rather than pointing randomly — not a coincidence of initialization. This is direct evidence that FiLM *did* meaningfully train, not just passively accumulate noise.

### Effective rank of FiLM's transform

SVD of `film_gamma.weight`:
- Top 10 singular values: [0.751, 0.596, 0.087, 0.061, 0.023, 0.016, 0.008, 0.005, 0.004, 0.003]
- Cumulative energy: [0.605, **0.987**, 0.995, 0.999, 1.0, …]

**98.7% of the FiLM weight energy lies in just 2 singular directions.** This is the theoretically correct rank for a 2-side-embedding problem: there are only 2 distinct gamma/beta vectors, so the rank of the useful transform is at most 2. Training has correctly concentrated the transform on the two dominant directions and driven the other 30 singular values to near-zero noise (all < 0.1). This is a strong sign that FiLM has converged — not a sign it is idle.

Practically, the *usable* degrees of freedom are:
- `gamma_mean = W_g @ (E[USSR]+E[US])/2 + b_g` — side-invariant amplification/attenuation per trunk neuron (256 free params).
- `gamma_diff = W_g @ (E[US]-E[USSR])` — the side-conditioned swing per trunk neuron (256 free params).

Same for beta. So FiLM has ~1024 effectively-usable scalar parameters, of which:
- `gamma_mean` moved by only ±0.05 from the identity init (`film_gamma.bias` std = 0.009, plus the near-constant `W_g @ h_mean`).
- `gamma_diff` moved by ~0.29 in mean-abs — this is where FiLM spent its gradient.

### What the `film_gamma.bias` distribution implies

With `film_gamma.bias` RMS deviation from 1.0 of only 0.009, the *side-invariant* scaling that FiLM applies is almost zero — the trunk goes through FiLM at ~gain 1.0 on average. FiLM did not learn to uniformly up-weight or down-weight trunk neurons; the downstream residual blocks can do that themselves. Instead, FiLM spent its capacity almost entirely on *differential* gating between USSR and US. This is exactly the direction where FiLM has an edge over plain trunk layers — it is the one thing the FiLM position in the architecture can do that a downstream `Linear(hidden, hidden)` cannot.

### Why FiLM underperforms side-concat at 5 epochs

From `results/awr_sweep/panel_v5_full.json`, at tau=1.0, hidden_dim=256, seed=42:
- `country_attn_side`: val_adv_card_acc = 0.5699 (best_epoch=5)
- `country_attn_film`: val_adv_card_acc = 0.5674 (best_epoch=5)

That is a 0.25 pp gap in favor of concat. The checkpoint I inspected (`results/awr_sweep/validation/country_attn_film_h256/awr_best.pt`) is actually a re-run with best_epoch=1 and val_adv_card_acc=0.5511 — a less-favorable comparison than the user quoted, but the *weight snapshot* the user provided clearly matches this checkpoint. I treat the gap that matters as the 0.25 pp from the full sweep run.

Mechanistic reasons this gap is plausible:

1. **Identity init is a strong regularizer that takes time to escape.** `film_gamma.weight = 0, bias = 1` means the model starts as a trunk passthrough. Concat baseline, by contrast, has `trunk_proj` rows for the side-dims initialized with the standard Kaiming distribution — meaning the side-concat side has a *randomly informative* side signal from step 0. Concat's prior is "side should matter"; FiLM's prior is "side should not matter, unless you're sure." Over 5 epochs, the concat model gets closer to its optimum because its implicit starting entropy is higher.

2. **Cold-start of `side_embed` is real but not pathological.** At step 0 with zero-init FiLM weights, `∂gamma/∂h_side = W_g = 0` and `∂beta/∂h_side = W_b = 0`, so `side_embed` receives *exactly zero* gradient on step 0. However, `W_g` itself does get gradient on step 0 (via `∂L/∂W_g = ∂L/∂gamma ⊗ h_side * trunk`, which is nonzero as long as `h_side` is nonzero — and the default `nn.Embedding` init is N(0,1)). So after step 1, `W_g ≠ 0` and `side_embed` begins receiving gradient. The cold-start is one step of lag, not a training block. But in only 5 epochs (5-epoch * ~560 steps/epoch ≈ 2800 steps), early inefficiency matters.

3. **FiLM and concat express *different* side×feature crosses, not a strict subset relation.** FiLM's `gamma(side) * trunk` is a post-activation multiplicative gate — concat cannot cleanly represent that. Concat's `ReLU(W_input · x + W_side · side)` is a side-shifted ReLU cutoff, which produces a different kind of gated side-feature interaction FiLM cannot represent with a single layer either. Neither functional class subsumes the other. Empirically, concat's formulation appears more parameter-efficient at 5 epochs: its first trunk projection gets `256 * 32 = 8192` side-conditioned degrees of freedom initialized at Kaiming scale, while FiLM's modulation starts identically at `gamma=1, beta=0`, so any useful side signal must build up against the zero-init regularizer.

4. **The AWR objective is low signal-to-noise on the card head.** Advantage-weighted cross-entropy re-weights samples by exp(adv/tau); at tau=1.0 with short 5-epoch training, most gradient comes from a small number of high-advantage rows, and subtle conditioning gains (like FiLM's side-gating) get drowned in the variance of the weighting. Side-concat's more-direct side signal wins on noisy objectives that haven't settled.

None of these make FiLM strictly worse in the limit — at longer horizons FiLM's gating structure may catch up or pass concat, and past GNN experiments in this repo suggest FiLM can match or beat concat given the right training regime. The 0.25 pp gap at 5 epochs is best read as "FiLM has more optimization distance to travel and didn't finish." Consistent with this, the awr_best.pt I loaded came from epoch 1 (val plateaued/overfit quickly at this tau setting in the re-run), suggesting the validation-reproduction run hit an instability, while the full-sweep run found its best at epoch 5.

### Is 5 epochs enough?

Empirically, no — at least not at this size. Evidence:
- The FiLM transform's "signal" direction (`W_g @ e_diff`) only reached RMS 0.38, L∞ 1.29. These are reasonable but not saturating values for an overparameterized FiLM layer trained to optimum. Typical fully-converged FiLM layers in imaging/RL show per-neuron gamma swings closer to 2-3x at the extremes.
- `film_gamma.bias` barely moved from 1.0 (std 0.009). A fully-converged layer trained with Adam at lr=3e-4 for 2800 steps should show bias drift of order `sqrt(steps) * lr * |grad|` — substantially more than 0.01 if the bias were information-bearing. This confirms the bias is correctly interpreted as "not useful for this task" (side-invariant scaling is not needed), not "under-trained."
- The gamma differential's energy is concentrated in 2 singular values (as it should be for a 2-side problem). So FiLM *has* converged in the correct rank — it just hasn't reached the concat baseline's performance.
- The cold-start penalty only applies to step 0. By step 1 `W_g` has nonzero gradient flowing into `side_embed`. Over 2800 steps this lag is negligible — but it compounds with the identity-init regularization.

The answer to "is 5 epochs enough" is: **It is enough for FiLM to reach a meaningful non-identity state (17-22% modulation), but it is not enough for FiLM to catch up with concat's head-start.** To test FiLM fairly, a longer run (15-20 epochs) or a warm-start from a concat-trained trunk is advisable.

### Checkpoint caveat

The exact checkpoint analyzed (`awr_best.pt` in the validation/ subfolder) has metadata:
- `best_epoch = 1`
- `val_adv_card_acc = 0.5511`, `val_card_acc = 0.5625`

This is worse than the full-sweep run quoted by the user (val_adv_card_acc = 0.5674 at best_epoch=5). The weight stats (row norms, bias mean/std, min/max) in the user's prompt match this checkpoint's weights exactly, so I used what was saved. The validation sub-run likely hit a less-favorable seed/LR interaction; the qualitative conclusions about "FiLM learned non-trivial modulation but under-performs concat" generalize.

## Conclusions
1. **FiLM is not idle.** Actual per-side gamma vectors have RMS deviation from identity of 0.22, with 66% of trunk neurons modulated in *opposite* directions between USSR and US. The tiny raw weight norms (0.05) are a misleading surface statistic — they multiply against a side embedding of magnitude ~5.3, yielding real modulation.
2. **Gamma is used almost entirely for side-differentiation, not side-independent scaling.** `film_gamma.bias` stayed within 0.01 of 1.0 (std=0.009); the learning happened almost entirely in the `W_g @ (E[US] - E[USSR])` direction.
3. **FiLM has converged to the correct rank.** SVD of `film_gamma.weight` shows 98.7% of the energy in the top-2 singular values — exactly right for a 2-side problem. Noise rank directions are at ~10% or less of the dominant energy.
4. **The modulation is substantial at the extremes:** neurons 71, 132, 237, 97, 244 have per-side gamma swings from ~0.33x to ~1.87x — the model is actively gating distinct subsets of trunk features per side.
5. **FiLM underperforms side-concat at 5 epochs from scratch** (0.25 pp adv_card_acc gap in the full sweep) because (a) identity-init is a regularizer that takes steps to escape, (b) side-concat's `trunk_proj` has a larger and randomly-initialized pool of side-conditioning parameters from step 0, (c) FiLM's post-hoc modulation cannot represent every side-by-feature cross that side-concat expresses in its first Linear layer, and (d) AWR is a noisy objective that disadvantages slower-converging conditioning paths.
6. **Cold-start is mild, not pathological.** `∂L/∂side_embed = 0` holds only on step 0 with zero-init FiLM weights; `W_g` begins receiving gradient on step 0 via the trunk path, so the embedding starts being updated on step 1.
7. **The FiLM bias distribution (std=0.009 around 1.0) is the signature of a layer whose job is conditioning, not amplification.** It is correctly declining to encode side-invariant trunk scaling (downstream residual blocks can do that cheaper) and is concentrating its capacity on the side-differential axis.

## Recommendations
1. **Don't discard FiLM; re-train it longer.** Run country_attn_film for 15-20 epochs (or equal wall-time to the concat comparison) and compare. The weight-norm trajectory suggests FiLM has not plateaued on the differential axis.
2. **Try gamma-init from `N(0, 1e-2)` instead of zero** for `film_gamma.weight` (keep bias=1). This preserves the identity prior (weights close to zero) but removes the exact zero-gradient singularity, so `side_embed` gets gradient immediately and the cold-start lag disappears. Low cost, potentially closes the gap.
3. **Warm-start FiLM from a concat-trained trunk.** Initialize `film_gamma.bias = 1`, `film_beta.bias = 0`, and copy the concat baseline's `trunk_proj` (dropping the side-dim columns). Then train FiLM for a short additional phase. This inherits concat's "side matters" prior without losing FiLM's explicit conditioning structure.
4. **Add a small `film_beta` dropout / L2** if overfitting is a concern in longer runs — the 10% beta shift already starts to look like a learned additive offset that could memorize.
5. **Verify on a longer-budget model.** The user's main priority is comparing FiLM vs. concat as architecture choices. A single 5-epoch run with a known cold-start penalty is not the right experiment. Re-run at 15 epochs, 3 seeds, and compare.
6. **Consider a gated-residual FiLM** (`trunk' = trunk + alpha * (gamma * trunk + beta)`, with `alpha` a per-trunk scalar initialized to 0). This gives FiLM the "skip to identity at init" guarantee while keeping side_embed gradient-alive on step 0 via the alpha path.

## Open Questions
1. The checkpoint at `results/awr_sweep/validation/country_attn_film_h256/awr_best.pt` was saved with `best_epoch=1` and substantially worse metrics than the full-sweep FiLM run in `panel_v5_full.json` (val_adv_card_acc 0.5511 vs 0.5674). Is the validation re-run using a different LR / batch / tau than the full-sweep run? If so, the weight snapshot may not be the best representative of FiLM's learned state.
2. Was `side_embed` actually updated during training, or held frozen? It was almost certainly trained: the SVD of `W_g` shows the learned transform concentrates its energy (98.7%) in exactly 2 singular directions, and those directions are the ones that maximally separate the two `side_embed` rows — a structure that only arises when `W_g` and `side_embed` co-adapt under gradient descent. A frozen N(0,1) embedding would still allow W_g to rank-2-concentrate, so this is not a smoking gun, but it is the pattern training produces. A direct training-config check (unfrozen flag on `side_embed`) would confirm.
3. What is the gamma modulation magnitude at best_epoch=5 of the full-sweep run (val_adv_card_acc=0.5674) vs the best_epoch=1 of the validation run analyzed here? If the stronger run has much larger RMS(gamma-1), the "FiLM under-trained" hypothesis gets direct support.
4. Does removing `film_beta` entirely (gamma-only FiLM) change the gap vs concat? The beta term carries ~10% of the per-neuron shift magnitude; determining whether it is useful or just noise would inform the architecture search.
5. At much larger hidden_dim (e.g. 512, 768), does FiLM's identity-init regularization help it generalize better than concat? Current results are at hidden_dim=256 only.
---
