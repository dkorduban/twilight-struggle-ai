Q:
Let's say I want to build an engine, a search-based engine for a turn-based game, and I want to use a heuristical value function together with something like Monte Carlo tree search. Is there some kind of rigorous or systematic way of tuning the weights of this? Let's say I have a linear combination of different features as a heuristical value function. Is there a way to find, or what are the options to find optimal weights that guarantee the best play?

A:
Yes. There are systematic ways, but the key point is:

there is usually **no general guarantee** that some weights are “globally optimal for best play” unless the game is small enough that you can compute the true game-theoretic values. In real engines, the best you can usually do is optimize weights for a **specific engine configuration**:

* search algorithm
* time budget / node budget
* opponent distribution
* opening distribution
* any randomness in search

For a linear evaluator
[
V_w(s)=w^\top \phi(s),
]
there are several different objectives you can optimize, and they are not the same.

## 1. Fit the evaluator to “true values” of positions

This is the cleanest formulation.

If for many positions (s) you have targets (y(s)) that approximate the true minimax value, then choose (w) to minimize
[
\sum_s (w^\top \phi(s)-y(s))^2
]
or a classification/logistic loss if the target is win/draw/loss.

Where do targets (y(s)) come from?

* exact solve for small subgames
* endgame tablebases
* much deeper search
* long-time-control search
* search values from a stronger engine

This gives a rigorous optimum for the chosen loss because linear regression / logistic regression is well-behaved.

But the guarantee is only:

* best fit to those targets
* within your feature class

It does **not** guarantee strongest play after search.

## 2. Fit directly to game outcomes

Use self-play or expert games and train the evaluator so that positions predict eventual result.

Typical methods:

* TD learning / TD(0) / TD((\lambda))
* Monte Carlo regression to final outcome
* LSTD / LSPI / approximate dynamic programming

This is more “RL-like” and does not require exact labels.

Good part:

* directly uses actual game outcomes

Bad part:

* very noisy
* slow credit assignment
* the best predictor of final result is not always the best leaf evaluator for search

So this is principled, but often not the strongest practical route by itself.

## 3. Optimize engine strength as a black-box objective

This is often the most relevant answer to your exact question.

Define
[
J(w)=\mathbb{E}[\text{score of engine with weights }w]
]
where score is measured by self-play matches or games against a fixed baseline.

Then optimize (J(w)) directly.

Common methods:

* SPSA
* CMA-ES
* cross-entropy method
* evolutionary strategies
* Bayesian optimization for lower-dimensional cases
* population-based tuning

This is attractive because it optimizes what you actually care about: winning games under your real search.

But:

* objective is noisy
* non-smooth
* expensive
* no global guarantee in general

Still, this is one of the most honest formulations of “best play.”

## 4. Train from search, not just from outcomes

This is often the strongest practical recipe.

Loop:

1. Use your current evaluator inside search.
2. Run stronger search to get better values or action choices.
3. Train the linear evaluator to match those search outputs.
4. Repeat.

Targets can be:

* root value from deeper search
* visit count distribution from MCTS
* best move from stronger search
* Q-values from search

This is a form of approximate policy iteration / expert iteration.

Why it works well:

* search produces lower-variance targets than raw game result
* evaluator learns to support the search you actually run

This is usually more effective than trying to learn from win/loss alone.

## 5. Classic “Texel tuning” style for linear evals

For chess-like engines with hand-built features, a very practical method is:

* collect many positions from games
* assign each position a game result target
* map eval to win probability with a logistic function
* optimize weights to minimize prediction error

This is systematic, efficient, and works especially well for linear evaluation functions.

It gives you a global optimum for that surrogate loss, which is nice.

But again, it optimizes **position-result prediction**, not guaranteed playing strength under search.

## What “optimal” can mean

There are really four notions:

1. **Best fit to exact minimax values**
   Good theoretically, usually impossible at scale.

2. **Best predictor of eventual outcome**
   Reasonable, but may not give strongest search behavior.

3. **Best support for limited-depth / limited-budget search**
   Usually what engine builders actually want.

4. **Highest empirical Elo / win rate**
   Most relevant operationally, but hardest to optimize rigorously.

In practice, 3 and 4 matter most.

## For MCTS specifically

With MCTS, your weights may affect:

* leaf value estimate
* rollout policy
* prior policy
* progressive bias / move ordering
* sometimes exploration-related heuristics

Important: a value function that is “accurate in isolation” is not always best inside MCTS.

Example:

* a slightly biased but low-variance evaluator can outperform a more accurate high-variance one
* an evaluator that separates tactical traps well may help MCTS more than one with better average calibration

So for MCTS, direct engine-strength tuning or iterative training-from-search is especially important.

## What guarantees are actually possible?

Very limited ones.

You can get a real guarantee only under stronger assumptions, such as:

* you know exact targets for a representative set of states
* the true value function lies in your linear feature family
* optimization problem is convex
* test distribution matches deployment distribution

Then you can guarantee best weights for that surrogate problem.

You usually **cannot** guarantee:

* globally strongest engine
* best play against all opponents
* best play under all time controls
* best play after interaction with search

## Strong practical recipe

For a search-based engine with linear eval, a good default pipeline is:

1. Design features carefully.
2. Generate a large corpus of positions.
3. For each position, get a better target from stronger search or long-budget search.
4. Fit linear weights with regression / logistic loss + regularization.
5. Plug into engine.
6. Run many head-to-head matches.
7. Fine-tune weights and search hyperparameters with SPSA or CMA-ES on Elo.
8. Validate on held-out openings, both sides, multiple time controls.

That gives you:

* stable offline learning
* then true closed-loop optimization for playing strength

## Very important pitfall

Do not tune only by self-play against the current version without care. That can overfit to:

* your own openings
* your own style
* one time control
* one seed / randomness pattern

Use:

* held-out opening suites
* side balancing
* multiple baselines
* SPRT or confidence intervals for match testing

## Bottom line

There is no general method that guarantees “best play” from heuristic weights alone in a real search engine.

The most rigorous options are:

* **supervised fitting to stronger-search or exact values** for clean optimization
* **direct black-box optimization of Elo/win rate** for actual engine strength
* **iterative search-improvement training** as the strongest practical middle ground

If the engine is serious, the usual best answer is:

**first fit the linear evaluator to stronger search targets, then fine-tune by match play.**

That is the closest thing to a systematic, principled pipeline.

I can also give a concrete recipe for tuning linear weights in MCTS with SPSA or with search-distillation targets.

Q:
To give a context, I'm not interested in kind of global optimality, just best possible under the search. I don't have a stronger engine, I'm kind of bootstrap in the engine, so I have a rule-based heuristic, which is kind of poor and very biased, so I'm not sure if it's useful. I have MCTS and ISMCTS implemented, also the game is with partial information. How expensive is evolutionary strategy or CMA-ES, which is also evolutionary, as far as I understand?

A:
If the objective is **“best play under my actual search”**, then **CMA-ES / evolutionary tuning is valid**, but for your setting it is usually **quite expensive** and often **not the first thing I would try**.

Because you have:

* partial information
* MCTS / ISMCTS
* a weak biased heuristic
* no stronger teacher

your optimization target is noisy in several ways at once:

* hidden-state sampling / determinization noise
* search randomness
* opening / seat bias
* opponent-coupling bias if you self-play against the current version

That makes black-box evolution work, but it raises the sample cost a lot.

## Rough cost intuition

Suppose your evaluator has (d) weights.

### CMA-ES

CMA-ES keeps a Gaussian over weight vectors and, per generation, evaluates about
[
\lambda \approx 4 + 3\ln d
]
candidates as a rough default.

So:

* (d=20) → maybe around 13 candidates / generation
* (d=100) → maybe around 17–20
* (d=500) → similar order, but covariance adaptation becomes heavier and less reliable

That candidate count is not the main problem.

The real problem is: **how many games do you need to tell candidate A is better than candidate B?**

If each candidate needs, say:

* 50–200 paired games for a noisy but usable signal,
  and you do:
* 15 candidates / generation
* 50 generations

then that is already roughly:

* (15 \times 100 \times 50 = 75{,}000) games

And in practice, for noisy search-based engines, it can easily be more.

If each game is expensive, CMA-ES becomes painful fast.

## Why CMA-ES gets especially expensive here

CMA-ES is best when:

* dimension is not too large
* parameters are continuous
* objective is noisy, but not insanely noisy
* you can afford many full evaluations

Your setup violates at least two of these:

* engine strength is a **very noisy** objective
* self-play is **expensive**
* with many handcrafted features, dimension can grow quickly

Also, CMA-ES learns a covariance matrix over parameters. That is useful when weights interact strongly, but it means it is spending budget learning the geometry of the parameter space, which is expensive when evaluations are noisy.

## In engine tuning, SPSA is often much cheaper

For this kind of problem, **SPSA** is often a better default than CMA-ES.

Why:

* per iteration, SPSA needs only **2 function evaluations**, essentially independent of dimension
* works surprisingly well for many weights
* easy to combine with noisy self-play

Very rough comparison:

* **CMA-ES**: maybe 10–20 candidates per generation
* **SPSA**: 2 perturbed candidates per iteration

So if one “evaluation” means a match batch, SPSA is often an order of magnitude cheaper in wall-clock sample cost.

That is why many game-engine tuning setups historically prefer:

* SPSA
* coordinate/local search
* small-batch hill climbing
  over full CMA-ES.

## But there is a catch with SPSA too

SPSA is cheaper per step, but the signal is still noisy. So you still need:

* paired matches
* side-swapping
* fixed opening suite
* common random numbers when possible
* enough repetitions

Still, if you have 50 or 200 weights, SPSA usually scales much better than CMA-ES.

## For your exact setup, I would rank the options like this

### Best practical first choice

**Small-scale self-play tuning with SPSA or local search**

* optimize actual engine win rate under fixed search budget
* use paired openings / both sides / fixed seeds when possible
* tune only the most important 10–30 weights first

### Second

**Offline learning from search targets generated by your own engine**
Even if the engine is weak, this can still help if done carefully:

* collect states from self-play
* for each state, run a much larger search than normal
* train linear weights to predict that deeper-search value
* iterate

This is bootstrap, but less brittle than training directly on final win/loss.

### Third

**CMA-ES / ES**
Use it if:

* number of weights is modest
* games are cheap
* you can parallelize many evaluations
* you want a broad global-ish search over the weight space

I would not make it my first hammer unless your feature count is small and compute is abundant.

## Important point: weak biased heuristic is still usable

A poor heuristic is not useless. It can still be useful as:

* initialization
* feature prior
* regularizer
* source of a starting search policy

What matters is whether search can partially correct it.

If the heuristic is biased but has some rank-order signal, search-improvement training can denoise it over time.

What is dangerous is when the heuristic causes systematic search pathology, for example:

* overvalues traps that only work under wrong beliefs
* badly misprices hidden-information states
* induces determinization artifacts in ISMCTS

Then direct black-box Elo tuning may merely overfit those pathologies.

## Partial information makes the objective nastier

With ISMCTS especially, evaluator quality is entangled with:

* belief sampling
* determinization policy
* rollout policy
* backup rule
* information leakage bugs or near-bugs

So sometimes “bad weights” are not the main issue.

Before heavy tuning, it is worth checking:

* does strength change more from evaluator weights, or from better belief/determinization?
* are rollouts dominating leaf eval?
* is search depth / breadth too low for evaluator improvements to matter much?

Because if search noise dominates, weight tuning will look much more expensive than it should.

## A useful cost model

Think of total cost as:

[
\text{total cost} \approx
(\text{candidates tested})
\times
(\text{games per candidate})
\times
(\text{cost per game})
]

CMA-ES reduces neither the games per candidate nor the cost per game. It mainly tries to be smarter about candidate generation.

In noisy engine tuning, the dominant term is often **games per candidate**.

That is why methods with very few candidate evaluations per step are attractive.

## Concrete recommendation

For your setting, I would do this:

1. Keep the linear evaluator.
2. Normalize features so weights live on comparable scales.
3. Start with only the most important weights, not all of them.
4. Tune with **SPSA** against a fixed baseline under a fixed search budget.
5. Use:

   * paired games
   * side swap
   * fixed opening set
   * mirrored random seeds if possible
6. Every so often, refresh the baseline to the best-so-far engine.
7. Separately, generate self-play positions and train the evaluator to match **deeper search outputs** from your own engine.
8. Alternate these two loops:

   * search-distillation / bootstrap
   * direct Elo tuning

That hybrid is usually much more compute-efficient than pure CMA-ES.

## Rule of thumb

* **< 20 weights, cheap games, lots of parallelism**: CMA-ES is reasonable.
* **20–200 weights, noisy expensive games**: SPSA is usually better.
* **many weights / many correlated features**: first reduce or group parameters, then tune.
* **very biased heuristic + partial info**: do not rely only on direct self-play Elo optimization.

## My honest answer

CMA-ES is not absurd here, but in your setting it is probably **too expensive relative to its benefit**, unless:

* your feature count is small,
* games are cheap,
* and you can run large parallel batches.

For a bootstrapping imperfect-information engine, I would much more strongly favor:

* **iterative self-distillation from deeper search**
  plus
* **SPSA-style direct strength tuning**

That tends to be the best compute/robustness tradeoff.

I can write a concrete tuning loop for your case, including exactly how many games per step, how to pair seeds/openings, and how to combine ISMCTS search targets with SPSA.

Q:
Explain SPSA

A:
SPSA = **Simultaneous Perturbation Stochastic Approximation**.

It is a way to optimize a noisy objective when you cannot compute gradients directly.

In your case, the objective could be something like:

[
J(w) = \text{engine strength under your actual search}
]

where (w) is the vector of heuristic weights.

## Core idea

Suppose you have (d) weights.

A standard finite-difference gradient estimate would change one weight at a time:

* bump (w_1) up/down
* bump (w_2) up/down
* ...
* bump (w_d) up/down

That costs about **2d objective evaluations** per gradient estimate.

SPSA does something much cheaper:

* perturb **all weights at once** in random directions
* evaluate only two points
* recover an approximate gradient for all coordinates from those two evaluations

So per step it needs only **2 evaluations**, no matter whether you have 10 weights or 500.

That is the main attraction.

---

## How one SPSA step works

Let current weights be (w_k).

### 1. Sample a random perturbation vector

Draw
[
\Delta_k = (\Delta_{k,1}, \dots, \Delta_{k,d})
]
where each coordinate is usually independently (+1) or (-1) with equal probability.

### 2. Evaluate two nearby points

Choose a small perturbation size (c_k), then evaluate:

[
J^+ = J(w_k + c_k \Delta_k)
]
[
J^- = J(w_k - c_k \Delta_k)
]

In your setting, one evaluation of (J(\cdot)) means:
run a match batch, measure win rate / Elo / score.

### 3. Estimate the gradient

The SPSA gradient estimate is

[
\hat g_{k,i} = \frac{J^+ - J^-}{2 c_k \Delta_{k,i}}
]

for each coordinate (i).

Since (\Delta_{k,i} \in {+1,-1}), this is basically:

* same numerator for every coordinate
* coordinate sign depends on whether that coordinate was perturbed up or down

So one noisy difference gives you an estimate for the whole gradient vector.

### 4. Update weights

If maximizing (J):

[
w_{k+1} = w_k + a_k \hat g_k
]

where (a_k) is the learning rate.

---

## Intuition

If pushing weights in a random signed direction (\Delta_k) helps, then the algorithm nudges the weights in roughly that direction.

Over many iterations, those random probes statistically reconstruct the gradient.

It sounds almost too crude, but it works surprisingly well when:

* objective is noisy
* dimension is moderate or large
* each evaluation is expensive

That is why it is popular in engine tuning.

---

## Why it is attractive for game engines

Suppose you have 100 heuristic weights.

A coordinate-wise finite-difference gradient step needs about:

* 200 match evaluations

SPSA needs:

* 2 match evaluations

That is a huge difference.

For engine tuning, objective evaluations are expensive because each one means many self-play games. So this reduction matters a lot.

---

## What the “objective evaluation” really is in your case

For a search engine, (J(w)) is not “the value of one position.”

It is usually something like:

* win rate against a baseline
* average score over a set of paired games
* approximate Elo from a match batch

So SPSA is not usually optimizing a clean mathematical function you can inspect exactly. It is optimizing a **noisy experimental measurement** of strength.

That is fine. SPSA was designed for noisy objectives.

---

## Very important detail: variance reduction

Naive SPSA can be extremely noisy. The biggest practical trick is to make the (+) and (-) evaluations as comparable as possible.

For engine tuning, that means:

* same opening positions
* same side assignments, or swapped symmetrically
* same random seeds if possible
* same opponent / baseline
* same search budget

So instead of comparing two unrelated match batches, compare:

* engine with (w + c\Delta)
* engine with (w - c\Delta)

on nearly the same test set

This massively reduces variance.

For imperfect-information search, this matters even more.

---

## Minimal concrete example

Say your heuristic has 3 weights:

[
w = (1.2, -0.7, 0.3)
]

Sample:
[
\Delta = (+1, -1, +1)
]

Take (c=0.1), so evaluate:

[
w^+ = (1.3, -0.8, 0.4)
]
[
w^- = (1.1, -0.6, 0.2)
]

Suppose:
[
J(w^+) = 0.56,\quad J(w^-) = 0.48
]

Then:
[
J^+ - J^- = 0.08
]

Gradient estimate is:

[
\hat g_1 = \frac{0.08}{2 \cdot 0.1 \cdot (+1)} = 0.4
]
[
\hat g_2 = \frac{0.08}{2 \cdot 0.1 \cdot (-1)} = -0.4
]
[
\hat g_3 = \frac{0.08}{2 \cdot 0.1 \cdot (+1)} = 0.4
]

So the algorithm says:

* increase weight 1
* decrease weight 2
* increase weight 3

Then update (w) with a learning rate.

---

## Why this estimate is not nonsense

The estimate is noisy, but under standard assumptions it is approximately unbiased up to small (O(c_k^2)) error, and over time behaves like a stochastic gradient method.

So the theory is not “magic heuristic.” It is a legitimate stochastic optimization method.

But the guarantee is only local/asymptotic, like other gradient methods. It does not guarantee the global best engine.

---

## Standard schedules

Usually you do not keep the step sizes fixed.

Typical form:

[
a_k = \frac{a}{(A+k+1)^\alpha}
]
[
c_k = \frac{c}{(k+1)^\gamma}
]

Common defaults from the SPSA literature are roughly:

* (\alpha \approx 0.602)
* (\gamma \approx 0.101)

Meaning:

* learning rate shrinks over time
* perturbation size also shrinks, but more slowly

In practice, for engine tuning, exact constants matter less than:

* proper feature scaling
* enough games per evaluation
* good variance reduction

---

## Why feature scaling matters a lot

If one feature typically ranges in ([0, 1000]) and another in ([0,1]), then the same perturbation magnitude on their weights means very different changes in evaluation.

So before SPSA, it is a good idea to normalize features so the weights live on comparable scales.

Otherwise tuning becomes unstable and slow.

---

## Strengths of SPSA

SPSA is good when:

* many weights
* no gradients
* noisy objective
* each evaluation expensive

That fits engine tuning quite well.

Compared with CMA-ES:

* much cheaper per iteration
* scales better in dimension
* simpler

Compared with coordinate search:

* can update all weights at once
* much more sample efficient in high dimension

---

## Weaknesses of SPSA

SPSA is still noisy and imperfect.

Main downsides:

* can converge slowly if objective is very noisy
* sensitive to bad scaling
* only local optimization
* if your engine match result is too noisy, updates become almost random
* interactions among weights can make it wander unless step sizes are tuned reasonably

Also, if your evaluator is fundamentally bad because the features are wrong, SPSA cannot fix that. It only tunes within the feature family you gave it.

---

## In your imperfect-information MCTS / ISMCTS setting

SPSA is usable, but I would be careful about what exactly gets tuned.

Good first targets:

* leaf evaluation weights
* rollout heuristic weights
* maybe a few exploration / mixing constants

Less ideal at first:

* too many parameters at once
* parameters entangled with belief bugs or determinization artifacts

Because in ISMCTS, “bad evaluator” and “bad hidden-state sampling” can look similar in match results.

So I would start with a modest set of important weights.

---

## Practical recipe for your case

A strong simple setup is:

1. Pick a baseline engine (w).
2. Sample random (\Delta).
3. Create (w^+ = w + c\Delta), (w^- = w - c\Delta).
4. Run paired matches:

   * same opening set
   * both sides
   * same search budget
   * same hidden-state sampling seeds if possible
5. Compute batch score difference (J^+ - J^-).
6. Form SPSA gradient estimate.
7. Update weights.
8. Repeat.

Often you also:

* clip weights to sane ranges
* average several SPSA gradients before updating
* keep the best-so-far parameter vector, not just the latest

---

## The simplest mental model

SPSA is basically:

“Try one random ‘all-weights-at-once’ push in both directions, see which side wins more games, and use that to nudge all weights.”

It is a noisy gradient descent/ascent method that is shockingly cheap in high dimension.

---

## When I would use it

I would use SPSA when:

* you care about actual playing strength
* you cannot get clean training targets
* full black-box evaluation is expensive
* you have more than a handful of weights

That sounds quite close to your setting.

If you want, I can next give a **concrete SPSA loop for engine tuning**, including match batching, paired seeds, and practical hyperparameter choices.

Q:
You're a world champion in TS and have a degree in computer science. Generate a decent heuristical value function to start with. It should include all "special" event cards

A:
Assuming **Twilight Struggle**.

A strong first evaluator is a **VP-equivalent, USSR-positive** function:

[
V(s)=
1.00\cdot VP
+\sum_{r} w_r\cdot urgency(r)\cdot scoreNow(r)
+0.25\cdot BGPressure
+0.18\cdot Access
+0.15\cdot Overcontrol
+0.35\cdot MilOpsEdge
+0.35\cdot DefconEdge
+0.25\cdot SpaceEdge
+0.75\cdot ChinaEdge
+SpecialActive
+0.35\cdot SpecialHand
]

Use these starting region weights:

[
w_{\text{Europe}}=1.20,;
w_{\text{Asia}}=1.00,;
w_{\text{Middle East}}=0.90,;
w_{\text{Central America}}=0.85,;
w_{\text{Africa}}=0.80,;
w_{\text{South America}}=0.90,;
w_{\text{SE Asia}}=0.70
]

`scoreNow(r)` should be the **exact official scoring if that region were scored now**, not a proxy. That is the single most important part. Asia, Europe, Middle East, Central America, Africa, South America, and Southeast Asia all have explicit scoring formulas, and the China Card is worth 4 Ops, +1 if fully spent in Asia, with 1 VP to the holder at game end. ([Twilight Strategy][1])

## Core features

`urgency(r)`:

* `0` if the scoring card is gone
* `1.30` if the scoring card is known in someone’s current hand
* `1.00` if it is live but unseen
* `0.60` if it only matters after reshuffle

`BGPressure`:
Sum over battlegrounds in still-live regions:
[
\sum_c regionScale(c)\cdot \tanh!\left(\frac{inf_{USSR}(c)-inf_{US}(c)}{stability(c)}\right)
]

`Access`:
Reward having legal placement paths into key regions/battlegrounds where the opponent does not. In practice, count swing access to places like Thailand, Pakistan/India, Iran, Egypt, Panama, South Africa, Angola, and Venezuela.

`Overcontrol`:
For each important country, add a small bonus for extra influence beyond control margin. This matters a lot in TS because many fights are really about how hard a country is to flip, not just who controls it now.

`MilOpsEdge`:
Expected end-of-turn military-ops advantage, not current raw difference. Missing the required amount is usually about a VP swing.

`DefconEdge`:
Count high-value legal coups/realignments available to each side under current DEFCON and current flags.

`SpaceEdge`:
Use current space VP difference plus a small bonus for being ahead on the track.

`ChinaEdge`:

* `+1.00` if USSR holds China and it is available
* `+0.45` if USSR holds it face-down/unavailable
* negate symmetrically for US

Also add `+0.25` if Asia is still live, because China is more tactical there. The exact China Card rule is stable enough that it is worth an explicit feature. ([Twilight Strategy][1])

## The special-card layer

Do **not** hard-code the immediate board or VP effect of special cards twice. If Camp David already put influence in Israel/Jordan/Egypt, or John Paul already changed Poland, that is already reflected in `scoreNow`, `BGPressure`, and `Overcontrol`. The `SpecialActive` term should only model the **residual rule-changing part**.

A clean way to do that is:

[
SpecialActive = TurnMods + TrapsAndLocks + ScoreOverrides + PairedCardThreats
]

### 1. Turn modifiers

Use these starting values:

[
\text{Containment} = -0.45 \cdot remAR_{US}
]
[
\text{Brezhnev} = +0.45 \cdot remAR_{USSR}
]
[
\text{Red Scare on US} = +0.55 \cdot remAR_{US}
]
[
\text{Red Scare on USSR} = -0.55 \cdot remAR_{USSR}
]
[
\text{Vietnam Revolts} = +0.20 + 0.20\cdot urgency(SEAsia)
]
[
\text{North Sea Oil} = -1.00
]
[
\text{Yuri and Samantha} = +0.40\cdot \mathbb{E}[US\ coups\ remaining]
]
[
\text{Latin American Death Squads} = \pm 0.25\cdot CA_SA_coupValue
]
[
\text{Iran-Contra} = +0.20\cdot US_realignValue(CA,SA)
]
[
\text{Chernobyl(region)} = -0.80\cdot USSR_need(region)
]
[
\text{NORAD} = -0.35\cdot \mathbb{E}[NORAD\ triggers]
]

These are all persistent turn-state effects rather than plain board moves. Containment and Brezhnev change Ops for the remainder of the turn; Red Scare/Purge reduces the affected side’s Ops; Vietnam Revolts gives the USSR a Southeast Asia all-in bonus; North Sea Oil grants the US an extra action round that turn; Latin American Death Squads and Iran-Contra change coup/realignment quality; Chernobyl blocks USSR influence placement in a named region; NORAD adds influence after action rounds when its condition is met; Yuri and Samantha pays VP on later US coups. ([Twilight Strategy][1])

### 2. Traps and hard locks

[
\text{Quagmire} = +1.20\cdot \mathbb{E}[lostAR_{US}]
]
[
\text{Bear Trap} = -1.20\cdot \mathbb{E}[lostAR_{USSR}]
]
[
\text{CMC on US} = +2.00\cdot coupNeed(US)-cancelCost(US)
]
[
\text{CMC on USSR} = -2.00\cdot coupNeed(USSR)+cancelCost(USSR)
]
[
\text{Nuclear Subs} = -0.60\cdot US_BG_coupValue
]
[
\text{SALT residual} = +0.20\cdot (coupNeed(US)-coupNeed(USSR))
]
[
\text{We Will Bury You pending} = +3.00\cdot (1-p(UN\ Intervention\ next\ US\ AR))
]
[
\text{U2 pending} = +1.00\cdot p(UN\ Intervention\ later\ this\ turn)
]

Quagmire and Bear Trap consume action rounds and can become devastating if the trapped side is short on 2+ Ops cards. Cuban Missile Crisis is a temporary “you basically may not coup unless you pay the cancel cost” lock. Nuclear Subs changes the DEFCON geometry of US battleground coups. SALT suppresses coup quality for both sides. We Will Bury You and U2 both create pending conditional value tied to UN Intervention. ([Twilight Strategy][1])

For the trap expectation, a decent first approximation is:

[
\mathbb{E}[lostAR] \approx \min(remAR,; 1.5 + 0.5\cdot I[\text{hand short on 2+ Ops}])
]

That is crude, but good enough to start.

### 3. Scoring overrides

For these, do not use fixed constants. Recompute the relevant score:

* **Formosan Resolution**: compute Asia score with Taiwan treated as an extra US battleground if Taiwan is US-controlled and China has not canceled the flag.
* **Shuttle Diplomacy**: compute the next Asia/Middle East score with USSR battleground count effectively reduced by one.
* **NATO**: do not change `scoreNow`; instead reduce USSR Europe attack/coup/realignment potential.
* **US/Japan Mutual Defense Pact**: reduce USSR Japan swing potential.
* **Willy Brandt**: increase West Germany attackability while the West-Germany NATO protection is off.
* **The Reformer**: penalize USSR Europe coup options only; the influence already placed belongs in the base board score.

Formosan changes Asia scoring, Shuttle Diplomacy changes battleground counting in the next Asia or Middle East scoring, NATO blocks USSR coups/realignments against US-controlled Europe, US/Japan locks Japan, Willy Brandt affects NATO on West Germany, and The Reformer bans USSR coups in Europe. ([Twilight Strategy][1])

### 4. Paired-card threats

Several “special” cards matter because they enable, cancel, or amplify some other event. Handle those with:

[
liveThreat(card)=0.60\cdot p(card\ still\ live)\cdot \max(0,\ eventSwing(card))
]

Then add:

[
\text{Camp David} = -liveThreat(Arab\text{-}Israeli\ War)
]
[
\text{John Paul II} = -liveThreat(Solidarity)
]
[
\text{Iranian Hostage Crisis} = +0.40\cdot liveThreat(Terrorism)
]
[
\text{Iron Lady} = -0.30\cdot liveThreat(Socialist\ Governments)
]
[
\text{AWACS} = -0.40\cdot liveThreat(Muslim\ Revolution)
]
[
\text{North Sea Oil extra} = -0.60\cdot liveThreat(OPEC)
]
[
\text{Flower Power} = +0.35\cdot \mathbb{E}[US\ war\ cards\ played]
]

If An Evil Empire has happened, set Flower Power’s term to zero. If Tear Down This Wall has happened, remove Willy Brandt’s special protection. These pairings are exactly the sort of thing a TS evaluator should model explicitly because the board alone does not capture them. ([Twilight Strategy][1])

## Cards in hand: how to include the “non-board” specials

For truncated search, add a small `SpecialHand` term. The rule I would use is:

[
SpecialHand = \sum_{c \in hand} handValue(c)
]

with `handValue(c)` defined as:

[
handValue(c)=0.25\cdot eventPV(c)+override(c)
]

where

[
eventPV(c)=V(applyEvent(c,s))-V(s)
]

This handles most one-shot special cards automatically. The manual overrides are only for cards whose main value is **information**, **cancelation**, or **instant game ending**.

Use these overrides:

[
Wargames =
\begin{cases}
+10^5 & \text{if USSR can fire it now at DEFCON 2 and still lead after giving 6 VP}\
-10^5 & \text{if US can}\
0 & \text{otherwise}
\end{cases}
]

[
MissileEnvy = 0.4 + 0.5\cdot(oppMaxOps-2)-eventRisk
]

[
Defectors = 0.8\cdot expectedOppHeadlineValue
]

[
UNIntervention = 0.8\cdot bestBadOpponentEventInOwnHand
]

For information cards, use **belief value**, not determinization truth:

[
infoValue = 0.60\cdot unknownScoringCount + 0.15\cdot oppHandSize + discardBonus
]

Apply that to **CIA Created, Lone Gunman, Aldrich Ames Remix, Cambridge Five, and Our Man in Tehran**. For Aldrich, `discardBonus` is larger because it also strips a chosen US card. For Cambridge Five, only count uncertainty over scoring cards. For Our Man in Tehran, interpret `discardBonus` as the value of filtering bad events out of the 5-card look. For China-steal cards—**Cultural Revolution, Nixon Plays the China Card, Ussuri River Skirmish**—just fold them into `ChinaEdge` through an expected China swing term. Wargames, Defectors, UN Intervention, CIA Created, Missile Envy, Grain Sales, Ask Not, Star Wars, Aldrich Ames, Cambridge Five, and Our Man in Tehran are all better modeled this way than as static board weights. ([Twilight Strategy][1])

That ISMCTS point matters: in a single determinization, CIA/Aldrich/Lone Gunman can look artificially weak because the engine already “knows” the hidden hand. Their real value is **belief collapse**.

## The actual starter version I would implement

Keep it simple at first:

1. Exact `scoreNow` for all live scoring regions.
2. China, MilOps, DEFCON/coup availability, Space.
3. The active special-card formulas above.
4. Small `SpecialHand` term only for:

   * Wargames
   * Missile Envy
   * Defectors
   * UN Intervention
   * CIA / Lone Gunman / Aldrich / Cambridge / Our Man
   * China-steal cards

Everything else can start as pure `eventPV`.

That gives you a good bootstrap evaluator without drowning in per-card constants.

## First weights to tune

Tune these first, in this order:

* region weights
* `extra Ops per remaining AR` coefficient (`0.45`)
* `lost trapped AR` coefficient (`1.20`)
* `coup lock` coefficient for Cuban Missile Crisis
* `paired-card threat` discount (`0.60`)
* China available / unavailable values
* information-card coefficient

Those 7 parameters will move strength much more than trying to hand-tune 30 card constants.

Next step is a concrete TypeScript implementation of this evaluator with exact helper signatures for `scoreNow`, `liveThreat`, and the TS event-flag enum.

[1]: https://twilightstrategy.com/card-list/ "https://twilightstrategy.com/card-list/"

Q:
well values is nice, but how to sample action weights for search? action space is huge

A:
Yes. For **search**, the right object is usually **not** a flat weight for every legal move. In TS the raw action space is too large because “play card for Ops” explodes into many influence allocations, realignment sequences, and target choices. A better design is:

1. keep the tree over **materialized** actions only,
2. use **progressive widening** so each node only grows a small number of children as visits increase,
3. generate each new child from a **proposal policy** (q(a\mid I)) over the current information set (I),
4. then use UCT/PUCT only over the already-materialized children.

That is exactly the kind of setting progressive widening was introduced for: large branching factors, where delaying expansion of low-priority moves lets MCTS search deeper. In imperfect-information games, ISMCTS also avoids some determinization pathologies by searching information sets rather than separate determinized trees, and Cowling et al. explicitly note that determinization duplicates work and suffers from strategy fusion. 

## The core pattern

At node (I) with visit count (N(I)), allow only

[
K(I)=K_0+\left\lfloor c_{\text{pw}},N(I)^\alpha \right\rfloor
]

children. A standard progressive-widening family uses this kind of polynomial schedule, and double progressive widening applies the same idea at chance nodes as well. 

Then:

* if (|\mathcal C(I)| < K(I)), sample a **new** action (a \sim q(\cdot\mid I)) and add it;
* otherwise, select among existing children with something like

[
\text{score}(a)=Q(I,a)+c_{\text{puct}},P(I,a)\frac{\sqrt{N(I)}}{1+N(I,a)}.
]

Here (P(I,a)) is not a full-policy output over all legal moves; it is just the prior on the **current candidate set**.

That is the cleanest way to handle huge action spaces.

## What to sample in Twilight Struggle

Do **not** sample complete raw moves directly. Sample them **hierarchically**:

[
q(a\mid I)=q(c\mid I);q(m\mid c,I);q(\tau\mid c,m,I);q(x\mid \tau,c,m,I)
]

where:

* (c) = card chosen
* (m) = mode: event / ops / space
* (\tau) = tactical template
* (x) = concrete instantiation: targets, allocation, subset, etc.

That factorization is the main trick.

## A good TS proposal policy

### 1. Choose the card

Score each card by its **best plausible use**:

[
S_{\text{card}}(c)=\max{S_{\text{event}}(c),,S_{\text{ops}}(c),,S_{\text{space}}(c)}
]

and sample

[
q(c\mid I)\propto \exp(\beta_c,S_{\text{card}}(c)).
]

For a start:

[
S_{\text{event}}(c)=\max_x \Big(V(T_{c,x}(I))-V(I)+\lambda_{\text{info}},IG(c,x)+\lambda_{\text{tempo}},Tempo(c,x)\Big)
]

where (T_{c,x}) means “apply event (c) with choice (x).”

This matters because plain determinization tends to undervalue **information-gathering plays**; Cowling et al. explicitly call out that determinization will not naturally choose information-gathering or information-hiding plays. In TS that means cards like **CIA Created, Lone Gunman, Cambridge Five, Aldrich Ames Remix, Our Man in Tehran** need an explicit information bonus (IG), not just board delta. ([White Rose Research Online][1])

A practical (IG) term:

[
IG(c,x)=H(b)-\mathbb E[H(b'\mid c,x)]
]

where (b) is your belief over opponent hand / unseen scoring / deck state.

### 2. Choose the mode for that card

Use:

[
q(m\mid c,I)\propto \exp(\beta_m,S_m(c,I))
]

with

* (m=\text{event}): as above
* (m=\text{space}): high when the event is toxic and space is legal
* (m=\text{ops}): based on the best coup / realign / influence line available with that card

So:

[
S_{\text{ops}}(c)=\max{S_{\text{coup}}(c),S_{\text{realign}}(c),S_{\text{place}}(c)}.
]

### 3. If Ops, choose a tactical template

For TS, I would start with these templates:

* `COUP_BG`
* `COUP_NONBG_MILOPS`
* `REALIGN_LINCHPIN`
* `DEFEND_CONTROL`
* `BREAK_CONTROL`
* `GAIN_ACCESS`
* `PREP_SCORING`
* `OVERPROTECT_BG`
* `SPACE_ESCAPE`
* `PURE_EVENT`
* `INFO_EVENT`

Then

[
q(\tau\mid c,m,I)\propto \exp(\beta_\tau U_\tau(c,m,I)).
]

The template utility is the best local opportunity of that type.

## Concrete starter utilities

### Coup target score

For each legal coup target (j),

[
u_{\text{coup}}(j)=
\mathbb E\big[V(s'_j)\big]-V(s)
+\lambda_1 \Delta \text{MilOps}
+\lambda_2 \Delta \text{DEFCONPressure}
+\lambda_3 \text{RegionUrgency}(j)
+\lambda_4 \text{AccessSwing}(j)
]

and

[
S_{\text{coup}}(c)=\max_j u_{\text{coup}}(j).
]

Interpretation:

* expected board swing after the coup
* plus military-ops value
* plus DEFCON trap / lock value
* plus urgency if the region is live for scoring
* plus access consequences

### Realignment target score

[
u_{\text{realign}}(j)=
\mathbb E\big[V(s'_j)\big]-V(s)
+\lambda_5 \text{Repeatability}(j)
+\lambda_6 \text{AdjacencyEdge}(j)
+\lambda_7 \text{ControlFragility}(j)
]

and

[
S_{\text{realign}}(c)=\max_j u_{\text{realign}}(j).
]

Realignment is usually about linchpins, repeated rolls, and adjacency asymmetry.

### Influence-placement score

Do **not** enumerate all allocations.

Instead define a **marginal one-step score** for adding influence to country (j) given partial allocation (p):

[
u_{\text{place}}(j\mid p)=
\Delta V_{1\text{ step}}(j\mid p)
+\lambda_8 \text{ProtectBG}(j)
+\lambda_9 \text{BreakControl}(j)
+\lambda_{10} \text{GainAccess}(j)
+\lambda_{11} \text{PrepScoring}(j)
-\lambda_{12} \text{OverstackPenalty}(j)
]

Then generate full allocations with a **stochastic beam search**.

## How to generate influence actions

This is the part that actually fixes the huge action space.

For an Ops value (k):

1. Start beam with the empty allocation.
2. Repeatedly spend 1 or 2 Ops according to legality.
3. From each partial allocation, expand only the top (M) countries by (u_{\text{place}}(j\mid p)).
4. Keep the best (B) partial allocations.
5. At the end, deduplicate identical resulting states.
6. Sample one of the final (K) allocations by softmax of total beam score.

So instead of generating thousands of placements, you generate maybe **16–64** serious candidates.

That is the TS-specific equivalent of “sample new child actions during progressive widening,” which later continuous-action MCTS work also uses: the policy is used to sample which new actions are worth adding rather than trying to score the entire action space. 

## How to handle special events

For most event cards with choices, use the same rule:

[
q(x\mid c,\text{event},I)\propto
\exp\Big(\beta_e,[V(T_{c,x}(I))-V(I)+\lambda_{\text{info}}IG(c,x)+\lambda_{\text{rule}}RuleValue(c,x)]\Big)
]

That handles all the “special” cards systematically.

Examples:

* **CIA / Lone Gunman / Cambridge Five / Aldrich / Our Man in Tehran**
  large (IG) term

* **Containment / Brezhnev / Quagmire / Bear Trap / CMC / NORAD / North Sea Oil / Formosan / Shuttle Diplomacy / NATO / Reformer / Yuri / Flower Power**
  large (RuleValue) or (Tempo) term, because their value is not fully visible in immediate board delta

* **Ask Not / Missile Envy / Grain Sales / Wargames**
  sample the internal choices with the same “top-(K) by quick eval + info/tempo” approach rather than full enumeration

## Use the prior in two places

Your heuristic proposal should affect search in **two** places.

First, **which new children get added**.

Second, **how new children are initialized**. A classical prior-knowledge UCT variant does this via a prior estimate (Q_i) and a pseudo-count (n_{\text{prior}}). 

A simple version:

[
N_0(I,a)=n_{\text{prior}},P(I,a),\qquad
W_0(I,a)=N_0(I,a),Q_{\text{prior}}(I,a)
]

with

[
Q_{\text{prior}}(I,a)\approx V(\text{quickApply}(I,a)).
]

That is much better than initializing every new child at zero.

## Very important for ISMCTS

If you are doing ISMCTS rather than plain determinization, actions are effectively available only under the current sampled compatible state. Cowling et al. handle this with **availability counts**: when an action was available for selection in that iteration, its availability is incremented, and that replaces the raw parent-visit count in UCB for the subset-armed-bandit setting. ([White Rose Research Online][1])

So in practice:

* sample a determinization from belief
* restrict proposal generation to actions compatible with it
* use availability-aware statistics

That matters in imperfect-information search.

## A starter recipe that should be decent

I would start with this:

[
K(I)=4+\lfloor 1.5,N(I)^{0.4}\rfloor
]

and at chance / belief-sampling nodes something smaller, like

[
K_z(I)=2+\lfloor N(I)^{0.3}\rfloor.
]

Proposal mixture:

[
q = 0.70,q_{\text{heur}} + 0.20,q_{\text{tactical}} + 0.10,q_{\text{uniform}}
]

where:

* (q_{\text{heur}}): the hierarchical scorer above
* (q_{\text{tactical}}): top coups / top realigns / top scoring-prep placements
* (q_{\text{uniform}}): random legal template then random legal instantiation

That 10% random tail is important. It prevents the policy from completely blinding the search.

For beam generation:

* root: beam width 16, keep 32 final allocations
* interior: beam width 8, keep 12 final allocations

## The main design principle

For TS, you do **not** want “weights over all actions.”

You want:

* a **proposal distribution over action templates and instantiations**
* **progressive widening** to limit how many children exist
* **pseudo-count / prior-value initialization** for new children
* explicit bonuses for **information** and **rule-modifying** event cards

That is the systematic way to make MCTS/ISMCTS work when the action space is huge.

A good next step is to define the exact TypeScript interfaces for:

* `scoreCardUse(card, state, belief)`
* `sampleInfluenceAllocation(cardOps, state, belief)`
* `sampleEventChoice(card, state, belief)`
* `addChildWithPrior(node, action, priorProb, priorValue)`

and wire them into widening.

[1]: https://eprints.whiterose.ac.uk/id/eprint/75048/1/CowlingPowleyWhitehouse2012.pdf "Information Set Monte Carlo Tree Search"

Q:
Write me some pseudocode both for the value function and for the proposal algorithm.

A:
Below is **TypeScript-flavored pseudocode for Twilight Struggle**, written for an **ISMCTS / MCTS engine with huge branching**.

Assumptions:

* all evaluator scores are **USSR-positive**
* `exactRegionScoreIfScoredNow(...)` already exists
* hidden-information terms use a **belief state**, not the sampled determinization, so the search does not leak knowledge into the heuristic
* “special cards” means cards whose value is **not captured just by the board delta**: persistent rule flags, info cards, hand-management cards, cancellation interactions, Wargames, China-transfer cards, and similar

---

## 1. Evaluator pseudocode

```ts
type Side = "US" | "USSR";
type Region =
  | "EUROPE" | "ASIA" | "MIDDLE_EAST"
  | "CENTRAL_AMERICA" | "SOUTH_AMERICA"
  | "AFRICA" | "SE_ASIA";

type GameState = {
  vp: number;                      // USSR-positive VP
  turn: number;
  ar: number;
  defcon: number;
  currentPlayer: Side;
  milOps: Record<Side, number>;
  spaceLevel: Record<Side, number>;
  chinaHolder: Side | null;
  chinaAvailable: boolean;
  activeFlags: Set<CardOrFlag>;
  discardPile: Card[];
  removedPile: Card[];
  handsKnown: {
    US: Set<Card>;                 // known own cards
    USSR: Set<Card>;
  };
  board: BoardState;
};

type BeliefState = {
  probCardLive(card: Card): number;
  probCardInHand(side: Side, card: Card): number;
  probCardBeforeReshuffle(card: Card): number;
  entropyOpponentHand(sideToMove: Side): number;
  expectedHeadlineValue(side: Side): number;
  expectedBestBadCardToCancel(side: Side): number;
  expectedUSCoupsRemaining(): number;
  expectedUSWarCardsRemaining(): number;
  expectedLookaheadDeckValue(side: Side, count: number): number;
};

type EvalWeights = {
  vp: number;
  region: Record<Region, number>;
  bgPressure: number;
  access: number;
  overcontrol: number;
  milOps: number;
  defcon: number;
  space: number;
  china: number;

  opsPerAR: number;
  redScarePerAR: number;
  extraAR: number;
  trapAR: number;
  cmc: number;
  yuri: number;
  lads: number;
  iranContra: number;
  chernobyl: number;
  norad: number;
  salt: number;
  buryYou: number;
  u2: number;
  flowerPower: number;
  formosan: number;
  shuttle: number;
  nato: number;
  usJapan: number;
  reformer: number;
  reformerCoupPenalty: number;
  pairThreat: number;

  info: number;
  discardChoice: number;
  chinaTransfer: number;
  starWars: number;
  askNot: number;
  grainSales: number;
};

const W: EvalWeights = /* tune later */ {} as any;

const SCORING_REGIONS: Region[] = [
  "EUROPE", "ASIA", "MIDDLE_EAST",
  "CENTRAL_AMERICA", "SOUTH_AMERICA",
  "AFRICA", "SE_ASIA"
];
```

### Main evaluator

```ts
function evaluateState(s: GameState, b: BeliefState): number {
  let v = 0.0; // USSR-positive

  // 1) Actual VP
  v += W.vp * s.vp;

  // 2) Exact region-score-if-scored-now, weighted by urgency
  for (const region of SCORING_REGIONS) {
    const urg = scoringUrgency(region, s, b);
    if (urg <= 0) continue;

    const immediateScore = exactRegionScoreIfScoredNow(s, region); // USSR-positive
    v += W.region[region] * urg * immediateScore;
  }

  // 3) Structural board terms
  v += W.bgPressure  * evalBattlegroundPressure(s);
  v += W.access      * evalAccess(s);
  v += W.overcontrol * evalOvercontrol(s);
  v += W.milOps      * evalMilOpsEdge(s);
  v += W.defcon      * evalDefconEdge(s);
  v += W.space       * evalSpaceEdge(s);
  v += W.china       * evalChinaEdge(s, b);

  // 4) Persistent special rules currently active
  v += evalPersistentFlags(s, b);

  // 5) Paired-card/cancel interactions
  v += evalPairThreats(s, b);

  // 6) Known or probabilistic value of special cards in hand
  v += expectedSpecialHandValue(s, b, "USSR");
  v -= expectedSpecialHandValue(s, b, "US");

  return clamp(v, -1000, +1000);
}
```

### Scoring urgency

Use belief, not determinization truth.

```ts
function scoringUrgency(region: Region, s: GameState, b: BeliefState): number {
  const scoringCard = scoringCardForRegion(region);

  if (isCardGoneForever(s, scoringCard)) return 0.0;

  const pNow =
    b.probCardInHand("US", scoringCard) +
    b.probCardInHand("USSR", scoringCard);

  const pSoon = b.probCardBeforeReshuffle(scoringCard);

  // Smooth urgency is better than hard if/else in imperfect info.
  return 0.40 + 0.90 * clamp01(pNow) + 0.20 * clamp01(pSoon);
}
```

### Structural features

These do not need to be perfect on day 1. They need to be consistent.

```ts
function evalBattlegroundPressure(s: GameState): number {
  let total = 0.0;

  for (const c of allCountries()) {
    if (!isBattleground(c)) continue;

    const diff =
      influence(s, "USSR", c) - influence(s, "US", c);

    const local = Math.tanh(diff / stability(c));
    total += regionScale(regionOf(c)) * local;
  }

  return total;
}

function evalAccess(s: GameState): number {
  let total = 0.0;
  for (const c of keyAccessCountries()) {
    const ussrCan = canPlaceInfluenceViaAccess(s, "USSR", c) ? 1 : 0;
    const usCan   = canPlaceInfluenceViaAccess(s, "US", c) ? 1 : 0;
    total += importance(c) * (ussrCan - usCan);
  }
  return total;
}

function evalOvercontrol(s: GameState): number {
  let total = 0.0;
  for (const c of allCountries()) {
    const ussrMargin = controlMargin(s, "USSR", c); // >0 if USSR controls
    const usMargin   = controlMargin(s, "US", c);
    total += countryImportance(c) * (max(0, ussrMargin) - max(0, usMargin));
  }
  return total;
}

function evalMilOpsEdge(s: GameState): number {
  return expectedEndTurnMilOpsScore(s, "USSR") - expectedEndTurnMilOpsScore(s, "US");
}

function evalDefconEdge(s: GameState): number {
  return legalCoupPressure(s, "USSR") - legalCoupPressure(s, "US");
}

function evalSpaceEdge(s: GameState): number {
  return spaceValue(s, "USSR") - spaceValue(s, "US");
}

function evalChinaEdge(s: GameState, b: BeliefState): number {
  let v = 0.0;

  if (s.chinaHolder === "USSR") {
    v += s.chinaAvailable ? 1.00 : 0.45;
  } else if (s.chinaHolder === "US") {
    v -= s.chinaAvailable ? 1.00 : 0.45;
  }

  // Slight extra value if Asia/SE Asia scoring is still live
  v += 0.25 * scoringUrgency("ASIA", s, b) * (s.chinaHolder === "USSR" ? 1 : s.chinaHolder === "US" ? -1 : 0);

  return v;
}
```

---

## 2. Special-card hooks

This is the clean way to “include all specials” without hard-coding them into one giant monolith.

### Persistent rules / active flags

```ts
function evalPersistentFlags(s: GameState, b: BeliefState): number {
  let v = 0.0;

  // Turn / rule modifiers
  if (s.activeFlags.has(CONTAINMENT)) {
    v += -W.opsPerAR * remainingAR(s, "US");
  }
  if (s.activeFlags.has(BREZHNEV_DOCTRINE)) {
    v += +W.opsPerAR * remainingAR(s, "USSR");
  }
  if (s.activeFlags.has(RED_SCARE_US)) {
    v += +W.redScarePerAR * remainingAR(s, "US");
  }
  if (s.activeFlags.has(RED_SCARE_USSR)) {
    v += -W.redScarePerAR * remainingAR(s, "USSR");
  }
  if (s.activeFlags.has(VIETNAM_REVOLTS)) {
    v += 0.20 + 0.20 * scoringUrgency("SE_ASIA", s, b);
  }
  if (s.activeFlags.has(NORTH_SEA_OIL)) {
    v += -W.extraAR;
    v += 0.50 * b.probCardLive(OPEC); // cancel / suppress OPEC threat
  }
  if (s.activeFlags.has(YURI_AND_SAMANTHA)) {
    v += W.yuri * b.expectedUSCoupsRemaining();
  }
  if (s.activeFlags.has(LATIN_AMERICAN_DEATH_SQUADS_US)) {
    v += -W.lads * coupMapValue(s, "US", ["CENTRAL_AMERICA", "SOUTH_AMERICA"]);
  }
  if (s.activeFlags.has(LATIN_AMERICAN_DEATH_SQUADS_USSR)) {
    v += +W.lads * coupMapValue(s, "USSR", ["CENTRAL_AMERICA", "SOUTH_AMERICA"]);
  }
  if (s.activeFlags.has(IRAN_CONTRA_SCANDAL)) {
    v += W.iranContra * realignMapValue(s, "USSR", ["CENTRAL_AMERICA", "SOUTH_AMERICA"]);
  }

  // Chernobyl is really a family of region-specific flags
  for (const region of SCORING_REGIONS) {
    if (s.activeFlags.has(chernobylFlag(region))) {
      v += -W.chernobyl * placementNeed(s, "USSR", region);
    }
  }

  if (s.activeFlags.has(NORAD)) {
    v += -W.norad * expectedNoradTriggers(s);
  }

  // Traps / locks
  if (s.activeFlags.has(QUAGMIRE)) {
    v += +W.trapAR * expectedLostAR(s, "US");
  }
  if (s.activeFlags.has(BEAR_TRAP)) {
    v += -W.trapAR * expectedLostAR(s, "USSR");
  }
  if (s.activeFlags.has(CUBAN_MISSILE_CRISIS_US)) {
    v += +W.cmc * coupNeed(s, "US") - cancelCost(s, "US");
  }
  if (s.activeFlags.has(CUBAN_MISSILE_CRISIS_USSR)) {
    v += -W.cmc * coupNeed(s, "USSR") + cancelCost(s, "USSR");
  }
  if (s.activeFlags.has(NUCLEAR_SUBMARINES)) {
    v += -0.60 * battlegroundCoupValue(s, "US");
  }
  if (s.activeFlags.has(SALT_NEGOTIATIONS)) {
    v += W.salt * (coupNeed(s, "US") - coupNeed(s, "USSR"));
  }
  if (s.activeFlags.has(WE_WILL_BURY_YOU)) {
    v += W.buryYou * (1.0 - probUNInterventionSoon(s, b));
  }
  if (s.activeFlags.has(U2_INCIDENT)) {
    v += W.u2 * probUNInterventionLaterThisTurn(s, b);
  }

  // Scoring / region rule overrides
  if (s.activeFlags.has(FORMOSAN_RESOLUTION)) {
    v += W.formosan * deltaAsiaScoreWithFormosan(s);
  }
  if (s.activeFlags.has(SHUTTLE_DIPLOMACY)) {
    v += W.shuttle * deltaNextAsiaOrMEScoreWithShuttle(s);
  }
  if (s.activeFlags.has(NATO)) {
    v += -W.nato * europeAttackPotential(s, "USSR");
  }
  if (s.activeFlags.has(US_JAPAN_MUTUAL_DEFENSE_PACT)) {
    v += -W.usJapan * countrySwingPotential(s, "USSR", JAPAN);
  }

  // Willy Brandt is canceled by Tear Down This Wall
  if (s.activeFlags.has(WILLY_BRANDT) && !s.activeFlags.has(TEAR_DOWN_THIS_WALL)) {
    v += 0.40 * westGermanyPressureValue(s);
  }

  // The Reformer adds value in Europe but reduces USSR coup options there
  if (s.activeFlags.has(THE_REFORMER)) {
    v += +W.reformer * europePresenceValue(s, "USSR");
    v += -W.reformerCoupPenalty * europeCoupPotential(s, "USSR");
  }

  // Flower Power is canceled by An Evil Empire
  if (s.activeFlags.has(FLOWER_POWER) && !s.activeFlags.has(AN_EVIL_EMPIRE)) {
    v += W.flowerPower * b.expectedUSWarCardsRemaining();
  }

  return v;
}
```

### Paired-card threats

```ts
function evalPairThreats(s: GameState, b: BeliefState): number {
  let v = 0.0;

  if (s.activeFlags.has(CAMP_DAVID_ACCORDS)) {
    v += -W.pairThreat * b.probCardLive(ARAB_ISRAELI_WAR) * abs(eventSwingEstimate(s, ARAB_ISRAELI_WAR));
  }
  if (s.activeFlags.has(JOHN_PAUL_II_ELECTED_POPE)) {
    v += -W.pairThreat * b.probCardLive(SOLIDARITY) * abs(eventSwingEstimate(s, SOLIDARITY));
  }
  if (s.activeFlags.has(IRANIAN_HOSTAGE_CRISIS)) {
    v += +0.40 * b.probCardLive(TERRORISM) * abs(eventSwingEstimate(s, TERRORISM));
  }
  if (s.activeFlags.has(THE_IRON_LADY)) {
    v += -0.30 * b.probCardLive(SOCIALIST_GOVERNMENTS) * abs(eventSwingEstimate(s, SOCIALIST_GOVERNMENTS));
  }
  if (s.activeFlags.has(AWACS_SALE_TO_SAUDIS)) {
    v += -0.40 * b.probCardLive(MUSLIM_REVOLUTION) * abs(eventSwingEstimate(s, MUSLIM_REVOLUTION));
  }

  return v;
}
```

### Special cards in hand

```ts
const SPECIAL_HAND_CARDS: Card[] = [
  WARGAMES, MISSILE_ENVY, DEFECTORS, UN_INTERVENTION,
  CIA_CREATED, LONE_GUNMAN, ALDRICH_AMES_REMIX, CAMBRIDGE_FIVE, OUR_MAN_IN_TEHRAN,
  STAR_WARS, ASK_NOT, GRAIN_SALES_TO_SOVIETS,
  CULTURAL_REVOLUTION, NIXON_PLAYS_THE_CHINA_CARD, USSURI_RIVER_SKIRMISH
];

function expectedSpecialHandValue(s: GameState, b: BeliefState, side: Side): number {
  let v = 0.0;

  for (const card of SPECIAL_HAND_CARDS) {
    const p = probSideHasCard(side, card, s, b);
    if (p <= 0) continue;
    v += p * evalSpecialCardInHand(card, s, b, side);
  }

  return v;
}

function evalSpecialCardInHand(card: Card, s: GameState, b: BeliefState, side: Side): number {
  switch (card) {
    case WARGAMES:
      return canLegallyWinWithWargames(s, side) ? 100000 : 0;

    case MISSILE_ENVY:
      return 0.40 + 0.50 * (expectedHighestOpsCardOfOpponent(s, b, side) - 2);

    case DEFECTORS:
      return isHeadlinePhase(s) ? 0.80 * b.expectedHeadlineValue(opponent(side)) : 0.10;

    case UN_INTERVENTION:
      return 0.80 * b.expectedBestBadCardToCancel(side);

    case CIA_CREATED:
    case LONE_GUNMAN:
      return W.info * expectedInfoGain(card, s, b, side);

    case ALDRICH_AMES_REMIX:
      return W.info * expectedInfoGain(card, s, b, side)
           + W.discardChoice * expectedTargetedDiscardValue(s, b, side);

    case CAMBRIDGE_FIVE:
      return W.info * expectedScoringInfoGain(s, b, side);

    case OUR_MAN_IN_TEHRAN:
      return W.info * b.expectedLookaheadDeckValue(side, 5);

    case STAR_WARS:
      return W.starWars * bestSpaceEligibleDiscardEventValue(s, side);

    case ASK_NOT:
      return W.askNot * bestDiscardSubsetValue(s, side);

    case GRAIN_SALES_TO_SOVIETS:
      return W.grainSales * expectedRandomCardGainValue(s, b, side);

    case CULTURAL_REVOLUTION:
    case NIXON_PLAYS_THE_CHINA_CARD:
    case USSURI_RIVER_SKIRMISH:
      return W.chinaTransfer * expectedChinaSwing(s, side);

    default:
      return 0.0;
  }
}
```

---

## 3. Proposal policy for search

The action space is too large to enumerate directly, so generate **small materialized candidate sets** hierarchically:

1. choose top cards
2. choose best mode for each card
3. materialize a small number of concrete actions
4. normalize scores into priors
5. let PUCT / UCT operate over those materialized children only

### Types

```ts
type ModeKind = "EVENT" | "OPS" | "SPACE";

type Template =
  | "COUP_BG"
  | "COUP_NONBG_MILOPS"
  | "REALIGN_LINCHPIN"
  | "DEFEND_CONTROL"
  | "BREAK_CONTROL"
  | "GAIN_ACCESS"
  | "PREP_SCORING"
  | "OVERPROTECT_BG";

type ModeCandidate = {
  kind: ModeKind;
  template?: Template;
  score: number;
  legal: boolean;
};

type CandidateAction = {
  action: Action;
  score: number;   // proposal score before normalization
  prior: number;   // normalized softmax prior
  q0: number;      // quick initial value estimate
};

const CARD_K = 5;
const MODE_K = 2;
const MAX_CHILD_CANDS = 12;
const COUP_K = 4;
const REALIGN_K = 4;
const EVENT_K = 4;
const INF_FINAL_K = 6;
```

### Main candidate generator

```ts
function proposeActionCandidates(
  det: GameState,      // sampled determinization for legality
  belief: BeliefState, // belief for info value and no-leak scoring
  side: Side
): CandidateAction[] {
  const legalCards = legalPlayableCards(det, side);

  const cardScored = legalCards.map(card => {
    const eventMode = estimateBestEventMode(card, det, belief, side);
    const opsMode   = estimateBestOpsMode(card, det, belief, side);
    const spaceMode = estimateSpaceMode(card, det, belief, side);

    return {
      card,
      modes: [eventMode, opsMode, spaceMode],
      score: max(eventMode.score, opsMode.score, spaceMode.score)
    };
  });

  const topCards = topK(cardScored, CARD_K, x => x.score);

  let candidates: CandidateAction[] = [];

  for (const cardInfo of topCards) {
    const topModes = topK(
      cardInfo.modes.filter(m => m.legal),
      MODE_K,
      m => m.score
    );

    for (const mode of topModes) {
      switch (mode.kind) {
        case "EVENT":
          candidates.push(...generateEventCandidates(cardInfo.card, det, belief, side));
          break;

        case "SPACE":
          candidates.push(makeSpaceCandidate(cardInfo.card, det, belief, side));
          break;

        case "OPS":
          candidates.push(...generateOpsCandidates(cardInfo.card, mode.template!, det, belief, side));
          break;
      }
    }
  }

  candidates = dedupCandidates(candidates);
  attachPriorsAndQ0(candidates, det, belief);
  return topK(candidates, MAX_CHILD_CANDS, c => c.score);
}
```

---

## 4. Scoring cards and modes

### Event mode

```ts
function estimateBestEventMode(card: Card, det: GameState, belief: BeliefState, side: Side): ModeCandidate {
  if (!canPlayEvent(card, det, side)) {
    return { kind: "EVENT", legal: false, score: -Infinity };
  }

  const choices = generateEventChoices(card, det, belief, side);
  if (choices.length === 0) {
    return { kind: "EVENT", legal: false, score: -Infinity };
  }

  let best = -Infinity;

  for (const choice of choices) {
    const score = scoreEventChoice(card, choice, det, belief, side);
    best = Math.max(best, score);
  }

  return { kind: "EVENT", legal: true, score: best };
}
```

### Ops mode

```ts
function estimateBestOpsMode(card: Card, det: GameState, belief: BeliefState, side: Side): ModeCandidate {
  if (!canPlayOps(card, det, side)) {
    return { kind: "OPS", legal: false, score: -Infinity };
  }

  const templates: ModeCandidate[] = [];

  if (existsLegalCoup(det, side)) {
    templates.push({
      kind: "OPS",
      template: "COUP_BG",
      legal: true,
      score: bestCoupScore(card, det, belief, side, true)
    });

    templates.push({
      kind: "OPS",
      template: "COUP_NONBG_MILOPS",
      legal: true,
      score: bestCoupScore(card, det, belief, side, false)
    });
  }

  if (existsLegalRealignment(det, side)) {
    templates.push({
      kind: "OPS",
      template: "REALIGN_LINCHPIN",
      legal: true,
      score: bestRealignScore(card, det, belief, side)
    });
  }

  // Influence templates
  templates.push({
    kind: "OPS",
    template: "DEFEND_CONTROL",
    legal: true,
    score: estimatePlacementTemplate(card, det, belief, side, "DEFEND_CONTROL")
  });
  templates.push({
    kind: "OPS",
    template: "BREAK_CONTROL",
    legal: true,
    score: estimatePlacementTemplate(card, det, belief, side, "BREAK_CONTROL")
  });
  templates.push({
    kind: "OPS",
    template: "GAIN_ACCESS",
    legal: true,
    score: estimatePlacementTemplate(card, det, belief, side, "GAIN_ACCESS")
  });
  templates.push({
    kind: "OPS",
    template: "PREP_SCORING",
    legal: true,
    score: estimatePlacementTemplate(card, det, belief, side, "PREP_SCORING")
  });
  templates.push({
    kind: "OPS",
    template: "OVERPROTECT_BG",
    legal: true,
    score: estimatePlacementTemplate(card, det, belief, side, "OVERPROTECT_BG")
  });

  return argmax(templates, x => x.score);
}
```

### Space mode

```ts
function estimateSpaceMode(card: Card, det: GameState, belief: BeliefState, side: Side): ModeCandidate {
  if (!canSpace(card, det, side)) {
    return { kind: "SPACE", legal: false, score: -Infinity };
  }

  const toxicEventPenalty = opponentEventPenaltyIfPlayedNormally(card, det, belief, side);
  const spaceGain = expectedSpaceAdvanceValue(det, side);

  return {
    kind: "SPACE",
    legal: true,
    score: spaceGain + toxicEventPenalty
  };
}
```

---

## 5. Event choices

For cards with choices, do not enumerate everything blindly. Generate only meaningful choices.

```ts
function generateEventChoices(card: Card, det: GameState, belief: BeliefState, side: Side): EventChoice[] {
  switch (card) {
    case CHERNOBYL:
      return SCORING_REGIONS.map(region => ({ type: "CHERNOBYL_REGION", region }));

    case STAR_WARS:
      return eligibleSpaceEventsInDiscard(det, side)
        .map(eventCard => ({ type: "STAR_WARS_PICK", eventCard }));

    case UN_INTERVENTION:
      return cancellableOpponentCardsInOwnHand(det, side)
        .map(targetCard => ({ type: "UN_CANCEL", targetCard }));

    case ASK_NOT:
      return generateBadCardDiscardSubsets(det, side); // small beam search over subsets

    case OUR_MAN_IN_TEHRAN:
      return generateTehranLookaheadChoices(det, belief, side); // discard/keep options if you model them

    case WARGAMES:
      return canLegallyWinWithWargames(det, side) ? [{ type: "FIRE_WARGAMES" }] : [];

    default:
      return [{ type: "NO_CHOICE" }];
  }
}
```

### Event scoring

```ts
function scoreEventChoice(
  card: Card,
  choice: EventChoice,
  det: GameState,
  belief: BeliefState,
  side: Side
): number {
  const baseEval = evaluateState(det, belief);

  // Apply event approximately or exactly if cheap
  const det2 = applyEventApprox(det, card, choice, side);

  const boardDelta = evaluateState(det2, belief) - baseEval;
  const infoDelta  = informationGain(card, choice, belief, side);
  const tempoDelta = tempoValue(card, choice, det, side);
  const ruleDelta  = residualRuleValue(card, choice, det, belief, side);

  // For random events, replace boardDelta by average over 2-4 small samples if needed.
  return boardDelta + 0.8 * infoDelta + 0.5 * tempoDelta + ruleDelta;
}
```

---

## 6. Ops candidates

### Coups

```ts
function generateOpsCandidates(
  card: Card,
  template: Template,
  det: GameState,
  belief: BeliefState,
  side: Side
): CandidateAction[] {
  switch (template) {
    case "COUP_BG":
      return topK(
        legalCoupTargets(det, side, true).map(country => makeCoupCandidate(card, country, det, belief, side)),
        COUP_K,
        c => c.score
      );

    case "COUP_NONBG_MILOPS":
      return topK(
        legalCoupTargets(det, side, false).map(country => makeCoupCandidate(card, country, det, belief, side)),
        COUP_K,
        c => c.score
      );

    case "REALIGN_LINCHPIN":
      return sampleRealignmentPlans(card, det, belief, side);

    default:
      return sampleInfluenceAllocations(card, template, det, belief, side);
  }
}

function makeCoupCandidate(
  card: Card,
  country: Country,
  det: GameState,
  belief: BeliefState,
  side: Side
): CandidateAction {
  const action = playCardForCoup(card, country);

  const det2 = quickApplyApprox(det, action, side);
  const score =
    (evaluateState(det2, belief) - evaluateState(det, belief))
    + 0.35 * milOpsImmediateGain(det, side, country)
    + 0.25 * defconPressureGain(det, side, country)
    + 0.25 * accessSwing(det, side, country);

  return { action, score, prior: 0, q0: 0 };
}
```

### Realignments

```ts
function sampleRealignmentPlans(
  card: Card,
  det: GameState,
  belief: BeliefState,
  side: Side
): CandidateAction[] {
  const ops = effectiveOps(card, det, side);

  type Partial = {
    plan: Country[];
    temp: GameState;
    remaining: number;
    score: number;
  };

  let beam: Partial[] = [{
    plan: [],
    temp: det,
    remaining: ops,
    score: 0
  }];

  const BEAM_W = 6;
  const EXPAND_K = 4;

  while (beam.some(x => x.remaining > 0)) {
    let next: Partial[] = [];

    for (const p of beam) {
      if (p.remaining <= 0) {
        next.push(p);
        continue;
      }

      const targets = topK(
        legalRealignTargets(p.temp, side).map(country => ({
          country,
          score: scoreRealignTarget(country, p.temp, belief, side)
        })),
        EXPAND_K,
        x => x.score
      );

      if (targets.length === 0) {
        next.push(p);
        continue;
      }

      for (const t of targets) {
        const action = realignOnceAction(card, t.country);
        const temp2 = quickApplyApprox(p.temp, action, side);

        next.push({
          plan: [...p.plan, t.country],
          temp: temp2,
          remaining: p.remaining - 1,
          score: p.score + t.score
        });
      }
    }

    beam = keepTopB(next, BEAM_W, x => x.score);
  }

  return topK(
    beam.map(p => ({
      action: playCardForRealignmentPlan(card, p.plan),
      score: p.score,
      prior: 0,
      q0: 0
    })),
    REALIGN_K,
    x => x.score
  );
}

function scoreRealignTarget(country: Country, det: GameState, belief: BeliefState, side: Side): number {
  const action = realignOnceAction(DUMMY_CARD, country);
  const det2 = quickApplyApprox(det, action, side);

  return (evaluateState(det2, belief) - evaluateState(det, belief))
    + 0.30 * repeatability(country, det, side)
    + 0.20 * adjacencyEdge(country, det, side)
    + 0.20 * controlFragility(country, det);
}
```

### Influence placements: beam search

This is the part that controls the explosion.

```ts
function sampleInfluenceAllocations(
  card: Card,
  template: Template,
  det: GameState,
  belief: BeliefState,
  side: Side
): CandidateAction[] {
  const ops = effectiveOps(card, det, side);

  type PartialAlloc = {
    alloc: Map<Country, number>;
    remaining: number;
    score: number;
  };

  let beam: PartialAlloc[] = [{
    alloc: new Map(),
    remaining: ops,
    score: 0
  }];

  const BEAM_W = isRootContext() ? 16 : 8;
  const EXPAND_K = 6;

  while (beam.some(x => x.remaining > 0)) {
    let next: PartialAlloc[] = [];
    let expanded = false;

    for (const p of beam) {
      if (p.remaining <= 0) {
        next.push(p);
        continue;
      }

      const countries = topKEligiblePlacementCountries(
        p.alloc, template, det, belief, side, EXPAND_K
      );

      if (countries.length === 0) {
        next.push(p);
        continue;
      }

      expanded = true;

      for (const country of countries) {
        const cost = placementCost(side, country, det, p.alloc);
        if (cost > p.remaining) continue;

        const alloc2 = cloneMap(p.alloc);
        alloc2.set(country, (alloc2.get(country) ?? 0) + 1);

        const delta = marginalPlacementScore(
          country, p.alloc, template, det, belief, side
        );

        next.push({
          alloc: alloc2,
          remaining: p.remaining - cost,
          score: p.score + delta
        });
      }
    }

    beam = keepTopB(dedupAllocs(next), BEAM_W, x => x.score);

    if (!expanded) break;
  }

  // Rescore complete allocations by quick whole-action eval
  const finals = beam.map(p => {
    const action = playCardForInfluence(card, p.alloc);
    const det2 = quickApplyApprox(det, action, side);
    return {
      action,
      score: p.score + (evaluateState(det2, belief) - evaluateState(det, belief)),
      prior: 0,
      q0: 0
    };
  });

  return topK(finals, INF_FINAL_K, x => x.score);
}

function topKEligiblePlacementCountries(
  partialAlloc: Map<Country, number>,
  template: Template,
  det: GameState,
  belief: BeliefState,
  side: Side,
  k: number
): Country[] {
  const scored = legalPlacementCountries(det, side, partialAlloc).map(country => ({
    country,
    score: marginalPlacementScore(country, partialAlloc, template, det, belief, side)
  }));

  return topK(scored, k, x => x.score).map(x => x.country);
}

function marginalPlacementScore(
  country: Country,
  partialAlloc: Map<Country, number>,
  template: Template,
  det: GameState,
  belief: BeliefState,
  side: Side
): number {
  const localDelta = oneStepPlacementDelta(country, det, partialAlloc, belief, side);

  const protectBG   = isBattleground(country) ? protectBattlegroundGain(country, det, partialAlloc, side) : 0;
  const breakCtrl   = breakControlGain(country, det, partialAlloc, side);
  const accessGain  = accessGainFromPlacement(country, det, partialAlloc, side);
  const scoringPrep = scoringPrepGain(country, det, partialAlloc, belief, side);
  const overstack   = overstackPenalty(country, det, partialAlloc, side);

  let templateBonus = 0.0;
  switch (template) {
    case "DEFEND_CONTROL":  templateBonus = 0.50 * defendControlSignal(country, det, side); break;
    case "BREAK_CONTROL":   templateBonus = 0.50 * attackControlSignal(country, det, side); break;
    case "GAIN_ACCESS":     templateBonus = 0.50 * accessGain; break;
    case "PREP_SCORING":    templateBonus = 0.50 * scoringPrep; break;
    case "OVERPROTECT_BG":  templateBonus = 0.50 * protectBG; break;
  }

  return localDelta
       + 0.35 * protectBG
       + 0.30 * breakCtrl
       + 0.25 * accessGain
       + 0.30 * scoringPrep
       - 0.20 * overstack
       + templateBonus;
}
```

---

## 7. Priors and initial child values

```ts
function attachPriorsAndQ0(
  candidates: CandidateAction[],
  det: GameState,
  belief: BeliefState
): void {
  const logits = candidates.map(c => c.score);
  const probs = softmax(logits, 1.0);

  for (let i = 0; i < candidates.length; i++) {
    candidates[i].prior = probs[i];

    const det2 = quickApplyApprox(det, candidates[i].action, det.currentPlayer);
    candidates[i].q0 = evaluateState(det2, belief);
  }
}
```

---

## 8. Progressive widening hook

This is how the proposal policy enters the tree.

```ts
function maybeExpandOrSelect(node: SearchNode, det: GameState, belief: BeliefState): SearchNode {
  const limit = 4 + Math.floor(1.5 * Math.pow(node.visits, 0.40));

  if (node.children.size < limit) {
    const cands = proposeActionCandidates(det, belief, det.currentPlayer);

    for (const cand of cands) {
      if (!node.children.has(actionKey(cand.action))) {
        const child = addChild(node, cand.action);

        // Prior initialization
        child.prior = cand.prior;
        child.visits = cand.prior * 1.0;   // pseudo-count if desired
        child.valueSum = child.visits * cand.q0;

        return child;
      }
    }
  }

  return selectByPUCT(node);
}
```

For ISMCTS, if you already track **availability counts**, use those in your UCB/PUCT denominator instead of raw parent visits.

---

## 9. What to implement first

Implement these first, in this order:

```ts
evaluateState()
exactRegionScoreIfScoredNow()
evalPersistentFlags()
expectedSpecialHandValue()

proposeActionCandidates()
scoreEventChoice()
sampleInfluenceAllocations()
maybeExpandOrSelect()
```

Then optimize only after it works:

* cache `evaluateState`
* make `quickApplyApprox` incremental
* precompute country adjacency / access / battleground masks
* use small sample averages for random events instead of exact expectation

The main design choice is this:

* **value function** = exact scoring + structural board terms + rule/info special hooks
* **proposal policy** = card → mode → template → concrete action
* **search** = progressive widening over only a small materialized action set

That combination is usually much stronger than trying to score every legal TS action flat.
