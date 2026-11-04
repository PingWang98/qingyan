$ErrorActionPreference = "Stop"
$sourceDir = Join-Path $PSScriptRoot "01_五大通用AI影视全局技能 (skills)"
$targetDir = Join-Path $env:USERPROFILE ".gemini\config\skills"

if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

Get-ChildItem -Path $sourceDir -Directory | ForEach-Object {
    $dest = Join-Path $targetDir $_.Name
    Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
    Write-Host "✅ 已安装全局技能: $($_.Name) -> $dest" -ForegroundColor Green
}

Write-Host "`n🎉 五大通用 AI 影视制片技能已全部安装完毕！现在可以直接在 Antigravity 中继续工作了。" -ForegroundColor Cyan
Pause
