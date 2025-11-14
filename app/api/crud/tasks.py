from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from typing import Optional
from datetime import datetime, UTC

from app.api.schemas.tasks import TaskCreated, TaskSchema
from app.db.models import Task


def compute_status(task: Task) -> str:
    if task.start_time is None:
        return "In Queue"
    elif task.time_to_execute is None:
        return "Run"
    else:
        return "Completed"


async def create_task(db: AsyncSession) -> TaskCreated:
    task = Task()
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return TaskCreated(id=task.id)


async def get_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()


async def get_task_schema(db: AsyncSession, task_id: int) -> Optional[TaskSchema]:
    task = await get_task(db, task_id)
    if task is None:
        return None
    task_schema = TaskSchema.model_validate(task)
    task_schema.status = compute_status(task)
    return task_schema


async def set_task_started(db: AsyncSession, task_id: int) -> None:
    await db.execute(
        update(Task).where(Task.id == task_id).values(start_time=datetime.now(UTC))
    )
    await db.commit()


async def set_task_completed(
    db: AsyncSession, task_id: int, exec_seconds: float
) -> None:
    await db.execute(
        update(Task).where(Task.id == task_id).values(time_to_execute=exec_seconds)
    )
    await db.commit()
