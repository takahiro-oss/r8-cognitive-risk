Set-Location "D:\r8_strategy"
$target = $args[0]
if (-not $target) { Write-Output "No Target"; pause; exit }
uv run --with youtube-transcript-api --with pymupdf r8.py $target
pause