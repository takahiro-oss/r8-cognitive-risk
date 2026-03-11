@echo off
cd /d %~dp0
powershell -ExecutionPolicy Bypass -File "./b.ps1"
pause