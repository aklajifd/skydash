from fastapi import APIRouter, HTTPException
from typing import List
from models.flight import Flight
from services.opensky import get_flights

router = APIRouter(
    prefix="/flights",
    tags=["flights"]
)

@router.get("/", response_model=List[Flight])
async def read_flights():
    try:
        flights = await get_flights()
        return flights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))