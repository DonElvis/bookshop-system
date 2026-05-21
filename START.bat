@echo off
REM ========================================
REM Snack Shop System - Quick Start Script
REM ========================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo   Snack Shop System - Quick Start
echo ========================================
echo.

REM Check prerequisites
echo [1/4] Checking prerequisites...
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo ✓ Docker found

docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker Compose is not installed
    echo Please ensure Docker Desktop is properly installed with Compose
    pause
    exit /b 1
)
echo ✓ Docker Compose found

REM Pull latest from GitHub
echo.
echo [2/4] Pulling latest from GitHub...
git pull origin main
if %errorlevel% neq 0 (
    echo WARNING: Could not pull from GitHub
    echo Proceeding with local files...
)

REM Build and start containers
echo.
echo [3/4] Building and starting services...
docker-compose up -d
if %errorlevel% neq 0 (
    echo ERROR: Failed to start services
    pause
    exit /b 1
)

REM Wait for services to be ready
echo.
echo [4/4] Waiting for services to be healthy (30 seconds)...
timeout /t 5 /nobreak

REM Check service status
cls
echo.
echo ========================================
echo   ✓ Services Started Successfully!
echo ========================================
echo.
echo SERVICE STATUS:
echo.
docker-compose ps
echo.
echo ========================================
echo   ACCESS THE SYSTEM:
echo ========================================
echo.
echo 🌐 Frontend (Angular):
echo    http://localhost:4200
echo.
echo 🔌 Backend API:
echo    http://localhost:8000
echo.
echo 📖 API Documentation (Swagger):
echo    http://localhost:8000/docs
echo.
echo 🗄️  Database (PostgreSQL):
echo    Host: localhost
echo    Port: 5432
echo    User: snackshop
echo    Password: snackshop_password
echo    Database: snackshop
echo.
echo ========================================
echo   USEFUL COMMANDS:
echo ========================================
echo.
echo View all logs:
echo   docker-compose logs -f
echo.
echo View backend logs:
echo   docker-compose logs -f backend
echo.
echo View frontend logs:
echo   docker-compose logs -f frontend
echo.
echo View database logs:
echo   docker-compose logs -f postgres
echo.
echo Stop all services:
echo   docker-compose down
echo.
echo Remove everything (including data):
echo   docker-compose down -v
echo.
echo ========================================
echo.

REM Optional: Open browser
setlocal enabledelayedexpansion
set /p OPEN_BROWSER="Open frontend in browser? (y/n): "
if /i "!OPEN_BROWSER!"=="y" (
    start http://localhost:4200
)

endlocal