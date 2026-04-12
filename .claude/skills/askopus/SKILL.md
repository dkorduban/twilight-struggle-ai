# askopus

Start a background Opus agent to deeply analyze a question or task, save the full analysis to a timestamped document, then immediately display a concise summary with key conclusions.

## Usage

```
/askopus <question or task>
```

Examples:
- `/askopus should we switch from BayesElo MM to TrueSkill for the rating system?`
- `/askopus what's the best architecture for ISMCTS under hidden information in TS?`
- `/askopus why is rollout_wr dropping on the US side across v18-v22?`

---

## Procedure

### Step 1 — Determine output path

Construct the output path:
```
results/analysis/opus_analysis_YYYYMMDD_HHMMSS_<stub>.md
```
- Use the current UTC time for the timestamp.
- Derive `<stub>` from the question: 2-4 lowercase words joined by underscores, capturing the core topic (e.g. `hidden_dim`, `us_win_rate`, `ismcts_design`, `bayeselo_vs_trueskill`).
- Example: `results/analysis/opus_analysis_20260409_183042_us_win_rate.md`

Tell the user the full file path before launching.

### Step 2 — Launch background Opus agent

Use the Agent tool with:
- `subagent_type`: `general-purpose`
- `model`: `opus`
- `run_in_background`: `true`

The agent prompt must include:

```
You are a deep-analysis agent for the Twilight Struggle AI project.

Working directory: /home/dkord/code/twilight-struggle-ai

Task / question:
<QUESTION>

Instructions:
1. Gather relevant context: read code, logs, results, ELO data, or memory files as needed.
2. Think carefully and thoroughly — this is an async background task, depth matters more than speed.
3. Write your full analysis to: <OUTPUT_PATH>

The output file must use this structure:
---
# Opus Analysis: <short title>
Date: <UTC timestamp>
Question: <full question>

## Executive Summary
2-4 sentence answer to the core question.

## Findings
Detailed analysis, evidence, reasoning. Use subheadings as needed.

## Conclusions
Numbered list of concrete conclusions.

## Recommendations
Numbered list of actionable next steps (if applicable).

## Open Questions
Any unresolved issues or things to verify.
---

4. After writing the file, print the Executive Summary and Conclusions sections verbatim to stdout so the calling agent can relay them immediately.
```

### Step 3 — Display immediate summary

While the background agent runs (it will surface findings via task notification), relay the summary output from the agent result directly to the user.

If the agent has not yet returned a summary (truly async), tell the user:
- The file path where full analysis will be saved
- That results will appear when the task notification fires

### Step 4 — On task notification

When the background agent completes (task-notification), read the output file and display the **Executive Summary**, **Conclusions**, and **Recommendations** sections to the user.

---

## Constraints

- Always use `model: opus` — this skill exists specifically to get Opus-level reasoning.
- Always save to `results/analysis/` so output persists across WSL restarts (never `/tmp`).
- Do not block the main conversation waiting for the agent — launch background, show summary when available.
- If the question is purely a rules lookup (no analysis needed), suggest `/rules-batcher` instead.
