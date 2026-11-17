#!/usr/bin/env bash
# SkillNote Zed AI Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$HOME/.config/zed/prompts"

echo "=== SkillNote Z Code (Zed AI) Installer ==="
echo "Maintainer: Chinmay Prakash Rout"
echo "Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"

mkdir -p "$TARGET_DIR"
cp "$SCRIPT_DIR/.zed/prompts/skillnote.mustache" "$TARGET_DIR/skillnote.mustache"

echo "✔ Successfully installed SkillNote prompt to $TARGET_DIR/skillnote.mustache"
echo ""
echo "Usage in Zed AI Assistant:"
echo "  /skillnote <prompt>           # Global mode across all 3,700+ skills"
echo "  /skillnote <category>         # Targeted sequential mode (e.g. /skillnote adapt)"
