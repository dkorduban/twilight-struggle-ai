Q:
the goal is not learning per se, but using offpolicy PG as a proxy for architecture evaluation on fixed dataset generated from current best models, for faster evals. because onpolicy training is expensive (rollouts)

A:
Yes — for **that** goal, I would **not** use “off-policy PG” in the usual online-RL sense.

I would use a **fixed-dataset, one-step weighted imitation objective** as the proxy. In practice that means **AWR-style / advantage-weighted BC first**, then **CRR or IQL** if the dataset is too noisy or too sparse-reward for vanilla AWR. The reason is that AWR is explicitly designed as a simple off-policy method built from supervised losses, supports **discrete actions**, and is easy to implement; later analysis of one-step methods argues they are especially attractive when strong regularization matters, even if they may have a lower asymptotic ceiling than heavier critic-regularized methods. That tradeoff is actually good for your use case, because you care about **stable architecture ranking**, not squeezing out the last Elo. ([arXiv][1])

My ranking for **“fixed dataset as a fast proxy for TS policy architecture evaluation”** would be:

1. **Fixed-target AWR / advantage-weighted behavioral cloning**
2. **CRR**
3. **IQL**
4. **AWAC**
5. **CQL**
6. **IMPALA / APPO / ACER / Reactor** for this specific proxy use case

That ranking is different from “best offline RL algorithm overall.” It is about **lowest tuning + highest chance of producing a useful rank-order over architectures**. AWR/CRR are near the top because they reduce learning largely to **weighted regression on dataset actions**, while IQL is stronger when you need more real offline-RL credit assignment, and CQL is usually more pessimistic and algorithmically heavier. IMPALA/APPO/ACER are mainly the wrong tool here because they are built for online actor-learner training rather than static-dataset model selection. ([arXiv][1])

The biggest practical distinction is this:

* If your dataset contains **good teacher information per state** — for example search visit counts, teacher logits, action rankings, teacher value estimates, or even a decent proxy advantage — then **AWR-style weighted BC is the best default**.
* If your dataset is mostly just **raw trajectories with delayed returns**, then **IQL or CRR** become more attractive, because they use a learned critic to recover more signal from the fixed data. IQL is especially relevant because it was designed to avoid evaluating unseen actions outside the dataset, and then extracts the policy with **advantage-weighted behavioral cloning**. ([arXiv][1])

There is also an important data-quality point. A 2022 paper asked when offline RL should beat plain BC and found that offline RL has a clearer edge under conditions like **sparse rewards** or **noisy/suboptimal data**; when the data is already demonstration-like, BC is the natural baseline. Since your data comes from your **current best models**, it is likely much closer to “good demonstrations” than to random exploration, which pushes the proxy even more toward **AWR/weighted BC** rather than heavy offline RL. ([arXiv][2])

So my actual recommendation would be:

**Best default proxy:**
Train each candidate architecture on the **same frozen dataset** with

[
L_{\pi} = - \mathbb{E}*{(s,a)\sim D}\left[w(s,a)\log \pi*\theta(a\mid s)\right]
]

where (w(s,a)) is one of:

* **search-derived** weight, such as normalized visit counts, teacher action score, or clipped ( \exp(A/\beta) )
* **critic-derived** weight from a **shared frozen critic**
* a simpler **rank-based** weight if your teacher only gives action ordering

For TS, that is attractive because it only needs the model to place probability mass on the **logged legal action**, so it works naturally with a huge factorized/combinatorial action space and does **not** require enumerating all actions. The key extra recommendation is to keep the **advantage source fixed across architectures**. Otherwise, if each architecture trains its own critic, you are partly measuring “which critic got luckier/easier to optimize” rather than “which policy trunk/head is better.” The idea of preferring one-step weighted imitation here is my inference from the method properties and your evaluation goal, rather than a claim made verbatim by one paper. ([arXiv][1])

For **secondary evaluation**, I would add **offline policy evaluation**, but only as a second opinion. The offline-RL literature repeatedly treats OPE as the standard way to select among candidate policies on fixed data, but also notes that it is hard: importance-sampling methods can have very high variance, while FQE/model-based methods bring their own modeling choices and hyperparameters. There is active recent work specifically on **model selection for OPE itself**, which tells you this remains a real problem. So I would use **bootstrap FQE on a held-out split** as a noisy auxiliary score, not as the sole arbiter. ([arXiv][3])

So the compressed answer is:

* **Yes, AWR becomes much more relevant in your setting.**
* For a **fixed-dataset architecture proxy**, I would usually prefer
  **AWR / weighted BC > CRR > IQL > AWAC > CQL**.
* If you can log **teacher/search advantages**, **AWR is probably the best default**.
* If you only have **trajectory returns** and the signal is sparse/noisy, **CRR or IQL** are safer than vanilla AWR.
* I would avoid using online-style off-policy actor-critic methods as the proxy at all.

A good practical recipe for TS is: **fixed dataset + frozen teacher weights/advantages + weighted imitation training + held-out weighted NLL/top-k metrics + optional bootstrap FQE + occasional tiny online audit to calibrate rank correlation**.

[1]: https://arxiv.org/abs/1910.00177?utm_source=chatgpt.com "Advantage-Weighted Regression: Simple and Scalable Off-Policy Reinforcement Learning"
[2]: https://arxiv.org/abs/2204.05618?utm_source=chatgpt.com "When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?"
[3]: https://arxiv.org/abs/1911.06854?utm_source=chatgpt.com "Empirical Study of Off-Policy Policy Evaluation for Reinforcement Learning"

Q:
one can argue returns are very delayed in TS?

A:
Yes — **absolutely**, but with an important nuance:

TS returns are **delayed enough to be a problem for naive return-weighted training**, but **not so delayed that there is no usable local signal**.

A good way to say it is:

* **Terminal reward is very delayed and very noisy**
* **Strategic reward is delayed**
* **Tactical reward is often immediate or short-horizon**

Why TS is delayed in the RL sense:

1. **Many good moves cash out much later**
   A placement now may matter only when:

   * a scoring card appears later,
   * a battleground flips after several ARs,
   * DEFCON / coup timing changes later,
   * an opponent is denied a line several turns from now,
   * final scoring matters.

2. **The same move can have very different final returns depending on hidden hand / future draws**
   So terminal outcome is a noisy label for the early action.

3. **Episode length is long enough for credit smearing**
   Even if TS is not huge by RTS standards, there are enough sequential decisions that “won the game” is a poor learning target for many earlier actions.

So if by “returns” you mean **episode return / winner**, then yes, TS is quite delayed.

But TS is **not purely sparse**. There is a lot of medium-horizon signal:

* immediate VP swings,
* regional position improvement,
* access / adjacency gains,
* threat creation,
* opponent constraint,
* military ops / DEFCON tempo,
* hand management consequences,
* survival / prevention of catastrophe.

That matters because for your **fixed-dataset architecture proxy**, the right conclusion is not “AWR is impossible,” but rather:

## What fails

**AWR with raw Monte Carlo return as the weight** is likely pretty bad.

Why:

* early actions in a game all inherit roughly the same final return,
* that return reflects many later decisions and hidden information,
* architecture ranking may then reflect noise more than true model quality.

So this kind of weight is weak:

[
w_t = \exp(G_t / \beta)
]

if (G_t) is mostly terminal outcome or long-horizon return.

## What is still good

**AWR-style weighted imitation is still good if the weight is better than raw return.**

For TS, better weights are:

1. **Teacher/search policy targets**
   visit counts, teacher logits, chosen-action margin

2. **Teacher value deltas**
   [
   A(s,a) \approx Q_{\text{teacher}}(s,a) - V_{\text{teacher}}(s)
   ]

3. **n-step bootstrapped advantages**
   not full-episode return, but short/medium horizon plus value bootstrap

4. **Event-local or decision-local scores**
   especially for combinatorial subdecisions like placement/removal

So the answer is:

* **Yes, TS is delayed enough that raw-return AWR is suspect**
* **No, TS is not so delayed that weighted imitation is useless**
* **You just need the weights to come from teacher/search/value estimates, not from episode outcome alone**

For your proxy-eval use case, I would phrase it even more strongly:

> In TS, “returns are delayed” is an argument **against using terminal-return-weighted offline PG as the proxy**, not against using **AWR-style weighted imitation with better local targets**.

So the proxy stack I would trust most is:

1. frozen dataset from current best policies/search
2. fixed teacher-derived local weights or action rankings
3. train candidate architectures with weighted NLL / weighted BC
4. compare on held-out weighted NLL, top-k teacher agreement, calibration, and maybe small-sample online audit

If you want, I can give a concrete TS-specific weighting recipe, from simplest to strongest, for your logged dataset format.

Q:
yes plz

A:
Yes. For **your exact use case** — fixed dataset from current best TS models, used as a **cheap architecture-ranking proxy** — I would treat this as **weighted imitation first**, and only then as offline RL. AWR is explicitly a simple off-policy method built from weighted supervised regression and supports discrete actions; CRR reframes policy learning as copying **dataset actions** with binary or exponential filtering; IQL goes further with multi-step value learning and then still extracts the policy with **advantage-weighted behavioral cloning**. CRR also explicitly warns that K-step or episodic-return-based advantage estimates can be problematic in offline settings. ([arXiv][1])

Here is the TS-specific ladder I would use, from **simplest** to **strongest**.

## First: what each logged TS decision should store

At each decision point, store:

* observation / info state
* legal action mask or legal candidate list
* chosen action
* decision type (`card`, `event mode`, `coup target`, `realignment target`, `placement bundle`, `removal bundle`, etc.)
* teacher policy info if available: visit counts, logits, or at least chosen-action score
* teacher value info if available: (V(s)), (Q(s,a)), or a short-horizon bootstrapped delta
* for multi-step/combinatorial actions, the **whole macro action** and its tokenization

That last point matters a lot in TS: a 4-ops placement should not get 4x the importance of a one-click decision just because it has more tokens. My recommendation is to compute a **single macro weight** and multiply it by the **average** token NLL over the decomposition.

[
L_{\text{macro}} ;=; -, w(s,a);\frac{1}{K}\sum_{i=1}^{K}\log \pi_\theta(t_i \mid s, t_{<i})
]

That formula is my recommendation for TS-style factorized policies.

## 1. Uniform BC baseline

Start with plain supervised cloning:

[
L_{\pi} = -\log \pi_\theta(a^* \mid s)
]

This is your floor. For architecture ranking, it is often surprisingly useful when the dataset is already near-demonstration quality. The offline-RL literature explicitly treats BC as the natural baseline when data resembles demonstrations, and highlights that offline RL tends to shine more under conditions like sparse rewards, noisy/suboptimal data, and long-horizon stitching. 

Use this baseline to answer one simple question: “Does the new architecture even model strong TS decisions better than the old one on frozen data?”

## 2. Teacher-policy distillation

If your generator can log **visit counts** or **teacher probabilities** over legal actions, this is usually the best cheap proxy.

[
L_{\text{distill}} ;=; - \sum_{a \in \mathcal{A}*{\text{legal}}(s)} p_T(a\mid s),\log \pi*\theta(a\mid s)
]

For TS, this is especially good for:

* card play choice
* event-vs-ops mode
* coup / realignment / war target
* headline choice
* any subdecision where the teacher can expose a legal-action distribution

For placement/removal bundles, either distill the full macro distribution if you have it, or distill each factor with the same macro weight. This is still my recommendation rather than a direct paper prescription.

If you have this data, I would often rank architectures by:

* held-out KL / cross-entropy to teacher
* top-1 agreement
* top-k teacher mass captured

This is often a **better proxy than raw BC** because it preserves teacher uncertainty instead of pretending one logged choice was uniquely correct.

## 3. AWR-lite: weighted BC with **local** advantage

This is the first thing I would call the real default.

Use:

[
L_{\pi} ;=; -,w(s,a^*)\log \pi_\theta(a^*\mid s),
\qquad
w(s,a^*) ;=; \min!\left(w_{\max}, \exp!\left(\frac{A_T(s,a^*)}{\beta}\right)\right)
]

AWR is built around weighted target actions, and IQL’s policy extraction is advantage-weighted BC; the official IQL implementation computes a clipped exponential weight from (Q-V) and multiplies it by the logged-action log-probability. ([arXiv][1])

For TS, the important part is **how you define (A_T)**. Do **not** use raw game outcome. TS returns are too delayed and too noisy for that. CRR explicitly argues that return-based advantage estimation can be problematic in offline settings. ([ar5iv][2])

Use one of these instead:

### 3a. Best case: search Q-values available

[
A_T(s,a) = Q_T(s,a) - \sum_b p_T(b\mid s),Q_T(s,b)
]

This is the cleanest version.

### 3b. Only visit counts available

A good TS proxy is:

[
A_T(s,a) = \log(N(s,a)+1) - \sum_b p_T(b\mid s)\log(N(s,b)+1)
]

Not theoretically pure, but very practical.

### 3c. Only chosen action + value before/after available

Use a bootstrapped local delta:

[
A_T(s,a^*) \approx r_{\text{local}} + \gamma^n V_T(s_{t+n}) - V_T(s_t)
]

Here (r_{\text{local}}) in TS can include immediate VP swing, DEFCON catastrophe avoidance, forced-scoring gain/loss, or other short-horizon tactical rewards. That part is my adaptation for TS.

For your proxy-eval goal, this is the one I would try first.

## 4. CRR-lite: filter out weak examples instead of softly weighting everything

CRR’s main idea is to copy **only dataset actions that look better than the current policy value baseline**, using either a **binary** filter or an **exponential** weight. The paper explicitly describes this as BC on a filtered dataset, and discusses when binary filtering can outperform exponential weighting by being more aggressive. ([ar5iv][2])

TS version:

[
w(s,a^*) = \mathbf{1}[A_T(s,a^*) > \delta]
]

or, more robustly, keep only the top (q%) of examples **within each decision type**.

I would use this when:

* your frozen dataset mixes stronger and weaker generator snapshots
* value estimates are noisy
* you want the proxy to focus on “clearly good” moves only

In TS, that often helps because many logged moves are merely acceptable, not architecture-discriminating.

A good recipe is:

* start with AWR-lite
* if rank-order is noisy, switch to CRR-lite filtering
* compare both correlations with a tiny online audit

## 5. IQL-lite: strongest proxy, but less “pure” for architecture ranking

IQL learns a value function via **expectile regression** over in-dataset actions, then backs up a Q-function without querying unseen actions, then extracts the policy with advantage-weighted BC. The paper emphasizes that it avoids querying out-of-sample actions during value learning, and uses weighted behavioral cloning for policy extraction. The official implementation uses clipped exponential weighting from (Q-V). ([ar5iv][3])

TS version:

1. Learn (V(s)) from dataset actions using an upper expectile objective.
2. Learn (Q(s,a_{\text{logged}})) with SARSA-style / bootstrapped targets using (V(s')).
3. Extract policy with:

[
w(s,a^*) = \min!\left(100,\exp((Q(s,a^*) - V(s))\cdot T)\right)
]

[
L_\pi = -,w(s,a^*)\log \pi_\theta(a^* \mid s)
]

That weight formula is from the official IQL code. ([GitHub][4])

This is the **strongest** proxy in the list if your dataset really requires long-horizon stitching. But it is also less clean for architecture comparison, because now your ranking depends on:

* the policy architecture
* the critic quality
* the interaction between them

So I would use IQL-lite as a **secondary proxy**, not the first one.

## My actual recommendation order for TS

For your setup, I would run:

1. **Uniform BC** as the sanity floor
2. **Teacher distillation** if you have visit distributions
3. **AWR-lite with teacher-local advantages** as the main proxy
4. **CRR-lite binary filter** as a robustness check
5. **IQL-lite** only for shortlisted architectures

That ordering matches your goal better than “best offline RL overall.”

## The single most important TS-specific rule

For TS, **never weight by final game result alone**.

Use weights from:

* search visits
* teacher action margins
* teacher (Q-V)
* short-horizon bootstrapped deltas

not from:

* win/loss
* final VP only
* long Monte Carlo return only

That recommendation is exactly because CRR points out the failure mode of return-based weighting in offline settings, while IQL shows how to keep value learning in-sample and still do weighted policy extraction. ([ar5iv][2])

## The simplest concrete recipe I would start with

If I had to pick one today:

* log teacher visit counts on legal actions
* compute
  [
  A_T(s,a^*) = \log(N(a^*)+1) - \sum_b p_T(b)\log(N(b)+1)
  ]
* train with
  [
  w = \min(w_{\max}, \exp(A_T/\beta))
  ]
* use macro-weighted **average token NLL** for bundle actions
* evaluate on held-out:

  * weighted NLL
  * teacher top-1 / top-k agreement
  * calibration by decision type
* periodically audit only the top few architectures with small online self-play

That is usually the best tradeoff between **cheap**, **stable**, and **actually correlated with future strength**.

If you want, I’ll turn this into exact pseudocode for your dataset/training loop.

[1]: https://arxiv.org/abs/1910.00177 "[1910.00177] Advantage-Weighted Regression: Simple and Scalable Off-Policy Reinforcement Learning"
[2]: https://ar5iv.labs.arxiv.org/html/2006.15134 "[2006.15134] Critic Regularized Regression"
[3]: https://ar5iv.labs.arxiv.org/html/2110.06169 "[2110.06169] Offline Reinforcement Learning with Implicit Q-Learning"
[4]: https://github.com/ikostrikov/implicit_q_learning/blob/master/actor.py "implicit_q_learning/actor.py at master · ikostrikov/implicit_q_learning · GitHub"
