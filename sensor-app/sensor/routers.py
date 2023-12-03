from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select, update
from sensor.models import *
from database import engine
from typing import List


router = APIRouter()


@router.post("/measure/add")
def send_measure(new_measure: MeasureCreate):
    with Session(engine) as session:
        db_measure = Measure.from_orm(new_measure)
        session.add(db_measure)
        session.commit()
        session.refresh(db_measure)
        return db_measure


@router.post("/sensor/add")
def create_sensor(new_sensor: SensorCreate):
    with Session(engine) as session:
        exists = session.exec(
            select(Sensor).where(Sensor.name == new_sensor.name)
        ).one_or_none()
        if exists is not None:
            raise HTTPException(
                status_code=400, detail="Sensor with this name already exist"
            )
        db_sensor = Sensor.from_orm(new_sensor)
        session.add(db_sensor)
        session.commit()
        session.refresh(db_sensor)
        return db_sensor


# @router.post("/sensor/update/{sensor_id}") # ToDo: Update operation


@router.post("/sensor/delete/{sensor_id}")
def delete_sensor_by_id(sensor_id: int):
    with Session(engine) as session:
        sensor = session.query(Sensor).get(sensor_id)
        if sensor is None:
            raise HTTPException(status_code=400, detail="No sensor with this id")
        session.delete(sensor)
        session.commit()
        return {"result": "Sensor deleted"}


@router.get("/sensor/list", response_model=List[Sensor])
def get_all_sensors():
    with Session(engine) as session:
        sensors = session.exec(select(Sensor)).all()
        return sensors


@router.get("/sensor/{sensor_id}")
def get_sensor_by_id(sensor_id: int):
    with Session(engine) as session:
        sensor = session.query(Sensor).get(sensor_id)
        if sensor is None:
            raise HTTPException(status_code=400, detail="No sensor with this id")
        return sensor
