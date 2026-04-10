

from app.entities.dto.request.tarefa_request import Tarefa
from infrastructure.database_mysql.repositories.tarefa.deletar_tarefa_repository import DeletarTarefaRepository


class DeletarTarefaUsecase:
    def __init__(self, repository: DeletarTarefaRepository):
        self.repository = repository
        
        
    async def execute(self, id: int):
        return await self.repository.deletar_tarefa(id) 