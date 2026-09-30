from sqlalchemy import select

from database import new_session
from schemas import STask, STaskAdd
from database import TasksOrm

class TaskRepository():
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            
            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            task_id = task.id
            await session.commit()
            return task_id
            
    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate() for task_orm in task_models]
            return task_models