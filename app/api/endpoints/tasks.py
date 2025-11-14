from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.crud.tasks import create_task, get_task_schema
from app.api.schemas.tasks import TaskCreated, TaskSchema
from app.db.database import get_async_session

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskCreated)
async def create_task_endpoint(db: AsyncSession = Depends(get_async_session)):
    return await create_task(db)


@router.get("/{task_id}", response_model=TaskSchema)
async def get_task_endpoint(
    task_id: int, db: AsyncSession = Depends(get_async_session)
):
    task = await get_task_schema(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
