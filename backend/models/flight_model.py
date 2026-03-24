from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.sql import func
from database import Base

class FlightModel(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    icao24 = Column(String, index=True)
    callsign = Column(String, nullable=True)
    origin_country = Column(String)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    altitude = Column(Float, nullable=True)
    velocity = Column(Float, nullable=True)
    heading = Column(Float, nullable=True)
    recorded_at = Column(DateTime, server_default=func.now())


