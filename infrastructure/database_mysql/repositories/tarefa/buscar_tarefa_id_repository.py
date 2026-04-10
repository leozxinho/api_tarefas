from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.models.tarefa_model import TarefaModel

class BuscarTarefaIDRepository:
    def __init__(self, session: AsyncSession):
        self.session = session 
        
    async def buscar_por_id(self, id: int):
        result = await self.session.execute(
            select(TarefaModel).filter_by(id=id)
        )
        return result.scalar_one_or_none()