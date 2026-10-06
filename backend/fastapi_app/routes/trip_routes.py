
from fastapi import APIRouter, HTTPException
from fastapi_app.models.trip_request import TripRequest
from fastapi_app.models.trip_response import TripResponse
from autogen_app.teams.travel_team import travel_team_service

router = APIRouter(prefix="/trips", tags=["trips"])

@router.post("/plan", response_model=TripResponse)
async def plan_trip(request: TripRequest):
    if not request.destination:
        raise HTTPException(status_code=400, detail="Destination is required.")
    # Pass all parameters as a dict to the team service
    itinerary = await travel_team_service.plan_trip(request.dict())
    return TripResponse(
        destination=request.destination,
        start_date=request.start_date,
        end_date=request.end_date,
        itinerary=itinerary
    )
