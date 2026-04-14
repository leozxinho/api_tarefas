# app/usecase/task_usecase.py
from fastapi import HTTPException
from app.entities.dto.request.task_request import Task, FilterTaskData
from app.entities.dto.response.task_response import TaskResponse
from app.interface.i_task import ITaskRepository


class CreateTaskUsecase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository
        
    async def execute(self, tarefa_model: TaskResponse):
        return await self.repository.create(tarefa_model)


class DeleteTaskUsecase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository
        
    async def execute(self, id: int):
        return await self.repository.delete(id)


class SearchTaskIDUsecase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository
        
    async def execute(self, id: int):
        tarefa = await self.repository.search_by_id(id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa


class UpdateTaskUsecase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository
        
    async def execute(self, id: int, tarefa_data: Task):
        return await self.repository.update(id, tarefa_data)


class ListTaskUsecase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    async def execute(self):
        return await self.repository.list()


class FilterTaskDataUsecase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository
    
    async def execute(self, filtro: FilterTaskData):
        return await self.repository.filter_task(filtro)