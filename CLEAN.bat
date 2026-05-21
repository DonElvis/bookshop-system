@echo off
REM ========================================
REM Snack Shop System - Clean Everything
REM ========================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   ⚠️  WARNING: CLEAN OPERATION
echo ========================================
echo.
echo This will STOP all services and DELETE:
echo   - All containers
echo   - All volumes (including database data!)
echo   - All networks
echo.
echo This action CANNOT be undone!
echo.

set /p CONFIRM="Are you sure? Type 'yes' to confirm: "

if /i not "%CONFIRM%"=="yes" (
    echo Operation cancelled
    exit /b 0
)

echo.
echo Removing all services and volumes...
docker-compose down -v

echo.
echo ✓ Clean complete
echo.
echo You can now run START.bat to begin fresh
echo.
pause