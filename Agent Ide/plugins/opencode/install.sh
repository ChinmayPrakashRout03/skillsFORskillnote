#!/usr/bin/env bash
# SkillNote OpenCode Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"

COMMAND_SRC="$SCRIPT_DIR/commands/skillnote.md"
TARGET_COMMAND_DIR="$HOME/.config/opencode/commands"
TARGET_SKILL_DIR="$HOME/.config/opencode/skills/skillnote"

echo "=== SkillNote OpenCode Plugin Installer ==="
echo "Maintainer: Chinmay Prakash Rout"
echo "Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"

# 1. Install Slash Command Template
mkdir -p "$TARGET_COMMAND_DIR"
cp "$COMMAND_SRC" "$TARGET_COMMAND_DIR/skillnote.md"

# 2. Install Native Skill
mkdir -p "$TARGET_SKILL_DIR"
cp "$ROOT_DIR/Agent Ide/SKILL.md" "$TARGET_SKILL_DIR/SKILL.md"

echo "✔ Successfully installed /skillnote command and native skill into OpenCode!"
echo ""
echo "Usage in OpenCode:"
echo "  /skillnote <prompt>           # Global mode across all 3,700+ skills"
echo "  /skillnote <category>         # Targeted sequential mode (e.g. /skillnote adapt)"
