from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.task_model import TaskModel

class ListTaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def listar_tarefas_all(self):
        result = await self.session.execute(select(TaskModel))
        return result.scalars().all()