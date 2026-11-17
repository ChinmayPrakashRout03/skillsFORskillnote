#!/usr/bin/env bash
# SkillNote Universal Web Installer
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

set -e

REPO_URL="https://github.com/ChinmayPrakashRout03/skillsFORskillnote.git"
INSTALL_DIR="$HOME/.skillnote"
BIN_DIR="$HOME/.local/bin"

echo ""
echo "=================================================================="
echo "    🚀  SKILLNOTE UNIVERSAL ONE-CLICK INSTALLER"
echo "    Adaptive Runtime & Autonomous Engineering Library"
echo "    Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)"
echo "=================================================================="
echo ""

# 1. Download or update ~/.skillnote directory
if [ -d "$INSTALL_DIR/.git" ]; then
    echo "▶ Updating existing SkillNote installation in $INSTALL_DIR..."
    git -C "$INSTALL_DIR" pull --quiet origin main || true
else
    echo "▶ Downloading SkillNote to $INSTALL_DIR..."
    mkdir -p "$INSTALL_DIR"
    git clone --depth 1 "$REPO_URL" "$INSTALL_DIR" --quiet
fi

# 2. Run master installation script
echo "▶ Configuring all 5 Agent IDEs..."
bash "$INSTALL_DIR/Agent Ide/install-all.sh"

# 3. Create global 'skillnote' CLI symlink in ~/.local/bin
mkdir -p "$BIN_DIR"
cat << 'EOF' > "$BIN_DIR/skillnote"
#!/usr/bin/env bash
INSTALL_DIR="$HOME/.skillnote"
if [ ! -d "$INSTALL_DIR" ]; then
    echo "Error: SkillNote not found at $INSTALL_DIR"
    exit 1
fi
python3 "$INSTALL_DIR/Agent Ide/scripts/skillnote.py" "$@"
EOF
chmod +x "$BIN_DIR/skillnote"

# Ensure ~/.local/bin is in PATH in common shell rc files
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

echo ""
echo "=================================================================="
echo "    🎉 INSTALLATION COMPLETE!"
echo "=================================================================="
echo ""
echo "SkillNote is now ready across all your AI Coding Agents:"
echo "  • Antigravity IDE: /skillnote adapt  or  /skillnote <prompt>"
echo "  • OpenCode CLI:    /skillnote secure or  /skillnote <prompt>"
echo "  • Claude Code:     /skillnote adapt  or  /skillnote <prompt>"
echo "  • OpenAI Codex:    /skillnote <prompt>"
echo "  • Zed AI:          /skillnote adapt  or  /skillnote <prompt>"
echo ""
echo "Global CLI command available:"
echo "  skillnote search \"auth jwt\""
echo "  skillnote route \"fix login exception\""
echo "  skillnote verify -c \"pytest\""
echo "=================================================================="
echo ""
