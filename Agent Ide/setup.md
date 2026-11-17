# SkillNote Agent IDE — Setup & Integration Guide

> **Curated, standardized, and maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Official Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)  
> **Maintainer Profile**: [https://github.com/ChinmayPrakashRout03](https://github.com/ChinmayPrakashRout03)

---

## 📖 Overview

**SkillNote Agent IDE** is a unified autonomous software engineering library containing over **3,700+ production-grade skills** organized into **32 distinct capability categories**. 

It standardizes autonomous execution across the top 5 modern AI coding runtimes:
1. **Claude Code** (Anthropic CLI)
2. **OpenAI Codex** (Codex CLI / Assistants)
3. **Antigravity** (Google DeepMind Agent)
4. **OpenCode** (OpenCode CLI)
5. **Z Code** (Zed AI Assistant)

---

## ⚡ Two-Part Execution System

Every platform exposes the universal `/skillnote` slash command and CLI runner, which features dynamic dual-mode routing:

```
                            ┌────────────────────────┐
                            │    /skillnote [ARGS]   │
                            └───────────┬────────────┘
                                        │
                    Does ARGS match a known category name?
                 (e.g., "adapt", "secure", "workflow", etc.)
                                        │
                       ┌────────────────┴────────────────┐
                       ▼                                 ▼
                    [ YES ]                           [ NO ]
          ┌─────────────────────────┐       ┌─────────────────────────┐
          │         PART 2          │       │         PART 1          │
          │   Targeted Category     │       │    Global Orchestration │
          │   Sequential Pipeline   │       │   Full Multi-Phase Run  │
          │ (Runs folder skills 1by1)│      │ (Decomposes any prompt) │
          └─────────────────────────┘       └─────────────────────────┘
```

### Part 1: Global Orchestration Mode (`/skillnote <prompt>`)
When passed any free-form feature request, bug fix, or project goal:
- Decomposes the prompt into a 6-phase engineering lifecycle.
- Coordinates skills across all 32 categories:
  - **Phase 1: Comprehend & Contextualize**: Map architecture, discover dependencies (`Comprehend`, `Contextualize`, `Navigate`).
  - **Phase 2: Architecture & Specification**: Formulate technical design, component layouts, and Mermaid diagrams (`Design`, `Prototype`, `Visualize`, `Style`, `Beautify`).
  - **Phase 3: Implementation & Synthesis**: Write clean, typed, modular code adhering to Guide standards (`Develop`, `Engineer`, `Create`, `Convert`).
  - **Phase 4: Automation & Execution**: Execute automated test suites and verify runtime stability (`Automate`, `Execute`, `Workflow`, `Simulate`).
  - **Phase 5: Security, Refinement & Optimization**: Audit vulnerabilities (OWASP), strip AI boilerplate, optimize memory/speed (`Audit`, `Secure`, `Refine`, `Optimize`, `Minimize`, `Simplify`).
  - **Phase 6: Delivery & Systematization**: Verify acceptance criteria, clean git history, and produce humanized documentation (`Systematize`, `Manage`, `Humanize`, `Curate`, `Official`, `Adapt`).

### Part 2: Targeted Category Sequential Execution (`/skillnote <category>`)
When passed one of the 32 category names (e.g., `/skillnote adapt`, `/skillnote secure`, `/skillnote workflow`, `/skillnote engineer`):
- Focuses exclusively on that category folder.
- Executes **all skills inside that folder sequentially, ONE BY ONE in strict order**.
- Logs each step's findings and actions.
- Delivers a consolidated summary and verification proof upon pipeline completion.

---

## 🗂️ Complete 32-Category Reference Directory

| Category | Folder Path | Skills Count | Pipeline Order / Key Skills |
| :--- | :--- | :---: | :--- |
| **Adapt** | `skills/Adapt/` | 6 | `audit-repo-quality` ➔ `list-shortcut-debt` ➔ `review-change-quality` ➔ `lazy-senior-dev` ➔ `show-savings` ➔ `show-help` |
| **Assist** | `skills/Assist/` | 447 | Broad library assists, API integrations, toolchain helpers |
| **Audit** | `skills/Audit/` | 1 | `audit-security` (comprehensive vulnerability, auth & dependency scan) |
| **Automate** | `skills/Automate/` | 69 | Automated pipelines, auto-merging, cron hooks, triggers |
| **Beautify** | `skills/Beautify/` | 1 | `design-tasteful-frontend` (aesthetic refinement & micro-interactions) |
| **Comprehend** | `skills/Comprehend/` | 8 | `ask-codebase` ➔ `build-knowledge-graph` ➔ `explain-code` ➔ `explain-diff` ➔ `extract-domain-knowledge` ➔ `graph-knowledge-base` ➔ `open-knowledge-dashboard` ➔ `write-onboarding-guide` |
| **Contextualize**| `skills/Contextualize/`| 20 | Context degradation mitigation, mental state modeling, prompt tuning |
| **Convert** | `skills/Convert/` | 1 | `convert-book-to-skill` (converting specs, books, RFCs to skills) |
| **Create** | `skills/Create/` | 113 | Architecture decision records, bootstrap agents, strategy synthesis |
| **Curate** | `skills/Curate/` | 24 | MCP server creation, brand management, visual artifacts |
| **Design** | `skills/Design/` | 1 | `design-frontend` (design system & UI component layout) |
| **Develop** | `skills/Develop/` | 71 | Interactive components, QA frameworks, browser automation |
| **Engineer** | `skills/Engineer/` | 25 | `break-down-tasks` ➔ `design-apis` ➔ `build-frontend-ui` ➔ `add-observability` ➔ `debugging` ➔ `adversarial-review` ➔ `deprecate-and-migrate` |
| **Execute** | `skills/Execute/` | 72 | Multi-step autonomous plan execution and milestone verification |
| **Guide** | `skills/Guide/` | 3 | `coding-guidelines` ➔ `coding-guidelines-project` ➔ `coding-guidelines-cursor.mdc` |
| **Humanize** | `skills/Humanize/` | 4 | `humanize-writing` ➔ `humanize-writing-claude` ➔ `humanize-writing-single-file` ➔ `humanize-writing.skill` |
| **Manage** | `skills/Manage/` | 60 | Pull request validation, issue triage, product evaluation |
| **Minimize** | `skills/Minimize/` | 6 | Code reduction, token savings, senior engineering restraint |
| **Navigate** | `skills/Navigate/` | 39 | Git safety guardrails, task decomposition, prototyping |
| **Official** | `skills/Official/` | 13 | Core Anthropic & foundational skills (`mcp-builder`, `skill-creator`, `frontend-design`, `web-artifacts-builder`, `edit-docx`, `edit-pdf`, `edit-pptx`, `edit-xlsx`, `algorithmic-art`, `doc-coauthoring`, `discernment-nudge`, `academy-guide`, `slack-gif-creator`) |
| **Optimize** | `skills/Optimize/` | 21 | Token compression, lean code generation, performance profiling |
| **Orchestrate** | `skills/Orchestrate/`| 72 | Multi-agent coordination, execution plans, phase gates |
| **Prototype** | `skills/Prototype/` | 11 | `research-app-idea` ➔ `write-mvp-prd` ➔ `write-mvp-tech-design` ➔ `select-workflow` ➔ `implement-project-slice` ➔ `add-bounded-feature` ➔ `verify-against-acceptance-criteria` ➔ `diagnose-and-fix-failure` ➔ `review-proposed-change` ➔ `prepare-handoff-context` ➔ `create-agent-instructions` |
| **Refine** | `skills/Refine/` | 8 | `clean-code-comments` ➔ `stop-ai-slop` ➔ `stop-ai-slop-pointer` ➔ `stop-ai-slop-cursor.mdc` ➔ `design-ui-without-slop` ➔ `design-for-real-people` ➔ `design-mobile-layout` ➔ `write-copy-without-slop` |
| **Secure** | `skills/Secure/` | 5 | `test-app-security` ➔ `test-owasp-top-10` ➔ `find-code-vulnerabilities` ➔ `pentest-web-app` ➔ `fix-vulnerabilities` |
| **Simplify** | `skills/Simplify/` | 1 | `write-for-adhd` (high-signal cognitive simplification) |
| **Simulate** | `skills/Simulate/` | 1 | `build-faux-product-ui` (interactive mock environments) |
| **Style** | `skills/Style/` | 6 | `build-design-system` ➔ `design-ui-ux` ➔ `style-ui` ➔ `manage-brand` ➔ `design-banners` ➔ `build-slides` |
| **Systematize**| `skills/Systematize/`| 15 | `brainstorm` ➔ `write-plans` ➔ `test-first` ➔ `develop-with-subagents` ➔ `dispatch-parallel-agents` ➔ `execute-plans` ➔ `debug-systematically` ➔ `diagnose-session` ➔ `request-code-review` ➔ `receive-code-review` ➔ `verify-before-completion` ➔ `finish-branch` ➔ `use-git-worktrees` ➔ `use-superpowers` ➔ `write-skills` |
| **Versatile** | `skills/Versatile/` | 2,646 | Deep domain capabilities across languages, frameworks, cloud |
| **Visualize** | `skills/Visualize/` | 5 | `make-diagrams` ➔ `tune-diagram-accuracy` ➔ `simplify-codebase` ➔ `improve-test-value` ➔ `review-with-evidence` |
| **Workflow** | `skills/Workflow/` | 14 | `analyzing-projects` ➔ `designing-architecture` ➔ `database-design` ➔ `convex-backend` ➔ `designing-apis` ➔ `security-patterns` ➔ `web-design-guidelines` ➔ `vercel-react-best-practices` ➔ `designing-tests` ➔ `optimizing-performance` ➔ `error-handling` ➔ `parallel-execution` ➔ `managing-git` ➔ `devops-infrastructure` |

---

## 🚀 Setup Guides per Platform

### 1. Claude Code
Install the command into your global Claude Code environment:
```bash
chmod +x "Agent Ide/plugins/claude-code/install.sh"
./"Agent Ide/plugins/claude-code/install.sh"
```
Or manually copy the command:
```bash
mkdir -p ~/.claude/commands
cp "Agent Ide/plugins/claude-code/commands/skillnote.md" ~/.claude/commands/skillnote.md
```
**Triggering in Claude Code**:
```bash
# Global mode
/skillnote create a high-performance web crawler with retry queues in TypeScript

# Targeted category mode
/skillnote adapt
/skillnote secure
/skillnote workflow
```

---

### 2. OpenAI Codex
Copy the agent contracts into your workspace root:
```bash
cp "Agent Ide/plugins/codex/CODEX.md" ./CODEX.md
cp "Agent Ide/plugins/codex/AGENTS.md" ./AGENTS.md
```
**Triggering in Codex**:
- **Interactive**: Type `/skillnote <prompt>` or `/skillnote <category>` into Codex.
- **Headless CLI**:
  ```bash
  ./"Agent Ide/plugins/codex/codex-skillnote.sh" adapt
  ./"Agent Ide/plugins/codex/codex-skillnote.sh" "build oauth2 auth service"
  ```

---

### 3. Antigravity
Install the skill into your Antigravity environment:
```bash
chmod +x "Agent Ide/plugins/antigravity/install.sh"
./"Agent Ide/plugins/antigravity/install.sh"
```
Or simply keep `Agent Ide/SKILL.md` in your project workspace.

**Triggering in Antigravity**:
```bash
/skillnote build full-stack dashboard with real-time analytics
/skillnote secure
/skillnote comprehend
```

---

### 4. OpenCode CLI
Install the command into your OpenCode configuration:
```bash
chmod +x "Agent Ide/plugins/opencode/install.sh"
./"Agent Ide/plugins/opencode/install.sh"
```
Or manually copy:
```bash
mkdir -p ~/.config/opencode/commands
cp "Agent Ide/plugins/opencode/commands/skillnote.md" ~/.config/opencode/commands/skillnote.md
```
**Triggering in OpenCode**:
```bash
opencode
> /skillnote build a distributed key-value store in Go
> /skillnote adapt
> /skillnote engineer
```

---

### 5. Z Code (Zed AI Assistant)
Install the slash command template into Zed:
```bash
chmod +x "Agent Ide/plugins/z-code/install.sh"
./"Agent Ide/plugins/z-code/install.sh"
```
Or copy manually:
```bash
mkdir -p ~/.config/zed/prompts
cp "Agent Ide/plugins/z-code/.zed/prompts/skillnote.mustache" ~/.config/zed/prompts/skillnote.mustache
```
**Triggering in Zed AI**:
Open the Assistant panel (`cmd-?` / `ctrl-?`):
```
/skillnote architect and build an event-driven microservice
/skillnote adapt
/skillnote refine
```

---

## 🛠️ Universal CLI Runner (`skillnote-runner.py`)

You can also run SkillNote directly from any shell or terminal without an AI IDE:

```bash
# List all 32 categories and skill statistics
python3 "Agent Ide/skillnote-runner.py" --list

# Inspect targeted pipeline sequence for a category
python3 "Agent Ide/skillnote-runner.py" adapt
python3 "Agent Ide/skillnote-runner.py" secure
python3 "Agent Ide/skillnote-runner.py" workflow

# Inspect multi-phase plan for an arbitrary prompt
python3 "Agent Ide/skillnote-runner.py" "create full-stack SaaS app"

# Output structured JSON for automation harnesses
python3 "Agent Ide/skillnote-runner.py" adapt --json
```

---

## 🛡️ Maintainer Statement

All skills, plugins, command runners, and documentation in this library are curated, updated, and maintained **individually and solely by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**.

- **GitHub Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)
- **Maintainer Profile**: [https://github.com/ChinmayPrakashRout03](https://github.com/ChinmayPrakashRout03)

For suggestions, issues, or new skill requests, please file an issue or pull request on the official repository.
