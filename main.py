from fastapi import FastAPI

from api.dates.router import router as dates_router

app = FastAPI()

app.include_router(dates_router)
