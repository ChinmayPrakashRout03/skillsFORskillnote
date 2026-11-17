---
description: "Master autonomous engineering engine. Executes all SkillNote skills globally for general prompts, or runs all skills inside a category folder sequentially one by one."
argument-format: "[<category> | <prompt>]"
---

# /skillnote — Master Autonomous Engineering Command

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

The `/skillnote` command is the universal entrypoint for the **SkillNote Agent IDE** library. It operates in two powerful modes based on the input argument provided by the user.

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
         │   Targeted Category     │       │    Global Orchestration │
         │   Sequential Pipeline   │       │   Full Multi-Phase Run  │
         │ (Runs folder skills 1by1)│       │ (Decomposes any prompt) │
         └─────────────────────────┘       └─────────────────────────┘
```

---

## 🌐 Mode 1: Global Orchestration (`/skillnote <prompt>`)

When the user passes any general feature request, debugging task, architectural design, or open-ended instruction that is **not** a single category name:

### Global Execution Protocol
1. **Context & Comprehension Phase**:
   - Activate skills from `Contextualize`, `Comprehend`, and `Navigate`.
   - Scan repository topology, detect languages, frameworks, and architecture.
   - Extract domain constraints and codebase invariants.

2. **Architecture & Specification Phase**:
   - Activate skills from `Design`, `Prototype`, `Visualize`, `Style`, and `Beautify`.
   - Produce technical specification, UI/UX aesthetics, and system diagrams (Mermaid/ASCII).

3. **Engineering & Implementation Phase**:
   - Activate skills from `Develop`, `Engineer`, `Create`, and `Convert`.
   - Write typed, tested, resilient production code with zero shortcuts.
   - Follow strict project guidelines from `Guide`.

4. **Automation & Execution Phase**:
   - Activate skills from `Automate`, `Execute`, `Workflow`, and `Simulate`.
   - Run tests, compile artifacts, automate validation scripts, and verify runtime behavior.

5. **Security, Refinement & Optimization Phase**:
   - Activate skills from `Audit`, `Secure`, `Refine`, `Optimize`, `Minimize`, and `Simplify`.
   - Run security audit (OWASP Top 10, secret detection, access control).
   - Strip AI boilerplate and synthetic complexity (`stop-ai-slop`, `clean-code-comments`).
   - Profile performance and optimize resource usage.

6. **Delivery & Systematization Phase**:
   - Activate skills from `Systematize`, `Manage`, `Humanize`, `Curate`, `Official`, and `Adapt`.
   - Verify all acceptance criteria before completion.
   - Generate clear, humanized PR description and commit logs.

---

## 📂 Mode 2: Targeted Category Sequential Execution (`/skillnote <category>`)

When the argument matches any of the **32 category folders** (case-insensitive), execute **all skills located in that specific category folder sequentially, ONE BY ONE**.

### Category Index & Step-by-Step Execution Sequence

#### 1. `/skillnote adapt` (or `/skillnote minimize`)
*Folder: `Agent Ide/skills/Adapt/` (6 skills)*
Executes senior-engineering minimalism, repo hygiene, and debt reduction:
1. `audit-repo-quality.md`: Scan repository health, layout, dead files, and dependency cleanliness.
2. `list-shortcut-debt.md`: Identify technical debt, hacks, workarounds, and temporary TODOs.
3. `review-change-quality.md`: Review recent git diffs against clean architecture standards.
4. `lazy-senior-dev.md`: Apply senior-dev pragmatism—prune bloated code, favor simple high-leverage solutions.
5. `show-savings.md`: Compute token, latency, code-line, and compute efficiency gains.
6. `show-help.md`: Output operational summary and next actions.

#### 2. `/skillnote audit`
*Folder: `Agent Ide/skills/Audit/` (1 skill)*
Executes comprehensive vulnerability and security posture scanning:
1. `audit-security.md`: Audit codebase for security vulnerabilities, exposed credentials, dangerous dependencies, injection vectors, and compliance risks.

#### 3. `/skillnote automate`
*Folder: `Agent Ide/skills/Automate/` (69 skills)*
Executes automated workflow generation and maintenance:
1. `action-converter.md` -> `aeon-doctor.md` -> `aeon-update.md` -> `anatomy.md` -> `auto-merge.md` -> `auto-workflow.md` -> `autoresearch.md` -> remaining automation skills in order.
Scans triggers, builds CI/CD automations, establishes autonomous hooks, and validates auto-execution.

#### 4. `/skillnote beautify`
*Folder: `Agent Ide/skills/Beautify/` (1 skill)*
Executes frontend visual elevation and aesthetic refinement:
1. `design-tasteful-frontend.md`: Inspect UI components, typography, color harmony, visual rhythm, micro-interactions, and elevate aesthetic craft to world-class level.

#### 5. `/skillnote comprehend`
*Folder: `Agent Ide/skills/Comprehend/` (8 skills)*
Executes deep architectural comprehension and onboarding synthesis:
1. `ask-codebase.md`: Index and semantic search across key modules and business logic.
2. `build-knowledge-graph.md`: Map entities, services, dependencies, and external integrations.
3. `explain-code.md`: Provide deep conceptual breakdown of mission-critical files.
4. `explain-diff.md`: Analyze recent commits and PR changes with contextual rationale.
5. `extract-domain-knowledge.md`: Extract core business rules, entity models, and domain constraints.
6. `graph-knowledge-base.md`: Generate structured visual architecture maps and dependency graphs.
7. `open-knowledge-dashboard.md`: Synthesize project topology into a scannable architectural dashboard.
8. `write-onboarding-guide.md`: Generate comprehensive developer onboarding documentation.

#### 6. `/skillnote contextualize`
*Folder: `Agent Ide/skills/Contextualize/` (20 skills)*
Executes context window optimization, mental state modeling, and prompt engineering:
1. `context-fundamentals.md` -> `context-compression.md` -> `context-degradation.md` -> `bdi-mental-states.md` -> `context-optimization.md` -> `advanced-evaluation.md` -> remaining contextualize skills.
Prevents context drift, reduces token bloat, and aligns agent memory states.

#### 7. `/skillnote convert`
*Folder: `Agent Ide/skills/Convert/` (1 skill)*
Executes specification and literature transformation:
1. `convert-book-to-skill.md`: Ingest technical specifications, RFCs, or documentation and extract structured, executable agent skills.

#### 8. `/skillnote create`
*Folder: `Agent Ide/skills/Create/` (113 skills)*
Executes foundational creation, strategy modeling, and architecture bootstrapping:
1. `architecture-decision.md` -> `agent-bootstrap.md` -> `abstract-strategy.md` -> `agile-coordinator.md` -> `agile-workflow.md` -> remaining create skills in sequence.
Bootstraps architectures, initializes ADRs, and produces core system assets.

#### 9. `/skillnote curate`
*Folder: `Agent Ide/skills/Curate/` (24 skills)*
Executes curation of MCP servers, themes, artifacts, and communication assets:
1. `build-mcp-servers.md` -> `build-html-artifacts.md` -> `build-themes.md` -> `apply-anthropic-brand.md` -> `create-skills.md` -> remaining curate skills.

#### 10. `/skillnote design`
*Folder: `Agent Ide/skills/Design/` (1 skill)*
Executes frontend system design and layout architecture:
1. `design-frontend.md`: Architect responsive layouts, component hierarchies, state boundaries, styling paradigms, and accessibility compliance.

#### 11. `/skillnote develop`
*Folder: `Agent Ide/skills/Develop/` (71 skills)*
Executes interactive development, QA, browser automation, and feature construction:
1. `capability-architect.md` -> `application-quality-assurance.md` -> `browser-automation-framework.md` -> `interactive-component-creator.md` -> `branch-finalization.md` -> remaining develop skills.

#### 12. `/skillnote engineer`
*Folder: `Agent Ide/skills/Engineer/` (25 skills)*
Executes core engineering rigor, refactoring, and constraint enforcement:
1. `break-down-tasks.md`: Decompose complex technical goals into discrete verifiable slices.
2. `design-apis.md`: Design clean, versioned, typed API contracts and schemas.
3. `build-frontend-ui.md`: Build resilient, accessible user interface components.
4. `add-observability.md`: Integrate telemetry, structured logging, metrics, and tracing.
5. `debugging.md`: Isolate root causes with scientific hypothesis testing.
6. `adversarial-review.md`: Red-team implementation for edge cases and regressions.
7. `deprecate-and-migrate.md`: Safely migrate legacy code and deprecate obsolete APIs.
8. `enforce-quality-constraints.md` -> `harden-security.md` -> `optimize-performance.md` -> remaining engineer skills.

#### 13. `/skillnote execute` (or `/skillnote orchestrate`)
*Folder: `Agent Ide/skills/Execute/` & `Orchestrate/` (72 skills)*
Executes autonomous multi-step execution and milestone auditing:
1. `capture-ideas.md` -> `ai-design-contract.md` -> `autonomous-execution.md` -> `validate-phase.md` -> `audit-milestone.md` -> `audit-fix-pipeline.md` -> `complete-milestone.md` -> `cleanup-archive.md`.

#### 14. `/skillnote guide`
*Folder: `Agent Ide/skills/Guide/` (3 skills)*
Executes coding guidelines and linting contract enforcement:
1. `coding-guidelines.md`: Enforce foundational engineering principles and defensive practices.
2. `coding-guidelines-project.md`: Validate project-specific architectural rules and module boundaries.
3. `coding-guidelines-cursor.mdc`: Verify IDE/Cursor editor linting and formatting configuration.

#### 15. `/skillnote humanize`
*Folder: `Agent Ide/skills/Humanize/` (4 skills)*
Executes human-like communication and writing cleanup:
1. `humanize-writing.md`: Strip corporate jargon, passive voice, and synthetic AI phrasing.
2. `humanize-writing-claude.md`: Calibrate natural prose flow and clarity.
3. `humanize-writing-single-file.md`: Humanize documentation and comments across targeted files.
4. `humanize-writing.skill`: Verify output readability against human editorial standards.

#### 16. `/skillnote manage`
*Folder: `Agent Ide/skills/Manage/` (60 skills)*
Executes project management, PR validation, and evaluation tracking:
1. `check-pr.md`: Audit pull requests for merge readiness, test coverage, and hygiene.
2. `add-product-e2e-eval.md`: Establish end-to-end product evaluation criteria.
3. `add-runner-eval.md`: Benchmark agent runner execution performance.
4. `content-calendar.md` -> `create-case.md` -> remaining manage skills.

#### 17. `/skillnote navigate`
*Folder: `Agent Ide/skills/Navigate/` (39 skills)*
Executes architectural navigation, git protection, and task decomposition:
1. `block-dangerous-git.md`: Enforce git safety guards (prevent destructive force pushes).
2. `break-into-tickets.md`: Split features into scoped, trackable work units.
3. `design-codebase.md`: Navigate system boundaries and module separation.
4. `build-prototype.md`: Rapidly navigate from concept to working prototype.
5. `coordinate-long-goal.md` -> remaining navigate skills.

#### 18. `/skillnote official`
*Folder: `Agent Ide/skills/Official/` (13 skills)*
Executes official Anthropic/Agent foundational toolchains:
1. `skill-creator.md`: Audit and author new production-ready agent skills.
2. `mcp-builder.md`: Build and test Model Context Protocol servers.
3. `frontend-design.md`: Enforce modern frontend design standards.
4. `web-artifacts-builder.md`: Generate self-contained HTML/React artifacts.
5. `edit-docx.md`: Read, generate, and edit Word documents.
6. `edit-pdf.md`: Inspect, parse, and manipulate PDF documents.
7. `edit-pptx.md`: Create and format PowerPoint presentations.
8. `edit-xlsx.md`: Create and calculate Excel spreadsheets with formulas.
9. `algorithmic-art.md`: Generate SVG/Canvas generative art.
10. `doc-coauthoring.md`: Co-author documents with structured feedback loops.
11. `discernment-nudge.md`: Apply critical reasoning and assumption checking.
12. `academy-guide.md`: Produce structured developer learning modules.
13. `slack-gif-creator.md`: Create developer communication graphics.

#### 19. `/skillnote optimize`
*Folder: `Agent Ide/skills/Optimize/` (21 skills)*
Executes performance, token, and system optimization:
1. `explore-repo-readonly.md`: Read-only zero-risk exploration of performance bottlenecks.
2. `compress-context.md`: Compress agent context to minimum necessary tokens.
3. `build-lean.md`: Refactor code for minimal memory footprint and execution cycles.
4. `caveman-ultra.md`: Strip verbose prose to raw high-density instructions.
5. `evaluate-optimization.md`: Measure speedup and resource improvements.
6. `delegate-to-crew.md` -> remaining optimize skills.

#### 20. `/skillnote prototype`
*Folder: `Agent Ide/skills/Prototype/` (11 skills)*
Executes rapid vertical slice validation from idea to testable prototype:
1. `research-app-idea.md`: Rapid technical feasibility and competitive scan.
2. `write-mvp-prd.md`: Formulate focused Minimal Viable Product specifications.
3. `write-mvp-tech-design.md`: Author lightweight technical architecture.
4. `select-workflow.md`: Choose fastest reliable stack and tooling.
5. `implement-project-slice.md`: Build working end-to-end slice.
6. `add-bounded-feature.md`: Expand prototype with isolated feature increments.
7. `verify-against-acceptance-criteria.md`: Test prototype against initial goals.
8. `diagnose-and-fix-failure.md`: Quick-fix prototype edge cases.
9. `review-proposed-change.md`: Code quality check before demo.
10. `prepare-handoff-context.md`: Package architecture context for production team.
11. `create-agent-instructions.md`: Generate tailored agent prompt instructions.

#### 21. `/skillnote refine`
*Folder: `Agent Ide/skills/Refine/` (8 skills)*
Executes slop removal, code cleanup, and authentic human-centered polish:
1. `clean-code-comments.md`: Remove redundant, noisy, or hallucinated comments.
2. `stop-ai-slop.md`: Detect and eradicate synthetic AI boilerplate and generic abstractions.
3. `stop-ai-slop-pointer.md`: Remove fake pointers and dead scaffolding.
4. `stop-ai-slop-cursor.mdc`: Enforce anti-slop rules in editor configuration.
5. `design-ui-without-slop.md`: Purge generic AI UI clichés (unnecessary gradients, useless badges).
6. `design-for-real-people.md`: Optimize for genuine user ergonomics and real-world clarity.
7. `design-mobile-layout.md`: Ensure bulletproof mobile touch responsiveness.
8. `write-copy-without-slop.md`: Polish microcopy, buttons, and user notifications.

#### 22. `/skillnote secure`
*Folder: `Agent Ide/skills/Secure/` (5 skills)*
Executes complete 5-stage defensive security lifecycle:
1. `test-app-security.md`: Audit security configurations, TLS, headers, and environment variables.
2. `test-owasp-top-10.md`: Test against OWASP Top 10 (Injection, Broken Auth, SSRF, XSS).
3. `find-code-vulnerabilities.md`: Perform static analysis to find memory leaks and vulnerability patterns.
4. `pentest-web-app.md`: Perform automated penetration testing on API endpoints and session cookies.
5. `fix-vulnerabilities.md`: Implement verified security patches and regression tests.

#### 23. `/skillnote simplify`
*Folder: `Agent Ide/skills/Simplify/` (1 skill)*
Executes maximum scannability and cognitive simplification:
1. `write-for-adhd.md`: Refactor complex documentation into high-signal, bulleted, scannable documentation.

#### 24. `/skillnote simulate`
*Folder: `Agent Ide/skills/Simulate/` (1 skill)*
Executes mock simulation:
1. `build-faux-product-ui.md`: Construct high-fidelity mock environments for instant testing.

#### 25. `/skillnote style`
*Folder: `Agent Ide/skills/Style/` (6 skills)*
Executes comprehensive styling and brand design system:
1. `build-design-system.md`: Define cohesive tokens, colors, typography, and spacing variables.
2. `design-ui-ux.md`: Formulate ergonomic UX layout and interaction flows.
3. `style-ui.md`: Implement production styling (Tailwind/CSS modules) with pixel fidelity.
4. `manage-brand.md`: Enforce brand colors, logo placement, and voice consistency.
5. `design-banners.md`: Generate banners and visual graphics.
6. `build-slides.md`: Generate executive slide decks and presentation layouts.

#### 26. `/skillnote systematize`
*Folder: `Agent Ide/skills/Systematize/` (15 skills)*
Executes end-to-end engineering discipline and subagent execution:
1. `brainstorm.md`: Structured divergent problem analysis.
2. `write-plans.md`: Write clear, phased, verifiable implementation plans.
3. `test-first.md`: Apply Test-Driven Development (TDD) red-green-refactor loop.
4. `develop-with-subagents.md`: Fan-out implementation across specialized subagents.
5. `dispatch-parallel-agents.md`: Run parallel test, review, and authoring threads.
6. `execute-plans.md`: Execute planned phases systematically with progress tracking.
7. `debug-systematically.md`: Apply scientific debugging and root cause isolation.
8. `diagnose-session.md`: Evaluate execution traces and fix anomalies.
9. `request-code-review.md`: Initiate formal code review.
10. `receive-code-review.md`: Triage and address code review feedback.
11. `verify-before-completion.md`: Execute complete verification gates before declaring done.
12. `finish-branch.md`: Squash commits, clean history, and prepare PR.
13. `use-git-worktrees.md`: Leverage isolated git worktrees for multi-tasking.
14. `use-superpowers.md`: Leverage meta-agent capabilities.
15. `write-skills.md`: Document newly learned patterns as reusable skills.

#### 27. `/skillnote visualize`
*Folder: `Agent Ide/skills/Visualize/` (5 skills)*
Executes architectural visualization and evidence verification:
1. `make-diagrams.md`: Generate clear, accurate Mermaid/ASCII architecture diagrams.
2. `tune-diagram-accuracy.md`: Validate diagrams against concrete implementation code.
3. `simplify-codebase.md`: Visualize codebase complexity hot spots and simplify structure.
4. `improve-test-value.md`: Map test coverage vs value boundaries.
5. `review-with-evidence.md`: Provide evidence-backed architectural reviews.

#### 28. `/skillnote workflow`
*Folder: `Agent Ide/skills/Workflow/` (14 skills)*
Executes complete production web/cloud workflow engineering:
1. `analyzing-projects.md`: Comprehensive codebase & dependency analysis.
2. `designing-architecture.md`: Clean architecture and modularity design.
3. `database-design.md`: Schema modeling, indexing, relations, and migrations.
4. `convex-backend.md`: Realtime serverless backend design.
5. `designing-apis.md`: RESTful/GraphQL API contracts and schemas.
6. `security-patterns.md`: Secure authentication, authorization, and cryptography.
7. `web-design-guidelines.md`: Modern web UI standards and responsiveness.
8. `vercel-react-best-practices.md`: High-performance React & Next.js conventions.
9. `designing-tests.md`: Unit, integration, and E2E testing architecture.
10. `optimizing-performance.md`: Computational and network optimization.
11. `error-handling.md`: Fault tolerance, circuit breakers, and telemetry.
12. `parallel-execution.md`: Async/parallel workflows and concurrencies.
13. `managing-git.md`: Branching strategies, rebase hygiene, and versioning.
14. `devops-infrastructure.md`: CI/CD pipelines, containerization, and cloud deployment.

#### 29. `/skillnote assist`
*Folder: `Agent Ide/skills/Assist/` (447 skills)*
Executes broad developer assistant and library capabilities:
Runs codebase knowledge acquisition (`acquire-codebase-knowledge.md`), readiness assessment (`acreadiness-assess.md`), educational commentary, and target toolkit workflows.

#### 30. `/skillnote versatile`
*Folder: `Agent Ide/skills/Versatile/` (2646 skills)*
Executes specialized domain solutions across programming languages, cloud systems, and frameworks.

---

## 📋 Response Format Contract

When executing `/skillnote`, always format your output with high signal:
1. **Header**: State the active mode (`Mode 1: Global Orchestration` or `Mode 2: Targeted Category (<Category>) Pipeline`).
2. **Execution Log**: Report each skill executed in order, with key actions taken and findings.
3. **Artifacts / Changes**: Provide clickable links to modified or created files.
4. **Verification**: List tests run, security scans passed, and verification proofs.
5. **Attribution**: Include maintainer badge for Chinmay Prakash Rout.
