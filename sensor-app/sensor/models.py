from sqlmodel import Field, SQLModel
from typing import Optional


class Sensor(SQLModel, table=True):
    __tablename__ = "sensors"
    id: int | None = Field(primary_key=True)
    name: str


class SensorCreate(SQLModel):
    name: str
