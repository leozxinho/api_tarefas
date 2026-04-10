from app.entities.dto.response.tarefas_response import TarefasResponse
from infrastructure.database_mysql.repositories.tarefa.criar_tarefa_repository import CriarTarefaRepository


class CriarTarefaUsecase:
    def __init__(self, repository: CriarTarefaRepository):
        self.repository = repository
        
    async def execute(self, tarefa_model: TarefasResponse):
        return await self.repository.criar_tarefa(tarefa_model)