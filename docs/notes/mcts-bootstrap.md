Yes. The cleanest distinction is between a queryable teacher and a search/self-play teacher.

If the heuristic teacher can label the states your current learner visits, the strict framework is DAgger-like online dataset aggregation: roll out the current policy, query the teacher on those visited states, add those labels to the dataset, and keep updating. That is exactly the formal answer to “can I interleave collection and training rather than do big outer-loop retrains?”, and the point of DAgger is that it gives guarantees under the learner-induced state distribution rather than only the expert’s distribution. 

If the “teacher” is your own MCTS or self-play, the clean theorem is weaker, but the principled systems pattern is well established: Expert Iteration frames the loop as search producing improved targets and a neural network generalizing them; AlphaZero-style systems implement that with self-play workers, replay, and continuous SGD. In the AlphaZero lineage, new models can be published directly to self-play workers instead of waiting for a full collect-then-train round, and IMPALA shows that decoupling acting from learning is a scalable way to get stable high-throughput training when policy lag is controlled. ([arXiv][1])

The most direct literature answer to your exact idea is Reanalyse / MuZero Unplugged. It explicitly mixes fresh interaction data with targets recomputed on old stored states using the latest network, calls that mix the reanalyse fraction, and varies that ratio while holding the total actor-search and learner-update computation fixed. The same paper also says this applies to demonstrations or data from other agents, so it maps cleanly onto “play against a fixed heuristic teacher, keep the old data, and relabel it later.” ([arXiv][2])

One important nuance: for stale data, the hard part is usually the **value target**, not the per-state policy target. MuZero Unplugged notes that policy targets from MCTS visit counts are attached to the state itself, while n-step TD value targets can inherit off-policy bias from old trajectories. It also found that “more trajectory-independent” is not automatically better: in Atari, 5-step TD beat direct regression to the search value even when learning was almost entirely from reanalysed off-policy data, while direct MCTS-value regression helped in lower-data DM Control. ([arXiv][2])

A practical high-throughput version of your loop is:

1. Keep two parameter streams: `θ_train` and a published `θ_pub` for actors, often as an EMA / smoothed snapshot. Actors always use `θ_pub`; the learner updates `θ_train` continuously; publish a new snapshot every so many learner steps or after a light gate. AlphaZero-style systems, KataGo’s snapshot averaging/gating, and IMPALA all point in this direction. 

2. Add a reanalyse stage between replay and learning. Sample old states from replay, rerun MCTS with the latest published model, and overwrite or append fresher targets. If some data came from another policy or a heuristic teacher, include the original behavior action among the actions considered during reanalysis; MuZero Unplugged does this explicitly for offline / other-agent data. ([arXiv][2])

3. Split search budget instead of using one fixed MCTS budget everywhere. KataGo’s playout-cap randomization uses cheap search on most turns and full search on a subset, which increases the number of games while preserving some high-quality training targets. If your root simulation budget is small, Gumbel AlphaZero / MuZero is a principled upgrade because it was designed to keep policy improvement working in the few-simulation regime. 

4. Do not start every game from the initial state. Go-Exploit samples restart states from an archive of interesting positions; the paper’s rationale is exactly that shorter trajectories give more independent value targets and better coverage of deeper parts of the tree. ([arXiv][3])

5. Make replay selective. MuZero Unplugged uses prioritized replay with importance weighting, with priority based on the gap between search value and observed return. KataGo also shows that extra supervisory heads can materially improve learning efficiency, so if you have any cheap dense side-targets, they are usually worth adding. ([arXiv][2])

So, in compact form: your current V1→V2→V3 loop should become an **actor → replay → reanalyse → learner** pipeline. The “strict” case is DAgger when you have a queryable teacher; for self-play/MCTS, the principled answer is asynchronous approximate policy iteration with bounded staleness, replay, and target refresh. That is the standard way to get better wall-clock utilization without giving up label quality.

[1]: https://arxiv.org/abs/1705.08439 "[1705.08439] Thinking Fast and Slow with Deep Learning and Tree Search"
[2]: https://arxiv.org/pdf/2104.06294 "Online and Offline Reinforcement Learning by Planning with a Learned Model"
[3]: https://arxiv.org/abs/2302.12359 "[2302.12359] Targeted Search Control in AlphaZero for Effective Policy Improvement"
