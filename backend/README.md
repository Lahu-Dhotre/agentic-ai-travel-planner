# Agentic AI Travel Planner Backend

## Overview
This backend is a FastAPI application that orchestrates a team of AI agents to generate travel plans based on user input. It integrates with OpenAI models and supports modular agent composition.

## Setup Instructions

1. **Clone the repository**
2. **Create and activate a Python environment**
   - Recommended: Anaconda/Miniconda
   - Example: `conda create -n agenticai3_12 python=3.12` and `conda activate agenticai3_12`
3. **Install dependencies**
   - `pip install -r requirements.txt`
4. **Configure your OpenAI API key**
   - Place your API key in `backend/autogen_app/config/.env` as:
     ```
     OPENAI_API_KEY=sk-...your_key_here...
     ```
5. **Run the backend**
   - From the `backend` directory:
     ```
     uvicorn fastapi_app.main:app --reload --host 0.0.0.0 --port 8000
     ```

## API
- `POST /trips/plan` — Accepts a JSON body with trip details and returns an itinerary as a list of strings.

## Notes
- The backend uses a team of agents (planner, local, summary) to generate plans.
- The initial user prompt is constructed from the request and should be injected into the agent team according to your agent framework's requirements.
- If you see repeated requests for user input from the agents, ensure the prompt is being passed correctly to the team.

## Troubleshooting
- **401 Authentication Error:** Ensure your OpenAI API key is set and loaded from `.env`.
- **CORS Issues:** CORS middleware is enabled for frontend-backend communication.
- **Agent Output Issues:** If agents only ask for input, check how the initial prompt is injected into the team.
