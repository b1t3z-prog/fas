from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI
from pydantic import BaseModel

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=True)

class Model(DeclarativeBase):
    pass

class TasksOrm(Model):
    __tablename__ = "Tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
    
async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)