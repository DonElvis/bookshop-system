@echo off
REM ========================================
REM Snack Shop System - Stop Services
REM ========================================

echo.
echo Stopping Snack Shop System services...
echo.

docker-compose down

echo.
echo ✓ All services stopped
echo.
pause