import httpx
from typing import List
from models.flight import Flight

OPENSKY_URL = "https://opensky-network.org/api/states/all"

async def get_flights() -> List[Flight]:
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(OPENSKY_URL)
        response.raise_for_status()
        data = response.json()

    flights = []
    for state in data["states"]:
        flight = Flight(
            icao24=state[0],
            callsign=state[1],
            origin_country=state[2],
            longitude=state[5],
            latitude=state[6],
            altitude=state[7],
            velocity=state[9],
            heading=state[10]
        )
        flights.append(flight)

    return flights