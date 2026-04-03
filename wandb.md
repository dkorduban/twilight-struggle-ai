For that specific question, the **better primary test** is:

**double the dataset and halve the epochs so total examples or tokens seen stays the same.**

That isolates the effect of **more unique data / better data mix** at roughly fixed training budget. If that run wins, your smaller dataset was likely being over-reused and extra diversity helped. If you keep epochs the same after doubling the dataset, you also double total data processed and compute, so you no longer know whether the gain came from **better data coverage** or just **more training**. This matches the usual scaling-law framing, which compares models by training tokens / compute rather than epochs; work on repeated-data regimes also shows that some repetition can be fine, but repeated tokens eventually have diminishing value. ([arXiv][1])

So I would run them in this order:

1. **Fair saturation test:** same total samples/tokens seen, bigger dataset, fewer epochs.
2. **“Can I buy quality with more data + more compute?” test:** bigger dataset, same epochs.
3. If budget allows, do a tiny curve: 0.5×, 1×, 2× unique data at fixed total tokens. That tells you whether you are still data-limited or already near saturation. ([arXiv][1])

On the W&B side: **yes, you can switch x-axis in the UI after the fact** as long as that axis metric was logged in the run. You do **not** need to emit separate copies of every metric for every axis. The important part is to log the candidate axes themselves, such as `global_step`, `samples_seen`, `tokens_seen`, and maybe `wall_clock_hours`. Then you can change x-axis at the workspace or panel level; `define_metric()` mainly sets the default x-axis for auto-generated charts. In one given panel, all runs share the same chosen x-axis key, so that key needs to exist consistently across runs. ([Weights & Biases Documentation][2])

For your PyTorch setup, the most practical durable pattern is:

* make **`samples_seen` or `tokens_seen`** the main cross-run axis
* keep **`global_step`** for optimizer/debugging
* keep **`epoch`** only as a convenience label, not as the main comparison axis when dataset size changes
* log all of them cumulatively and restore them from checkpoint on resume. ([Weights & Biases Documentation][3])

A good minimal logging scheme is:

```python
run = wandb.init(
    project="my_project",
    id=run_id,
    resume="allow",
    config={
        "model": model_name,
        "dataset_name": dataset_name,
        "dataset_version": dataset_version,
        "dataset_size": dataset_size,
        "batch_size": batch_size,
        "lr": lr,
    },
)

run.define_metric("*", step_metric="samples_seen")

global_step = ckpt.get("global_step", 0)
samples_seen = ckpt.get("samples_seen", 0)
tokens_seen = ckpt.get("tokens_seen", 0)

for batch in loader:
    loss = train_step(batch)

    global_step += 1
    samples_seen += len(batch["input_ids"])
    tokens_seen += int(batch["attention_mask"].sum())

    run.log({
        "global_step": global_step,
        "samples_seen": samples_seen,
        "tokens_seen": tokens_seen,
        "epoch": samples_seen / dataset_size,   # convenience only
        "train/loss": float(loss),
        "opt/lr": scheduler.get_last_lr()[0],
    })
```

This avoids W&B’s internal log-call counter being your de facto step, which is often wrong once train and eval log at different cadences. W&B explicitly recommends defining your step metric instead of relying on the internal counter. ([Weights & Biases Documentation][3])

For the messy “37 panels” problem, switch the project from **automatic** to **manual** workspace. Automatic mode creates one plot per metric; manual mode is a blank slate and is better when you care about a focused subset of metrics. W&B also recommends manual mode for large metric counts because it loads faster. Then use a naming scheme like `train/...`, `val/...`, `opt/...`, `sys/...`, `data/...`, and group sections by the **first prefix**. ([Weights & Biases Documentation][4])

A good workspace layout is only 5–7 panels:

* `train/loss`, maybe train accuracy if relevant
* `val/loss` + main selection metric
* `opt/lr`, `opt/grad_norm`
* `data/samples_seen`, `data/tokens_seen`, throughput
* `sys/gpu_mem`, `sys/gpu_util`, maybe CPU RAM
* one debug panel for anything special

Use W&B’s **multi-metric line plots** with regex so one panel can show related metrics together, and optionally clean up the auto-generated single-metric panels. Save that as a **saved view**, and if you like the defaults, save a **personal workspace template** so new projects start with the same x-axis and plot settings. ([Weights & Biases Documentation][5])

For run durability and reproducibility, I would also do three more things:

* store the full experiment settings in `run.config`, since W&B uses config values for grouping, comparison, and reproducibility ([Weights & Biases Documentation][6])
* save checkpoints and datasets as **artifacts**; artifacts version inputs and outputs, and checkpoint artifacts can use aliases like `latest` and `best-val` ([Weights & Biases Documentation][7])
* resume with an explicit `run_id` and `resume="allow"`; W&B recommends `allow` with a specific run ID over `auto` because `auto` can behave unexpectedly across directories or multiple failed runs ([Weights & Biases Documentation][8])

Net: for the science question, **fix total tokens/examples first**. For W&B, make **`samples_seen` or `tokens_seen` the main axis**, use **manual workspace**, and treat **epoch as secondary only**. That setup survives dataset-size changes much better.

If useful, I can turn this into a small reusable `WandbLogger` helper for plain PyTorch.

[1]: https://arxiv.org/abs/2203.15556 "[2203.15556] Training Compute-Optimal Large Language Models"
[2]: https://docs.wandb.ai/models/track/log/customize-logging-axes "Customize log axes - Weights & Biases Documentation"
[3]: https://docs.wandb.ai/models/integrations/add-wandb-to-any-library "Add W&B to a Python library - Weights & Biases Documentation"
[4]: https://docs.wandb.ai/models/app/features/panels "Panels - Weights & Biases Documentation"
[5]: https://docs.wandb.ai/models/app/features/panels/line-plot "Line plots overview - Weights & Biases Documentation"
[6]: https://docs.wandb.ai/models/track/config "Configure experiments - Weights & Biases Documentation"
[7]: https://docs.wandb.ai/models/artifacts "Artifacts overview - Weights & Biases Documentation"
[8]: https://docs.wandb.ai/models/runs/resuming "Resume a run - Weights & Biases Documentation"
