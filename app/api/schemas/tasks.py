from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    status: Optional[str] = Field(None)


class TaskCreate(BaseModel):
    pass


class TaskCreated(BaseModel):
    id: int


class TaskSchema(TaskBase):
    id: int
    create_time: datetime
    start_time: Optional[datetime]
    time_to_execute: Optional[float]

    class Config:
        from_attributes = True
