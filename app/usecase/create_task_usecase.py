from app.entities.dto.response.task_response import TaskResponse
from infrastructure.database_mysql.repositories.task.create_task_repository import CreateTaskRepository


class CreateTaskUsecase:
    def __init__(self, repository: CreateTaskRepository):
        self.repository = repository
        
    async def execute(self, tarefa_model: TaskResponse):
        return await self.repository.criar_tarefa(tarefa_model)