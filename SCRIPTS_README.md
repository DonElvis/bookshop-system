# 🚀 Quick Start Scripts

This directory contains Windows batch scripts to easily manage the Snack Shop System.

## 📋 Scripts Overview

### **START.bat** ⭐ (Start Here!)
Main script to start the entire system.

**What it does:**
1. ✓ Checks for Docker and Docker Compose
2. ✓ Pulls latest code from GitHub
3. ✓ Builds Docker images
4. ✓ Starts all services (PostgreSQL, FastAPI Backend, Angular Frontend)
5. ✓ Displays service status and access URLs
6. ✓ Optionally opens frontend in browser

**Usage:**
```bash
Double-click START.bat
# or from command line:
START.bat
```

**Output:**
```
✓ Services Started Successfully!

ACCESS THE SYSTEM:

🌐 Frontend (Angular):
   http://localhost:4200

🔌 Backend API:
   http://localhost:8000

📖 API Documentation (Swagger):
   http://localhost:8000/docs
```

---

### **STOP.bat** ⏹️
Gracefully stop all running services.

**What it does:**
- Stops all Docker containers
- Preserves database data
- Cleans up networks

**Usage:**
```bash
Double-click STOP.bat
```

---

### **STATUS.bat** 📊
Check the status of all services.

**What it does:**
- Shows running containers
- Displays service health
- Lists access URLs

**Usage:**
```bash
Double-click STATUS.bat
```

**Output:**
```
CONTAINER ID   IMAGE                        STATUS              PORTS
abc123...      snackshop_postgres:latest    Up 2 minutes        0.0.0.0:5432->5432/tcp
def456...      snackshop_backend:latest     Up 1 minute         0.0.0.0:8000->8000/tcp
ghi789...      snackshop_frontend:latest    Up 45 seconds       0.0.0.0:4200->80/tcp
```

---

### **LOGS.bat** 📝
View live logs from services.

**What it does:**
- Interactive menu to select which logs to view
- Options:
  1. All services (combined)
  2. Backend API (FastAPI)
  3. Frontend (Angular)
  4. Database (PostgreSQL)
  5. Exit

**Usage:**
```bash
Double-click LOGS.bat
# Select option 1-4
```

**Example Output:**
```
backend_1 | 2026-05-21 16:57:54 INFO:     Uvicorn running on http://0.0.0.0:8000
frontend_1 | ✔ Compiled successfully.
postgres_1 | PostgreSQL is ready to accept connections
```

---

### **REBUILD.bat** 🔨
Rebuild Docker images from scratch.

**What it does:**
- Stops all services
- Removes old images
- Rebuilds from Dockerfile (without cache)
- Starts services again
- Useful after code changes or to fix issues

**Usage:**
```bash
Double-click REBUILD.bat
# Confirm when prompted
```

**⏱️ Time:** 3-5 minutes (downloads dependencies)

---

### **CLEAN.bat** 🧹
Complete cleanup - delete everything.

**⚠️ WARNING:** This action CANNOT be undone!

**What it does:**
- Stops all services
- Removes all containers
- **DELETES all volumes (including database data!)**
- Removes networks

**Usage:**
```bash
Double-click CLEAN.bat
# Type 'yes' when prompted to confirm
```

**Use case:** Fresh start or troubleshooting persistent issues

---

## 🎯 Common Workflows

### First Time Setup
```
1. Double-click START.bat
2. Wait for "Services Started Successfully!"
3. Frontend opens in browser (http://localhost:4200)
4. You're ready to go!
```

### Daily Development
```
1. Double-click START.bat in the morning
2. Work on code
3. Double-click STOP.bat when done (or just close CMD window)
4. Repeat next day
```

### Debugging Issues
```
1. Double-click STATUS.bat to check services
2. If any service is red/unhealthy:
   a. Double-click LOGS.bat to see error details
   b. Fix the code
   c. Double-click REBUILD.bat
3. If issues persist:
   a. Double-click CLEAN.bat
   b. Double-click START.bat
```

### After Pulling Code Changes
```
1. (Services may already be running)
2. Double-click REBUILD.bat to rebuild images
3. Services restart automatically
```

---

## 🔧 Manual Commands (Alternative)

If you prefer using command line instead of batch scripts:

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View status
docker-compose ps

# View logs
docker-compose logs -f           # All services
docker-compose logs -f backend   # Just backend
docker-compose logs -f frontend  # Just frontend
docker-compose logs -f postgres  # Just database

# Rebuild images
docker-compose build --no-cache
docker-compose up -d

# Clean everything
docker-compose down -v
```

---

## 🌐 Access Points

Once services are running:

| Service | URL | Purpose |
|---------|-----|----------|
| **Frontend** | http://localhost:4200 | Angular UI |
| **Backend API** | http://localhost:8000 | REST API |
| **API Docs** | http://localhost:8000/docs | Swagger/OpenAPI |
| **Database** | localhost:5432 | PostgreSQL |

---

## 📊 Service Ports

| Service | Container Port | Host Port |
|---------|---|---|
| **PostgreSQL** | 5432 | 5432 |
| **FastAPI** | 8000 | 8000 |
| **Angular** | 80 | 4200 |

---

## 🗄️ Database Connection

**When connecting from host machine:**
```
Host: localhost
Port: 5432
User: snackshop
Password: snackshop_password
Database: snackshop
```

**When connecting from inside Docker:**
```
Host: postgres
Port: 5432
User: snackshop
Password: snackshop_password
Database: snackshop
```

---

## ⚡ Performance Tips

1. **First run is slow**: Building images takes 3-5 minutes
2. **Subsequent runs are fast**: ~10-15 seconds to start
3. **Close unused services**: Run `STOP.bat` when not developing
4. **Allocate resources**: In Docker Desktop settings, increase CPU/RAM for faster builds

---

## 🐛 Troubleshooting

### "Docker is not installed"
- Install Docker Desktop: https://www.docker.com/products/docker-desktop

### "Port already in use"
- Another service is using port 4200, 8000, or 5432
- Stop that service or change the port in `docker-compose.yml`

### "Services won't start"
- Run `STATUS.bat` to check which service failed
- Run `LOGS.bat` to see error details
- Try `REBUILD.bat`
- If still failing, try `CLEAN.bat` then `START.bat`

### "Database connection refused"
- Make sure PostgreSQL container is running: `STATUS.bat`
- Give PostgreSQL 30 seconds to fully start
- Check logs: `LOGS.bat` → option 4

### "Frontend blank or errors"
- Check backend is running: `STATUS.bat`
- Open browser console (F12) for errors
- Try hard refresh: `Ctrl + Shift + R`

---

## 📞 Need Help?

- Check the main **README.md** in the project root
- View **ARCHITECTURE_OVERVIEW.md** for system design
- See **API documentation**: http://localhost:8000/docs

---

**Built with ❤️ for the Snack Shop System**