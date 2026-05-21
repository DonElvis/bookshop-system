@echo off
REM ========================================
REM Snack Shop System - Service Status
REM ========================================

cls
echo.
echo ========================================
echo   Snack Shop System - Service Status
echo ========================================
echo.

docker-compose ps

echo.
echo ========================================
echo   SERVICE INFORMATION:
echo ========================================
echo.

if exist .env (
    echo Configuration loaded from .env
) else (
    echo Using default configuration
)

echo.
echo Frontend URL: http://localhost:4200
echo Backend URL: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.

echo ========================================
echo.
pause