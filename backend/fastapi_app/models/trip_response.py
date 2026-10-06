from pydantic import BaseModel, Field
from typing import List

class TripResponse(BaseModel):
    destination: str = Field(..., example="Paris")
    start_date: str = Field(..., example="2025-12-01")
    end_date: str = Field(..., example="2025-12-10")
    itinerary: List[str] = Field(..., example=["Day 1: Arrive at Paris", "Day 2: Explore city"])
