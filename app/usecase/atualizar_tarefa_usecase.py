from app.entities.dto.request.tarefa_request import Tarefa
from infrastructure.database_mysql.repositories.tarefa.atualizar_tarefa_repository import AtualizarTarefaRepository


class AtualizarTarefaUsecase:
    def __init__(self, repository: AtualizarTarefaRepository):
        self.repository = repository
        
    async def execute(self, id: int, tarefa_data: Tarefa):
        return await self.repository.atualizar_tarefa(id, tarefa_data) 