from fastapi import HTTPException

from infrastructure.database_mysql.repositories.tarefa.search_task_id_repository import SearchTaskIDRepository


class SearchTaskIDUsecase:
    def __init__(self, repository: SearchTaskIDRepository):
        self.repository = repository
        
    async def execute(self, id: int):
        tarefa = await self.repository.buscar_por_id(id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa