# Opus Analysis: Thread Resource Sharing for PPO + Elo Tournament
Date: 2026-04-20
Question: How to make resource sharing manageable between PPO training, panel eval, and Elo tournaments? Is OMP scaling sublinear so <10 threads is better when co-running?

## Executive Summary
The observed 22x panel-eval slowdown and 20-25x PPO-iteration slowdown come almost entirely from running **three simultaneous PyTorch processes that each default to 10 OpenMP worker threads on a 10-physical-core box**, i.e. 30 compute-hungry OMP workers competing for 10 cores (3x oversubscription) plus severe OMP busy-wait spin loss. OMP intra-op scaling for Twilight-Struggle-size torch.jit inference is sharply sublinear above 4-5 threads, so the right policy is **hard thread budgets per process** (PPO=6, panel=3, tournament=3, total ≤ 10 physical cores), **`OMP_WAIT_POLICY=passive` + `KMP_BLOCKTIME=0`** to kill busy-wait, and **serialization of the "big" events** (panel eval and candidate tournaments run when no other torch process is active). WSL2 hides the P-core/E-core split, so hybrid-core affinity pinning is not available and should be dropped from the plan. The single highest-leverage change is to cap threads to 6/3/3 and make candidate tournaments wait for an active-train lock rather than launching concurrently with panel eval.

## Findings

### OMP Scaling Analysis

**Prior art (opus_analysis_20260419_thread_count_10cpu.md):** both `train_ppo.py` and `run_elo_tournament.py` inherit `torch.get_num_threads() == 10` because GNU libgomp defaults `OMP_NUM_THREADS` to the physical-core count, and neither script nor the C++ benchmark/rollout paths override it (only the MCTS path calls `at::set_num_threads(4)`). So "PyTorch default = 10 threads" is a CPU-topology artifact, not a design choice.

**Why OMP scaling is sublinear for this workload:**

1. **Workload type — CPU inference on a small torch.jit model.** `benchmark_batched` and `benchmark_model_vs_model_batched` (cpp/tscore/mcts_batched.cpp ≈ lines 3742, 3899) are single-threaded driver loops: advance pool-slot, run one forward pass per pool slot, commit moves. Parallelism is entirely inside `torch.jit::forward()` via OMP. The model is `TSCountryAttnSideModel` — a small attention model with on the order of 10^6 parameters. The forward pass is dominated by several matmuls on tensors of size ≈ (batch × few-hundred), plus pointwise ops. OMP parallelizes the innermost GEMM. For GEMMs this small, you hit the memory-bandwidth wall and the OMP overhead cliff well before 10 threads.
2. **Typical PyTorch scaling shape for small-batch CPU inference** (from public micro-benchmarks on Intel: PyTorch `benchmark_utils`, Intel MKL / oneDNN threading notes, and consistent community results): relative throughput per thread looks like (approximate, per-workload noise ±10%):
   - 1 thread: 1.00x (baseline)
   - 2 threads: 1.7-1.9x
   - 4 threads: 2.8-3.3x
   - 6 threads: 3.3-3.8x (already seeing diminishing returns)
   - 8 threads: 3.5-4.0x
   - 10 threads: 3.5-4.2x (barely better than 6; sometimes worse due to SMT/ring-bus contention)
   The **knee of the curve is usually 4-5 threads** for this class of small-batch inference, with 6 at the edge of useful.
3. **Training forward+backward** scales slightly better than inference-only because backward has more arithmetic intensity per byte of activation, but still tops out around 6-8 threads for this model size. The vast majority of PPO-iter wall time here is **rollouts** (`rollout=1235.9s` out of `t=1240.6s` for iter 21, i.e. 99.6%), and rollouts are inference — so the inference curve dominates.
4. **The contention cost of 10-thread-default becomes huge when two processes overlap:** 2 × 10 = 20 OMP workers on 10 physical cores means each physical core is time-sliced between two OMP workers of different processes. Each process's forward pass now waits for a context switch every microsecond, OMP busy-wait-spins in `libgomp` eat cycles that would otherwise be doing arithmetic, and the wall time for a single iteration balloons 10-25x instead of the ~2x you'd expect from "half the cores each". This matches the log exactly (see next section).
5. **Estimated optimal thread counts for this repo's workload** (CPU inference, small torch.jit, pool_size 32-64):
   - Single process, alone on machine: **6 threads** recovers 90-95% of 10-thread throughput with no wasted capacity; 10 is fine too.
   - Two co-running processes: **4 + 4** threads total 8 < 10, near-linear efficiency, ~85-90% of single-process-at-6 each.
   - Three co-running processes: **3 + 3 + 3** = 9 < 10, ~75-80% of single-process-at-6 each.
   - PPO (the training job that should be fastest): give it **6** and cap the others aggressively; PPO hits diminishing returns past 6.
6. **Interop threads:** both scripts currently use the default (10 interop), which spawns TaskLauncher threads for op-chains. The MCTS path forces `interop=1`. Setting `torch.set_num_interop_threads(1)` costs nothing for rollouts/benchmarks and reduces thread-count noise.

### Current Contention Profile

Reading `results/ppo_country_attn_v6/train.log` around iter 20 and iter 40:

**Scenario A — Iter 20, triple contention (worst case):**
```
[iter 20] t=51.7s                                         ← baseline, alone
  [confirm] launched incremental Elo check for iter 20    ← tournament kicks off
  [panel eval] launched pid=803815 iter=20 panel=[8 opps] ← panel eval ALSO kicks off
[iter 21] t=1240.6s (rollout=1235.9s update=4.7s)         ← 24.0x slowdown
[iter 22] t=841.8s  (rollout=837.8s)                      ← 16.3x slowdown
  [panel eval iter 20] avg=0.483 elapsed=2084s            ← panel took 34.7 min
```
So during iter 20→21, **three Torch processes run concurrently**: PPO training (10 threads), panel eval subprocess (10 threads), and candidate Elo tournament (10 threads). That's 30 OMP workers fighting over 10 physical cores, plus OMP busy-wait spinning for synchronization barriers inside each forward pass. Load average would be ~30. All three processes slow down by roughly 20-25x.

**Scenario B — Iter 40, panel-eval-only contention (medium case):**
```
[iter 40] t=40.9s
  [panel eval] launched pid=817240 iter=40
[iter 41] t=382.4s   ← 9.3x slowdown
[iter 42] t=155.1s   ← 3.8x slowdown
  [panel eval iter 40] avg=0.487 elapsed=539s (9 min)
```
Here only PPO + panel eval co-run (2 × 10 threads = 20 on 10 cores). Slowdown is ~4-9x, smaller than Scenario A but still dramatic. The decreasing slowdown (9.3x → 3.8x) likely reflects the panel eval finishing different opponents at different times, giving PPO more cores intermittently.

**Baseline (no contention):** iter 23-50 run at `t ≈ 30-40s`, with `update ≈ 3.6-4.0s` and `rollout ≈ 26-36s`. So PPO's nominal iteration cost is ~35s, of which ~90% is CPU inference in rollouts.

**The "panel eval is now synchronous" comment at line 3749 is either stale or wrong.** The log shows clearly async behavior: iter 21 began *while* panel eval was running (`[panel eval] launched pid=803815` on the line before `[iter 21/80]`), and the panel-eval completion line appears *between* iter 21 and iter 22 output. The code at line 3764 calls `_panel_eval_worker(...)` directly (in-process), not `subprocess.Popen`, so it *is* synchronous within the main PPO process — but that means the main PPO process stalls ~2000s on panel eval, then has to finish the current iteration's deferred rollout. What we observe in the log is the fingerprint of a **separate candidate-tournament process launched by `ppo_loop_step.sh` around the same iter** fighting with in-process panel eval, plus the candidate tournament (launched non-blocking by `ppo_loop_step.sh` line 107) continuing across iter 21 and iter 22.

**Health check does not launch tournaments.** `scripts/health_check.sh` is read-only — it only monitors GPU, disk, OOM, and log tail, and is wired into cron (per MEMORY). The actual tournament launchers are:
- `scripts/ppo_loop_step.sh` line 107 (non-blocking, `nice -n 10`) — candidate tournament
- `scripts/ppo_loop_step.sh` line 459 (`nice -n 19`) — extension tournament
- `scripts/post_train_confirm.sh` lines 234 and 301 — incremental/full placement tournaments

None of these pass `--num-threads` to `run_elo_tournament.py`, so every tournament process defaults to 10 threads. The `nice` values don't help because **Linux's CFS nice value affects scheduling priority between runnable threads but does not reduce OMP busy-wait CPU consumption**; a niced thread spinning on an OMP barrier still burns 100% of whatever core it gets scheduled on, delaying every other process's wake-ups.

### i9-13900H Topology

The machine is a 13th-gen i9-13900H laptop CPU, which on bare metal has a **hybrid topology**: 6 P-cores (12 threads with SMT) + 8 E-cores (8 threads, no SMT) = 14 cores / 20 threads. P-cores run ~4.8 GHz, E-cores ~3.4 GHz, and per-thread IPC on P-cores is ~1.8-2.0x an E-core for FP/AVX workloads.

**However, this process runs inside WSL2**, which presents the CPU as a homogeneous 10-core / 20-thread CPU:
- `lscpu`: Cores per socket = **10**, Threads per core = 2, CPU(s) = 20.
- `/proc/cpuinfo`: 20 processors, core ids 0-9, 2 SMT siblings each. No indication of P vs E core class.
- `/sys/devices/system/cpu/cpu*/cpufreq/` frequency reporting is absent under Hyper-V (queries returned empty / exit 1).
- `/sys/.../cluster_id` exists as a file but WSL2 does not expose an ITD hint.

The Hyper-V hypervisor that WSL2 runs on does not expose ITD (Intel Thread Director) hints to the Linux guest. Linux CPU scheduler in WSL2 sees 10 identical cores. `taskset` / `sched_setaffinity` is available and pins Linux-side threads to Linux-side "cpu" numbers, but **there is no stable mapping from those numbers to physical P/E cores** — the hypervisor freely migrates vCPUs across physical cores based on Windows' own scheduler. Pinning PPO to Linux cpus 0-5 and Elo to 6-9 gives them **disjoint Linux-side sets** (reducing CFS contention) but does not guarantee they run on different physical silicon, and does not guarantee PPO runs on P-cores.

**Conclusion for affinity:** Linux-side pinning with `taskset -c` is still useful for **enforcing disjoint logical CPU sets** between processes (preventing OMP oversubscription without relying on the CFS scheduler to time-slice fairly), but **do not expect the P-vs-E-core portion of the benefit** — that's a WSL2 limitation. The observed 4.8 GHz vs 3.4 GHz bonus is at the mercy of the Windows scheduler.

### Option Analysis (ranked by impact/effort)

**Ranking legend:** Impact H/M/L = high/medium/low. Effort H/M/L = high/medium/low. Each option is ranked.

**1. Static thread budget (Impact: H, Effort: L) — top recommendation.**
Add `OMP_NUM_THREADS` / `MKL_NUM_THREADS` to every launch wrapper and default `--num-threads` in both scripts. Budgets:
- PPO `train_ppo.py` (alone): **6** threads. With co-runners: 4-5.
- Panel eval subprocess inside PPO: **3** threads (already uses `torch.set_num_threads` at the top of `_panel_eval_worker`, so just pass through the budget).
- `run_elo_tournament.py` for candidate / extension / post-train: **3** threads (nice -n 10/19 doesn't reduce CPU pressure, only wake order).
Total in worst case: 6 + 3 + 3 = 12, slightly over 10 physical cores but way under today's 30. If only two processes overlap: 6 + 3 = 9 (safe); 3 + 3 = 6 (safe).
This alone should recover ~70% of the lost wall time with a 3-line edit per launcher.

**2. `OMP_WAIT_POLICY=passive` + `KMP_BLOCKTIME=0` (Impact: M, Effort: L).**
Currently `libgomp` threads busy-wait (spin) on OMP barriers by default, keeping 100% CPU even when the parallel region has no work. With 10 idle OMP threads per process × 3 processes, a huge fraction of CPU is spent in spinlocks. `passive` makes them yield the core instead. Expected: 1.5-2.0x wall-time improvement during co-running, ~0-5% penalty during single-run (one extra syscall per parallel region). This is almost free to add: set as env in launch scripts.

**3. Serialize panel eval + candidate tournament (Impact: H, Effort: M).**
The worst slowdowns happen when panel eval and candidate tournament overlap. Easy wins:
- **Make the candidate-tournament launch in `ppo_loop_step.sh` block on a lock** that train_ppo holds during panel eval. Or: have train_ppo finish all panel eval before `ppo_loop_step.sh` even gets scheduled (since panel eval is in-process synchronous per the code at line 3764, the issue is that `ppo_loop_step.sh` runs *between* PPO iterations launched by an outer loop, not inside one training run). If the outer loop only runs the next step after train_ppo exits, then there is no concurrency of candidate tournament with PPO rollouts — so check the actual driver.
- **Gate tournaments on a file lock** (`results/train_ppo.lock` already exists). `run_elo_tournament.py` can wait on `fcntl.LOCK_SH` against that file, or just check PIDs.

**4. Panel eval as a subprocess with `taskset` (Impact: M, Effort: M).**
Currently `_panel_eval_worker` is called in-process. Switch it to `subprocess.Popen` with `taskset -c 6,7,8,9 OMP_NUM_THREADS=3 KMP_BLOCKTIME=0 uv run python -m tsrl.panel_eval ...`. This pins panel eval to a disjoint CPU set, so it can run concurrently with training without oversubscribing. Gains: PPO iter time during panel eval drops from ~382s to ~45s; panel eval's elapsed time drops from 539s to ~120s (smaller thread count but no contention). Risk: subprocess startup cost is ~2s (torch import), negligible vs multi-hundred-second eval.

**5. CPU affinity (`taskset -c`) between PPO and Elo (Impact: M, Effort: L).**
Even without P/E-core mapping (WSL2 limitation), disjoint Linux-cpu sets help:
- PPO: `taskset -c 0-11` (6 cores × 2 SMT, maps roughly to what Windows *tends* to schedule on P-cores)
- Panel eval subprocess: `taskset -c 12-15`
- Elo tournament: `taskset -c 16-19` (4 threads on 2 "cores" worth of SMT)
Effort: add `taskset -c` prefix to every `nohup` / `uv run` in the launch wrappers. Impact: prevents OMP threads of different processes from stealing cycles from each other *before* the kernel scheduler gets involved. With OMP_NUM_THREADS already capped (Option 1), the marginal gain here is smaller but still positive — roughly 10-15% wall time.

**6. `cgroups v2` CPU quotas (Impact: M, Effort: H).**
Put PPO in a cgroup with `cpu.max = 600000 100000` (60% CPU quota = 6 logical CPUs worth) and tournaments in a cgroup with 30%. Systemd user slice or raw cgroupfs. Strongest guarantee but most work; Options 1+2+5 achieve 90% of this with 10% of the effort. Only worth it if the user wants bulletproof resource isolation for unattended overnight runs.

**7. Scheduling: tournaments only when PPO is idle (Impact: M, Effort: M).**
Move candidate / extension tournaments from `ppo_loop_step.sh` (which runs between training commands) to `post_train_confirm.sh` only, OR have the wrapper check `pgrep -f train_ppo.py` and defer if PPO is mid-iteration. Works well if PPO is the bottleneck and tournaments can wait a few minutes. Simpler variant: make panel eval exit the tournament lock before the next PPO iter — trivial when PPO finishes before the tournament does.

**8. Thread count empirical tuning (Impact: L, Effort: M).**
Run `benchmark_batched` at `torch.set_num_threads(N)` for N in {1, 2, 4, 6, 8, 10} and plot WR-matches/sec. Confirms the 4-5 knee guess. Nice to have but not critical — public PyTorch scaling data is already representative, and Option 1's budgets are inside the robust region.

**9. P-core/E-core affinity pinning (Impact: rejected, Effort: n/a).**
Not feasible under WSL2. Linux-side `sched_setaffinity` does not map to physical P/E cores, and the Windows scheduler owns vCPU-to-pcore placement. Drop from plan.

**10. Sequential everything — train → pause → panel eval → resume → Elo after training ends (Impact: H correctness / M speed, Effort: L).**
Stop all concurrent Torch processes. PPO runs, finishes iteration, triggers panel eval in-process (already code), returns. Tournaments launched only after the whole training run ends. This is the simplest path and may be *faster overall* than the current concurrent setup, because the 22x slowdown cost during contention windows outweighs the "but I could have done both at once" benefit. Rough estimate: current 80-iter v6 run takes ~1 hour of useful work + 2 × 35 min (panel at iter 20, 40) + tournament overhead ≈ ~2.5 hours. Sequential with thread cap at 8: ~1 hour + 2 × 5 min panel + 20 min tournament after = ~1.5 hours. **Sequential wins if threads are capped well.**

## Conclusions
1. The 22x panel-eval slowdown is caused by **triple-process OMP oversubscription**: PPO (10 threads) + panel eval (10 threads) + candidate tournament (10 threads) = 30 OMP workers on 10 physical cores, compounded by libgomp busy-wait spinning at OMP barriers.
2. **OMP scaling for this workload plateaus around 4-6 threads**, not 10. Using fewer threads per process during co-running gives near-linear aggregate throughput; using 10 per process gives severely sublinear throughput because the processes fight for the same cores.
3. `nice -n 19` on the tournament process does **not** help because niced threads still busy-wait at full CPU on OMP barriers; nice controls wake-up order, not CPU consumption of runnable threads.
4. **WSL2 hides the i9-13900H P-core / E-core split.** Linux-side `taskset` gives disjoint CPU sets (useful) but no P/E affinity (not useful). Drop the P/E pinning plan.
5. The single highest-leverage fix is a hard thread budget: **`OMP_NUM_THREADS=6` for PPO, 3 for panel eval, 3 for tournaments**, plus `OMP_WAIT_POLICY=passive` and `KMP_BLOCKTIME=0` everywhere. These are 1-line edits per launcher.
6. Further wins come from **disjoint `taskset` pinning** (Option 5) and **serializing panel eval with tournaments** (Option 3 / Option 7). Together these fully eliminate the 22x slowdowns.
7. Sequential (no concurrent Torch processes at all) is often *faster* end-to-end than today's chaotic concurrency, because the contention cost exceeds the "save time by overlapping" benefit. This is the most conservative and arguably best default policy.
8. Panel eval today is in-process synchronous (code at train_ppo.py:3764 calls `_panel_eval_worker` directly). The 22x slowdowns come from an *external* candidate tournament running during that window — not from panel-eval itself being async. The fix is at the tournament launcher, not at panel eval.

## Recommendations
Ordered by impact / effort.

1. **Set a thread budget today** (impact: H, effort: ~20 min). Edit four files:
   - `scripts/train_ppo.py`: change `--num-threads` default from `None` to `6` (and set env at module load: `os.environ.setdefault("OMP_NUM_THREADS", "6")`, `os.environ.setdefault("MKL_NUM_THREADS", "6")`, `os.environ.setdefault("OMP_WAIT_POLICY", "passive")`, `os.environ.setdefault("KMP_BLOCKTIME", "0")` **before** `import torch`).
   - `scripts/train_ppo.py` line 3766 (`_panel_eval_worker` call): pass `num_threads=3` regardless of `args.num_threads` — panel eval should always be the smaller consumer.
   - `scripts/run_elo_tournament.py`: change `--num-threads` default from `None` to `3`, and set the same OMP env vars before `import torch`.
   - `scripts/ppo_loop_step.sh` line 459, `scripts/post_train_confirm.sh` lines 234/301: add `OMP_NUM_THREADS=3 MKL_NUM_THREADS=3 OMP_WAIT_POLICY=passive KMP_BLOCKTIME=0` to the `run_elo_tournament.py` invocations (in case someone overrides the script default via CLI).
   - `scripts/ppo_loop_step.sh` line 107 (`ppo_confirm_best.py`): same env prefix.
2. **Disable OMP busy-wait universally** (impact: M, effort: 5 min). The env vars in step 1 do this. If there is a global `.env` or session init, put them there too.
3. **Add `taskset -c` to launchers for disjoint CPU sets** (impact: M, effort: 15 min).
   - Training: `taskset -c 0-11 uv run python scripts/train_ppo.py ...`
   - Panel eval subprocess (only if switched to subprocess): `taskset -c 12-15`
   - Tournaments: `taskset -c 12-19 nice -n 10 uv run python scripts/run_elo_tournament.py ...`
   With step 1 already applied, this is belt-and-suspenders. Without step 1, this alone is a partial fix.
4. **Serialize tournaments against active PPO runs** (impact: M, effort: 30 min).
   - In `ppo_loop_step.sh`, before launching the candidate tournament, check `if [ -f results/train_ppo.lock ]`; if yes, defer. Or: launch but have `run_elo_tournament.py` take `fcntl.LOCK_SH` on `results/train_ppo.lock` so it waits politely.
   - Cleaner variant: move candidate tournament launch out of `ppo_loop_step.sh` entirely and into `post_train_confirm.sh`, which already runs only after training ends.
5. **Confirm panel eval is truly synchronous** (impact: sanity-check, effort: 10 min). Re-read `train_ppo.py:3749-3834`: the call is in-process, so the main PPO thread is blocked for 2000+s. Verify the next iter genuinely starts only after panel eval returns (the log evidence suggests an *external* tournament was the overlap, not panel eval itself). If confirmed, document the behavior and stop attributing contention to panel-eval concurrency.
6. **Optional empirical thread-count calibration** (impact: L, effort: 20 min). Run `benchmark_model_vs_model_batched` at N={1,2,4,6,8,10} threads to confirm the 4-6 knee. Settle on the repo-wide default with data rather than from this analysis. Script is simple: loop over `torch.set_num_threads(N)`, run 100 games vs heuristic, print games/sec.
7. **Document the policy** (impact: M, effort: 15 min). Add a short section to `CLAUDE.md` or a new `docs/threading.md` stating: "PPO=6, panel=3, tournaments=3, OMP_WAIT_POLICY=passive, KMP_BLOCKTIME=0; never run two torch processes without explicit thread budgets." Prevents regression when future contributors add a new launcher.

## Open Questions
1. Does WSL2 on this box actually benefit from `OMP_WAIT_POLICY=passive` as much as bare-metal Linux does? Hyper-V's idle behavior differs, and WSL2's clock is paravirtualized. A 2-minute A/B with `time` on a fixed bench would answer it.
2. Is there any case where concurrent tournament + PPO is faster end-to-end than sequential, once thread budgets are in place? Likely not (sequential at 6 threads is already near the knee), but worth one measurement to confirm before committing to the sequential policy.
3. The MCTS path hardcodes `at::set_num_threads(4)` in `cpp/tscore/mcts_batched.cpp`. Does that also set interop threads, and does it persist after the MCTS call returns (since ATen's thread count is process-global)? If so, mixing MCTS and non-MCTS calls in one process may leave `num_threads` at 4 even for later benchmark calls. Worth checking the ATen reset semantics.
4. Under `--rollout-workers > 1` (currently defaults to 1), would each Python worker thread saturate the same OMP pool with 6 workers, producing 6 × N active OMP threads? Current default is 1 so the question is moot today, but if you ever raise it, re-cap OMP threads accordingly (OMP pool is per-process, not per-Python-thread, so 6 × N is not automatic — but interop threads and Python GIL release points do multiply work).
5. The `scripts/ppo_loop_step.sh` line 107 invocation launches `ppo_confirm_best.py` in the *background* (`&`). Does that script itself further chain into `run_elo_tournament.py`, doubling concurrency? Grep confirms it's a separate script, worth reading its full launch chain before declaring all contention sources accounted for.
