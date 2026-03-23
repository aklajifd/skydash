from pydantic import BaseModel
from typing import Optional

class Flight(BaseModel):
    icao24: str
    callsign: Optional[str] = None
    origin_country: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    altitude: Optional[float]= None
    velocity: Optional[float] = None
    heading: Optional[float] = None