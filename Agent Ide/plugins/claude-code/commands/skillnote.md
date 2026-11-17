---
description: "Adaptive cognitive architecture for Claude Code. Dynamic task classification, on-demand skill retrieval, safety gates, and observable verification across 32 engineering domains."
argument-format: "[<category> | <prompt>] [--all]"
---

# /skillnote — Claude Code Adaptive Engineering Engine

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

You are executing the **SkillNote Adaptive Engineering Engine** inside Claude Code.

---

## 🔀 Step 1: Input Evaluation & Dynamic Routing

Inspect `$ARGUMENTS`:

```python
KNOWN_CATEGORIES = [
    "adapt", "assist", "audit", "automate", "beautify", "comprehend",
    "contextualize", "convert", "create", "curate", "design", "develop",
    "engineer", "execute", "guide", "humanize", "manage", "minimize",
    "navigate", "official", "optimize", "orchestrate", "prototype",
    "refine", "secure", "simplify", "simulate", "style", "systematize",
    "versatile", "visualize", "workflow"
]
```

### Route A: Targeted Category Mode (`/skillnote <category>`)
If `$ARGUMENTS` matches any category name in `KNOWN_CATEGORIES` (case-insensitive):

1. **Curated Small Categories (< 20 skills)**: Execute the deterministic pipeline sequentially in order:
   - **adapt** / **minimize**: `audit-repo-quality` ➔ `list-shortcut-debt` ➔ `review-change-quality` ➔ `lazy-senior-dev` ➔ `show-savings` ➔ `show-help`.
   - **secure** / **audit**: `test-app-security` ➔ `test-owasp-top-10` ➔ `find-code-vulnerabilities` ➔ `pentest-web-app` ➔ `fix-vulnerabilities`.
   - **comprehend** / **contextualize**: `ask-codebase` ➔ `build-knowledge-graph` ➔ `explain-code` ➔ `context-compression` ➔ `write-onboarding-guide`.
   - **refine**: `clean-code-comments` ➔ `stop-ai-slop` ➔ `design-ui-without-slop` ➔ `design-for-real-people` ➔ `write-copy-without-slop`.
   - **style** / **beautify**: `build-design-system` ➔ `design-ui-ux` ➔ `style-ui` ➔ `design-tasteful-frontend`.
   - **workflow**: `analyzing-projects` ➔ `designing-architecture` ➔ `database-design` ➔ `designing-apis` ➔ `designing-tests` ➔ `optimizing-performance` ➔ `managing-git`.
   - **visualize**: `make-diagrams` ➔ `tune-diagram-accuracy` ➔ `simplify-codebase` ➔ `improve-test-value` ➔ `review-with-evidence`.
   - **systematize**: `brainstorm` ➔ `write-plans` ➔ `test-first` ➔ `execute-plans` ➔ `verify-before-completion` ➔ `finish-branch`.

2. **Large Categories (> 50 skills)** (e.g. `Versatile` [2,646], `Assist` [447], `Create` [113], `Develop` [71], `Automate` [69]):
   - **Relevance-Filtered by Default**: Query SQLite FTS5 index and select only the top 3–5 skills matching the active workspace.
   - Use `--all` flag to intentionally execute every skill in the folder.

---

### Route B: Adaptive Task Engine (`/skillnote <prompt>`)
If `$ARGUMENTS` is any engineering prompt, bug report, or feature request:

1. **Classify Task Complexity**:
   - **Micro Mode**: Targeted fix, single file, zero ceremony, immediate unit test.
   - **Standard Mode**: Contract plan ➔ modular implementation ➔ test suite validation.
   - **Complex Mode**: Architecture breakdown, dependency graph, milestone verification.
   - **Experimental Mode**: Benchmark competing hypotheses while preserving safety boundaries.
2. **On-Demand Skill Retrieval**: Pull top 1–3 skills from catalog via SQLite FTS5 (<1ms).
3. **Safety Gate**: Pause for user confirmation before deleting files, dropping tables, or rewriting git history.
4. **Observable Evidence**: Run real test/lint commands, capture exit codes (`0`), and report logs. If unverified, state `NOT VERIFIED`.
