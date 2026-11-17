#!/usr/bin/env bash
# SkillNote Antigravity Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$HOME/.gemini/antigravity/skills/skillnote"

echo "=== SkillNote Antigravity Skill Installer ==="
echo "Maintainer: Chinmay Prakash Rout"
echo "Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"

mkdir -p "$TARGET_DIR"
cp "$SCRIPT_DIR/SKILL.md" "$TARGET_DIR/SKILL.md"
cp "$SCRIPT_DIR/skillnote.json" "$TARGET_DIR/skillnote.json"

echo "✔ Successfully installed SkillNote into Antigravity: $TARGET_DIR"
echo ""
echo "Usage in Antigravity:"
echo "  /skillnote <prompt>           # Global mode across all 3,700+ skills"
echo "  /skillnote <category>         # Targeted sequential mode (e.g. /skillnote adapt)"
