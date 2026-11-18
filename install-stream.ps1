# SkillNote Zero-Disk Streaming Installer for Windows PowerShell
# Installs SkillNote across all 5 Agent IDEs WITHOUT cloning the git repository
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

$ErrorActionPreference = "Stop"

$RawBase = "https://raw.githubusercontent.com/ChinmayPrakashRout03/skillsFORskillnote/main"
$InstallDir = Join-Path $HOME ".skillnote"
$BinDir = Join-Path $HOME ".local\bin"

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "    🚀  SKILLNOTE ZERO-DISK STREAMING INSTALLER (WINDOWS)" -ForegroundColor Cyan
Write-Host "    100% Cloud-Streamed • Zero Git Clone • Zero Disk Bloat" -ForegroundColor Cyan
Write-Host "    Maintained by: Chinmay Prakash Rout (ChinmayPrakashRout03)" -ForegroundColor DarkCyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Create directories
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
New-Item -ItemType Directory -Force -Path $BinDir | Out-Null

# 2. Download lightweight catalog & streaming client
Write-Host "▶ [1/3] Downloading lightweight catalog index & client (~1MB)..." -ForegroundColor Yellow
Invoke-RestMethod -Uri "$RawBase/Agent%20Ide/resources/skills-index.json" -OutFile "$InstallDir\skills-index.json"
Invoke-RestMethod -Uri "$RawBase/Agent%20Ide/scripts/skillnote-stream.py" -OutFile "$InstallDir\skillnote-stream.py"
Invoke-RestMethod -Uri "$RawBase/Agent%20Ide/SKILL.md" -OutFile "$InstallDir\SKILL.md"

# Create Windows batch wrapper skillnote.cmd in .local\bin
$BatchContent = @"
@echo off
python "%USERPROFILE%\.skillnote\skillnote-stream.py" %*
"@
Set-Content -Path "$BinDir\skillnote.cmd" -Value $BatchContent -Encoding ASCII

# Ensure ~/.local/bin is in User PATH
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($UserPath -notlike "*$BinDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$UserPath;$BinDir", "User")
    $env:Path += ";$BinDir"
    Write-Host "  ✔ Added $BinDir to User PATH" -ForegroundColor Green
}

# 3. Configure Agent IDEs
Write-Host "▶ [2/3] Configuring Agent IDEs..." -ForegroundColor Yellow

# Claude Code
$ClaudeCommands = Join-Path $HOME ".claude\commands"
New-Item -ItemType Directory -Force -Path $ClaudeCommands | Out-Null
Invoke-RestMethod -Uri "$RawBase/Agent%20Ide/plugins/claude-code/commands/skillnote.md" -OutFile "$ClaudeCommands\skillnote.md"
Write-Host "  ✔ Claude Code command installed to .claude\commands" -ForegroundColor Green

# OpenCode
$OpenCodeCommands = Join-Path $HOME ".config\opencode\commands"
$OpenCodeSkills = Join-Path $HOME ".config\opencode\skills\skillnote"
New-Item -ItemType Directory -Force -Path $OpenCodeCommands | Out-Null
New-Item -ItemType Directory -Force -Path $OpenCodeSkills | Out-Null
Invoke-RestMethod -Uri "$RawBase/Agent%20Ide/plugins/opencode/commands/skillnote.md" -OutFile "$OpenCodeCommands\skillnote.md"
Copy-Item "$InstallDir\SKILL.md" "$OpenCodeSkills\SKILL.md" -Force
Write-Host "  ✔ OpenCode command & skill installed" -ForegroundColor Green

# Antigravity IDE
$AntigravityPlugin = Join-Path $HOME ".gemini\config\plugins\skillnote"
$AntigravitySkill = Join-Path $HOME ".gemini\config\plugins\skillnote\skills\skillnote"
New-Item -ItemType Directory -Force -Path $AntigravitySkill | Out-Null
Copy-Item "$InstallDir\SKILL.md" "$AntigravitySkill\SKILL.md" -Force

$PluginJson = @"
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
"@
Set-Content -Path "$AntigravityPlugin\plugin.json" -Value $PluginJson -Encoding UTF8
Write-Host "  ✔ Antigravity plugin configured" -ForegroundColor Green

# ZCode / Zed
$ZCodeSkills = Join-Path $HOME ".zcode\skills\skillnote"
$ZCodeCache = Join-Path $HOME ".zcode\cli\plugins\cache\zcode-plugins-official\skillnote\1.0.0\skills\skillnote"
$AgentsSkills = Join-Path $HOME ".agents\skills\skillnote"
New-Item -ItemType Directory -Force -Path $ZCodeSkills | Out-Null
New-Item -ItemType Directory -Force -Path $ZCodeCache | Out-Null
New-Item -ItemType Directory -Force -Path $AgentsSkills | Out-Null
Copy-Item "$InstallDir\SKILL.md" "$ZCodeSkills\SKILL.md" -Force
Copy-Item "$InstallDir\SKILL.md" "$ZCodeCache\SKILL.md" -Force
Copy-Item "$InstallDir\SKILL.md" "$AgentsSkills\SKILL.md" -Force
Write-Host "  ✔ ZCode & Zed skills configured" -ForegroundColor Green

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "    🎉 ZERO-DISK INSTALLATION COMPLETE!" -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ready across all AI Coding Agents:"
Write-Host "  • Antigravity IDE: /skillnote <prompt>  or  /skillnote adapt"
Write-Host "  • Claude Code:     /skillnote <prompt>  or  /skillnote secure"
Write-Host "  • OpenCode CLI:    /skillnote <prompt>  or  /skillnote workflow"
Write-Host "  • ZCode / Zed AI:  @skillnote <prompt>  or  /skillnote refine"
Write-Host ""
Write-Host "CLI command available:"
Write-Host "  skillnote ""fix login exception"""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""
