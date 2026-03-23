from fastapi import FastAPI
from routers import flights

app = FastAPI(
    title="SkyDash API",
    description="Aviation data explorer API",
    version="0.1.0"
)

app.include_router(flights.router)

@app.get("/")
def read_root():
    return {"message": "SkyDash API is running"}