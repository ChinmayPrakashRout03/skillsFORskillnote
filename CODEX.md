# CODEX.md — SkillNote Adaptive Cognitive Architecture for Codex

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

This document establishes the behavioral specification and cognitive execution protocol for **OpenAI Codex** agents operating within this workspace.

---

## 🎯 Command Protocol: `/skillnote`

When the user or orchestration harness issues `/skillnote [arguments]`:

### 1. Adaptive Task Engine (`/skillnote <prompt>`)
When passed an engineering prompt, bug fix, refactor, or feature:
1. **Modulate Complexity**:
   - **Micro Mode** (single-file fixes, typos, isolated logic patches): Surgical edit + targeted test. ~3k token budget.
   - **Standard Mode** (features, API endpoints, components, refactoring): Architecture contract ➔ typed implementation ➔ test suite validation. ~20k token budget.
   - **Complex Mode** (subsystems, multi-service architectures, schema migrations): Milestone planning, dependency graphs, full systematic validation. ~60k token budget.
   - **Experimental Mode** (novel algorithms, performance spikes): Benchmark competing approaches while strictly enforcing safety boundaries.
2. **On-Demand Retrieval (<1ms)**: Retrieve only the 1–3 most relevant skills from the local SQLite FTS5 catalog.
3. **Safety Gate**: Pause for user approval before deleting non-trivial files, dropping tables, or rewriting git history.
4. **Observable Evidence**: Run real commands (`pytest`, `npm test`, linters), log exit codes (`0`), and provide output logs. Never report synthetic compliance.

---

### 2. Category Execution (`/skillnote <category>`)
When the argument matches one of the **32 category folder names**:
- **Curated Small Categories (< 20 skills)** (adapt, secure, comprehend, refine, style, workflow, visualize, systematize):
  Execute the deterministic sequential pipeline step-by-step.
- **Large Categories (> 50 skills)** (versatile, assist, create, develop, automate):
  **Relevance-filtered by default**. Uses SQLite FTS5 search to activate only the top 3–5 skills matching the active workspace. Pass `--all` if an intentional exhaustive sweep is requested.

---

## 🛡️ Operating Invariants for Codex

1. **Proof Before Claims**: Never claim code is tested or verified without executing a real command and logging the exit code. If tests cannot run, report: `NOT VERIFIED (Reason: ...)`.
2. **Safety Gates**: Request confirmation before deleting files, dropping schemas, modifying credentials, or force-pushing.
3. **Honest Limitations**: State external dependencies, missing environment variables, or manual operational steps clearly.
4. **No Placeholders**: Never write `# TODO: implement later` or truncated snippets. Deliver working, typed code.
