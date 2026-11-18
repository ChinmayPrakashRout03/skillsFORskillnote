# SkillNote Clean Uninstaller for Windows PowerShell
# Maintained solely and independently by Chinmay Prakash Rout (ChinmayPrakashRout03)
# GitHub: https://github.com/ChinmayPrakashRout03/skillsFORskillnote

$ErrorActionPreference = "SilentlyContinue"

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "    🗑️  SKILLNOTE UNINSTALLER (WINDOWS)" -ForegroundColor Cyan
Write-Host "    Removing SkillNote runtime, CLI, and Agent IDE integrations..." -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Remove runtime directory
$InstallDir = Join-Path $HOME ".skillnote"
if (Test-Path $InstallDir) {
    Remove-Item -Recurse -Force $InstallDir
    Write-Host "  ✔ Removed .skillnote directory" -ForegroundColor Green
}

# 2. Remove CLI binary
$BinFile = Join-Path $HOME ".local\bin\skillnote.cmd"
if (Test-Path $BinFile) {
    Remove-Item -Force $BinFile
    Write-Host "  ✔ Removed skillnote.cmd CLI" -ForegroundColor Green
}

# 3. Remove Claude Code integration
$ClaudeFile = Join-Path $HOME ".claude\commands\skillnote.md"
if (Test-Path $ClaudeFile) {
    Remove-Item -Force $ClaudeFile
    Write-Host "  ✔ Removed .claude\commands\skillnote.md" -ForegroundColor Green
}

# 4. Remove OpenCode integration
$OpenCodeCmd = Join-Path $HOME ".config\opencode\commands\skillnote.md"
$OpenCodeSkill = Join-Path $HOME ".config\opencode\skills\skillnote"
if (Test-Path $OpenCodeCmd) { Remove-Item -Force $OpenCodeCmd }
if (Test-Path $OpenCodeSkill) { Remove-Item -Recurse -Force $OpenCodeSkill }
Write-Host "  ✔ Removed OpenCode integrations" -ForegroundColor Green

# 5. Remove Antigravity plugin
$AntigravityPlugin = Join-Path $HOME ".gemini\config\plugins\skillnote"
$AntigravitySkill = Join-Path $HOME ".gemini\config\skills\skillnote"
if (Test-Path $AntigravityPlugin) { Remove-Item -Recurse -Force $AntigravityPlugin }
if (Test-Path $AntigravitySkill) { Remove-Item -Recurse -Force $AntigravitySkill }
Write-Host "  ✔ Removed Antigravity plugin" -ForegroundColor Green

# 6. Remove ZCode / Zed integration
$ZCodeSkills = Join-Path $HOME ".zcode\skills\skillnote"
$ZCodeCache = Join-Path $HOME ".zcode\cli\plugins\cache\zcode-plugins-official\skillnote"
$AgentsSkills = Join-Path $HOME ".agents\skills\skillnote"
if (Test-Path $ZCodeSkills) { Remove-Item -Recurse -Force $ZCodeSkills }
if (Test-Path $ZCodeCache) { Remove-Item -Recurse -Force $ZCodeCache }
if (Test-Path $AgentsSkills) { Remove-Item -Recurse -Force $AgentsSkills }
Write-Host "  ✔ Removed ZCode & Zed integrations" -ForegroundColor Green

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "    ✨ SKILLNOTE SUCCESSFULLY UNINSTALLED!" -ForegroundColor Green
Write-Host "    All integrations and cache files have been completely removed." -ForegroundColor Green
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""
