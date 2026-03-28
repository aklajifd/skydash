from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import flights

app = FastAPI(
    title="SkyDash API",
    description="Aviation data explorer API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flights.router)

@app.get("/")
def read_root():
    return {"message": "SkyDash API is running"}