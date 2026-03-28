from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import flights

app = FastAPI(
    title="SkyDash API",
    description="Aviation data explorer API",
    version="0.2.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://skydash-frontend-daniel.s3-website-us-east-1.amazonaws.com",
        "https://d3r43tijueh8sn.cloudfront.net",
        "https://d2hoe9vnfb9per.cloudfront.net"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flights.router)

@app.get("/")
def read_root():
    return {"message": "SkyDash API is running"}