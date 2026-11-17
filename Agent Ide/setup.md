# SkillNote Agent IDE — Setup & Integration Guide

> **Curated, standardized, and maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Official Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)  
> **Maintainer Profile**: [https://github.com/ChinmayPrakashRout03](https://github.com/ChinmayPrakashRout03)

---

## 📖 Overview

**SkillNote** is an **Adaptive Cognitive Architecture and Autonomous Engineering Runtime** for AI coding agents. It provides a structured cognitive operating layer across the top 5 modern AI coding environments:
1. **Claude Code** (Anthropic CLI)
2. **Antigravity** (Google DeepMind Agent)
3. **OpenCode** (OpenCode CLI)
4. **OpenAI Codex** (Codex CLI / Assistants)
5. **ZCode.app & Zed** (ZCode & Zed Assistant)

Instead of relying on unguided code generation or rigid prose checklists that waste tokens, SkillNote gives AI agents an adaptive cognitive brain: it classifies task complexity, queries a local pre-indexed SQLite FTS5 catalog to retrieve only relevant skills in `<1ms`, pauses at safety gates before destructive actions, and demands observable evidence (exit codes, real test output) before claiming success.

---

## ⚡ Instant One-Line Install (Zero Download Needed)

Any user on macOS or Linux can install SkillNote across all supported AI coding agents with a single command — **without manually cloning or downloading the repository**:

```bash
curl -fsSL https://raw.githubusercontent.com/ChinmayPrakashRout03/skillsFORskillnote/main/install.sh | bash
```

This single command:
1. Installs the **SkillNote Adaptive Runtime** and pre-indexed SQLite FTS5 catalog into `~/.skillnote`.
2. Configures the `/skillnote` command across all active AI coding agents.
3. Provides a global `skillnote` CLI utility (`skillnote search`, `skillnote route`, `skillnote verify`).

---

## ⚡ Dual Execution System

Every platform exposes the universal `/skillnote` command with dynamic routing:

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
          │         MODE 2          │       │         MODE 1          │
          │    Targeted Category    │       │  Adaptive Task Engine   │
          │   (Curated / Filtered)  │       │  (Micro/Std/Cplx/Expt)  │
          └─────────────────────────┘       └─────────────────────────┘
```

### Mode 1: Adaptive Task Execution (`/skillnote <prompt>`)
When passed a prompt, feature request, bug fix, or architectural objective:
1. **Complexity Modulation**:
   - **Micro Mode** (single-file fixes, typo corrections, isolated logic patches): Surgical patch + direct test. ~3k token budget.
   - **Standard Mode** (features, API endpoints, components, refactoring): Architecture contract ➔ modular code ➔ test suite. ~20k token budget.
   - **Complex Mode** (subsystems, multi-service architectures, schema migrations): Phased milestones, dependency maps, systematic verification. ~60k token budget.
   - **Experimental Mode** (novel algorithms, performance spikes): Benchmarks competing approaches with relaxed constraints while strictly maintaining safety invariants.
2. **On-Demand Skill Retrieval (<1ms)**: Pulls only the 1–3 most relevant skills from the SQLite FTS5 catalog.
3. **Safety & Destructive Action Gates**: Prompts for explicit confirmation before file deletions, table drops, or git history rewrites.
4. **Observable Evidence**: Requires real command execution (`pytest`, `npm test`, linters) with logged exit codes (`0`).

### Mode 2: Targeted Category Execution (`/skillnote <category>`)
When passed one of the 32 category names (e.g., `/skillnote adapt`, `/skillnote secure`, `/skillnote workflow`):
- **Curated Pipelines (< 20 skills)**: Executes a deterministic, sequential engineering pipeline step-by-step.
- **Large Categories (> 50 skills)** (`Versatile` [2,646], `Assist` [447], `Create` [113], `Develop` [71], `Automate` [69]): **Relevance-filtered by default** (selects top 3–5 skills matching current workspace). An explicit `--all` flag is available for intentional exhaustive runs.

---

## 🗂️ Complete 32-Category Reference Directory

| Category | Folder Path | Skills Count | Execution Profile |
| :--- | :--- | :---: | :--- |
| **Adapt** | `skills/Adapt/` | 6 | Curated sequential: `audit-repo-quality` ➔ `list-shortcut-debt` ➔ `review-change-quality` ➔ `lazy-senior-dev` ➔ `show-savings` ➔ `show-help` |
| **Assist** | `skills/Assist/` | 447 | Relevance-filtered by default (top 3–5 matching skills); `--all` for full sweep |
| **Audit** | `skills/Audit/` | 1 | `audit-security` (comprehensive vulnerability, auth & dependency scan) |
| **Automate** | `skills/Automate/` | 69 | Relevance-filtered by default (top 3–5 matching workflow automations) |
| **Beautify** | `skills/Beautify/` | 1 | `design-tasteful-frontend` (aesthetic refinement & micro-interactions) |
| **Comprehend** | `skills/Comprehend/` | 8 | Curated sequential: `ask-codebase` ➔ `build-knowledge-graph` ➔ `explain-code` ➔ `extract-domain-knowledge` ➔ `write-onboarding-guide` |
| **Contextualize**| `skills/Contextualize/`| 20 | Context degradation mitigation, mental state modeling, prompt tuning |
| **Convert** | `skills/Convert/` | 1 | `convert-book-to-skill` (converting specs, books, RFCs to skills) |
| **Create** | `skills/Create/` | 113 | Relevance-filtered by default (ADRs, bootstrap agents, strategy synthesis) |
| **Curate** | `skills/Curate/` | 24 | Curated: MCP servers, brand management, visual artifacts |
| **Design** | `skills/Design/` | 1 | `design-frontend` (design system & UI component layout) |
| **Develop** | `skills/Develop/` | 71 | Relevance-filtered by default (interactive components, QA, browser automation) |
| **Engineer** | `skills/Engineer/` | 25 | Curated sequential: `break-down-tasks` ➔ `design-apis` ➔ `build-frontend-ui` ➔ `add-observability` ➔ `debugging` ➔ `adversarial-review` |
| **Execute** | `skills/Execute/` | 72 | Relevance-filtered by default (milestone execution, task tracking) |
| **Guide** | `skills/Guide/` | 3 | Curated: `coding-guidelines` ➔ `coding-guidelines-project` ➔ `coding-guidelines-cursor.mdc` |
| **Humanize** | `skills/Humanize/` | 4 | Curated: `humanize-writing` (removes robotic AI patterns, natural communication) |
| **Manage** | `skills/Manage/` | 60 | Relevance-filtered by default (PR validation, issue triage, product evaluation) |
| **Minimize** | `skills/Minimize/` | 6 | Curated sequential: code reduction, token savings, senior engineering restraint |
| **Navigate** | `skills/Navigate/` | 39 | Relevance-filtered by default (symbol navigation, call hierarchies) |
| **Official** | `skills/Official/` | 13 | Curated: foundational skills (`mcp-builder`, `skill-creator`, `web-artifacts-builder`, `doc-coauthoring`) |
| **Optimize** | `skills/Optimize/` | 21 | Relevance-filtered by default (memory profiling, CPU/query optimization) |
| **Orchestrate** | `skills/Orchestrate/`| 72 | Relevance-filtered by default (multi-agent coordination, phase gates) |
| **Prototype** | `skills/Prototype/` | 11 | Curated sequential: `research-app-idea` ➔ `write-mvp-prd` ➔ `write-mvp-tech-design` ➔ `implement-project-slice` ➔ `verify-acceptance` |
| **Refine** | `skills/Refine/` | 8 | Curated sequential: `clean-code-comments` ➔ `stop-ai-slop` ➔ `design-ui-without-slop` ➔ `write-copy-without-slop` |
| **Secure** | `skills/Secure/` | 5 | Curated sequential: `test-app-security` ➔ `test-owasp-top-10` ➔ `find-code-vulnerabilities` ➔ `pentest-web-app` ➔ `fix-vulnerabilities` |
| **Simplify** | `skills/Simplify/` | 1 | `write-for-adhd` (high-signal cognitive simplification) |
| **Simulate** | `skills/Simulate/` | 1 | `build-faux-product-ui` (interactive mock environments) |
| **Style** | `skills/Style/` | 6 | Curated sequential: `build-design-system` ➔ `design-ui-ux` ➔ `style-ui` ➔ `manage-brand` |
| **Systematize**| `skills/Systematize/`| 15 | Curated sequential: `brainstorm` ➔ `write-plans` ➔ `test-first` ➔ `execute-plans` ➔ `verify-before-completion` ➔ `finish-branch` |
| **Versatile** | `skills/Versatile/` | 2,646 | Relevance-filtered by default (top 3–5 matching skills); `--all` for full sweep |
| **Visualize** | `skills/Visualize/` | 5 | Curated sequential: `make-diagrams` ➔ `tune-diagram-accuracy` ➔ `simplify-codebase` ➔ `improve-test-value` |
| **Workflow** | `skills/Workflow/` | 14 | Curated sequential: `analyzing-projects` ➔ `designing-architecture` ➔ `database-design` ➔ `designing-apis` ➔ `designing-tests` ➔ `optimizing-performance` |

---

## 🚀 Setup Guides per Platform

### 1. Claude Code
Install the command into your global Claude Code environment:
```bash
chmod +x "Agent Ide/plugins/claude-code/install.sh"
./"Agent Ide/plugins/claude-code/install.sh"
```
**Triggering in Claude Code**:
```bash
# Adaptive task execution
/skillnote create a high-performance web crawler with retry queues in TypeScript

# Targeted category pipelines
/skillnote adapt
/skillnote secure
/skillnote workflow
```

---

### 2. Antigravity
Install the skill into your Antigravity environment:
```bash
chmod +x "Agent Ide/plugins/antigravity/install.sh"
./"Agent Ide/plugins/antigravity/install.sh"
```
Or keep `Agent Ide/SKILL.md` in your project workspace.

**Triggering in Antigravity**:
```bash
/skillnote build full-stack dashboard with real-time analytics
/skillnote secure
/skillnote comprehend
```

---

### 3. OpenCode CLI
Install the command into your OpenCode configuration:
```bash
chmod +x "Agent Ide/plugins/opencode/install.sh"
./"Agent Ide/plugins/opencode/install.sh"
```
**Triggering in OpenCode**:
```bash
opencode
> /skillnote build a distributed key-value store in Go
> /skillnote adapt
> /skillnote workflow
```

---

### 4. OpenAI Codex
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

### 5. ZCode.app & Zed
Install the plugin into ZCode.app and Zed:
```bash
chmod +x "Agent Ide/plugins/z-code/install.sh"
./"Agent Ide/plugins/z-code/install.sh"
```
**Triggering in ZCode.app**:
- Type `@skillnote` or `/skillnote` in the chat input.

**Triggering in Zed AI**:
- Open the Assistant panel (`cmd-?` / `ctrl-?`) and type `/skillnote <task>`.

---

## 🛠️ CLI Utilities & Verification

You can also run SkillNote operations directly from any terminal:

```bash
# Search skills via SQLite FTS5 (<1ms)
python3 "Agent Ide/scripts/skillnote.py" search "jwt authentication security"

# Route a task and inspect the selected mode and skills
python3 "Agent Ide/scripts/skillnote.py" route "fix null check in userService"

# Verify test execution and record observable evidence
python3 "Agent Ide/scripts/skillnote.py" verify -- pytest tests/
```

---

## 🛡️ Maintainer Statement

All skills, plugins, command runners, and documentation in this library are curated, updated, and maintained **individually and solely by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**.

- **GitHub Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)
- **Maintainer Profile**: [https://github.com/ChinmayPrakashRout03](https://github.com/ChinmayPrakashRout03)
