# SkillNote for Z Code (Zed AI)

> **Maintained solely and independently by [Chinmay Prakash Rout](https://github.com/ChinmayPrakashRout03)**  
> **Repository**: [https://github.com/ChinmayPrakashRout03/skillsFORskillnote](https://github.com/ChinmayPrakashRout03/skillsFORskillnote)

SkillNote integrates the library of 3,700+ skills directly into the **Zed editor** AI assistant.

---

## ⚡ Installation

Run the one-click installer:

```bash
chmod +x "Agent Ide/plugins/z-code/install.sh"
./"Agent Ide/plugins/z-code/install.sh"
```

Or copy the prompt template manually:

```bash
mkdir -p ~/.config/zed/prompts
cp "Agent Ide/plugins/z-code/.zed/prompts/skillnote.mustache" ~/.config/zed/prompts/skillnote.mustache
```

For project-level integration, copy `.zed/` and `.rules` into your project root:

```bash
cp -r "Agent Ide/plugins/z-code/.zed" ./
cp "Agent Ide/plugins/z-code/.rules" ./
```

---

## 💬 Usage in Zed Assistant Panel

Open the Zed AI Assistant (`cmd-?` on macOS or `ctrl-?` on Linux):

### Mode 1: Global Orchestration
Type:
```
/skillnote create a typed microservice in Rust with Actix-web and PostgreSQL pool
```
Zed AI will execute full-lifecycle engineering across all 32 categories.

### Mode 2: Targeted Category Execution
Type:
```
/skillnote adapt       # Runs all 6 minimalism & debt removal skills sequentially
/skillnote secure      # Runs all 5 defensive security & OWASP skills sequentially
/skillnote comprehend  # Runs all 8 codebase comprehension & graphing skills sequentially
/skillnote engineer    # Runs all 25 core engineering rigor skills sequentially
/skillnote refine      # Runs all 8 anti-slop & comment cleanup skills sequentially
/skillnote workflow    # Runs all 14 web & cloud workflow skills sequentially
/skillnote style       # Runs all 6 design system & UI styling skills sequentially
/skillnote systematize # Runs all 15 TDD, planning & subagent execution skills sequentially
```
Zed AI runs every skill in that category folder one by one in sequence.
