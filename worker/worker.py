import asyncio
import random
import time
from concurrent.futures.thread import ThreadPoolExecutor

from sqlalchemy import select

from app.api.crud.tasks import set_task_started, set_task_completed
from app.db.database import async_session_maker
from app.db.models import Task

task_queue: asyncio.Queue[int] = asyncio.Queue()

MAX_WORKERS = 2
semaphore = asyncio.Semaphore(MAX_WORKERS)

executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)


def execute_task() -> float:
    start = time.perf_counter()
    time.sleep(random.randint(1, 10))
    end = time.perf_counter()
    return round(end - start, 2)


async def worker(name: str):
    while True:
        task_id = await task_queue.get()
        async with semaphore:
            async with async_session_maker() as db:
                await set_task_started(db, task_id)

                loop = asyncio.get_running_loop()
                exec_time = await loop.run_in_executor(executor, execute_task)

                await set_task_completed(db, task_id, exec_time)

        task_queue.task_done()

async def enqueue_pending_tasks():
    async with async_session_maker() as db:
        result = await db.execute(
            select(Task.id).where(Task.time_to_execute.is_(None))
        )
        task_ids = result.scalars().all()
        for task_id in task_ids:
            await task_queue.put(task_id)

async def start_workers(num_workers: int = MAX_WORKERS):

    await enqueue_pending_tasks()

    workers = []
    for i in range(num_workers):
        workers.append(asyncio.create_task(worker(f"worker id: {i + 1}")))
    await asyncio.gather(*workers)
