from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from router import router as tasks_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")
    
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)






if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)