import httpx
import os
from typing import List
from models.flight import Flight

AVIATIONSTACK_URL = "http://api.aviationstack.com/v1/flights"
AVIATIONSTACK_KEY = os.environ.get("AVIATIONSTACK_KEY", "")

async def get_flights() -> List[Flight]:
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            AVIATIONSTACK_URL,
            params={
                "access_key": AVIATIONSTACK_KEY,
                "limit": 100,
                "flight_status": "active"
            }
        )
        response.raise_for_status()
        data = response.json()

    flights = []
    for item in data.get("data", []):
        flight = Flight(
            icao24=item.get("flight", {}).get("icao") or item.get("flight", {}).get("iata") or "unknown",
            callsign=item.get("flight", {}).get("iata"),
            origin_country=item.get("airline", {}).get("name") or "Unknown",
            longitude=item.get("live", {}).get("longitude") if item.get("live") else None,
            latitude=item.get("live", {}).get("latitude") if item.get("live") else None,
            altitude=item.get("live", {}).get("altitude") if item.get("live") else None,
            velocity=item.get("live", {}).get("speed_horizontal") if item.get("live") else None,
            heading=item.get("live", {}).get("direction") if item.get("live") else None
        )
        flights.append(flight)

    return flights