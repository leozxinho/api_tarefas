from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.entities.dto.response.task_response import TaskCreate, TaskResponse
from app.entities.dto.request.task_request import FilterTaskData, TaskUpdate
from app.usecase.task_usecase import CreateTaskUsecase, DeleteTaskUsecase, FilterTaskDataUsecase, ListTaskUsecase, SearchTaskIDUsecase, UpdateTaskUsecase
from infrastructure.database_mysql.mysql_connection import get_session

from infrastructure.database_mysql.repositories.task.task_repository  import TaskRepository




with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

router = APIRouter(
    tags=["Tarefas"],
    prefix="/api/v1",
)


# Listar todas as tarefas
@router.get("/tarefas", response_model=List[TaskResponse])
async def listar_tarefas(session: AsyncSession = Depends(get_session)):
   repository = TaskRepository(session)
   usecase = ListTaskUsecase(repository)
   tarefa = await usecase.execute()
   return tarefa

#Buscar tarefas por data
@router.get("/tarefas/data", response_model=List[TaskResponse])
async def filtrar_tarefa_data(filtro: FilterTaskData = Depends(), session: AsyncSession = Depends(get_session)):
    repository = TaskRepository(session)
    usecase = FilterTaskDataUsecase(repository)
    tarefa = await usecase.execute(filtro)
    return tarefa


# Buscar tarefa por ID
@router.get("/tarefas/{id}", response_model=TaskResponse)
async def buscar_tarefa_id(id: int, session: AsyncSession = Depends(get_session)):
    repository = TaskRepository(session)
    usecase = SearchTaskIDUsecase(repository)
    tarefa = await usecase.execute(id)
    return tarefa
    
    
# Criar uma nova tarefa
@router.post("/tarefas", response_model=TaskResponse)
async def criar_tarefa(tarefa_model: TaskCreate, session: AsyncSession = Depends(get_session)):
    repository = TaskRepository(session)
    usecase = CreateTaskUsecase(repository)
    tarefa = await usecase.execute(tarefa_model)
    return tarefa
                                       
                                       
# Atualizar uma tarefa existente
@router.put("/tarefas/{id}", response_model=TaskResponse)
async def atualizar_tarefa_id(id: int, tarefa_data: TaskUpdate, session: AsyncSession = Depends(get_session)):
    repository = TaskRepository(session)
    usecase = UpdateTaskUsecase(repository) 
    tarefa = await usecase.execute(id, tarefa_data)
    return tarefa
  

# Excluir uma tarefa
@router.delete("/tarefas/{id}", status_code=200)
async def excluir_tarefa_id(id: int, session: AsyncSession = Depends(get_session)):
    repository = TaskRepository(session)
    usecase = DeleteTaskUsecase(repository)
    await usecase.execute(id)
    return {"detail": "Tarefa excluída com sucesso."}