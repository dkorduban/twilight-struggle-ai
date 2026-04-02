Assuming you mean **Anthropic Claude Code**, the most practical setup is:

**keep Claude local as the planner/editor, keep your project in Git, and make remote training go through one small submit/poll/pull wrapper script.**
Point that wrapper at either:

1. a **GPU VM over SSH** for the best overall workflow, or
2. **Kaggle kernels** when the priority is Kaggle’s GPU-backed batch runs.

That fits Claude Code well because Claude Code can run locally, on Anthropic-hosted remote sessions, or through **SSH to a remote machine you manage**. Anthropic-hosted remote sessions can continue after you close the app, but Anthropic’s docs note that **custom environment images and snapshots are not yet supported**, so for ML stacks with pinned CUDA/PyTorch environments, **SSH to your own GPU box is the cleaner default**. ([Claude][1])

The other reason this works well is that Claude Code already has the right building blocks: **hooks** for deterministic automation, **skills** for repeatable workflows, **CLI tool usage** for external services, **plan/auto permission modes**, **worktrees** for parallel isolated sessions, and headless/scriptable operation through `claude -p`, JSON output, and scheduled tasks or GitHub Actions. ([Claude][2])

## The workflow I would actually use

### 1) Make the repo the control plane

Use a normal repo, not notebook-first:

```text
repo/
  train.py
  configs/
    base.yaml
    exp_*.yaml
  scripts/
    submit_experiment.py
    poll_experiment.py
    fetch_results.py
    summarize_results.py
  backends/
    kaggle/
    ssh/
  runs/
  .claude/
    skills/
      experiment-runner/SKILL.md
    settings.json
  CLAUDE.md
```

Claude should only change:

* code
* configs
* wrapper scripts
* summary files

Claude should **not** directly improvise cloud operations. Instead, it should call one safe wrapper such as:

```bash
python scripts/submit_experiment.py --backend kaggle --config configs/exp_017.yaml
```

That keeps the agentic part narrow and reliable.

### 2) Use a **script-first** Kaggle adapter, not notebook editing

Kaggle supports kernels with metadata specifying the `code_file`, `language`, and `kernel_type`, where `kernel_type` can be `script` or `notebook`. It also supports `enable_gpu`, `enable_internet`, and dataset / model sources in `kernel-metadata.json`. ([GitHub][3])

So the clean Kaggle pattern is:

* keep canonical code in normal `.py` files in Git
* have `submit_experiment.py` render a Kaggle job folder
* generate a small `kernel-metadata.json`
* push it with the Kaggle CLI
* poll status
* pull outputs back into `runs/`

Kaggle’s CLI supports exactly that flow: `kaggle kernels init`, `push`, `status`, and `output`. `push` uploads the code and metadata and then attempts to run the kernel; `status` checks the latest run; `output` downloads the generated files. ([GitHub][4])

A minimal rendered metadata file would look like this:

```json
{
  "id": "yourname/exp-017",
  "title": "exp-017",
  "code_file": "train_kaggle.py",
  "language": "python",
  "kernel_type": "script",
  "enable_gpu": "true",
  "enable_internet": "false",
  "dataset_sources": ["yourname/your-dataset"],
  "model_sources": []
}
```

That is much easier for Claude to manipulate than raw notebook JSON.

### 3) Give Claude a fixed Kaggle command path

For Kaggle, the wrapper should reduce everything to four operations:

```bash
kaggle kernels init -p build/exp-017
kaggle kernels push -p build/exp-017 --accelerator NvidiaTeslaT4
kaggle kernels status yourname/exp-017
kaggle kernels output yourname/exp-017 -p runs/exp-017 -o
```

Kaggle’s CLI docs list `--accelerator` support on `kernels push`, including values like `NvidiaTeslaP100`, `NvidiaTeslaT4`, `NvidiaTeslaA100`, `NvidiaL4`, and others, while also noting that some accelerators are only available in certain competitions or to Kaggle admins. ([GitHub][4])

So the wrapper should choose a conservative default such as `NvidiaTeslaT4`, and your repo should treat anything fancier as optional.

### 4) Let Claude operate at the experiment level, not the shell-command level

Use a repo skill such as `.claude/skills/experiment-runner/SKILL.md`. Claude Code docs explicitly support skills for repeatable workflows, including workflows with side effects that you invoke manually. Hooks are the deterministic mechanism for actions that must always happen. ([Claude][5])

That skill should tell Claude to do this loop:

1. create or modify a config
2. call `submit_experiment.py`
3. wait or poll through `poll_experiment.py`
4. fetch artifacts into `runs/<exp>/`
5. update `runs/summary.md`
6. propose the next configs based on the metrics

In other words, Claude is choosing experiments, but your scripts are doing the cloud mechanics.

### 5) Use worktrees for parallel branches of experimentation

Claude Code supports **parallel sessions with Git worktrees**, including separate worktrees per task/branch, so experiment streams do not collide. ([Claude][6])

That makes a good pattern like:

* `baseline-tuning`
* `augmentation-tests`
* `optimizer-sweep`

Each gets its own Claude session and its own result summary.

### 6) Add just enough automation around Claude

Claude Code can run in **Plan mode**, **Auto-accept edits**, or **Auto mode**, and can also be used headlessly with `claude -p`, pipes, JSON output, and scheduled tasks / GitHub Actions. ([Claude][7])

That means the practical automation stack is:

* **Plan mode first** while you validate the workflow
* allow only trusted commands in permissions, such as:

  * `python scripts/*.py`
  * `git status`
  * `git diff`
  * `gh pr create`
  * `kaggle kernels *`
* add a **Notification hook** so Claude can work without you watching the terminal
* optionally run a nightly “analyze yesterday’s runs and propose the next batch” task with `claude -p` in GitHub Actions or another scheduler. ([Claude][2])

## Best overall recommendation

For **serious training**, I would choose this order:

**Best overall:** GitHub repo + GPU VM + Claude Code over SSH
**Best Kaggle-specific:** GitHub repo + local Claude Code + Kaggle submit/poll/output wrapper

Kaggle is workable, but the API surface is basically **render job → push kernel → poll status → pull outputs**, which makes it more of a **batch backend** than a great interactive agent workspace. That is a reasonable fit for sweeps and reproducible runs, but a less natural fit for long-lived training environments or heavily customized CUDA stacks. That conclusion follows from the Kaggle kernel workflow and metadata surface exposed by the CLI/docs. ([GitHub][4])

A concrete instruction you could hand Claude once this is wired up:

```text
Use the experiment-runner workflow.
Start from configs/base.yaml.
Create 4 variants for learning rate and batch size.
Submit them to the kaggle backend.
Wait for completion, pull outputs into runs/.
Compare metrics.json files, update runs/summary.md, and propose the next 2 configs.
Do not use arbitrary shell commands outside the approved wrapper scripts.
```

A good next step is to build the wrapper around **both** backends from day one:

```bash
python scripts/submit_experiment.py --backend ssh --config ...
python scripts/submit_experiment.py --backend kaggle --config ...
```

Then Claude gets one stable interface, and you can swap between Kaggle and a real GPU VM without changing the agent workflow.

[1]: https://code.claude.com/docs/en/desktop-quickstart "Get started with the desktop app - Claude Code Docs"
[2]: https://code.claude.com/docs/en/hooks-guide "Automate workflows with hooks - Claude Code Docs"
[3]: https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels_metadata.md "kaggle-cli/docs/kernels_metadata.md at main · Kaggle/kaggle-cli · GitHub"
[4]: https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels.md "kaggle-cli/docs/kernels.md at main · Kaggle/kaggle-cli · GitHub"
[5]: https://code.claude.com/docs/en/best-practices "Best Practices for Claude Code - Claude Code Docs"
[6]: https://code.claude.com/docs/en/common-workflows "Common workflows - Claude Code Docs"
[7]: https://code.claude.com/docs/en/how-claude-code-works "How Claude Code works - Claude Code Docs"
