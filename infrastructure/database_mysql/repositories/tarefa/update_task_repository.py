from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.task_model import TaskModel


class UpdateTaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def atualizar_tarefa(self, id: int, tarefa: TaskModel):
        stmt = (
            update(TaskModel)
            .where(TaskModel.id == id)
            .values(
                titulo=tarefa.titulo,
                descricao=tarefa.descricao,
                concluido=tarefa.concluido,
            )
        )
        await self.session.execute(stmt)
        await self.session.commit()
        
        result = await self.session.execute(select(TaskModel).where(TaskModel.id == id))
        return result.scalar_one_or_none()