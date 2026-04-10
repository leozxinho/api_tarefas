from infrastructure.database_mysql.repositories.tarefa.listar_tarefa_repository import ListarTarefaRepository

class ListarTarefaUsecase:
    def __init__(self, repository: ListarTarefaRepository):
        self.repository = repository

    async def execute(self):
        return await self.repository.listar_tarefas_all()