from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.task_model import TaskModel

class DeleteTaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def deletar_tarefa(self, tarefa: int):
            stmt = (
                delete(TaskModel)
                .where(TaskModel.id == tarefa)
            )
            await self.session.execute(stmt)
            await self.session.commit()
            
            return True