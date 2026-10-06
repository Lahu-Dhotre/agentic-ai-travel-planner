from pydantic import BaseModel, Field
from typing import Optional

class TripRequest(BaseModel):
    destination: str = Field(..., example="Paris")
    start_date: str = Field(..., example="2025-12-01")
    end_date: str = Field(..., example="2025-12-10")
    travelers: Optional[int] = Field(1, example=2)
    preferences: Optional[str] = Field(None, example="sightseeing, food")
