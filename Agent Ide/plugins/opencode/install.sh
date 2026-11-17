#!/usr/bin/env bash
# SkillNote OpenCode Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMMAND_SRC="$SCRIPT_DIR/commands/skillnote.md"
TARGET_DIR="$HOME/.config/opencode/commands"

echo "=== SkillNote OpenCode Plugin Installer ==="
echo "Maintainer: Chinmay Prakash Rout"
echo "Repository: https://github.com/ChinmayPrakashRout03/skillsFORskillnote"

mkdir -p "$TARGET_DIR"

if [ -f "$COMMAND_SRC" ]; then
    cp "$COMMAND_SRC" "$TARGET_DIR/skillnote.md"
    echo "✔ Successfully installed /skillnote command to $TARGET_DIR/skillnote.md"
    echo ""
    echo "Usage in OpenCode CLI:"
    echo "  opencode"
    echo "  > /skillnote <prompt>           # Global mode across all 3,700+ skills"
    echo "  > /skillnote <category>         # Targeted sequential mode (e.g. /skillnote adapt)"
else
    echo "Error: Command source not found at $COMMAND_SRC"
    exit 1
fi
