@echo off
REM ========================================
REM Snack Shop System - View Logs
REM ========================================

setlocal enabledelayedexpansion

cls
echo.
echo ========================================
echo   Snack Shop System - Live Logs
echo ========================================
echo.
echo Select which logs to view:
echo.
echo 1) All services (combined)
echo 2) Backend API (FastAPI)
echo 3) Frontend (Angular)
echo 4) Database (PostgreSQL)
echo 5) Exit
echo.

set /p CHOICE="Enter your choice (1-5): "

if "%CHOICE%"=="1" (
    docker-compose logs -f
) else if "%CHOICE%"=="2" (
    docker-compose logs -f backend
) else if "%CHOICE%"=="3" (
    docker-compose logs -f frontend
) else if "%CHOICE%"=="4" (
    docker-compose logs -f postgres
) else if "%CHOICE%"=="5" (
    exit /b 0
) else (
    echo Invalid choice
    pause
    exit /b 1
)

endlocal