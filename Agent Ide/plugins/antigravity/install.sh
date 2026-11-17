#!/usr/bin/env bash
# SkillNote Antigravity Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"

GEMINI_CONFIG="$HOME/.gemini/config"
SKILL_DIR="$GEMINI_CONFIG/skills/skillnote"
PLUGIN_DIR="$GEMINI_CONFIG/plugins/skillnote"

echo "=== SkillNote Antigravity Skill & Plugin Installer ==="
echo "Maintainer: Chinmay Prakash Rout"
echo "Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"

# 1. Install Skill
mkdir -p "$SKILL_DIR"
cp "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/SKILL.md"

# 2. Install Plugin & Command
mkdir -p "$PLUGIN_DIR/commands"
mkdir -p "$PLUGIN_DIR/skills/skillnote"
cp "$ROOT_DIR/Agent Ide/commands/skillnote.md" "$PLUGIN_DIR/commands/skillnote.md"
cp "$SCRIPT_DIR/SKILL.md" "$PLUGIN_DIR/skills/skillnote/SKILL.md"

cat << 'EOF' > "$PLUGIN_DIR/plugin.json"
{
  "name": "skillnote",
  "description": "Master autonomous engineering engine. Supports /skillnote <prompt> (all skills across 32 categories) or /skillnote <category> (executes all skills inside that folder one by one).",
  "version": "1.0.0",
  "author": {
    "name": "Chinmay Prakash Rout",
    "email": "chinmayprakashrout3@gmail.com",
    "url": "https://github.com/ChinmayPrakashRout03"
  },
  "repository": "https://github.com/ChinmayPrakashRout03/skillsFORskillnote"
}
EOF

# 3. Enable in Antigravity config.json
CONFIG_FILE="$GEMINI_CONFIG/config.json"
if [ -f "$CONFIG_FILE" ]; then
    python3 -c "
import json
path = '$CONFIG_FILE'
try:
    with open(path) as f:
        cfg = json.load(f)
    if 'plugins' not in cfg:
        cfg['plugins'] = {}
    cfg['plugins']['skillnote'] = {'enabled': True}
    with open(path, 'w') as f:
        json.dump(cfg, f, indent=2)
    print('✔ Enabled skillnote in config.json')
except Exception as e:
    print('Warning: could not update config.json:', e)
"
fi

echo "✔ Successfully installed SkillNote into Antigravity!"
echo ""
echo "Note: If Antigravity IDE is open, please restart or reload it (Cmd + Shift + P -> Developer: Reload Window) to load the new /skillnote command."
echo ""
echo "Usage in Antigravity Chat:"
echo "  /skillnote <prompt>           # Global mode across all 3,700+ skills"
echo "  /skillnote <category>         # Targeted sequential mode (e.g. /skillnote adapt)"
