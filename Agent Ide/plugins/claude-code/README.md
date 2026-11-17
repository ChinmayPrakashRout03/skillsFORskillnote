# SkillNote for Claude Code

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

SkillNote transforms **Claude Code** into a master full-lifecycle software engineering agent.

---

## 🚀 Quick Installation

Run the one-click installer:

```bash
chmod +x "Agent Ide/plugins/claude-code/install.sh"
./"Agent Ide/plugins/claude-code/install.sh"
```

Or manually copy the command into your global Claude configuration:

```bash
mkdir -p ~/.claude/commands
cp "Agent Ide/plugins/claude-code/commands/skillnote.md" ~/.claude/commands/skillnote.md
```

---

## 💡 How to Use

### 1. Global Orchestration Mode (`/skillnote <prompt>`)
Use for any feature, refactor, architecture, or general software task:

```bash
/skillnote build a high-performance REST API in Go with JWT authentication and rate limiting
```
- Coordinates across all 32 categories in `Agent Ide/skills/`.
- Decomposes into 6 phases: Comprehend ➔ Design ➔ Implement ➔ Automate ➔ Audit & Optimize ➔ Deliver.

### 2. Targeted Category Sequential Mode (`/skillnote <category>`)
Use to execute **all skills inside a specific folder one by one**:

```bash
/skillnote adapt       # Executes all 6 minimalism & debt removal skills sequentially
/skillnote secure      # Executes all 5 defensive security & OWASP skills sequentially
/skillnote comprehend  # Executes all 8 codebase comprehension & graphing skills sequentially
/skillnote engineer    # Executes all 25 core engineering rigor skills sequentially
/skillnote refine      # Executes all 8 anti-slop & comment cleanup skills sequentially
/skillnote workflow    # Executes all 14 web & cloud workflow skills sequentially
/skillnote style       # Executes all 6 design system & UI styling skills sequentially
/skillnote systematize # Executes all 15 TDD, planning & subagent execution skills sequentially
```

Every skill in that folder will execute in strict sequence with individual status logs.
