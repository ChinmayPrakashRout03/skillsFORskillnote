# SkillNote for OpenCode CLI

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

SkillNote equips **OpenCode** CLI with the complete library of 3,700+ skills organized into 32 capability categories.

---

## ⚡ Installation

Run the one-click installer:

```bash
chmod +x "Agent Ide/plugins/opencode/install.sh"
./"Agent Ide/plugins/opencode/install.sh"
```

Or copy the command manually into OpenCode's configuration:

```bash
mkdir -p ~/.config/opencode/commands
cp "Agent Ide/plugins/opencode/commands/skillnote.md" ~/.config/opencode/commands/skillnote.md
```

You can also drop `Agent Ide/plugins/opencode/opencode.json` into your project root to auto-enable SkillNote on project open.

---

## 💻 Commands

Launch OpenCode in your workspace:

```bash
opencode
```

Then in the interactive prompt:

### Mode 1: Global Orchestration
```
/skillnote implement a real-time event streaming pipeline using Kafka and FastAPI
```
Triggers the multi-phase engineering pipeline across all 32 categories.

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
OpenCode will run every skill file inside that folder in strict sequential order.
