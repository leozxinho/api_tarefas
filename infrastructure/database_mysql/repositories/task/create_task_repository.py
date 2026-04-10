from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.dto.response.task_response import TaskResponse
from app.entities.models.task_model import TaskModel



class CreateTaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session 
        
    async def criar_tarefa(self, tarefa_model: TaskResponse):
        new = TaskModel(
            titulo=tarefa_model.titulo,
            descricao=tarefa_model.descricao,
        )
        self.session.add(new)
        await self.session.commit()
        await self.session.refresh(new)
        return new