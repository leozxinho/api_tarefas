from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.tarefa_model import TarefaModel

class ListarTarefaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def listar_tarefas_all(self):
        result = await self.session.execute(select(TarefaModel))
        return result.scalars().all()