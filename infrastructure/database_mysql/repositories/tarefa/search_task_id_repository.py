from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.task_model import TaskModel

class SearchTaskIDRepository:
    def __init__(self, session: AsyncSession):
        self.session = session 
        
    async def buscar_por_id(self, id: int):
        result = await self.session.execute(
            select(TaskModel).filter_by(id=id)
        )
        return result.scalar_one_or_none()