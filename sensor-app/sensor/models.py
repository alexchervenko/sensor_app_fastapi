from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime


class Sensor(SQLModel, table=True):
    __tablename__ = "sensors"
    id: int | None = Field(primary_key=True)
    name: str = Field(unique=True)


class SensorCreate(SQLModel):
    name: str


class Measure(SQLModel, table=True):
    __tablename__ = "measures"
    id: int | None = Field(primary_key=True)
    data: str = Field(min_length=3, max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    sensor_id: int | None = Field(nullable=False, foreign_key="sensors.id")


class MeasureCreate(SQLModel):
    data: str
    sensor_id: int
