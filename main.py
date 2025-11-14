import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api.endpoints.tasks import router as tasks_router
from worker.worker import start_workers


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(start_workers())
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
