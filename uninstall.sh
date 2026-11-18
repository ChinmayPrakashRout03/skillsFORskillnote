#!/usr/bin/env bash
# SkillNote Clean Uninstaller (macOS & Linux)
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

set -e

echo ""
echo "=================================================================="
echo "    🗑️  SKILLNOTE UNINSTALLER (macOS & Linux)"
echo "    Removing SkillNote runtime, CLI, and Agent IDE integrations..."
echo "=================================================================="
echo ""

# 1. Remove runtime directory
if [ -d "$HOME/.skillnote" ]; then
    rm -rf "$HOME/.skillnote"
    echo "  ✔ Removed ~/.skillnote"
fi

# 2. Remove CLI binary
if [ -f "$HOME/.local/bin/skillnote" ]; then
    rm -f "$HOME/.local/bin/skillnote"
    echo "  ✔ Removed ~/.local/bin/skillnote"
fi

# 3. Remove Claude Code integration
if [ -f "$HOME/.claude/commands/skillnote.md" ]; then
    rm -f "$HOME/.claude/commands/skillnote.md"
    echo "  ✔ Removed ~/.claude/commands/skillnote.md"
fi
if [ -d "$HOME/.claude/skills/skillnote" ]; then
    rm -rf "$HOME/.claude/skills/skillnote"
    echo "  ✔ Removed ~/.claude/skills/skillnote"
fi

# 4. Remove OpenCode integration
if [ -f "$HOME/.config/opencode/commands/skillnote.md" ]; then
    rm -f "$HOME/.config/opencode/commands/skillnote.md"
    echo "  ✔ Removed ~/.config/opencode/commands/skillnote.md"
fi
if [ -d "$HOME/.config/opencode/skills/skillnote" ]; then
    rm -rf "$HOME/.config/opencode/skills/skillnote"
    echo "  ✔ Removed ~/.config/opencode/skills/skillnote"
fi

# 5. Remove Antigravity plugin
if [ -d "$HOME/.gemini/config/plugins/skillnote" ]; then
    rm -rf "$HOME/.gemini/config/plugins/skillnote"
    echo "  ✔ Removed ~/.gemini/config/plugins/skillnote"
fi
if [ -d "$HOME/.gemini/config/skills/skillnote" ]; then
    rm -rf "$HOME/.gemini/config/skills/skillnote"
    echo "  ✔ Removed ~/.gemini/config/skills/skillnote"
fi
if [ -f "$HOME/.gemini/config/config.json" ]; then
    python3 -c "
import json
path = '$HOME/.gemini/config/config.json'
try:
    with open(path) as f:
        cfg = json.load(f)
    if 'plugins' in cfg and 'skillnote' in cfg['plugins']:
        del cfg['plugins']['skillnote']
        with open(path, 'w') as f:
            json.dump(cfg, f, indent=2)
        print('  ✔ Disabled skillnote in ~/.gemini/config/config.json')
except Exception:
    pass
" 2>/dev/null || true
fi

# 6. Remove ZCode & Zed integration
if [ -d "$HOME/.zcode/skills/skillnote" ]; then
    rm -rf "$HOME/.zcode/skills/skillnote"
    echo "  ✔ Removed ~/.zcode/skills/skillnote"
fi
if [ -d "$HOME/.zcode/cli/plugins/cache/zcode-plugins-official/skillnote" ]; then
    rm -rf "$HOME/.zcode/cli/plugins/cache/zcode-plugins-official/skillnote"
    echo "  ✔ Removed ~/.zcode/cli/plugins/cache/.../skillnote"
fi
if [ -d "$HOME/.agents/skills/skillnote" ]; then
    rm -rf "$HOME/.agents/skills/skillnote"
    echo "  ✔ Removed ~/.agents/skills/skillnote"
fi
if [ -f "$HOME/.config/zed/prompts/skillnote.mustache" ]; then
    rm -f "$HOME/.config/zed/prompts/skillnote.mustache"
    echo "  ✔ Removed ~/.config/zed/prompts/skillnote.mustache"
fi

echo ""
echo "=================================================================="
echo "    ✨ SKILLNOTE SUCCESSFULLY UNINSTALLED!"
echo "    All integrations and cache files have been completely removed."
echo "=================================================================="
echo ""
