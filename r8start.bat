@echo off
cd /d D:\r8_strategy
powershell -NoExit -ExecutionPolicy Bypass -Command ".\.venv\Scripts\Activate.ps1; Write-Host '[R8] 環境起動完了' -ForegroundColor Green"
