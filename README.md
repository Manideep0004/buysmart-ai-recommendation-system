<div align="center">
  <img src="https://img.shields.io/badge/AI-Recommendation_System-6366f1?style=for-the-badge&logo=appveyor" alt="AI Recommendation">
  <img src="https://img.shields.io/badge/Python-Backend-0ea5e9?style=for-the-badge&logo=python" alt="Python API">
  <img src="https://img.shields.io/badge/Vanilla_JS-Frontend-22c55e?style=for-the-badge&logo=javascript" alt="JavaScript">

  # 🛒 BuySmart AI Recommendation System
  
  **A full-stack, AI-powered e-commerce recommendation engine with a beautifully modernized web UI.**
</div>

<br />

## ✨ Features

- **🛍️ Intelligent Product Search**: Find specific products across the catalog in real-time with case-insensitive fuzzy matching.
- **✨ Personalized Recommendations (`User Rec`)**: Discover products tailored specifically for individual user IDs using KNN algorithms.
- **🔥 Trending & Popular**: Explore what other users are currently engaging with via pre-computed suggestion categories.
- **💡 "More Like This" & Similar Products**: Deep-dive into items related to any selected product card with one click.
- **🎨 Premium Dark UI**: Glassmorphism design with smooth animations, glowing accents, CSS variables, and silky card grids.
- **👤 User Authentication**: Secure signup/login with JWT tokens and bcrypt password hashing.
- **⚡ Lightning Fast**: Sub-100ms recommendation latency using pre-trained scikit-learn models.
- **📱 Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices.
- **🔐 API Security**: CORS enabled, email validation, secure token management.
- **📊 Interactive Analytics**: Real-time product search and user-specific track recommendations.

---

## 💻 Tech Stack

**Frontend:**
- HTML5, CSS3, Vanilla JavaScript (ES6+)
- Google Fonts (`Outfit`, `Plus Jakarta Sans`)
- FontAwesome 6 Icons
- Intersection Observer API for animations
- No build tools required

**Backend:**
- FastAPI (modern Python web framework)
- Uvicorn (ASGI server)
- Pydantic (data validation)
- python-jose (JWT authentication)
- passlib + bcrypt (password security)

**Machine Learning:**
- scikit-learn (K-Nearest Neighbors)
- pandas (data processing)
- numpy (numerical computing)
- scipy (scientific functions)
- Pre-trained pickle models

**Database & Storage:**
- Pickle files (model, matrix, metadata)
- JSON files (product data)
- CSV (rating history)
- In-memory user storage (extendable to PostgreSQL/MongoDB)

**Deployment:**
- FastAPI backend on Render
- Vanilla frontend (static hosting ready)
- Environment variables via python-dotenv

---

## 📖 Comprehensive Features & Tech Stack Documentation

For detailed information about every feature, technology, and capability, see the **[FEATURES_AND_TECHSTACK.md](FEATURES_AND_TECHSTACK.md)** file which includes:
- ✅ Complete feature breakdown with examples
- ✅ Full tech stack details with versions
- ✅ API endpoint documentation
- ✅ Architecture diagrams
- ✅ Performance metrics
- ✅ Learning resources
- ✅ Future enhancement opportunities

---

---

## 📂 Project Structure

```bash
📦 buysmart-ai-recommendation-system
├── 📂 backend
│   ├── app.py             # Main API Server
│   ├── requirements.txt   # Python dependencies
│   ├── matrix.pkl         # Recommendation similarities
│   └── meta.pkl           # Product metadata mappings
├── 📂 frontend
│   ├── index.html         # Main app markup
│   ├── style.css          # Premium glassmorphism dark theme
│   └── script.js          # API consumption & DOM rendering
├── 📂 dashboard           # Analytical dashboards (future/wip)
├── 📂 database            # Local DB / Data configurations
├── 📂 docs                # Additional project documentation
├── 📂 model               # Model training scripts and notebooks
└── 📂 notebooks           # Jupyter env for NLP/RecSys modeling
```

---

## 🚀 Getting Started - Complete Setup Guide

### Prerequisites

Before starting the project, ensure your system has the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Usually comes with Python (verify with `pip --version`)
- **Git** (optional) - [Download Git](https://git-scm.com/)
- **Any modern web browser** - Chrome, Firefox, Edge, Safari

Verify your installations:
```bash
python --version
pip --version
```

---

### Step 1: Clone/Download the Project

If using Git:
```bash
git clone <your-repo-url>
cd buysmart-ai-recommendation-system
```

Or download the ZIP file and extract it.

---

### Step 2: Setup Backend

#### Navigate to Backend Directory
```bash
cd backend
```

#### Create Virtual Environment (Recommended)
This isolates Python dependencies for this project.

**Windows (PowerShell/CMD):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

The `requirements.txt` contains:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `pandas` - Data processing
- `scikit-learn` - ML library
- `python-jose` - JWT tokens
- `passlib` - Password hashing
- And other required packages

#### Verify Model Files Exist
The backend requires pre-trained model files. Ensure these exist in the `backend/` directory:
- `model.pkl` - The recommendation ML model
- `matrix.pkl` - Similarity matrix
- `meta.pkl` - Product metadata
- `product_map.pkl` - Product ID mappings

#### Start the Backend Server
```bash
# From inside the backend directory
python run.py
```

Or manually with uvicorn:
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ **Success**: You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

Access the API documentation at: **`http://localhost:8000/docs`**

---

### Step 3: Setup Frontend

#### Navigate to Frontend Directory
```bash
cd frontend
```

#### Start Frontend Server
```bash
# From inside the frontend directory
python -m http.server 3000
```

Or use any other local server:

**Node.js (if installed):**
```bash
npx http-server -p 3000
```

**Python (alternative port):**
```bash
python -m http.server 8080
```

✅ **Success**: You should see:
```
Serving HTTP on :: port 3000 (http://[::]:3000/) ...
```

---

### Step 4: Access the Application

Open your browser and navigate to:

**Frontend**: `http://localhost:3000`
**Backend API Docs**: `http://localhost:8000/docs`

🎉 **The application is now running!**

---

## 📋 Project Startup Summary

Here's a quick checklist for starting on a new system:

1. ✅ Install Python 3.8+
2. ✅ Clone/Download project
3. ✅ Navigate to `backend/` folder
4. ✅ Create virtual environment: `python -m venv venv`
5. ✅ Activate virtual environment
6. ✅ Install dependencies: `pip install -r requirements.txt`
7. ✅ Start backend: `python run.py` (runs on port 8000)
8. ✅ In new terminal, navigate to `frontend/` folder
9. ✅ Start frontend: `python -m http.server 3000` (runs on port 3000)
10. ✅ Open browser to `http://localhost:3000`

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'fastapi'"
**Solution**: Make sure you've activated the virtual environment and installed requirements:
```bash
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"
**Solution**: Use a different port:
```bash
python -m uvicorn app.main:app --port 8001
```

### Issue: "No module named 'app'"
**Solution**: Ensure you're running the command from the `backend/` directory.

### Issue: CORS errors in frontend
**Solution**: Backend CORS middleware is configured to accept all origins. If errors persist:
1. Check backend is running on `http://localhost:8000`
2. Check frontend `script.js` has correct `API_BASE` URL
3. Verify `.env` file exists in project root

### Issue: "Can't connect to backend from frontend"
**Solution**: 
- Backend must be running on `http://localhost:8000`
- Frontend `script.js` should show: `const API_BASE = "http://localhost:8000"`
- Check both are running in separate terminal windows

### Issue: "Permission denied" when activating virtual environment (Mac/Linux)
**Solution**: Make script executable:
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

---

## 🌍 Environment Variables

Create a `.env` file in the **project root** if it doesn't exist:

```env
JWT_SECRET_KEY=your_secret_key_here_change_in_production
SUPABSE_PASS=your_password_here
```

**Format**: Use `KEY=VALUE` (not `KEY : VALUE`)

---

## 📱 API Endpoints

Once the backend is running, these endpoints are available:

```
POST   /auth/signup           - Register new user
POST   /auth/login            - Login user
GET    /products/{index}      - Get recommendations by index
GET    /products/by-id/{pid}  - Get recommendations by product ID
GET    /products/search/{query} - Search products
```

Full documentation: `http://localhost:8000/docs`

---

## 🎯 Quick Start Commands (Copy-Paste)

**Terminal 1 (Backend):**
```bash
cd backend
python -m venv venv
# Activate venv (Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python run.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
python -m http.server 3000
```

Then open: `http://localhost:3000`

---



<div align="center">
  <i>Developed with ❤️ for the modern web.</i>
</div>