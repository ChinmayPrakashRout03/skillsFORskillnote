---
description: "Master autonomous engineering engine. Supports /skillnote <prompt> (all skills across 32 categories) or /skillnote <category> (executes all skills inside that folder one by one)."
argument-format: "[<category> | <prompt>]"
---

# /skillnote — OpenCode Autonomous Engineering Command

> **Curated & Maintained Solely by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

You are executing the **SkillNote Autonomous Engineering Engine** inside OpenCode CLI.

---

## 🧭 Dynamic Routing Logic

Check `$ARGUMENTS`:

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

### Path 1: Targeted Category Pipeline (`/skillnote <category>`)
When the argument is any category from `KNOWN_CATEGORIES`:
1. Navigate to the folder `Agent Ide/skills/<Category>/`.
2. Execute **all skills present in that folder one by one in sequence**.
3. For each skill:
   - Announce: `▶ Running [<category>]: <skill-name>`
   - Apply its checks, refactorings, or tests.
   - Report progress and intermediate findings.
4. Conclude with a final verification report and summary of savings.

### Path 2: Global Orchestration (`/skillnote <prompt>`)
When the argument is an arbitrary prompt or feature request:
1. Orchestrate across all 32 capability categories.
2. Execute the 6 phases:
   - **Phase 1: Comprehend & Contextualize**: Map architecture, discover dependencies.
   - **Phase 2: Architecture & Specification**: Technical design and Mermaid diagrams.
   - **Phase 3: Implementation**: Clean, typed, modular code adhering to Guide rules.
   - **Phase 4: Automation & Execution**: Automated test runs and execution checks.
   - **Phase 5: Security & Refinement**: OWASP scan, secret check, anti-slop polish.
   - **Phase 6: Delivery**: Final git commit review, verification summary.
