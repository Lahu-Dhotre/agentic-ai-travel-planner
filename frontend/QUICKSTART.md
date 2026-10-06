# Quick Start Guide - Agentic Trip Planner Frontend

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```powershell
cd frontend
npm install
```

### Step 2: Start the Development Server
```powershell
npm start
```

### Step 3: Open Your Browser
Navigate to: **http://localhost:4200**

---

## ✅ What You Should See

A beautiful trip planning interface with:
- 🌍 Destination input field
- 📅 Start date picker
- 📅 End date picker
- 💰 Optional budget field
- ✈️ "Plan My Trip" button

---

## 🔗 Backend Connection

The frontend expects a FastAPI backend running at:
```
http://localhost:8000
```

**Important**: Make sure your backend is running before testing the full functionality!

---

## 📝 How to Use

1. **Enter Destination**: Type any city or country (e.g., "Paris", "Tokyo")
2. **Select Dates**: Choose your trip start and end dates
3. **Add Budget** (optional): Enter your budget in USD
4. **Click "Plan My Trip"**: The app will send the request to your backend
5. **View Results**: The AI-generated trip plan will appear on the right

---

## ⚠️ Troubleshooting

### "Cannot find module '@angular/core'"
This is expected before running `npm install`. The error will disappear after installing dependencies.

### CORS Error
Add this to your FastAPI backend:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Port 4200 Already in Use
Run on a different port:
```powershell
ng serve --port 4300
```

---

## 📦 Next Steps

1. ✅ Frontend Complete
2. ⏳ Build Backend (Python FastAPI)
3. ⏳ Implement LLM Orchestration (Microsoft Autogen)

---

**You're ready to go! 🎉**
