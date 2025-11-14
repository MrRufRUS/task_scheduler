import datetime
from sqlalchemy import DateTime, Integer, Float, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, autoincrement=True
    )

    create_time: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    start_time: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    time_to_execute: Mapped[float] = mapped_column(Float, nullable=True)

    model_config = {"from_attributes": True}
