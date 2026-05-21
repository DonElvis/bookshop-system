@echo off
REM ========================================
REM Snack Shop System - Rebuild Images
REM ========================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   Snack Shop System - Rebuild
echo ========================================
echo.
echo This will rebuild all Docker images
echo.

set /p CONFIRM="Continue? (y/n): "

if /i not "%CONFIRM%"=="y" (
    echo Operation cancelled
    exit /b 0
)

echo.
echo Stopping services...
docker-compose down

echo.
echo Rebuilding images (this may take a few minutes)...
docker-compose build --no-cache

echo.
echo Starting services...
docker-compose up -d

echo.
echo Waiting for services to be healthy...
timeout /t 10 /nobreak

echo.
echo ✓ Rebuild complete
echo.
docker-compose ps
echo.
pause