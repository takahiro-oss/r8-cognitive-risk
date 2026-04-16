Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$img = [System.Windows.Forms.Clipboard]::GetImage()
if ($img) {
    $path = "D:\r8_strategy\corpus\screenshot\ss_$(Get-Date -Format 'yyyyMMdd_HHmmss').png"
    $img.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host "[OK] Saved: $path" -ForegroundColor Green
} else {
    Write-Host "[ERROR] No image in clipboard. Use Win+Shift+S first." -ForegroundColor Red
}
