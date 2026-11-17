---
description: "Master autonomous engineering engine. Supports /skillnote <prompt> or /skillnote <category>"
argument-format: "[<category> | <prompt>]"
---
Execute SkillNote on: $ARGUMENTS

**Directives for Assistant**:
- If `$ARGUMENTS` is empty:
  Display a concise menu:
  `SkillNote Master Engine (by Chinmay Prakash Rout)`
  - **Global Mode**: `/skillnote <your task>` (orchestrates across all 32 categories)
  - **Targeted Category Pipeline**: `/skillnote <category>` (e.g. `/skillnote adapt`, `/skillnote secure`, `/skillnote engineer`, `/skillnote workflow`)
  Ask the user what they would like to run.

- If `$ARGUMENTS` matches any category (adapt, assist, audit, automate, beautify, comprehend, contextualize, convert, create, curate, design, develop, engineer, execute, guide, humanize, manage, minimize, navigate, official, optimize, orchestrate, prototype, refine, secure, simplify, simulate, style, systematize, versatile, visualize, workflow):
  Navigate to `Agent Ide/skills/<Category>/` and execute **all skills present in that folder sequentially, one by one**. Report progress after each skill.

- If `$ARGUMENTS` is any other task/prompt:
  Execute full-lifecycle engineering across all 32 categories:
  1. Comprehend & Contextualize
  2. Architecture & Design (Mermaid diagrams)
  3. Clean, typed Implementation
  4. Test automation & verification
  5. Security audit (OWASP) & anti-slop refinement
  6. Git delivery & humanized summary.
