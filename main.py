from fastapi import FastAPI

from students.controllers import router
from students.database import create_tables, start_mappers

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
def startup_event():
    start_mappers()
    create_tables()
