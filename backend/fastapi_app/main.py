from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_app.routes import trip_routes


app = FastAPI(title="Agentic AI Trip Planner API", version="1.0.0")

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include trip planning routes
app.include_router(trip_routes.router)

@app.get("/")
def root():
    return {"message": "Agentic AI Trip Planner Backend is running."}
