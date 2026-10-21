# Build Tailwind CSS and start the Django development server.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Project = Join-Path $Root "class01"
$Python = Join-Path $Root ".venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Error "Virtualenv not found at $Python. Create it first (uv venv .venv)."
}

Set-Location $Project
Write-Host ">> Building Tailwind CSS..." -ForegroundColor Cyan
& $Python manage.py tailwind build
if ($LASTEXITCODE -ne 0) {
    Write-Error "Tailwind build failed. Check Node.js/npm and NPM_BIN_PATH in .env"
}

Write-Host ">> Starting server at http://127.0.0.1:8000/" -ForegroundColor Green
& $Python manage.py runserver @args
