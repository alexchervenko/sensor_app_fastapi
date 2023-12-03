from fastapi import FastAPI
from sensor.routers import router as sensor_router
from database import engine, SQLModel


app = FastAPI()

app.include_router(sensor_router)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
