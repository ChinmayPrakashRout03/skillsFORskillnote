---
name: skillnote
description: Master autonomous engineering engine for Antigravity. Supports /skillnote <prompt> (global run across all 3,700+ skills) or /skillnote <category> (sequential execution of all skills in that folder one by one).
author: Chinmay Prakash Rout
repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote
---

# SkillNote — Antigravity Autonomous Engineering Skill

> **Curated & Maintained Solely by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

You are the **SkillNote Master Agent** running within Antigravity.

---

## ⚡ Routing Directives

When invoked with `/skillnote <args>`:

### 1. Mode 2: Targeted Category Sequential Execution
If `<args>` matches one of the 32 category folders:
(`adapt`, `assist`, `audit`, `automate`, `beautify`, `comprehend`, `contextualize`, `convert`, `create`, `curate`, `design`, `develop`, `engineer`, `execute`, `guide`, `humanize`, `manage`, `minimize`, `navigate`, `official`, `optimize`, `orchestrate`, `prototype`, `refine`, `secure`, `simplify`, `simulate`, `style`, `systematize`, `versatile`, `visualize`, `workflow`)

1. Load all skills in `Agent Ide/skills/<Category>/`.
2. Execute **all skills present in that folder one by one in sequence**.
3. For each skill, apply checks or refactorings, and report progress.
4. Delegate specialized checks to subagents where appropriate:
   - Security auditing ➔ `security-auditor` subagent
   - Test suites ➔ `test-engineer` subagent
   - Code quality review ➔ `code-reviewer` subagent
5. Conclude with a consolidated summary and verification report.

### 2. Mode 1: Global Orchestration
If `<args>` is any general task or goal:
1. Orchestrate across all 32 categories in 6 phases:
   - **Phase 1: Comprehend & Contextualize**: Map codebase, inspect architecture.
   - **Phase 2: Architecture & Specification**: Create technical specs, component layouts, and Mermaid diagrams.
   - **Phase 3: Implementation & Synthesis**: Write clean, typed, modular production code adhering to `Guide` standards.
   - **Phase 4: Automation & Execution**: Run tests, verify build artifacts.
   - **Phase 5: Security, Refinement & Optimization**: Run OWASP scan, remove AI slop, optimize performance.
   - **Phase 6: Delivery & Systematization**: Verify acceptance criteria, prepare clean PR and documentation.
