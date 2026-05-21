# 📈 Snack Shop System - Quick Reference Guide

## 🚀 Getting Started

### First-Time Setup (5 minutes)
```batch
1. Double-click START.bat
2. Wait for "Services Started Successfully!"
3. Open http://localhost:4200 in browser
4. You're ready to develop!
```

---

## 💲 Quick Scripts Reference

### 🚀 START.bat
```
What:  Start all services
When:  First time or daily
Time:  3-5 minutes (first), 10-15s (subsequent)
Do:    Checks Docker → Pulls code → Builds → Starts → Shows URLs
```

### ⏹️ STOP.bat
```
What:  Stop all services gracefully
When:  End of day or before restart
Time:  5-10 seconds
Note:  Database data is preserved
```

### 📊 STATUS.bat
```
What:  Show service status
When:  Check if services are running
Time:  1-2 seconds
Do:    Shows containers, ports, URLs
```

### 📝 LOGS.bat
```
What:  View live logs
When:  Debugging issues
Time:  Interactive
Do:    Menu to select which service logs to view
```

### 🔨 REBUILD.bat
```
What:  Rebuild images from scratch
When:  After code changes or if stuck
Time:  3-5 minutes
Do:    Stops → Removes old images → Builds → Starts
```

### 🧹 CLEAN.bat
```
What:  Delete everything (nuclear option)
When:  Fresh start needed
Time:  30 seconds
Warn:  ⚠️ DELETES database data! Cannot undo!
Do:    Removes containers, images, volumes, networks
```

---

## 🌐 Access URLs

| Component | URL | Purpose | Credentials |
|-----------|-----|---------|-------------|
| **Frontend** | http://localhost:4200 | Angular UI | username/password |
| **API** | http://localhost:8000 | REST endpoints | /api/v1/* |
| **Docs** | http://localhost:8000/docs | Swagger UI | (no auth) |
| **Database** | localhost:5432 | PostgreSQL | snackshop / snackshop_password |

---

## 🔌 API Endpoints Cheat Sheet

### Authentication
```
POST /api/v1/auth/register
  body: {"username": "...", "email": "...", "password": "..."}

POST /api/v1/auth/login
  body: {"username": "...", "password": "..."}
  returns: {"access_token": "...", "token_type": "bearer"}
```

### Products
```
GET    /api/v1/products                    # List all
POST   /api/v1/products                    # Create
GET    /api/v1/products/{id}               # Get one
PUT    /api/v1/products/{id}               # Update
DELETE /api/v1/products/{id}               # Delete
```

### Inventory
```
GET    /api/v1/inventory                   # List all
GET    /api/v1/inventory/low-stock         # Low stock alerts
GET    /api/v1/inventory/{product_id}      # Get stock
PATCH  /api/v1/inventory/{id}/quantity     # Update quantity
PATCH  /api/v1/inventory/{id}/reorder      # Set reorder level
```

### Orders (POS)
```
GET    /api/v1/orders                      # List orders
POST   /api/v1/orders                      # Create order
GET    /api/v1/orders/{id}                 # Get order
PATCH  /api/v1/orders/{id}/status          # Change status
PATCH  /api/v1/orders/{id}/cancel          # Cancel order
```

### Customers
```
GET    /api/v1/customers                   # List customers
POST   /api/v1/customers                   # Create customer
GET    /api/v1/customers/{id}              # Get customer
PUT    /api/v1/customers/{id}              # Update customer
PATCH  /api/v1/customers/{id}/loyalty      # Add loyalty points
DELETE /api/v1/customers/{id}              # Delete customer
```

### Staff
```
GET    /api/v1/staff                       # List staff
POST   /api/v1/staff                       # Create staff
GET    /api/v1/staff/{id}                  # Get staff
PUT    /api/v1/staff/{id}                  # Update staff
DELETE /api/v1/staff/{id}                  # Deactivate
```

### Health Check
```
GET    /api/v1/health                      # System status
```

---

## �� Database Tables

```
users
├─ id (PK)
├─ username (UNIQUE)
├─ email (UNIQUE)
├─ hashed_password
├─ full_name
├─ role (admin|manager|cashier|inventory_staff)
├─ is_active
└─ timestamps

products
├─ id (PK)
├─ name (INDEX)
├─ category_id (FK → categories)
├─ price
├─ cost
├─ is_active
└─ timestamps

inventory
├─ id (PK)
├─ product_id (FK → products, UNIQUE)
├─ quantity
├─ reorder_level
└─ timestamps

orders
├─ id (PK)
├─ customer_id (FK → customers, nullable)
├─ total_amount
├─ discount_amount
├─ payment_method (enum)
├─ status (pending|completed|cancelled)
└─ timestamps

order_items
├─ id (PK)
├─ order_id (FK → orders)
├─ product_id (FK → products)
├─ quantity
├─ unit_price
└─ created_at

customers
├─ id (PK)
├─ name (INDEX)
├─ email (UNIQUE)
├─ phone (UNIQUE)
├─ loyalty_points
├─ total_spent
└─ timestamps

staff
├─ id (PK)
├─ name (INDEX)
├─ position
├─ shift (enum)
├─ hourly_rate
├─ is_active
└─ timestamps

categories
├─ id (PK)
├─ name (UNIQUE)
└─ timestamps

audit_logs
├─ id (PK)
├─ user_id
├─ action
├─ resource_type
├─ resource_id
├─ details
└─ created_at (INDEX)
```

---

## 🔨 Development Workflow

### Making Code Changes
```
1. Services running? No → Run START.bat
2. Edit your code (backend or frontend)
3. Services auto-reload? 
   - Backend (FastAPI): YES ✓ (watches for changes)
   - Frontend (Angular): YES ✓ (ng serve watches)
4. Test in browser at http://localhost:4200
5. Done? Run STOP.bat
```

### If Services Won't Reload
```
1. Run STATUS.bat
2. Check logs: LOGS.bat
3. Try REBUILD.bat
4. If stuck, CLEAN.bat then START.bat
```

### Database Changes
```
1. Modify model in backend/app/models/
2. If using migrations: apply them
3. REBUILD.bat will recreate tables
4. Old data is lost (clean rebuild)
```

---

## 🐛 Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| **Port 4200 in use** | Stop other services on :4200 or change port |
| **Port 8000 in use** | Stop other services on :8000 or change port |
| **"Cannot connect to db"** | Wait 30s for PostgreSQL, check LOGS.bat |
| **Frontend is blank** | Check backend is running (STATUS.bat), F12 for errors |
| **API returns 401** | Token expired, login again at /login |
| **Services stuck** | LOGS.bat to see errors, then REBUILD.bat |
| **Lost data** | If you ran CLEAN.bat, data is deleted permanently |
| **Container won't start** | Run LOGS.bat to see error, try REBUILD.bat |

---

## 📋 File Locations

```
Project Root/
├── START.bat              ← Run this first
├── STOP.bat               ← Stop services
├── STATUS.bat             ← Check status
├── LOGS.bat               ← View logs
├── REBUILD.bat            ← Rebuild images
├── CLEAN.bat              ← Delete everything
├── SCRIPTS_README.md      ← Detailed script help
├── QUICK_REFERENCE.md     ← This file
├── ARCHITECTURE_OVERVIEW.md
├── README.md
├── docker-compose.yml
│
├── backend/               ← FastAPI (Python)
│   ├── app/
│   │   ├── models/        ← Database models
│   │   ├── schemas/       ← Request/response schemas
│   │   ├── crud/          ← Database operations
│   │   ├── routes/        ← API endpoints
│   │   ├── auth/          ← Security (JWT, bcrypt)
│   │   ├── main.py        ← FastAPI app
│   │   └── database.py    ← DB configuration
│   ├── Dockerfile
│   └── requirements.txt
│
└── frontend/              ← Angular (TypeScript)
    ├── src/
    │   ├── app/
    │   │   ├── pages/     ← Feature modules (8)
    │   │   ├── services/  ← API services
    │   │   ├── models/    ← TypeScript interfaces
    │   │   └── ...
    │   ├── styles.scss
    │   ├── index.html
    │   └── main.ts
    ├── Dockerfile
    ├── nginx.conf
    ├── package.json
    └── angular.json
```

---

## ✨ Tech Stack Summary

| Component | Technology | Version |
|-----------|-----------|----------|
| **Backend** | FastAPI | 0.104.1 |
| **Backend Lang** | Python | 3.11 |
| **Database** | PostgreSQL | 15 |
| **Frontend** | Angular | 17 |
| **Frontend Lang** | TypeScript | 5.2 |
| **UI Library** | Angular Material | 17 |
| **Auth** | JWT + bcrypt | - |
| **Container** | Docker | Latest |
| **Orchestration** | Docker Compose | 3.8 |

---

## 📄 Documentation Files

| File | Purpose | Read When |
|------|---------|----------|
| **README.md** | Main documentation | Getting started |
| **ARCHITECTURE_OVERVIEW.md** | System design & structure | Understanding the system |
| **SCRIPTS_README.md** | Detailed script help | Using scripts |
| **QUICK_REFERENCE.md** | This file! | Quick lookup |

---

## 📆 Git Workflow

```bash
# Check status
git status

# View recent commits
git log --oneline -10

# Pull latest
git pull origin main

# Make changes
# (edit files)

# Stage changes
git add .

# Commit
git commit -m "description"

# Push
git push origin main
```

---

## 📱 Default Credentials

**Database:**
```
Host: localhost
Port: 5432
User: snackshop
Password: snackshop_password
Database: snackshop
```

**JWT Auth:**
```
Secret: dev-secret-key-change-in-production
Expiry: 30 minutes
Algorithm: HS256
```

---

**Always check SCRIPTS_README.md for more detailed help!**
