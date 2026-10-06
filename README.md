# 🌍 Agentic Trip Planner - Full Stack Application

A modern full-stack application that uses AI agents to collaboratively plan detailed travel itineraries.

---

## 📊 Project Status

| Component | Status | Progress |
|-----------|--------|----------|
| **Frontend (Angular)** | ✅ Complete | 100% |
| **Backend (FastAPI)** | ⏳ Pending | 0% |
| **LLM Orchestration (Autogen)** | ⏳ Pending | 0% |

---

## 🏗️ Architecture Overview

```
┌─────────────────┐      HTTP/JSON      ┌──────────────────┐      Agent      ┌─────────────────┐
│                 │   POST /plan-trip   │                  │  Orchestration  │                 │
│  Angular SPA    │ ─────────────────> │  FastAPI Backend │ ─────────────> │ Autogen Agents  │
│  (Port 4200)    │                     │  (Port 8000)     │                 │  (Multi-Agent)  │
│                 │ <───────────────── │                  │ <───────────── │                 │
└─────────────────┘   { plan: "..." }   └──────────────────┘    Trip Plan    └─────────────────┘
```

---

## 🎯 How It Works

1. **User Input**: User enters trip details in Angular form
   - Destination
   - Start date
   - End date
   - Budget (optional)

2. **Frontend Validation**: Angular validates input
   - Required fields
   - Date range validation
   - Budget constraints

3. **API Request**: Angular sends POST to FastAPI
   ```json
   {
     "destination": "Paris",
     "start_date": "2025-06-01",
     "end_date": "2025-06-07",
     "budget": 3000
   }
   ```

4. **Backend Processing**: FastAPI receives and validates
   - Pydantic model validation
   - Data sanitization

5. **Agent Orchestration**: Autogen agents collaborate
   - Research agent: Gathers destination info
   - Planning agent: Creates itinerary
   - Budget agent: Optimizes costs
   - Review agent: Finalizes plan

6. **Response**: Backend returns detailed plan
   ```json
   {
     "plan": "Detailed multi-day travel itinerary..."
   }
   ```

7. **Display**: Angular shows formatted plan to user

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: Angular 17
- **Language**: TypeScript 5.2
- **Forms**: Reactive Forms with validation
- **HTTP**: HttpClient with RxJS
- **Styling**: CSS3 with animations
- **Build**: Angular CLI

### Backend (Planned)
- **Framework**: Python FastAPI
- **Validation**: Pydantic models
- **CORS**: Enabled for localhost:4200
- **API**: RESTful JSON API

### LLM Orchestration (Planned)
- **Framework**: Microsoft Autogen
- **Pattern**: Multi-agent collaboration
- **Agents**: AssistantAgents with specific roles
- **LLM**: OpenAI GPT (configurable)

---

## 📁 Project Structure

```
agentic_ai_travel_planner_full_stack/
├── frontend/              ✅ COMPLETE
│   ├── src/
│   │   ├── app/
│   │   │   ├── models/
│   │   │   ├── services/
│   │   │   └── trip-planner/
│   │   ├── environments/
│   │   └── ...
│   ├── package.json
│   ├── angular.json
│   └── README.md
│
├── backend/               ⏳ TO DO
│   ├── agents/
│   ├── api/
│   ├── config/
│   ├── models/
│   ├── teams/
│   ├── test/
│   └── utils/
│
└── README.md             (This file)
```

---

## 🚀 Quick Start

### Frontend (Ready Now!)

```powershell
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm start

# Open browser to http://localhost:4200
```

### Backend (Coming Soon!)
```powershell
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn main:app --reload

# API will be at http://localhost:8000
```

---

## ✨ Features

### Current (Frontend)
- ✅ Beautiful, responsive UI
- ✅ Form validation with error messages
- ✅ Loading states and animations
- ✅ Error handling
- ✅ Type-safe TypeScript models
- ✅ HTTP service for API calls
- ✅ Production-ready build system

### Planned (Backend)
- ⏳ FastAPI REST API
- ⏳ Pydantic data validation
- ⏳ CORS configuration
- ⏳ Error handling middleware
- ⏳ Logging and monitoring

### Planned (LLM Orchestration)
- ⏳ Multi-agent system
- ⏳ Collaborative trip planning
- ⏳ Budget optimization
- ⏳ Personalized recommendations
- ⏳ Real-time progress updates

---

## 🎨 UI Preview

The Angular frontend features:
- **Gradient Purple Theme**: Modern and professional
- **Two-Column Layout**: Form on left, results on right
- **Smooth Animations**: Fade, slide, and spin effects
- **Responsive Design**: Works on all screen sizes
- **Custom Scrollbar**: Matches theme colors
- **Error States**: Clear, helpful validation messages

---

## 📝 API Documentation

### POST /plan-trip

**Request**:
```json
{
  "destination": "string",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "budget": number | null
}
```

**Response**:
```json
{
  "plan": "string"
}
```

**Error Response**:
```json
{
  "detail": "Error message"
}
```

---

## 🔧 Configuration

### Frontend
- **API URL**: `http://localhost:8000` (configurable in `environment.ts`)
- **Dev Port**: 4200 (configurable with `ng serve --port`)

### Backend (Planned)
- **API Port**: 8000 (configurable)
- **CORS Origins**: localhost:4200 (configurable)
- **Autogen Config**: LLM settings, agent roles

---

## 📚 Documentation

Each component has detailed documentation:

- **Frontend**:
  - `/frontend/README.md` - Comprehensive guide
  - `/frontend/QUICKSTART.md` - Quick start guide
  - `/frontend/FRONTEND_SUMMARY.md` - Complete summary

- **Backend** (Coming):
  - `/backend/README.md` - Setup and API docs
  - `/backend/API.md` - API reference

---

## 🧪 Testing

### Frontend
```powershell
cd frontend
npm test
```

### Backend (Planned)
```powershell
cd backend
pytest
```

---

## 🛣️ Development Roadmap

### Phase 1: Frontend ✅ COMPLETE
- [x] Angular project setup
- [x] TypeScript models
- [x] HTTP service
- [x] Trip planner component
- [x] Form validation
- [x] UI/UX design
- [x] Error handling
- [x] Documentation

### Phase 2: Backend ⏳ NEXT
- [ ] FastAPI setup
- [ ] Pydantic models
- [ ] /plan-trip endpoint
- [ ] CORS configuration
- [ ] Error handling
- [ ] Testing

### Phase 3: LLM Orchestration ⏳ PENDING
- [ ] Autogen setup
- [ ] Agent definitions
- [ ] Multi-agent collaboration
- [ ] Trip planning logic
- [ ] Integration with backend

### Phase 4: Integration ⏳ PENDING
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Documentation
- [ ] Deployment preparation

---

## 🤝 Contributing

This is a complete full-stack AI application showcasing:
- Modern frontend development with Angular
- RESTful API design with FastAPI
- Multi-agent AI orchestration with Autogen

---

## 📄 License

This project is for educational and demonstration purposes.

---

## 🎯 Next Steps

**Frontend is complete and ready!** 🎉

When you're ready for the backend:
1. Let me know, and I'll create the FastAPI backend
2. Implement Pydantic models
3. Set up the /plan-trip endpoint
4. Configure CORS
5. Prepare for Autogen integration

When you're ready for LLM orchestration:
1. Set up Microsoft Autogen
2. Define AssistantAgents
3. Implement collaborative planning
4. Integrate with FastAPI

---

**Ready to continue? Just say the word! 🚀**
