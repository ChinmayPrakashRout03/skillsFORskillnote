---
name: skillnote
description: Adaptive cognitive architecture and autonomous engineering runtime for AI agents. Provides task-complexity classification, on-demand SQLite FTS5 skill retrieval, safety gates, and observable verification across 32 specialized engineering domains.
author: Chinmay Prakash Rout
repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote
---

# SkillNote — Adaptive Cognitive Architecture for AI Coding Agents

SkillNote serves as an **adaptive cognitive operating layer** for AI coding agents (**Antigravity**, **Claude Code**, **OpenCode**, **OpenAI Codex**, and **ZCode**). 

Standard AI agents typically oscillate between two extremes: jumping blindly into code without planning, or drowning in massive prompt checklists that waste tokens and produce simulated claims of success. SkillNote bridges this gap by giving the agent a structured cognitive brain: it classifies task complexity, pulls only the exact skills needed on demand, respects safety boundaries, and requires observable evidence before declaring work complete.

---

## 🧠 Core Architecture: How the Cognitive Engine Operates

```
                            ┌────────────────────────┐
                            │    /skillnote [TASK]   │
                            └───────────┬────────────┘
                                        │
                         [ 1. Task Complexity Classifier ]
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           ▼                            ▼                            ▼
      [ MICRO ]                   [ STANDARD ]                 [ EXPERIMENTAL ]
   Targeted fix                Plan ➔ Code ➔ Test          Hypothesis exploration
  (Budget: ~3k tokens)        (Budget: ~20k tokens)         (Budget: ~20k tokens)
           │                            │                            │
           └────────────────────────────┼────────────────────────────┘
                                        │
                       [ 2. SQLite FTS5 Skill Router ]
                 (Selects top 1–3 targeted skills in <1ms)
                                        │
                        [ 3. Safety & Approval Gate ]
                 (Pauses for user approval on destructive actions)
                                        │
                     [ 4. Evidence Verification Engine ]
                 (Executes real tests: exit code, duration, logs)
                                        │
                      [ 5. Observable Verification Report ]
```

---

## ⚡ Dual Execution Modes

### Mode 1: Adaptive Task Execution (`/skillnote <prompt>`)
When passed a prompt, feature request, bug description, or architectural objective:

1. **Complexity Classification**:
   - **Micro Mode** (single-file fixes, typo corrections, isolated logic patches):
     Bypasses heavy planning rituals. Touches only the target file, applies surgical edits, and executes the targeted test.
   - **Standard Mode** (features, API endpoints, UI components, targeted refactors):
     Formulates a clear interface contract, implements modular code, and validates with unit/integration tests.
   - **Complex Mode** (subsystems, multi-service architectures, migrations, security audits):
     Breaks work into verifiable milestones, maps dependencies, and validates each layer systematically.
   - **Experimental Mode** (novel algorithms, performance spikes, exploratory prototypes):
     Relaxes rigid pattern constraints to benchmark competing approaches while preserving security and correctness boundaries.

2. **On-Demand Skill Retrieval**:
   - Queries the local SQLite FTS5 catalog across 3,786 primary skills in `<1ms`.
   - Injects only the 1 to 3 most relevant skills into working memory, preserving token budget and avoiding context drift.

3. **Evidence-Based Delivery**:
   - Executes real commands (`pytest`, `npm test`, linters, build scripts).
   - Reports exact exit codes, execution durations, and test logs.

---

### Mode 2: Targeted Category Execution (`/skillnote <category>`)
When passed one of the **32 category names**:

- **Curated Pipelines (< 20 skills)**: Executes a deterministic, sequential engineering pipeline:
  - `adapt` / `minimize`: `audit-repo-quality` ➔ `list-shortcut-debt` ➔ `review-change-quality` ➔ `lazy-senior-dev` ➔ `show-savings`
  - `secure` / `audit`: `test-app-security` ➔ `test-owasp-top-10` ➔ `find-code-vulnerabilities` ➔ `pentest-web-app` ➔ `fix-vulnerabilities`
  - `comprehend` / `contextualize`: `ask-codebase` ➔ `build-knowledge-graph` ➔ `explain-code` ➔ `extract-domain-knowledge` ➔ `write-onboarding-guide`
  - `refine`: `clean-code-comments` ➔ `stop-ai-slop` ➔ `design-ui-without-slop` ➔ `design-for-real-people` ➔ `write-copy-without-slop`
  - `style` / `beautify`: `build-design-system` ➔ `design-ui-ux` ➔ `style-ui` ➔ `design-tasteful-frontend`
  - `workflow`: `analyzing-projects` ➔ `designing-architecture` ➔ `database-design` ➔ `designing-apis` ➔ `designing-tests` ➔ `optimizing-performance`

- **Large Categories (> 50 skills)** (e.g. `Versatile` [2,646], `Assist` [447], `Create` [113], `Develop` [71], `Automate` [69]):
  - **Relevance-Filtered by Default**: Uses SQLite FTS5 search to select only the top 3–5 skills matching the active workspace. Avoids impractical context bloat.
  - **Explicit Exhaustive Flag (`--all`)**: Available if a full sequential sweep across every skill in the category is explicitly requested.

---

## 🛡️ Core Operating Invariants (No Hawabaazi, Keep It Real)

1. **Proof Before Claims (Zero Process Theater)**:
   - Never declare an implementation "tested", "secure", or "production-ready" without running real commands.
   - If tests cannot be run (e.g. missing external credentials, no test runner installed), explicitly report: `STATUS: NOT VERIFIED (Reason: <concrete explanation>)`.
   - Never manufacture synthetic compliance reports.

2. **Safety & Destructive Action Gates**:
   - The agent MUST pause and request user confirmation before:
     - Deleting non-trivial files or directories.
     - Dropping database tables or executing destructive migrations.
     - Modifying secret keys, environment variables, or access permissions.
     - Rewriting git history via force-pushes or upstream rebases.

3. **Conflict Resolution Hierarchy**:
   - `User Security & Permissions` > `Project Invariants & Linters` > `SkillNote Guidelines` > `Agent Defaults`.

4. **Transparent Boundaries & Limitations**:
   - If a solution requires manual steps (e.g. DNS configuration, payment gateway keys, cloud IAM provisioning), document them explicitly as remaining action items rather than glossing over them.

---

## 📊 Catalog Distribution (32 Categories · 3,786 Primary Skills)

| Domain | Categories | Focus |
| :--- | :--- | :--- |
| **Discovery & Context** | `Comprehend`, `Contextualize`, `Navigate` | Topology mapping, dependency trees, context degradation defense |
| **Architecture & Aesthetics** | `Design`, `Prototype`, `Visualize`, `Style`, `Beautify` | Interface specifications, UI tokens, Mermaid diagrams, clean UX |
| **Engineering & Synthesis** | `Develop`, `Engineer`, `Create`, `Convert` | Modular typed code, API contracts, refactoring, resilience |
| **Execution & Automation** | `Automate`, `Execute`, `Workflow`, `Simulate` | Test suites, CI/CD, migration pipelines, runtime assertions |
| **Security & Optimization** | `Audit`, `Secure`, `Refine`, `Optimize`, `Minimize`, `Simplify` | OWASP Top 10, anti-slop pruning, memory/token efficiency |
| **Governance & Delivery** | `Guide`, `Manage`, `Humanize`, `Systematize`, `Curate`, `Official` | Coding standards, PR review, authentic documentation, git finish |
| **Domain Specialization** | `Versatile`, `Assist`, `Adapt` | 2,646+ specialized framework, language, and cloud implementations |

---

## 📋 Response Format Contract

When responding to `/skillnote`:
1. **Mode**: State the selected execution mode (`Micro`, `Standard`, `Complex`, `Experimental`, or `Targeted Category`).
2. **Activated Skills**: List the 1–3 skills retrieved on demand.
3. **Changes**: Link modified files with concise explanations of structural changes.
4. **Observable Evidence**: Display exact command executed, exit code, execution time, and test summary.
5. **Limitations & Next Steps**: Note any remaining manual requirements or unverified boundaries.
