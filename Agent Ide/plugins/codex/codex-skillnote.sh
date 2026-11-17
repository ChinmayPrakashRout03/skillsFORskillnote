#!/usr/bin/env bash
# SkillNote Codex CLI Wrapper
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"
RUNNER="$ROOT_DIR/Agent Ide/skillnote-runner.py"

if [ ! -f "$RUNNER" ]; then
    echo "Error: SkillNote runner not found at $RUNNER"
    exit 1
fi

python3 "$RUNNER" "$@"
