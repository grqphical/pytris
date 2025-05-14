Write-Host "PyTris Windows Build Script Version 1.0.0, Made by grqphical"

if (!(Test-Path -Path "./venv")) {
    Write-Host "Creating virtual env..."
    python -m venv venv > $null
}

Write-Host "Installing Dependencies..."
./venv/scripts/activate.ps1 > $null
pip install pygame-ce pyinstaller Pillow > $null

Write-Host "Building PyTris"
pyinstaller PyTris.spec

Write-Host ""
Write-Host "PyTris has been built in dist/. Make sure to include all the asset folders when distributing"