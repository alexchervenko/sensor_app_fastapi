from pydantic import BaseModel
from typing import List


class SensorBaseSchema(BaseModel):
    id: str | None = None
    title: str

    # class Config:
    #     from_attributes = False
    #     populate_by_name = True
    #     arbitrary_types_allowed = True


class ListSensorResponse(BaseModel):
    status: str
    results: int
    sensors: List[SensorBaseSchema]
