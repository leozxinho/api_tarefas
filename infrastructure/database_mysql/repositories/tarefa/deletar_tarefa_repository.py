from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.tarefa_model import TarefaModel

class DeletarTarefaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def deletar_tarefa(self, tarefa: int):
            stmt = (
                delete(TarefaModel)
                .where(TarefaModel.id == tarefa)
            )
            await self.session.execute(stmt)
            await self.session.commit()
            
            return True