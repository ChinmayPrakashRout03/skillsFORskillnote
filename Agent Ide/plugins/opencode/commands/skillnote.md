---
description: "Adaptive cognitive architecture for OpenCode. Task-adaptive execution, on-demand skill retrieval, and evidence-based verification across 32 engineering domains."
argument-format: "[<category> | <prompt>] [--all]"
---
Execute SkillNote on: $ARGUMENTS

**Directives for Assistant**:
- If `$ARGUMENTS` is empty:
  Display menu:
  `SkillNote Adaptive Engine (by Chinmay Prakash Rout)`
  - **Adaptive Task Mode**: `/skillnote <your task>` (classifies into Micro/Standard/Complex/Experimental)
  - **Targeted Category Pipeline**: `/skillnote <category>` (e.g. `/skillnote adapt`, `/skillnote secure`, `/skillnote workflow`, `/skillnote refine`)
  Ask the user what to run.

- If `$ARGUMENTS` matches any category:
  - **Small Categories (< 20 skills)** (adapt, secure, comprehend, refine, style, workflow, visualize, systematize): Execute the curated sequential pipeline.
  - **Large Categories (> 50 skills)** (versatile, assist, create, develop, automate): **Relevance-filtered by default** (select top 3–5 matching skills). Use `--all` for exhaustive sweep.

- If `$ARGUMENTS` is any engineering prompt or feature:
  1. Classify complexity: Micro (single fix) | Standard (feature/refactor) | Complex (subsystem) | Experimental (spike).
  2. Pull top 1–3 relevant skills from local catalog via SQLite FTS5 (<1ms).
  3. Safety gate: Require explicit confirmation before destructive file/schema/git actions.
  4. Observable evidence: Run real tests/linters, record exit codes (`0`) and logs. Never claim unverified success.
