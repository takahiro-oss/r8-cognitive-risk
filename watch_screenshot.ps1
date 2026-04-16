Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$screenshotDir = "D:\r8_strategy\corpus\screenshot"
$scanDir       = "D:\r8_strategy\corpus\phase2\scan"
$tesseract     = "C:\Users\Mow\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
$phase2Dir     = "D:\r8_strategy\corpus\phase2"
$doneDir       = "$screenshotDir\done"
$exts          = @(".png", ".jpg", ".jpeg", ".bmp")

if (-not (Test-Path $doneDir)) { New-Item -ItemType Directory -Path $doneDir | Out-Null }

Write-Host "[WATCH] Monitoring: $screenshotDir (recursive)" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop." -ForegroundColor Yellow

function Get-MaxNumber {
    $max = 0
    Get-ChildItem $phase2Dir -Recurse -File | ForEach-Object {
        if ($_.Name -match '(?:web|note|sn|ad|bl|phish)[_]?(\d+)') {
            $num = [int]$Matches[1]
            if ($num -gt $max) { $max = $num }
        }
    }
    return $max
}

while ($true) {
    $images = Get-ChildItem $screenshotDir -Recurse -File | Where-Object {
        ($exts -contains $_.Extension.ToLower()) -and
        ($_.FullName -notlike "*\done\*")
    }

    foreach ($img in $images) {
        $nextNum = (Get-MaxNumber) + 1
        $outName = "sn$nextNum.txt"
        $outPath = "$scanDir\$outName"
        $outBase = $outPath -replace "\.txt$", ""

        Write-Host "[OCR] $($img.Name) -> $outName" -ForegroundColor Yellow

        & $tesseract $img.FullName $outBase -l jpn --psm 6 2>$null

        if (Test-Path $outPath) {
            $content = Get-Content $outPath -Raw -Encoding UTF8
            $header  = "[SOURCE] screenshot: $($img.Name)`n`n"
            Set-Content $outPath -Value ($header + $content) -Encoding UTF8
            Move-Item $img.FullName "$doneDir\$($img.Name)" -Force
            Write-Host "[OK] Saved: $outName" -ForegroundColor Green
        } else {
            Write-Host "[ERROR] OCR failed: $($img.Name)" -ForegroundColor Red
        }
    }

    Start-Sleep -Seconds 2
}
