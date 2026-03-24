<div align="center">
  <img src="https://img.shields.io/badge/AI-Recommendation_System-6366f1?style=for-the-badge&logo=appveyor" alt="AI Recommendation">
  <img src="https://img.shields.io/badge/Python-Backend-0ea5e9?style=for-the-badge&logo=python" alt="Python API">
  <img src="https://img.shields.io/badge/Vanilla_JS-Frontend-22c55e?style=for-the-badge&logo=javascript" alt="JavaScript">

  # 🛒 BuySmart AI Recommendation System
  
  **A full-stack, AI-powered e-commerce recommendation engine with a beautifully modernized web UI.**
</div>

<br />

## ✨ Features

- **🛍️ Intelligent Product Search**: Find specific products across the catalog in real-time.
- **✨ Personalized Recommendations (`User Rec`)**: Discover products tailored specifically for individual user IDs.
- **🔥 Trending & Popular**: Explore what other users are currently engaging with.
- **💡 "More Like This" & Similar Products**: Deep-dive into items related to any selected product card.
- **🎨 Premium Dark UI**: A blazing-fast, strictly vanilla Frontend utilizing glassmorphism, glowing accents, CSS variables, and silky smooth horizontally-snapping card grids.

---

## 💻 Tech Stack

- **Frontend Core**: Vanilla HTML5, CSS3, JavaScript (ES6+).
- **Frontend Styling**: Google Fonts (`Outfit`), FontAwesome 6, native CSS animations.
- **Backend**: Python (Flask/FastAPI) hosting ML endpoints.
- **Machine Learning**: Pre-computed recommendation matrices and Pickled models (`model.pkl`, `matrix.pkl`, `meta.pkl`).
- **Cloud/Deployment**: The API is hosted and served from Render (`https://buysmart-api-kqj5.onrender.com`).

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

## 🚀 Getting Started Locally

### Prerequisites
- Any modern web browser.
- Python 3.8+ (If you plan to run the backend locally).

### Running the Frontend
The frontend relies completely on native browser technologies and requires no bundlers!

1. Clone the repository.
2. Navigate to the `frontend/` directory.
3. Serve the directory locally (e.g., via Python):
   ```bash
   python -m http.server 8080
   ```
4. Open your browser and go to `http://localhost:8080`.

*(Alternatively, you can just open `index.html` directly in your browser or through the VS Code Live Server extension).*

### Running the Backend

If you wish to run the backend model locally instead of querying the Render deployment:
1. `cd backend/`
2. `pip install -r requirements.txt`
3. Start the server (e.g., `python app.py`)
4. Point your `frontend/script.js` fetch functions to your localized API loopback!

---

<div align="center">
  <i>Developed with ❤️ for the modern web.</i>
</div>