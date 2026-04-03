# Combined conversation (markdown)

## Q1
in Twilight Struggle I have a heuristic that has 2:1 win rate with USSR vs US against itself; I'm trying to teach a model (imitation, with MCTS, or otherwise) play at least the same strength. how can I utilize heuristic rollouts in MCTS? I'm afraid that naive rollout and taking result for granted will just reinsforce the idea that position is advantaged for USSR, while in fact it may be not. hope you understood the concenr

## A1
Yes — the concern is exactly right.

If your rollout / default policy is the same heuristic that already has a built-in USSR skew, then plain MCTS values are not “ground truth.” They are closer to:

- “how well this position does when both sides continue with my biased heuristic”

not

- “the actual value of the position”

So if you use naive rollout returns directly, you can absolutely reinforce a false belief like “USSR is winning here” when the truth is only “USSR does well under this flawed continuation policy.”

What to do instead:

## 1. Do not treat rollout return as truth
Treat heuristic rollout as a noisy, biased evaluator.

In practice this means:
- use it mainly for move ranking / variance reduction
- do not train value head directly on raw rollout outcome without correction
- do not fully trust absolute values, especially across sides

This is the main mindset shift.

---

## 2. Prefer **relative action comparison** over absolute state value
Even if the heuristic is biased, it can still be useful for ranking candidate moves from the same root.

Example:
- from state `s`, compare actions `a1, a2, a3`
- run search / rollouts under the same biased continuation policy
- use results to decide which action looks best **relative to siblings**

Why this is safer:
- much of the side bias is common-mode and cancels when comparing sibling actions
- “USSR is always a bit overestimated” is less harmful than “this move is better than that move”

So for training:
- policy targets from visit counts are usually safer than value targets from rollout winrates
- value targets should be smoothed / corrected / mixed with other targets

If you only trust one thing from heuristic-guided search, trust the **policy improvement signal** first.

---

## 3. Use **leaf evaluation**, not long terminal rollouts, whenever possible
Classic full playouts are especially dangerous here because the bias compounds over many decisions.

Better:
- search to some depth
- stop
- evaluate leaf with a heuristic value function, or shallow continuation bundle

This reduces:
- compounding policy bias
- variance
- compute cost

For Twilight Struggle, long rollouts are particularly suspect because:
- card timing matters
- side-specific strategic errors accumulate
- DEFCON / scoring / event handling errors compound badly

So instead of full rollout to terminal, prefer one of:
- shallow rollout + heuristic eval
- no rollout, just leaf eval
- a few tactical “forced” steps then eval

This is usually much better than old-school random/default-policy playouts.

---

## 4. Make rollouts **side-symmetric by construction**
This is one of the most important fixes for your exact problem.

If the same heuristic, when played against itself, gives USSR a 2:1 win rate, then before using it heavily in search you should try to remove or compensate that asymmetry.

Useful approaches:

### A. Measure bias as a calibration function
Sample many states `s`, and estimate:
- `V_h(s)` = heuristic/MCTS value from side-to-move convention
- true-ish value proxy from stronger search, self-play populations, or side-swapped evaluation

Then fit correction:
- global intercept
- phase-specific intercept
- maybe score/DEFCON/AR-specific calibration

At minimum, if the heuristic systematically overvalues USSR by `b`, subtract or re-center.

### B. Side-swap evaluation
For a state `s`, create mirrored equivalent evaluation perspective where possible.

In TS you cannot perfectly “mirror the board” like in chess, but you can still do something conceptually similar:
- evaluate from USSR perspective and US perspective using separately normalized value conventions
- force all values into a common “probability USSR wins from objectively correct play” scale
- remove side-to-move / side-identity offsets

Even simpler:
- when gathering training data, stratify by side and calibrate separately

### C. Debias by self-play population
Instead of one heuristic policy, use a pool:
- heuristic A
- noisy heuristic A
- heuristic A with softened parameters
- older model snapshots
- side-randomized variants

This reduces one fixed ideology from dominating all continuations.

---

## 5. Use rollouts as **control variates**, not final targets
A strong pattern is:

- maintain a learned value model `Vθ(s)`
- use rollout return `R` only as an auxiliary noisy estimate
- combine them, for example:
  - backed-up target = `α * R + (1-α) * Vθ(leaf)`
  - or use `R - baseline_h(s)` as a residual signal

Even better:
train the model to predict **residual over heuristic**:
- `true_value ≈ heuristic_value + learned_residual`

This is very natural for your setting.

If your heuristic is decent but biased, ask the model to learn:
- where heuristic is wrong
- by how much
- especially in specific card/timing/DEFCON situations

That is much easier than learning TS from scratch.

So a strong setup is:
- heuristic gives prior policy + rough value
- model learns correction to policy and value
- MCTS uses both

---

## 6. For value learning, use **reanalysis / stronger search targets**, not raw rollout outcomes
Bad pipeline:
- run heuristic rollout
- use terminal winner as value target
- train value head on that

Better pipeline:
- run search
- use improved root statistics as policy target
- use root value from search, but only after calibration / smoothing / averaging
- optionally reanalyze old positions with newer stronger models

Best practical principle:
**policy target can come from search; value target should come from stronger or more stable estimate than one cheap rollout.**

For TS specifically, I would trust:
1. visit-count policy targets
2. value targets from many-search average or deeper search
3. raw rollout win/loss only as weak auxiliary signal

---

## 7. Use **limited-depth tactical rollout**, not full strategic rollout
A good compromise is to let heuristic rollouts handle only the near future where it is most trustworthy.

For example:
- expand from root
- play 2–8 plies with heuristic/default policy
- stop and evaluate

This lets rollouts capture:
- immediate coups / realignments
- headline follow-through
- DEFCON traps
- urgent scoring timing
- obvious event sequencing

without forcing them to “solve the whole rest of the game” with a biased policy.

In TS this is especially attractive because many action differences are local/tactical even though full-game value is strategic.

---

## 8. Inject noise / policy softening in rollouts
If rollout policy is deterministic heuristic, MCTS can become “the heuristic plus search-shaped confirmation bias.”

Instead:
- sample from softmax over heuristic action scores
- add Dirichlet/Gumbel/noise at rollout choice points
- use ε-mixture between heuristic and random/legal-top-k

Why:
- makes rollouts less brittle
- exposes alternative continuations
- prevents one side’s preferred line from dominating solely because heuristic insists on it

But do not add too much randomness; random TS playouts are usually garbage.  
A good version is:
- 80–95% heuristic-guided
- 5–20% exploratory

---

## 9. Use **PUCT with heuristic prior**, but weak value backup
This is usually the cleanest way to “utilize heuristic rollouts” without overcommitting to them.

Let heuristic provide:
- action prior probabilities at node
- maybe progressive bias term in UCB/PUCT

but rely less on:
- terminal rollout returns

In other words:
- heuristic is excellent as a policy prior
- heuristic is dangerous as an unquestioned value oracle

This separation matters a lot.

A practical formula:
- prior from heuristic scores over legal moves
- leaf value from model / calibrated heuristic
- little or no full playout
- root visit counts become training policy target

That often outperforms classical rollout-heavy MCTS in structured games.

---

## 10. Train by **self-play population**, not by pure imitation of one biased heuristic
If your goal is “at least match the heuristic,” pure imitation may succeed, but it inherits its bias ceiling.

A better ladder is:

### Stage 1
Behavior clone the heuristic policy to get legal, sensible play.

### Stage 2
Run search on top of that policy.
Use visit counts as improved labels.

### Stage 3
Self-play model vs:
- itself
- heuristic
- older checkpoints
- perturbed opponents

### Stage 4
Keep an Elo gate:
only promote a new model if it beats a balanced evaluation suite.

This prevents the model from merely learning “USSR-favoring style.”

---

## 11. Evaluate in a way that detects side bias directly
This is essential.

Do not evaluate only by aggregate winrate in self-play. Track:

- model as USSR vs heuristic as US
- model as US vs heuristic as USSR
- model vs itself with fixed sides
- opening / scenario buckets
- early / mid / late war buckets

If a new model improves only on USSR side and gets worse as US, that is a red flag: it may be learning the same bias rather than genuine strength.

For your case, the most important metric is probably something like:
- average of winrate when assigned USSR and when assigned US against a reference pool

not raw combined winrate.

---

## 12. Best practical recipe for you
Given your exact setup, I would recommend this default:

### Version 1
Use heuristic in MCTS as:
- policy prior over legal actions
- shallow rollout policy for maybe 2–6 plies max
- then heuristic or learned leaf eval

Do **not** use full naive playout-to-end as main value target.

Train:
- policy head on root visit counts
- value head on search root value averaged over many simulations, with side-wise calibration
- optionally add auxiliary target to predict heuristic eval

### Version 2
Once model is decent:
- replace heuristic leaf eval with learned value model
- keep heuristic only as optional rollout / opponent policy / prior source
- use reanalysis to generate better targets

### Version 3
Move toward AlphaZero-style search:
- policy prior from model
- value from model
- heuristic only as bootstrap / fallback / evaluation opponent

---

## 13. A very useful trick: learn **delta over heuristic**
This deserves repeating because it fits your problem so well.

Let:
- `H(s)` = heuristic value estimate
- model predicts `Δ(s)`
- final value = `H(s) + Δ(s)`

and similarly for policy:
- heuristic action logits + learned correction logits

This way the learner starts from the heuristic’s knowledge but is explicitly allowed to fix its blind spots, including USSR bias.

That is often much more sample-efficient than learning everything from scratch.

---

## 14. What I would avoid
I would avoid these, at least initially:

### Avoid 1: full rollout-to-terminal with deterministic heuristic
Too biased, too slow, too reinforcing.

### Avoid 2: training value head directly on one-search rollout winner
Too noisy and policy-dependent.

### Avoid 3: evaluating progress only by self-play mirror matches
Can hide side bias and cyclic superiority.

### Avoid 4: pure imitation with no search improvement
You inherit the heuristic ceiling and asymmetry.

---

## 15. The short answer
Use heuristic rollouts mainly as a **search aid**, not as truth.

Best roles for the heuristic:
- action prior
- shallow continuation policy
- auxiliary baseline
- residual target base
- opponent in evaluation / self-play pool

Most dangerous role:
- unquestioned long-horizon value oracle

---

My concrete recommendation for a simple but strong first version:

- behavior clone heuristic policy
- run PUCT
- heuristic provides prior over actions
- rollout only a few plies, not to terminal
- leaf evaluated by calibrated heuristic or learned value
- train policy on root visit counts
- train value on calibrated search value, not raw rollout winner
- evaluate separately by side against fixed references

That gives you real policy improvement while minimizing “USSR advantage hallucination.”

If you want, I can next give a very concrete TS-specific design for:
1. node statistics and backup equations,
2. exactly how to combine heuristic prior + shallow rollout + learned value,
3. an incremental training pipeline from imitation to stronger-than-heuristic play.

---

## Q2
is there such a thing as meaningful visit counts in TS? kinda too sparse / noisy, no?

## A2
Yes, but only in a narrower sense than in games like Go or chess.

In Twilight Struggle, raw visit counts are often much less clean and much less information-dense because:

- branching factor is huge and irregular
- many positions are partially tactical, partially long-horizon strategic
- hidden information matters
- a lot of actions are “same-ish” at coarse level but differ in downstream card/timing consequences
- search budgets are usually small relative to tree width

So your intuition is right: **naive visit counts can be sparse and noisy**.

But that does **not** mean they are useless. It means you need to be careful about where they are meaningful.

## When visit counts are meaningful

They are useful when MCTS is mostly answering:

- which broad action family is better
- which of a few tactically critical moves is best
- whether one move is clearly bad
- how much search prefers one candidate over close alternatives

Examples in TS:
- coup vs influence vs event vs space
- which battleground to fight over
- whether to dump a bad card now or hold
- whether a headline / action is tactically urgent

In those cases, visit counts can absolutely carry signal, even if not super sharp.

Especially if:
- the root prior is decent
- legality and action abstraction are good
- leaf eval is not terrible
- search budget is enough to separate top few actions

Then root visits often give a better policy target than plain imitation.

## When visit counts are not very meaningful

They get weak when:

- almost every action gets only a few visits
- action space is huge because of combinatorial influence placements
- rollout / value noise dominates edge differences
- hidden-information uncertainty is large
- search depth is too shallow to resolve strategic consequences

Then counts may mostly reflect:
- prior bias
- exploration noise
- accidental early lucky rollouts
- tree-shape artifacts

In that regime, using visit counts as a hard target is dangerous.

## The right mental model

In TS, root visit counts are usually not “truth.”  
They are more like a **soft improvement hint** over the behavior policy.

That is the important framing.

Good use:
- as a softened policy target
- as ranking among top actions
- as a filtering signal

Bad use:
- as if 37 visits vs 21 visits means very precise superiority
- as if low-budget counts define exact move probabilities
- as if every searched state yields equally trustworthy targets

## What makes them more meaningful

### 1. Action abstraction
This matters a lot.

If your actions are extremely fine-grained, counts spread too thin.  
For TS, often better to search over more structured actions, for example:

- choose operation mode
- choose target region / country / coup target
- use a small exact decoder later for multi-influence placement

rather than treating every full allocation as a separate flat action from the start.

Otherwise counts become hopelessly diluted.

### 2. Strong prior
If the prior is decent, visits can refine it.  
If the prior is weak, visits mostly chase noise.

So visit counts become much more meaningful once you have:
- a cloned policy from heuristic or human-ish policy
- good legality masking
- reasonable move ordering

### 3. Better leaf value than rollout-to-end
If value estimates are noisy or biased, visit counts inherit that noise.

Counts become more meaningful when leaf evaluation is:
- learned
- calibrated
- at least more stable than long biased rollouts

### 4. Larger root budget
Even if deeper tree stats are noisy, root counts can still be useful if root simulations are large enough.

Usually in TS you care much more about:
- root action ranking quality

than about:
- precise deep subtree frequencies

## A practical distinction: top-1 meaningful, full distribution not so much

This is often the right answer.

In TS, visit counts may be good enough to tell you:
- “these 2–4 actions are the real candidates”
- “this action is probably strongest”

but not good enough to tell you:
- exact calibrated probabilities over all legal actions

So often the most reliable signal is:

- top action
- top-k set
- margin between best and second-best
- entropy / concentration of root visits

rather than the full raw distribution.

## Use confidence gating

This is one of the best fixes.

Only trust visit counts strongly when the root looks decisive.

For example, use them more when:
- best action has much larger visit share than runner-up
- search value is stable across batches
- root entropy is low enough
- top-k ranking is stable under reruns / noise
- both sides / belief samples agree

Use them less when:
- visits are diffuse
- top action changes a lot across reruns
- root value is unstable
- many actions are near-tied

So instead of “all visit counts are labels,” use:
- strong-search states as training gold
- weak-search states as weak supervision or skip them

## Better than raw visit counts: improved targets

A few stronger variants:

### A. Temperature-smoothed counts
Do not imitate raw counts directly. Use softened or sharpened target depending on budget.

For low-budget TS search, often you want a target between:
- policy prior
- one-hot argmax
- raw counts

not just raw `N(a)/sum N`.

### B. Mix prior and visits by confidence
For example:
- if search is weak, stay closer to prior
- if search is decisive, move toward visits

That is much safer in sparse domains.

### C. Train only on top-k mass
Collapse tail actions.  
The tail is often meaningless noise in TS.

### D. Use pairwise preferences
Instead of learning exact probabilities, learn:
- action A preferred over B

This is often more robust in noisy-search games.

## A very important TS-specific point

Because TS has huge combinatorial action spaces for influence placement, **visit counts are often much more meaningful at intermediate decisions than at fully expanded atomic actions**.

Example:
search may meaningfully tell you:
- Europe over Asia
- Iran over Iraq
- coup better than place influence

but not meaningfully distinguish every exact 4-op allocation pattern at low budget.

So hierarchical search / policy helps a lot:
- count signal at high-level branch
- maybe separate decoder for exact allocation

This is much more data-efficient.

## What I would trust in order

For TS, roughly:

1. Search top-1 move in tactically sharp states  
2. Search top-k ranking at root  
3. Visit concentration / confidence signals  
4. Full root distribution  
5. Deep-node visit stats

So yes, meaningful counts exist, but mostly at the root and mostly as ranking / preference signal, not as an accurate probability distribution.

Your skepticism is correct. The right move is not “discard visit counts,” but “use them selectively, structurally, and with confidence filtering.”

## Concrete recommendation

Treat root visits as meaningful only when they pass some quality checks.

A good default:
- use visit-count targets only for root
- keep only states where best visit share is above some threshold, or top-1/top-2 gap is large enough
- for diffuse roots, train less on counts and more on prior / imitation / value
- use hierarchical action representation so counts are not spread across absurdly many exact actions
- prefer pairwise or top-k supervision over full-distribution supervision for giant action sets

## Bottom line

So: **yes, meaningful visit counts in TS do exist, but they are not universally meaningful.**

They are usually:
- useful as a noisy policy-improvement signal at the root
- most valuable for top-k ranking and branch choice
- much less trustworthy as an exact distribution over a huge flat action space

---

Your skepticism is correct. The right move is not “discard visit counts,” but “use them selectively, structurally, and with confidence filtering.”

A better next step would be: use visit counts only for the root, filtered by confidence, plus a hierarchical action representation.

