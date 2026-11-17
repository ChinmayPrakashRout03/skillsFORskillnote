---
description: "Master autonomous engineering engine. Adaptive cognitive architecture for AI coding agents: task-adaptive execution, on-demand skill retrieval, and evidence-based verification across 32 engineering domains."
argument-format: "[<category> | <prompt>] [--all]"
---

# /skillnote — Master Autonomous Engineering Command

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

The `/skillnote` command equips AI coding agents with an **adaptive cognitive operating layer**. It dynamically modulates reasoning based on task complexity, retrieves only the exact skills needed on demand via SQLite FTS5 (<1ms), enforces strict safety gates on destructive operations, and validates results with observable evidence before declaring success.

---

## 🎯 Command Routing Logic

Evaluate `$ARGUMENTS`:

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

---

## 🌐 Mode 1: Adaptive Task Execution (`/skillnote <prompt>`)

When the user passes a feature request, bug fix, refactor, or architectural objective:

### 1. Complexity Classification
The engine automatically modulates effort to match task scope:
- **Micro Mode** (single-file fixes, typo corrections, isolated logic patches):
  Bypasses heavy ceremony. Touches only the affected file, applies surgical edits, and runs the targeted test.
- **Standard Mode** (features, API endpoints, components, refactoring):
  Formulates a concise interface contract, writes modular code, and validates with unit/integration tests.
- **Complex Mode** (subsystems, multi-service architectures, schema migrations, security rewrites):
  Decomposes work into verifiable milestones, constructs dependency maps, and validates each layer.
- **Experimental Mode** (novel algorithms, performance spikes, exploratory spikes):
  Relaxes rigid pattern constraints to benchmark competing approaches while preserving security boundaries.

### 2. On-Demand Skill Retrieval (<1ms)
- Automatically searches the local SQLite FTS5 catalog across 3,786 primary skills.
- Loads only the 1 to 3 skills directly relevant to the objective, eliminating token bloat and context drift.

### 3. Evidence-Based Verification
- Executes real commands (`pytest`, `npm test`, linters, build runners).
- Captures exact exit codes, execution duration, and output logs.

---

## 📂 Mode 2: Targeted Category Execution (`/skillnote <category>`)

When the argument matches any of the **32 category domains**:

### Category Execution Rules:
1. **Small Categories (< 20 skills)**: Executes a curated, deterministic sequential pipeline in order.
2. **Large Categories (> 50 skills)**: **Relevance-filtered by default**. Uses SQLite FTS5 search to activate only the top 3–5 skills relevant to the current workspace. Use the `--all` flag to intentionally execute every skill sequentially.

---

### Category Directory & Curated Pipelines

#### 1. `/skillnote adapt` (or `/skillnote minimize`)
*Folder: `Agent Ide/skills/Adapt/` (6 skills)*
Executes senior-engineering minimalism and debt reduction:
1. `audit-repo-quality.md`: Scan repository layout, dead files, and dependency cleanliness.
2. `list-shortcut-debt.md`: Identify technical debt, hacks, workarounds, and temporary TODOs.
3. `review-change-quality.md`: Review recent git diffs against clean architecture standards.
4. `lazy-senior-dev.md`: Apply senior-dev pragmatism—prune bloated code, favor simple high-leverage solutions.
5. `show-savings.md`: Compute token, latency, code-line, and compute efficiency gains.
6. `show-help.md`: Output operational summary and next actions.

#### 2. `/skillnote audit` / `secure`
*Folder: `Agent Ide/skills/Audit/` & `Secure/` (6 skills)*
Executes security posture verification:
1. `test-app-security.md`: Comprehensive threat surface mapping.
2. `test-owasp-top-10.md`: Injection, broken authentication, IDOR, sensitive data exposure tests.
3. `find-code-vulnerabilities.md`: Static AST security scan for insecure dependencies and secrets.
4. `pentest-web-app.md`: Dynamic boundary and permission verification.
5. `fix-vulnerabilities.md`: Implement secure patches with regression assertions.

#### 3. `/skillnote automate`
*Folder: `Agent Ide/skills/Automate/` (69 skills · Relevance-filtered by default)*
Executes automated workflow generation and maintenance. Selects top 3–5 relevant skills (e.g. `auto-workflow.md`, `auto-merge.md`, `aeon-doctor.md`) based on repo tooling. Pass `--all` for exhaustive sweep.

#### 4. `/skillnote beautify` / `style`
*Folder: `Agent Ide/skills/Beautify/` & `Style/` (5 skills)*
Executes frontend visual elevation and aesthetic refinement:
1. `build-design-system.md`: Cohesive design tokens, typography scales, spacing units.
2. `design-ui-ux.md`: User interaction hierarchies and visual feedback.
3. `style-ui.md`: Clean styling application (Tailwind / CSS Modules / Stitches).
4. `design-tasteful-frontend.md`: Elevate micro-interactions, layout rhythm, and aesthetic craft.

#### 5. `/skillnote comprehend` / `contextualize`
*Folder: `Agent Ide/skills/Comprehend/` & `Contextualize/` (28 skills)*
Executes architectural comprehension and context optimization:
1. `ask-codebase.md`: Index and semantic search across key modules and business logic.
2. `build-knowledge-graph.md`: Map entities, services, dependencies, and external integrations.
3. `explain-code.md`: Conceptual breakdown of mission-critical files.
4. `context-compression.md`: Prune redundant context to prevent context drift.
5. `write-onboarding-guide.md`: Generate clear developer onboarding documentation.

#### 6. `/skillnote convert`
*Folder: `Agent Ide/skills/Convert/` (1 skill)*
1. `convert-book-to-skill.md`: Ingest technical specifications, RFCs, or documentation and extract structured, executable agent skills.

#### 7. `/skillnote create`
*Folder: `Agent Ide/skills/Create/` (113 skills · Relevance-filtered by default)*
Executes foundational creation, strategy modeling, and architecture bootstrapping. Selects top 3–5 matching skills (e.g. `architecture-decision.md`, `agent-bootstrap.md`, `agile-workflow.md`).

#### 8. `/skillnote curate`
*Folder: `Agent Ide/skills/Curate/` (24 skills)*
Executes curation of MCP servers, themes, artifacts, and communication assets.

#### 9. `/skillnote design` / `prototype`
*Folder: `Agent Ide/skills/Design/` & `Prototype/` (12 skills)*
Architect responsive layouts, component hierarchies, state boundaries, and rapid exploratory prototypes.

#### 10. `/skillnote develop` / `engineer`
*Folder: `Agent Ide/skills/Develop/` & `Engineer/` (106 skills · Relevance-filtered by default)*
Executes core feature development and typed engineering. Selects top 3–5 matching skills for the target framework/language.

#### 11. `/skillnote execute`
*Folder: `Agent Ide/skills/Execute/` (10 skills)*
Executes structured milestone runs, task tracking, and worktree isolation.

#### 12. `/skillnote guide`
*Folder: `Agent Ide/skills/Guide/` (11 skills)*
Enforces coding standards, simplicity principles, and engineering invariants.

#### 13. `/skillnote humanize`
*Folder: `Agent Ide/skills/Humanize/` (1 skill)*
1. `humanize-docs.md`: Rewrites synthetic, robotic AI prose into clear, authentic human communication.

#### 14. `/skillnote manage`
*Folder: `Agent Ide/skills/Manage/` (1 skill)*
1. `manage-tasks.md`: Track issue lifecycles, kanban boards, and task transitions.

#### 15. `/skillnote navigate`
*Folder: `Agent Ide/skills/Navigate/` (5 skills)*
Inspects call hierarchies, reference cross-links, and codebase symbols.

#### 16. `/skillnote official`
*Folder: `Agent Ide/skills/Official/` (20 skills)*
Executes official reference implementations for document processing, web scrapers, and data analysis.

#### 17. `/skillnote optimize`
*Folder: `Agent Ide/skills/Optimize/` (11 skills)*
Memory profiling, CPU optimization, query optimization, and latency reduction.

#### 18. `/skillnote orchestrate`
*Folder: `Agent Ide/skills/Orchestrate/` (11 skills)*
Coordinates multi-phase workflows and multi-agent delegation.

#### 19. `/skillnote refine`
*Folder: `Agent Ide/skills/Refine/` (5 skills)*
Executes anti-slop cleaning and prose pruning:
1. `clean-code-comments.md`: Remove useless, verbose, or redundant comments.
2. `stop-ai-slop.md`: Remove typical AI filler patterns, synthetic jargon, and generic boilerplate.
3. `design-ui-without-slop.md`: Strip generic gradients, floating cards, and AI-cliché layouts.
4. `write-copy-without-slop.md`: Deliver direct, concise, and genuine product copy.

#### 20. `/skillnote simplify`
*Folder: `Agent Ide/skills/Simplify/` (1 skill)*
1. `simplify-workflow.md`: Reduce cognitive overload, consolidate steps, and streamline complex procedures.

#### 21. `/skillnote simulate`
*Folder: `Agent Ide/skills/Simulate/` (1 skill)*
1. `simulate-runtime.md`: Simulate load conditions, network latency, and failure modes.

#### 22. `/skillnote systematize`
*Folder: `Agent Ide/skills/Systematize/` (15 skills)*
Executes systematic quality standards: TDD workflows, verification-before-completion, and disciplined git finish.

#### 23. `/skillnote visualize`
*Folder: `Agent Ide/skills/Visualize/` (5 skills)*
1. `make-diagrams.md`: Generate clear, accurate Mermaid/ASCII architecture diagrams.
2. `tune-diagram-accuracy.md`: Validate diagrams against concrete implementation code.
3. `simplify-codebase.md`: Visualize codebase complexity hot spots.
4. `improve-test-value.md`: Map test coverage vs value boundaries.
5. `review-with-evidence.md`: Provide evidence-backed architectural reviews.

#### 24. `/skillnote workflow`
*Folder: `Agent Ide/skills/Workflow/` (14 skills)*
Executes complete production web/cloud workflow engineering:
1. `analyzing-projects.md`: Comprehensive codebase & dependency analysis.
2. `designing-architecture.md`: Clean architecture and modularity design.
3. `database-design.md`: Schema modeling, indexing, relations, and migrations.
4. `designing-apis.md`: RESTful/GraphQL API contracts and schemas.
5. `security-patterns.md`: Secure authentication, authorization, and cryptography.
6. `designing-tests.md`: Unit, integration, and E2E testing architecture.
7. `optimizing-performance.md`: Computational and network optimization.
8. `managing-git.md`: Branching strategies, rebase hygiene, and versioning.

#### 25. `/skillnote assist`
*Folder: `Agent Ide/skills/Assist/` (447 skills · Relevance-filtered by default)*
Specialized assistant skills for libraries, SDKs, and platforms. Selects top 3–5 matching skills. Pass `--all` for exhaustive sweep.

#### 26. `/skillnote versatile`
*Folder: `Agent Ide/skills/Versatile/` (2,646 skills · Relevance-filtered by default)*
Specialized framework and cloud recipes. Selects top 3–5 skills matching your tech stack. Pass `--all` for exhaustive sweep.

---

## 🛡️ Core Invariants (Keep It Real — Zero Hawabaazi)

1. **Proof Before Claims**: Never report that code is tested or verified without executing a real command and logging the exit code. If tests cannot run, report: `NOT VERIFIED (Reason: ...)`.
2. **Safety Gates**: Request confirmation before deleting files, dropping schemas, modifying credentials, or force-pushing.
3. **Honest Limitations**: State external dependencies, missing environment variables, or manual operational steps clearly.

---

## 📋 Response Format Contract

When executing `/skillnote`:
1. **Mode**: State the active mode (`Micro`, `Standard`, `Complex`, `Experimental`, or `Targeted Category`).
2. **Activated Skills**: List the 1–3 targeted skills selected on demand.
3. **Changes**: Link modified files with concise explanations of changes.
4. **Observable Evidence**: Output real test commands, exit codes (`0`), duration, and test output.
5. **Limitations & Next Steps**: Note any unverified items or manual verification steps needed.
