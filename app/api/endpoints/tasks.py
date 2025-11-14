from fastapi import APIRouter

tasks_router = APIRouter(prefix='/tasks', tags=['Tasks'])

@tasks_router.get('/{task_id}')
async def get_task(task_id: int):
    pass

@tasks_router.post('/')
async def create_task():
    pass