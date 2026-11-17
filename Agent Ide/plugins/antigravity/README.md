# SkillNote for Antigravity

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

SkillNote transforms **Antigravity** into an orchestrating agent capable of coordinating subagents, running tests, executing security audits, and driving full-lifecycle development.

---

## ⚡ Installation

Run the one-click installer:

```bash
chmod +x "Agent Ide/plugins/antigravity/install.sh"
./"Agent Ide/plugins/antigravity/install.sh"
```

Or keep the `Agent Ide/SKILL.md` in your workspace, and Antigravity will automatically load it as a skill.

---

## 💬 Usage

In your Antigravity chat:

### Mode 1: Global Orchestration
```
/skillnote create a high-throughput async processing pipeline in Python with Redis queue
```
Antigravity automatically orchestrates across all 32 categories, fanning out subtasks to specialized subagents (`research`, `code-reviewer`, `security-auditor`, `test-engineer`).

### Mode 2: Targeted Category Execution
```
/skillnote adapt       # Executes all 6 minimalism & debt removal skills sequentially
/skillnote secure      # Executes all 5 defensive security & OWASP skills sequentially
/skillnote comprehend  # Executes all 8 codebase comprehension & graphing skills sequentially
/skillnote engineer    # Executes all 25 core engineering rigor skills sequentially
/skillnote refine      # Executes all 8 anti-slop & comment cleanup skills sequentially
/skillnote workflow    # Executes all 14 web & cloud workflow skills sequentially
/skillnote style       # Executes all 6 design system & UI styling skills sequentially
/skillnote systematize # Executes all 15 TDD, planning & subagent execution skills sequentially
```
Antigravity iterates through every skill file inside the category directory, executing them one by one in sequence and verifying each step.
