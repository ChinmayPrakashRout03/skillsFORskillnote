#!/usr/bin/env bash
# SkillNote ZCode Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"

echo "=== SkillNote ZCode (and Zed) Installer ==="
echo "Maintainer: Chinmay Prakash Rout"
echo "Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"

# 1. Install for ZCode App (~/.zcode and ~/.agents)
mkdir -p "$HOME/.zcode/skills/skillnote"
mkdir -p "$HOME/.agents/skills/skillnote"
mkdir -p "$HOME/.claude/skills/skillnote"

cp "$ROOT_DIR/Agent Ide/SKILL.md" "$HOME/.zcode/skills/skillnote/SKILL.md"
cp "$ROOT_DIR/Agent Ide/SKILL.md" "$HOME/.agents/skills/skillnote/SKILL.md"
cp "$ROOT_DIR/Agent Ide/SKILL.md" "$HOME/.claude/skills/skillnote/SKILL.md"

# 2. Also install for Zed Editor if present
mkdir -p "$HOME/.config/zed/prompts"
cp "$SCRIPT_DIR/.zed/prompts/skillnote.mustache" "$HOME/.config/zed/prompts/skillnote.mustache"

echo "✔ Successfully installed SkillNote into ZCode (~/.zcode/skills and ~/.agents/skills)!"
echo ""
echo "Usage in ZCode App:"
echo "  Type /skillnote or select skillnote from the menu"
