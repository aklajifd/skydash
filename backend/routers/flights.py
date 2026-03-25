from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from models.flight import Flight
from models.flight_model import FlightModel
from services.opensky import get_flights
from database import get_db

router = APIRouter(
    prefix="/flights",
    tags=["flights"]
)

@router.get("/", response_model=List[Flight])
async def read_flights(db: Session = Depends(get_db)):
    try:
        flights = await get_flights()
        for flight in flights:
            db_flight = FlightModel(
                icao24=flight.icao24,
                callsign=flight.callsign,
                origin_country=flight.origin_country,
                longitude=flight.longitude,
                latitude=flight.latitude,
                altitude=flight.altitude,
                velocity=flight.velocity,
                heading=flight.heading
            )
            db.add(db_flight)
        db.commit()
        return flights
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/history", response_model=List[Flight])
def read_flight_history(db: Session = Depends(get_db)):
    flights = db.query(FlightModel).order_by(
        FlightModel.recorded_at.desc()
    ).limit(100).all()
    return flights