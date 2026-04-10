from app.entities.dto.request.task_request import Task
from infrastructure.database_mysql.repositories.task.update_task_repository import UpdateTaskRepository


class UpdateTaskUsecase:
    def __init__(self, repository: UpdateTaskRepository):
        self.repository = repository
        
    async def execute(self, id: int, tarefa_data: Task):
        return await self.repository.atualizar_tarefa(id, tarefa_data) 