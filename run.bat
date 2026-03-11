@echo off
set /p target="Target(t.txt or URL): "
powershell.exe -ExecutionPolicy Bypass -File ".\b.ps1" "%target%"
pause