from fastapi import HTTPException

from infrastructure.database_mysql.repositories.tarefa.buscar_tarefa_id_repository import BuscarTarefaIDRepository


class BuscarTarefaIDUsecase:
    def __init__(self, repository: BuscarTarefaIDRepository):
        self.repository = repository
        
    async def execute(self, id: int):
        tarefa = await self.repository.buscar_por_id(id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa