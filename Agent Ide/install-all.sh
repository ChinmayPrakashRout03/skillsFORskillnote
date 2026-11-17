#!/usr/bin/env bash
# SkillNote Master Universal Installer for ALL Agent IDEs
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$SCRIPT_DIR/.."

echo "================================================================="
echo "  SKILLNOTE MASTER INSTALLER — ADAPTIVE RUNTIME & AGENT PLUGINS"
echo "  Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)"
echo "  Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"
echo "================================================================="
echo ""

# 0. Build / verify SQLite FTS5 Catalog
echo "▶ [0/5] Indexing SkillNote SQLite FTS5 Catalog..."
python3 "$SCRIPT_DIR/scripts/skillnote.py" index --library "$SCRIPT_DIR/skills"

# 1. Claude Code
echo "▶ [1/5] Installing for Claude Code..."
mkdir -p "$HOME/.claude/commands"
cp "$SCRIPT_DIR/commands/skillnote.md" "$HOME/.claude/commands/skillnote.md"
echo "  ✔ Claude Code command installed to ~/.claude/commands/skillnote.md"

# 2. OpenCode CLI
echo "▶ [2/5] Installing for OpenCode..."
mkdir -p "$HOME/.config/opencode/commands"
mkdir -p "$HOME/.config/opencode/skills/skillnote"
cp "$SCRIPT_DIR/plugins/opencode/commands/skillnote.md" "$HOME/.config/opencode/commands/skillnote.md"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.config/opencode/skills/skillnote/SKILL.md"
echo "  ✔ OpenCode command & native skill installed to ~/.config/opencode/"

# 3. Antigravity IDE
echo "▶ [3/5] Installing for Antigravity IDE..."
mkdir -p "$HOME/.gemini/config/skills/skillnote"
mkdir -p "$HOME/.gemini/config/plugins/skillnote/commands"
mkdir -p "$HOME/.gemini/config/plugins/skillnote/skills/skillnote"

cp "$SCRIPT_DIR/SKILL.md" "$HOME/.gemini/config/skills/skillnote/SKILL.md"
cp "$SCRIPT_DIR/commands/skillnote.md" "$HOME/.gemini/config/plugins/skillnote/commands/skillnote.md"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.gemini/config/plugins/skillnote/skills/skillnote/SKILL.md"

cat << 'EOF' > "$HOME/.gemini/config/plugins/skillnote/plugin.json"
{
  "name": "skillnote",
  "description": "SkillNote Adaptive Runtime & Autonomous Engineering Engine",
  "version": "1.0.0",
  "author": {
    "name": "Chinmay Prakash Rout",
    "email": "chinmayprakashrout3@gmail.com",
    "url": "https://github.com/ChinmayPrakashRout03"
  },
  "repository": "https://github.com/ChinmayPrakashRout03/skillsFORskillnote"
}
EOF

# Auto-enable in config.json
if [ -f "$HOME/.gemini/config/config.json" ]; then
    python3 -c "
import json
path = '$HOME/.gemini/config/config.json'
try:
    with open(path) as f:
        cfg = json.load(f)
    if 'plugins' not in cfg:
        cfg['plugins'] = {}
    cfg['plugins']['skillnote'] = {'enabled': True}
    with open(path, 'w') as f:
        json.dump(cfg, f, indent=2)
    print('  ✔ Enabled skillnote in ~/.gemini/config/config.json')
except Exception as e:
    print('  Notice: could not update config.json:', e)
"
fi
echo "  ✔ Antigravity skill & plugin installed"

# 4. OpenAI Codex
echo "▶ [4/5] Preparing OpenAI Codex workspace files..."
cp "$SCRIPT_DIR/plugins/codex/CODEX.md" "$ROOT_DIR/CODEX.md"
cp "$SCRIPT_DIR/plugins/codex/AGENTS.md" "$ROOT_DIR/AGENTS.md"
chmod +x "$SCRIPT_DIR/plugins/codex/codex-skillnote.sh"
echo "  ✔ Codex CODEX.md & AGENTS.md copied to workspace root"

# 5. ZCode App (and Zed AI)
echo "▶ [5/5] Installing for ZCode App..."
mkdir -p "$HOME/.zcode/skills/skillnote"
mkdir -p "$HOME/.agents/skills/skillnote"
mkdir -p "$HOME/.claude/skills/skillnote"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.zcode/skills/skillnote/SKILL.md"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.agents/skills/skillnote/SKILL.md"
cp "$SCRIPT_DIR/SKILL.md" "$HOME/.claude/skills/skillnote/SKILL.md"

mkdir -p "$HOME/.config/zed/prompts"
cp "$SCRIPT_DIR/plugins/z-code/.zed/prompts/skillnote.mustache" "$HOME/.config/zed/prompts/skillnote.mustache" 2>/dev/null || true
echo "  ✔ ZCode skill installed to ~/.zcode/skills & ~/.agents/skills"

echo ""
echo "================================================================="
echo "  🎉 ALL 5 AGENT IDES SUCCESSFULLY UPDATED & CONFIGURED!"
echo "================================================================="
echo ""
echo "How to run in your agents:"
echo ""
echo "1. Antigravity IDE:"
echo "   Reload window (Cmd + Shift + P -> Developer: Reload Window), then in chat:"
echo "   /skillnote adapt"
echo "   /skillnote fix python login exception"
echo ""
echo "2. OpenCode CLI:"
echo "   Run 'opencode', then in chat:"
echo "   /skillnote secure"
echo "   /skillnote create full-stack nextjs dashboard"
echo ""
echo "3. Claude Code:"
echo "   Run 'claude', then in chat:"
echo "   /skillnote adapt"
echo "   /skillnote optimize database queries"
echo ""
echo "4. OpenAI Codex:"
echo "   In Codex chat: /skillnote <prompt>"
echo "   In terminal:   ./\"Agent Ide/plugins/codex/codex-skillnote.sh\" adapt"
echo ""
echo "5. Z Code (Zed AI):"
echo "   Open Assistant (Cmd + ?), then in chat:"
echo "   /skillnote adapt"
echo "   /skillnote invent novel algorithm"
echo ""
