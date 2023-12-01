from fastapi import APIRouter
from sqlmodel import Session, select
from sensor.models import *
from database import engine


router = APIRouter()


@router.post("/sensor/add")
def create_sensor(new_sensor: SensorCreate, response_model=Sensor):
    with Session(engine) as session:
        db_sensor = Sensor.from_orm(new_sensor)
        session.add(db_sensor)
        session.commit()
        session.refresh(db_sensor)
        return db_sensor


@router.get("/sensor/list", response_)
def get_all_sensors():
    with Session(engine) as session:
        sensors = session.exec(select(Sensor)).all()
        return sensors
