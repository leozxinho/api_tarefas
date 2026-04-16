from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from application.dependencies import get_repository, get_session
from domain.entities.dto.response.task_response import TaskCreate, TaskResponse
from domain.entities.dto.request.task_request import FilterTaskData, TaskUpdate
from application.usecase.task_usecase import CreateTaskUsecase, DeleteTaskUsecase, FilterTaskDataUsecase, ListTaskUsecase, SearchTaskIDUsecase, UpdateTaskUsecase




with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

router = APIRouter(
    tags=["Tarefas"],
    prefix="/api/v1",
)


# Listar todas as tarefas
@router.get("/tarefas", response_model=List[TaskResponse])
async def list_task(session: AsyncSession = Depends(get_session)):
   repository = get_repository(session)
   usecase = ListTaskUsecase(repository)
   tarefa = await usecase.execute()
   return tarefa

#Buscar tarefas por data
@router.get("/tarefas/data", response_model=List[TaskResponse])
async def filter_task(filtro: FilterTaskData = Depends(), session: AsyncSession = Depends(get_session)):
    repository = get_repository(session)
    usecase = FilterTaskDataUsecase(repository)
    tarefa = await usecase.execute(filtro)
    return tarefa


# Buscar tarefa por ID
@router.get("/tarefas/{id}", response_model=TaskResponse)
async def search_by_id(id: int, session: AsyncSession = Depends(get_session)):
    repository = get_repository(session)
    usecase = SearchTaskIDUsecase(repository)
    tarefa = await usecase.execute(id)
    return tarefa
    
    
# Criar uma nova tarefa
@router.post("/tarefas", response_model=TaskResponse)
async def create(tarefa_model: TaskCreate, session: AsyncSession = Depends(get_session)):
    repository = get_repository(session)
    usecase = CreateTaskUsecase(repository)
    tarefa = await usecase.execute(tarefa_model)
    return tarefa
                                       
                                       
# Atualizar uma tarefa existente
@router.put("/tarefas/{id}", response_model=TaskResponse)
async def update(id: int, tarefa_data: TaskUpdate, session: AsyncSession = Depends(get_session)):
    repository = get_repository(session)
    usecase = UpdateTaskUsecase(repository) 
    tarefa = await usecase.execute(id, tarefa_data)
    return tarefa
  

# Excluir uma tarefa
@router.delete("/tarefas/{id}", status_code=200)
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    repository = get_repository(session)
    usecase = DeleteTaskUsecase(repository)
    await usecase.execute(id)
    return {"detail": "Tarefa excluída com sucesso."}