---
description: "Master autonomous engineering engine. Supports /skillnote <prompt> (all skills across 32 categories) or /skillnote <category> (executes all skills inside that folder one by one)."
argument-format: "[<category> | <prompt>]"
---

# /skillnote — Claude Code Autonomous Engineering Command

> **Curated & Maintained Solely by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

You are executing the **SkillNote Autonomous Engineering Engine** inside Claude Code.

---

## 🔀 Step 1: Input Evaluation & Dynamic Routing

Inspect `$ARGUMENTS` (or query passed):

```
KNOWN_CATEGORIES = [
  "adapt", "assist", "audit", "automate", "beautify", "comprehend",
  "contextualize", "convert", "create", "curate", "design", "develop",
  "engineer", "execute", "guide", "humanize", "manage", "minimize",
  "navigate", "official", "optimize", "orchestrate", "prototype",
  "refine", "secure", "simplify", "simulate", "style", "systematize",
  "versatile", "visualize", "workflow"
]
```

### Route A: Targeted Sequential Category Mode (`/skillnote <category>`)
If `$ARGUMENTS` matches any category name in `KNOWN_CATEGORIES` (case-insensitive):
1. **Target Directory**: Locate `Agent Ide/skills/<Category>/`.
2. **Sequential Execution**: Load and execute **every skill file in that directory one by one in strict sequence**.
3. **Continuous Reporting**: After executing each skill, output a brief status:
   - `✔ [Skill Name]`: key checks performed, refactorings applied, or risks uncovered.
4. **Final Summary**: Conclude with a consolidated summary of changes, savings, and recommended next actions.

#### Category Pipeline Index:
- **adapt** / **minimize**: `audit-repo-quality` ➔ `list-shortcut-debt` ➔ `review-change-quality` ➔ `lazy-senior-dev` ➔ `show-savings` ➔ `show-help`.
- **audit**: `audit-security` (comprehensive vulnerability, auth & dependency scan).
- **beautify**: `design-tasteful-frontend` (aesthetic refinement & micro-interactions).
- **comprehend**: `ask-codebase` ➔ `build-knowledge-graph` ➔ `explain-code` ➔ `explain-diff` ➔ `extract-domain-knowledge` ➔ `graph-knowledge-base` ➔ `open-knowledge-dashboard` ➔ `write-onboarding-guide`.
- **convert**: `convert-book-to-skill` (technical literature & spec transformation).
- **design**: `design-frontend` (design system & UI component layout).
- **engineer**: `break-down-tasks` ➔ `design-apis` ➔ `build-frontend-ui` ➔ `add-observability` ➔ `debugging` ➔ `adversarial-review` ➔ `deprecate-and-migrate`.
- **execute** / **orchestrate**: `capture-ideas` ➔ `ai-design-contract` ➔ `autonomous-execution` ➔ `validate-phase` ➔ `audit-milestone` ➔ `audit-fix-pipeline` ➔ `complete-milestone` ➔ `cleanup-archive`.
- **guide**: `coding-guidelines` ➔ `coding-guidelines-project` ➔ `coding-guidelines-cursor.mdc`.
- **humanize**: `humanize-writing` ➔ `humanize-writing-claude` ➔ `humanize-writing-single-file` ➔ `humanize-writing.skill`.
- **official**: `skill-creator` ➔ `mcp-builder` ➔ `frontend-design` ➔ `web-artifacts-builder` ➔ `edit-docx` ➔ `edit-pdf` ➔ `edit-pptx` ➔ `edit-xlsx` ➔ `algorithmic-art` ➔ `doc-coauthoring` ➔ `discernment-nudge` ➔ `academy-guide` ➔ `slack-gif-creator`.
- **prototype**: `research-app-idea` ➔ `write-mvp-prd` ➔ `write-mvp-tech-design` ➔ `select-workflow` ➔ `implement-project-slice` ➔ `add-bounded-feature` ➔ `verify-against-acceptance-criteria` ➔ `diagnose-and-fix-failure` ➔ `review-proposed-change` ➔ `prepare-handoff-context` ➔ `create-agent-instructions`.
- **refine**: `clean-code-comments` ➔ `stop-ai-slop` ➔ `stop-ai-slop-pointer` ➔ `stop-ai-slop-cursor.mdc` ➔ `design-ui-without-slop` ➔ `design-for-real-people` ➔ `design-mobile-layout` ➔ `write-copy-without-slop`.
- **secure**: `test-app-security` ➔ `test-owasp-top-10` ➔ `find-code-vulnerabilities` ➔ `pentest-web-app` ➔ `fix-vulnerabilities`.
- **simplify**: `write-for-adhd` (high-signal cognitive simplification).
- **simulate**: `build-faux-product-ui` (interactive mock environment).
- **style**: `build-design-system` ➔ `design-ui-ux` ➔ `style-ui` ➔ `manage-brand` ➔ `design-banners` ➔ `build-slides`.
- **systematize**: `brainstorm` ➔ `write-plans` ➔ `test-first` ➔ `develop-with-subagents` ➔ `dispatch-parallel-agents` ➔ `execute-plans` ➔ `debug-systematically` ➔ `diagnose-session` ➔ `request-code-review` ➔ `receive-code-review` ➔ `verify-before-completion` ➔ `finish-branch` ➔ `use-git-worktrees` ➔ `use-superpowers` ➔ `write-skills`.
- **visualize**: `make-diagrams` ➔ `tune-diagram-accuracy` ➔ `simplify-codebase` ➔ `improve-test-value` ➔ `review-with-evidence`.
- **workflow**: `analyzing-projects` ➔ `designing-architecture` ➔ `database-design` ➔ `convex-backend` ➔ `designing-apis` ➔ `security-patterns` ➔ `web-design-guidelines` ➔ `vercel-react-best-practices` ➔ `designing-tests` ➔ `optimizing-performance` ➔ `error-handling` ➔ `parallel-execution` ➔ `managing-git` ➔ `devops-infrastructure`.
- **automate**, **contextualize**, **create**, **curate**, **develop**, **manage**, **navigate**, **optimize**, **assist**, **versatile**: Execute all respective skills in that directory sequentially.

---

### Route B: Global Orchestration Mode (`/skillnote <prompt>`)
If `$ARGUMENTS` is any free-form task or project objective:
1. Deconstruct the prompt across the 6 autonomous engineering phases:
   - **Phase 1: Comprehend & Contextualize**: Map architecture, inspect existing codebase, prevent context drift.
   - **Phase 2: Architecture & Specification**: Formulate technical design, component hierarchy, and Mermaid architecture diagrams.
   - **Phase 3: Implementation & Synthesis**: Write clean, typed, modular production code adhering to `Guide` standards.
   - **Phase 4: Automation & Execution**: Execute test suites, verify runtime stability, and run build commands.
   - **Phase 5: Security, Refinement & Optimization**: Run OWASP security scan, strip AI boilerplate and slop, and optimize performance.
   - **Phase 6: Delivery & Systematization**: Verify acceptance criteria, clean git history, and produce humanized documentation.
2. Provide clickable file links and complete verification proofs.
