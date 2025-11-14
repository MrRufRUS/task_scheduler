from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    id: int
    status: Optional[str] = Field(None)


class TaskCreate(BaseModel):
    pass


class TaskCreated(BaseModel):
    id: int


class TaskSchema(TaskBase):
    create_time: datetime
    start_time: Optional[datetime]
    time_to_execute: Optional[float]

    class Config:
        from_attributes = True
