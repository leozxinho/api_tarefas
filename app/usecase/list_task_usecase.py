from infrastructure.database_mysql.repositories.task.list_task_repository import ListTaskRepository

class ListTaskUsecase:
    def __init__(self, repository: ListTaskRepository):
        self.repository = repository

    async def execute(self):
        return await self.repository.listar_tarefas_all()