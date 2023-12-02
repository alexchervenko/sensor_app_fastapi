from sqlmodel import Field, SQLModel
from typing import Optional


class Sensor(SQLModel, table=True):
    __tablename__ = "sensors"
    id: int | None = Field(primary_key=True)
    name: str = Field(unique=True)


class SensorCreate(SQLModel):
    name: str
