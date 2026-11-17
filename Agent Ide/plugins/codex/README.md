# SkillNote for OpenAI Codex

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

SkillNote equips **OpenAI Codex** agents with full-lifecycle software engineering autonomy across 32 specialized categories.

---

## 🚀 Setup for OpenAI Codex

### Project Workspace Setup
Copy the Codex agent configuration files into your project root:

```bash
cp "Agent Ide/plugins/codex/CODEX.md" ./CODEX.md
cp "Agent Ide/plugins/codex/AGENTS.md" ./AGENTS.md
```

Codex will automatically detect `CODEX.md` and `AGENTS.md` upon opening the workspace.

---

## 💻 Usage with Codex

### 1. Interactive Chat / Prompt in Codex
In your Codex chat or agent interface:
- **Global Orchestration**:
  ```
  /skillnote design and implement an end-to-end payment webhook system with idempotency and retry queues
  ```
- **Targeted Category Pipeline**:
  ```
  /skillnote adapt       # Runs all 6 minimalism & debt removal skills sequentially
  /skillnote secure      # Runs all 5 defensive security & OWASP skills sequentially
  /skillnote comprehend  # Runs all 8 codebase comprehension & graphing skills sequentially
  /skillnote engineer    # Runs all 25 core engineering rigor skills sequentially
  /skillnote refine      # Runs all 8 anti-slop & comment cleanup skills sequentially
  /skillnote workflow    # Runs all 14 web & cloud workflow skills sequentially
  ```

### 2. Headless CLI Execution via `codex exec`
You can invoke SkillNote non-interactively in CI/CD or shell scripts:

```bash
# Targeted category run
./"Agent Ide/plugins/codex/codex-skillnote.sh" adapt

# Global prompt run
./"Agent Ide/plugins/codex/codex-skillnote.sh" "build a GraphQL server with Apollo and TypeScript"
```
