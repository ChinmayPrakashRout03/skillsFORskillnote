# AGENTS.md — SkillNote Multi-Agent Delegation Matrix

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

This file defines the specialized subagent roster and delegation protocol for **OpenAI Codex** and autonomous multi-agent swarms.

---

## 👥 Specialized Agent Roster

| Agent Role | Primary Category | Responsibilities | Hand-off To |
| :--- | :--- | :--- | :--- |
| **Architect** | `Comprehend`, `Contextualize`, `Navigate` | Topology mapping, dependency trees, knowledge graphs | `Designer`, `Engineer` |
| **Designer** | `Design`, `Style`, `Beautify`, `Visualize` | UI/UX systems, CSS/Tailwind tokens, Mermaid diagrams | `Engineer` |
| **Engineer** | `Develop`, `Engineer`, `Create`, `Guide` | Fullstack implementation, typed interfaces, APIs | `QA-Automator` |
| **QA-Automator**| `Automate`, `Execute`, `Workflow`, `Simulate` | Test suite execution, CI/CD validation, runtime assertions | `Security-Auditor` |
| **Security-Auditor**| `Audit`, `Secure` | OWASP Top 10, penetration tests, auth verification | `Optimizer-Refiner` |
| **Optimizer-Refiner**| `Refine`, `Optimize`, `Adapt`, `Minimize` | AI slop removal, token compression, memory profiling | `Delivery-Manager` |
| **Delivery-Manager**| `Systematize`, `Manage`, `Humanize`, `Official`| Git commit hygiene, humanized docs, PR completion | User / Coordinator |

---

## 🔄 Sequential Execution Protocol for Category Commands

When an agent is invoked via `/skillnote <category>`:
1. The Lead Agent claims the task and assigns it to the corresponding specialist above.
2. The specialist reads `Agent Ide/skills/<Category>/` and processes each skill file sequentially.
3. Every completed skill outputs a verifiable checkpoint before advancing to the next skill.
4. If a step fails, the specialist invokes `Engineer` or `Security-Auditor` to remediate before continuing.
5. All completed steps roll up to `Delivery-Manager` for final reporting.
