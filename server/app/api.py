from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import models, employee
from app.database import engine

models.Base.metadata.create_all(bind=engine)  # Create all tables stored in the metadat

app = FastAPI()

origins = [
    "*",  # needed to call by front-end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(employee.router, tags=['employees'], prefix='/api')
