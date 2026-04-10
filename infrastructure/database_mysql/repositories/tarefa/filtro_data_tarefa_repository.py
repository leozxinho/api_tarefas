from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.dto.request.tarefa_request import FiltroTarefaData
from app.entities.models.tarefa_model import TarefaModel

class FiltroTarefaDataRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def filtro_tarefa_data(self, filtro: FiltroTarefaData):
        query = select(TarefaModel)
        
        i = {
            "data_inicio": (TarefaModel.data_tarefa, ">="),
            "data_fim": (TarefaModel.data_tarefa, "<="),
        }
        for j, (coluna, operador) in i.items():
            z = getattr(filtro, j)
            
            if z:
                if operador == ">=":
                    query = query.where(coluna >= z)
                elif operador == "<=":
                    query = query.where(coluna <= z)
        
        result = await self.session.execute(query)
        return result.scalars().all()