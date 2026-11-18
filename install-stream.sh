#!/usr/bin/env bash
# SkillNote Zero-Disk Streaming Installer
# Installs SkillNote across all 5 Agent IDEs WITHOUT cloning the git repository
# Total size: ~1 MB (vs 378 MB full repository). Total time: ~2 seconds.
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

set -e

RAW_BASE="https://raw.githubusercontent.com/ChinmayPrakashRout03/skillsFORskillnote/main"
INSTALL_DIR="$HOME/.skillnote"
BIN_DIR="$HOME/.local/bin"

echo ""
echo "=================================================================="
echo "    🚀  SKILLNOTE ZERO-DISK STREAMING INSTALLER"
echo "    100% Cloud-Streamed • Zero Git Clone • Zero Disk Bloat"
echo "    Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)"
echo "=================================================================="
echo ""

# 1. Prepare minimal directory in ~/.skillnote (~1 MB total)
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

echo "▶ [1/4] Fetching lightweight catalog index & streaming client (~1MB)..."
curl -fsSL "$RAW_BASE/Agent%20Ide/resources/skills-index.json" -o "$INSTALL_DIR/skills-index.json"
curl -fsSL "$RAW_BASE/Agent%20Ide/scripts/skillnote-stream.py" -o "$INSTALL_DIR/skillnote-stream.py"
chmod +x "$INSTALL_DIR/skillnote-stream.py"

# Create global 'skillnote' CLI command in ~/.local/bin
cat << 'EOF' > "$BIN_DIR/skillnote"
#!/usr/bin/env bash
exec python3 "$HOME/.skillnote/skillnote-stream.py" "$@"
EOF
chmod +x "$BIN_DIR/skillnote"

# Ensure ~/.local/bin is in PATH in shell rc files
SHELL_RC=""
if [ -n "$ZSH_VERSION" ] || [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [ -n "$SHELL_RC" ]; then
    if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$SHELL_RC"; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    fi
fi
echo "  ✔ Global CLI installed to $BIN_DIR/skillnote"

# 2. Fetch master SKILL.md definition
echo "▶ [2/4] Downloading core cognitive specification..."
curl -fsSL "$RAW_BASE/Agent%20Ide/SKILL.md" -o "$INSTALL_DIR/SKILL.md"

# 3. Configure all 5 Agent IDEs
echo "▶ [3/4] Configuring all 5 Agent IDEs..."

# Claude Code
mkdir -p "$HOME/.claude/commands"
curl -fsSL "$RAW_BASE/Agent%20Ide/plugins/claude-code/commands/skillnote.md" -o "$HOME/.claude/commands/skillnote.md"
echo "  ✔ Claude Code command installed to ~/.claude/commands/skillnote.md"

# OpenCode CLI
mkdir -p "$HOME/.config/opencode/commands"
mkdir -p "$HOME/.config/opencode/skills/skillnote"
curl -fsSL "$RAW_BASE/Agent%20Ide/plugins/opencode/commands/skillnote.md" -o "$HOME/.config/opencode/commands/skillnote.md"
cp "$INSTALL_DIR/SKILL.md" "$HOME/.config/opencode/skills/skillnote/SKILL.md"
echo "  ✔ OpenCode command & skill installed"

# Antigravity IDE
mkdir -p "$HOME/.gemini/config/skills/skillnote"
mkdir -p "$HOME/.gemini/config/plugins/skillnote/commands"
mkdir -p "$HOME/.gemini/config/plugins/skillnote/skills/skillnote"
cp "$INSTALL_DIR/SKILL.md" "$HOME/.gemini/config/skills/skillnote/SKILL.md"
cp "$INSTALL_DIR/SKILL.md" "$HOME/.gemini/config/plugins/skillnote/skills/skillnote/SKILL.md"

cat << 'EOF' > "$HOME/.gemini/config/plugins/skillnote/plugin.json"
{
  "name": "skillnote",
  "description": "SkillNote Zero-Disk Adaptive Cognitive Architecture",
  "version": "1.0.0",
  "author": {
    "name": "Chinmay Prakash Rout",
    "url": "https://github.com/ChinmayPrakashRout03"
  },
  "repository": "https://github.com/ChinmayPrakashRout03/skillsFORskillnote"
}
EOF

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
    pass
" 2>/dev/null || true
fi
echo "  ✔ Antigravity plugin configured"

# ZCode.app & Zed
mkdir -p "$HOME/.zcode/skills/skillnote"
mkdir -p "$HOME/.zcode/cli/plugins/cache/zcode-plugins-official/skillnote/1.0.0/skills/skillnote"
mkdir -p "$HOME/.agents/skills/skillnote"
cp "$INSTALL_DIR/SKILL.md" "$HOME/.zcode/skills/skillnote/SKILL.md"
cp "$INSTALL_DIR/SKILL.md" "$HOME/.zcode/cli/plugins/cache/zcode-plugins-official/skillnote/1.0.0/skills/skillnote/SKILL.md"
cp "$INSTALL_DIR/SKILL.md" "$HOME/.agents/skills/skillnote/SKILL.md"

mkdir -p "$HOME/.config/zed/prompts"
curl -fsSL "$RAW_BASE/Agent%20Ide/plugins/z-code/.zed/prompts/skillnote.mustache" -o "$HOME/.config/zed/prompts/skillnote.mustache" 2>/dev/null || true
echo "  ✔ ZCode & Zed skills configured"

# 4. Final Summary
echo ""
echo "=================================================================="
echo "    🎉 ZERO-DISK INSTALLATION COMPLETE!"
echo "=================================================================="
echo ""
echo "Stats:"
echo "  • Disk space used:    ~1.2 MB total (0 files cloned from git!)"
echo "  • Skills accessible:  3,786 primary skills (cloud streamed in RAM)"
echo "  • Installation time:  ~2 seconds"
echo ""
echo "Ready across all your AI Coding Agents:"
echo "  • Antigravity IDE: /skillnote <prompt>  or  /skillnote adapt"
echo "  • Claude Code:     /skillnote <prompt>  or  /skillnote secure"
echo "  • OpenCode CLI:    /skillnote <prompt>  or  /skillnote workflow"
echo "  • ZCode / Zed AI:  @skillnote <prompt>  or  /skillnote refine"
echo ""
echo "CLI utility ready:"
echo "  skillnote \"fix python login exception\""
echo "  skillnote search \"oauth2 auth\""
echo "  skillnote verify -v \"pytest\""
echo "=================================================================="
echo ""
