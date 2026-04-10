from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.dto.response.tarefas_response import TarefasResponse
from app.entities.models.tarefa_model import TarefaModel



class CriarTarefaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session 
        
    async def criar_tarefa(self, tarefa_model: TarefasResponse):
        new = TarefaModel(
            titulo=tarefa_model.titulo,
            descricao=tarefa_model.descricao,
        )
        self.session.add(new)
        await self.session.commit()
        await self.session.refresh(new)
        return new