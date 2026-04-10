from app.entities.dto.request.tarefa_request import FiltroTarefaData


class FiltroTarefaDataUsecase:
    def __init__(self, repository):
        self.repository = repository
    
    async def execute(self, filtro: FiltroTarefaData):
        return await self.repository.filtro_tarefa_data(filtro)