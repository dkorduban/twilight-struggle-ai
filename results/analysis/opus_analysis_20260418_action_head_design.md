# Opus Analysis: Middle-Ground Action Head Approaches for Twilight Struggle
Date: 2026-04-18 UTC
Question: Between fully factored heads and full autoregressive decoding, what are practical middle-ground approaches that capture joint card+mode coupling?

## Executive Summary

The cheapest joint-coupling upgrades are **per-card bias on the mode head** and **card-conditioned country scores**, both achieved by one extra forward pass over trunk hidden state and static card features — not by re-running the trunk. Two middle-ground architectures dominate the cost/benefit frontier: (1) a **"branch factorization" with card-aware mode and mode-aware country heads** (one trunk pass, a cheap O(hand-size × mode-count) decoder, full joint card×mode×country distribution expressible) and (2) **cached-trunk mini-autoregressive decoding** (one trunk pass, 2–4 tiny decoder layers over candidate cards, ~2–4× slower per decision than factored but far cheaper than N forward passes). Opponent-event mitigation is structurally identical to "respond-to-card" selection: the opponent card ID is observable, so it becomes a context token injected into the trunk or a conditioning vector for the mode/country heads — no new architecture is needed, only a "source_card_id" frame feature. The practical recommendation is the branch factorization as v1, with a small AR fallback for rare multi-step events; the user's existing CountryAllocHead marginal head and card-country cross-attention encoder already pay 80% of the infrastructure cost.

## Findings

### 1. The coupling problem, precisely stated

Fully factored heads emit `P(card) · P(mode|s) · P(country|s)` from a single hidden vector. This factorization forces the country distribution to be **the same** regardless of which `(card, mode)` the policy picks. In TS, the best target country depends tightly on the (card, mode) pair:

- **Decolonization** (2 ops event): best targets are Africa/SE-Asia battlegrounds.
- **Decolonization** (2 ops influence): probably Europe/Asia, different mask.
- **Junta** (2 ops event): follows with a free coup; target is an enemy-dominant CA/SA country.
- **Junta** (2 ops influence): totally different target set.
- **China Card** (event mode not legal; mode always ops): best scope is Asia, but *only if* China is in your hand and face-up.
- **Missile Envy response** (opponent forces you to give a card): best card to give is a *low-ops* card you don't need, not the strongest.

The factored model compensates by learning a country distribution that is a **marginalized average** over all plausible (card, mode) combinations weighted by the current distribution. This averaging is why factored heads often plateau — the country logits are a compromise, never optimal for a specific (card, mode) branch.

### 2. The cost/expressiveness frontier

Let T = trunk-pass cost, H = head cost. Head costs are O(10–100K FLOPs), trunk is O(1–10M FLOPs). Trunk dominates.

| Approach | Trunk passes per decision | Country head calls | Expresses P(country \| card, mode)? |
|---|---|---|---|
| **Fully factored** (current) | 1 | 1 | No — marginalized |
| **Card-conditioned country head** | 1 | 1 | Yes, factored per card |
| **Branch factorization** (card+mode → country) | 1 | Hand×Mode (light) | Yes, full joint |
| **Cached-trunk mini-AR** | 1 | Hand (seq decoder) | Yes, true autoregressive |
| **Full AR (trunk re-run per card)** | Hand-size × Mode-count | same | Yes |
| **Scorer network** (state,action → score) | 1 + Actions×scorer | per legal action | Yes |

Trunk re-running is the only truly expensive option. Everything between factored and cached-trunk AR is **almost free** in FLOPs — the question is parameter efficiency and trainability.

### 3. Middle-ground approach A: card-conditioned country head

Predict `score[c | card_id]` by combining trunk hidden with a per-card embedding:

```
country_logits[card, c] = MLP(trunk_hidden ⊕ card_embedding[card] ⊕ country_features[c])
```

The existing **CardCountryCrossAttn** in `TSControlFeatGNNCardAttnModel` (model.py:1988-2116) is 60% of this design. Currently cross-attention output is pooled over the hand to produce one card-conditioned feature that feeds the trunk. To get per-card country logits, skip the pooling: keep the (B, hand_size, country_dim) cross-attention output and emit country logits per card.

**Cost**: one extra cross-attn pass, ~30K params, ~100K FLOPs at 4 heads × 32 dim.

**Limitation**: does not factor mode. A mode-independent "best target given card" is a decent compromise for events (modes are often forced) but weaker for ops/event disambiguation on the same card.

### 4. Middle-ground approach B: branch factorization (recommended v1)

Treat `(card, mode)` as a joint branch index, then emit country logits per branch. This is equivalent to the user's original "K=4 strategy mixture" but with branches meaningful (card+mode) instead of arbitrary (k=0..3).

**Architecture**:
1. Trunk → `h` (single pass, same as today).
2. For each legal card × mode pair, compute a branch vector:
   `b[card, mode] = h ⊕ card_emb[card] ⊕ mode_emb[mode] ⊕ card_x_mode_interaction`
3. Emit country logits per branch:
   `country_logits[card, mode, c] = CountryAllocHead(b[card, mode])_c`
4. Joint action probability:
   `P(card, mode, targets | s) = softmax_branch(branch_logit[card, mode]) · softmax_country(country_logits[card, mode])`
5. Train: use marginal card/mode heads for regularization, but the *action* loss uses the joint distribution. Factored heads still exist for backward compat.

**Cost analysis** (assume hand=9, modes=6, countries=86, hidden=256):
- Branch vectors: 9×6 = 54 branches. If each uses a shared MLP `Linear(h+card+mode → country_alloc)`, total FLOPs = 54 × (256+8+6) × 86 = ~1.2M. That's **comparable to the trunk pass itself**, but it's fully parallel on GPU (batched matmul). On CPU (C++ inference), the current `strategy_heads = Linear(hidden, 4×86)` already does 4 × 86 = 344 outputs; 54 × 86 = 4644 outputs is ~13× more, still <10ms per decision.
- In MCTS, branch score factorization lets you avoid enumerating all 54 × 86 = 4644 flat actions — the search computes branch priors (54 numbers) and conditional target priors lazily.

**Why this is the best compromise**:
- Captures full joint card × mode × country without N trunk passes.
- Reuses the existing CountryAllocHead (DP-decoded marginal head from Phase 2).
- The existing card-country cross-attention naturally produces per-card country features; mode conditioning is just adding `mode_emb` to the query.
- Training signal is still a single chosen action per step — no autoregressive canonicalization headache.
- Multimodality handled: two different (card, mode) branches can both have high branch-prior mass while their country distributions differ arbitrarily.

This is what the **"pragmatic head"** long-prompt recommends: card×use×scope×typed-args, executed with typed engine decision nodes. Branch factorization is the learning-side implementation of that grammar.

### 5. Middle-ground approach C: cached-trunk mini-AR

One heavy trunk pass, then a tiny 2–4 layer transformer decoder that autoregressively emits card → mode → country(s). This is the "good AR" from `head-architecture.md`.

**Cost**: one trunk pass + ~50K FLOPs per decoder step × 3–5 steps = <5× factored.
**Expressiveness**: strictly greater than branch factorization — captures country-dependent country choice (place-influence stacking, path-dependent placements like De-Stalinization).
**Downsides**:
- Sequential latency even on GPU.
- Canonical ordering for multisets needed in training.
- Training target sparsity: only one sampled trajectory per state, so rare conditional modes are undertrained.

This is the right approach for **Phase 3 or later**, not v1. The branch factorization captures most of the coupling with far less infrastructure change.

### 6. Middle-ground approach D: proposal + scorer (AlphaStar-style)

Generate a shortlist of K candidate full actions via a cheap factored proposer, then re-score each with a small scorer that sees the full `(state, action)` pair. This is what **AlphaStar** does for StarCraft and what **MuZero variants** do when the action space is too large to enumerate.

**Cost**: 1 trunk pass + K scorer calls. K ≈ 20–40 for TS. Scorer is a small MLP.
**Expressiveness**: matches AR in the limit.
**Downsides**:
- Needs a proposer that already has some coverage — cold-start is awkward.
- Search integration is non-trivial: MCTS priors want all-action coverage, not top-K.

For TS specifically, this is **overkill for v1 but ideal for later strength push**.

### 7. What AlphaStar / MuZero / OpenAI Five do

- **OpenAI Five** (Dota 2): multiple semantic action heads with **shared trunk** and explicit cross-attention between picked unit/target. Equivalent to branch factorization: pick "action type" first, then per-type parameter heads are conditioned on that choice via a residual/FiLM embedding. **Key insight**: they do *not* autoregressively re-run the trunk; they condition down-stream heads on earlier-head outputs via concatenation or FiLM.
- **AlphaStar** (StarCraft II): pointer-network-style autoregressive decoder with action-type, delay, queued, selected_units, target_unit, target_point. Uses residual LSTM state between heads — this is "cached-trunk mini-AR". The trunk is massive (transformer over entities) and runs once.
- **MuZero** (Go, chess, Atari): **no coupling problem** because action space is already small (361 Go moves, ~4700 chess moves). Uses flat action embedding.
- **Stratego (DeepNash)**: factored action heads + value/policy mixing. Huge action space. Uses sampling-based MCTS with flat action vocabulary — similar to what we'd do with branch factorization.
- **Hanabi / imperfect-info games**: small action space (~20), no coupling issue.

**The consistent pattern**: large composite action spaces → shared trunk + either (a) per-head conditioning on earlier head outputs (branch factorization / FiLM) or (b) cached-trunk mini-AR decoder. No one re-runs the trunk per sub-action.

### 8. Where coupling matters most (evidence from TS structure)

Not all decisions need strong coupling. The coupling problem is most severe for:

1. **Mode ambiguity on opponent cards**: "play Truman Doctrine for event (remove 1 opp inf from any non-BG) vs play for 1 ops influence" — country targets are disjoint.
2. **Ops scope variants**: China Card (Asia-only), Vietnam Revolts (SE-Asia bonus). Current model can't express "if scope=asia, countries here; if scope=normal, countries there".
3. **Coup vs realign vs influence for the same card**: completely different country masks and scoring.
4. **Free-coup events**: Junta, Ortega — after the card resolves, engine needs a follow-up country target that depends on the original card's scope.
5. **Warmup modes**: Space race is card-agnostic (highest-ops is best), so coupling matters least.

Coupling matters *least* for:

- **Card choice itself** (headline, ops card): mostly a function of board state, weakly dependent on mode (you'll figure out mode after picking card).
- **Value head**: coupling doesn't apply (one scalar).
- **SmallChoice events**: the card-id context is already in the frame, and small discrete choices are already card-conditioned via `source_card_id`.

### 9. Opponent event mitigation (the sub-question)

The user asked specifically about **card-specific response to opponent events**. Two cases:

**Case A: Mitigation happens before ops phase (event-before-ops for opponent card, or forced by card text like Missile Envy)**. The player must pick responses that depend entirely on which card the opponent played. Examples:
- Missile Envy → give up your lowest-value card.
- Blockade → discard a 3+ ops card or lose Western Europe stability.
- UN Intervention → pick the paired card.
- Grain Sales / Ask Not → card selection from hand or discard.
- Aldrich Ames → pick a card from opponent's hand.

These are all `CardHead` decisions per the pragmatic-head document. The **source_card_id** must be in the decision frame (concatenated to trunk hidden before the card head).

**Case B: Response to opponent's main-AR card play (decide event-first vs ops-first for an opp card)**. Already implemented as `ActionMode::EventFirst=5`. The SmallChoiceHead can learn this with source_card_id context — no new head needed.

**Key insight**: opponent-event response is a **CardHead-level** decision, not a country-level one. The current model already has card-head context; it just needs the `source_card_id` frame feature exposed during training (from the typed decision-node framework Phase 3 is building).

### 10. Concrete recommendation stack

For v1 (quick win on the factored-head plateau):

1. **Add card-conditioned mode head**: `mode_logits[card] = Linear([h, card_emb[card]])`. Cost: one extra Linear, 9×6 = 54 numbers per decision.
2. **Add card×mode-conditioned country head**: reuse marginal head but compute with branch embedding concatenated to trunk hidden.
3. **Keep factored heads** (`card_logits`, `mode_logits`, `country_logits`) for backward compatibility and auxiliary losses.
4. **Training**: cross-entropy on the joint `(card, mode, country)` using branch softmax; auxiliary marginal losses at 0.3× weight.
5. **MCTS integration**: prior is joint factorization; legal-action expansion uses branch × conditional-country product.

For v2 (if v1 plateaus):

6. Cached-trunk mini-AR for event-resolution multi-country decisions (De-Stalinization, Marshall Plan placement).
7. Proposal + scorer for MCTS root when legal action count exceeds 200.

### 11. What NOT to do

- **Do NOT run trunk once per (card, mode) pair**: even 54 forward passes per decision is 50× slowdown.
- **Do NOT use a flat (card × mode × country) one-hot head**: 54 × 86 = 4644 classes is both sparse and parameter-wasteful. The existing `strategy_heads = Linear(h, 4×86)` pattern scales to `Linear(h, 54×86)` but needlessly couples parameters across unrelated branches.
- **Do NOT add full autoregressive decoding before branch factorization**: AR inherits all the canonicalization and multimodal target issues; get the cheap branch win first.
- **Do NOT conflate "K=4 strategy mixture" with branch factorization**: the current K=4 mixture has no semantics — each strategy is an arbitrary latent. Branch factorization makes branches correspond to real `(card, mode)` pairs the engine understands.

## Conclusions

1. The full autoregressive approach (N trunk passes) is unnecessary and empirically unused in comparable systems (AlphaStar, OpenAI Five, DeepNash); the standard pattern is **one trunk pass + conditioned downstream heads**.
2. **Branch factorization** is the right v1 upgrade: predict `(card, mode)` branch priors jointly and emit per-branch country logits from a shared trunk. Expresses full `P(card, mode, country | state)` at ~2× inference cost, with ~50K extra params.
3. The existing `TSControlFeatGNNCardAttnModel` cross-attention encoder already provides per-card country features — switching from pooled output to per-card output is ~20 lines of model code, not a rewrite.
4. The existing `TSMarginalValueModel` CountryAllocHead (`score[c, t]` with DP decoding) is the right country-emission mechanism for each branch — no replacement needed, just per-branch conditioning.
5. Mode-independent "card-conditioned country" is a weaker intermediate that doesn't handle event-vs-ops mode ambiguity; branch factorization is only marginally more expensive and handles it cleanly.
6. Cached-trunk mini-autoregressive decoding is the right approach *later* (v2+) for multi-step event resolutions (De-Stalinization place-after-remove, Marshall Plan multi-country placement) where path-dependence and permutation symmetry bite.
7. Opponent-event mitigation is not a new head problem — it is a **decision-frame context problem**: expose `source_card_id` as a frame feature (already planned in Phase 3 of `plan_pragmatic_heads.md`) and the existing CardHead/SmallChoiceHead/CountryAllocHead handle the response decision natively.
8. Multimodality ("two opposite allocations both good") is orthogonal to coupling: it needs soft targets (teacher visit distributions, AWR-style weighting) regardless of whether heads are factored, branch-factored, or AR.
9. China Card / Vietnam Revolts scope is an argument for making **scope a masked SmallChoice inside the Ops branch**, not for a separate architecture — branch factorization can absorb scope as `(card, mode, scope)` with minimal extra branches.

## Recommendations

1. **Immediate (this week)**: Prototype a branch-factored country head on top of `TSControlFeatGNNCardAttnModel`. Produce per-(card, mode) country logits of shape `(B, hand_size, num_modes, 86)`. Train via joint cross-entropy on logged `(card, mode, country)` tuples from self-play. Gate behind a new model key `branch_factored_country` in MODEL_REGISTRY; keep existing factored heads for backward compat.
2. **Short-term (2–3 weeks)**: Add `source_card_id` to the decision frame for all SmallChoiceHead / CountryAllocHead / CardHead call sites. Condition each head on `source_card_id` via an embedding concat, then retrain. This fixes opponent-event mitigation and card-specific event resolution simultaneously.
3. **Medium-term (4–6 weeks)**: Once branch factorization is trained, integrate into MCTS: branch priors at root, lazy per-branch country priors during simulation. Measure Elo delta vs current factored baseline.
4. **Longer-term (if needed)**: Cached-trunk mini-AR decoder for multi-step event resolution nodes only (De-Stalinization, Marshall Plan multi-placement, Ask Not). Use a 2-layer transformer decoder with shared K/V over country embeddings.
5. **Evaluation protocol**: Use the AWR-lite proxy from `off-policy-architecture-ranking.md` to rank branch-factored vs current factored on frozen teacher data *before* committing to full PPO. This avoids wasted rollouts on a bad coupling design. Expected signal: held-out joint NLL and top-1 agreement on `(card, mode, country)` tuples.
6. **Benchmark target**: The pragmatic-heads plan targets +20 Elo per phase. Branch factorization should be evaluated against that bar; anything <10 Elo improvement means the coupling gap was smaller than assumed and effort is better spent on ISMCTS or distillation.

## Open Questions

1. Does the current factored head's *country* distribution actually contain a recoverable "card, mode" signal under the hood (i.e., is the problem truly marginalization, or is the trunk already attention-weighting by the *likely* card)? A diagnostic: fix a state with a known bimodal best action (card A event vs card B influence, different targets) and inspect the factored country head's distribution vs teacher visit counts.
2. Is the existing `TSControlFeatGNNCardAttnModel` already learning card-conditional features in the pooled cross-attention output, or is the pooling destroying that signal? Ablation: replace `cross_attn_proj(attn_pool)` with per-card argmax selection by `card_logits` top-1.
3. For opponent-event mitigation, are there cases where the response depends on **opponent's likely hand**, not just the played card? If so, the belief-state features matter as much as source_card_id.
4. How does branch factorization interact with temperature-based action sampling at the root? Sampling over 54 branches then conditional country sampling may need explicit temperature per level.
5. Should EventFirst mode get its own branch dimension, or be treated as just another mode value (6 → 7 modes)? Design note in plan_pragmatic_heads.md suggests mode-level treatment is correct.
6. What is the minimum dataset size for reliable joint `(card, mode, country)` NLL training? Sparse (card × mode) pairs (e.g., a low-frequency card played in an unusual mode) may suffer; teacher distillation with soft targets mitigates this.
