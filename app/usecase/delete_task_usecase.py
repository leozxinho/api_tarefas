

from app.entities.dto.request.task_request import Task
from infrastructure.database_mysql.repositories.tarefa.delete_task_repository import DeleteTaskRepository


class DeleteTaskUsecase:
    def __init__(self, repository: DeleteTaskRepository):
        self.repository = repository
        
        
    async def execute(self, id: int):
        return await self.repository.deletar_tarefa(id) 