from app.entities.dto.request.task_request import FilterTaskData


class FilterTaskDataUsecase:
    def __init__(self, repository):
        self.repository = repository
    
    async def execute(self, filtro: FilterTaskData):
        return await self.repository.filtro_tarefa_data(filtro)