from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.entities.dto.response.tarefas_response import TarefaCreate, TarefasResponse
from app.entities.dto.request.tarefa_request import FiltroTarefaData, TarefaUpdate
from app.usecase.filtro_data_tarefa_usecase import FiltroTarefaDataUsecase
from infrastructure.database_mysql.mysql_connection import get_session
from infrastructure.database_mysql.repositories.tarefa.atualizar_tarefa_repository import AtualizarTarefaRepository
from infrastructure.database_mysql.repositories.tarefa.buscar_tarefa_id_repository import BuscarTarefaIDRepository
from infrastructure.database_mysql.repositories.tarefa.deletar_tarefa_repository import DeletarTarefaRepository
from infrastructure.database_mysql.repositories.tarefa.filtro_data_tarefa_repository import FiltroTarefaDataRepository
from infrastructure.database_mysql.repositories.tarefa.listar_tarefa_repository import ListarTarefaRepository
from infrastructure.database_mysql.repositories.tarefa.criar_tarefa_repository import CriarTarefaRepository
from app.usecase.atualizar_tarefa_usecase import AtualizarTarefaUsecase
from app.usecase.buscar_tarefa_id_usecase import BuscarTarefaIDUsecase
from app.usecase.deletar_tarefa_usecase import DeletarTarefaUsecase
from app.usecase.listar_tarefas_usecase import ListarTarefaUsecase
from app.usecase.criar_tarefa_usecase import CriarTarefaUsecase


with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

router = APIRouter(
    tags=["Tarefas"],
    prefix="/api/v1",
)


# Listar todas as tarefas
@router.get("/tarefas", response_model=List[TarefasResponse])
async def listar_tarefas(session: AsyncSession = Depends(get_session)):
   repository = ListarTarefaRepository(session)
   usecase = ListarTarefaUsecase(repository)
   tarefa = await usecase.execute()
   return tarefa

#Buscar tarefas por data
@router.get("/tarefas/data", response_model=List[TarefasResponse])
async def filtrar_tarefa_data(filtro: FiltroTarefaData = Depends(), session: AsyncSession = Depends(get_session)):
    repository = FiltroTarefaDataRepository(session)
    usecase = FiltroTarefaDataUsecase(repository)
    tarefa = await usecase.execute(filtro)
    return tarefa


# Buscar tarefa por ID
@router.get("/tarefas/{id}", response_model=TarefasResponse)
async def buscar_tarefa_id(id: int, session: AsyncSession = Depends(get_session)):
    repository = BuscarTarefaIDRepository(session)
    usecase = BuscarTarefaIDUsecase(repository)
    tarefa = await usecase.execute(id)
    return tarefa
    
    
# Criar uma nova tarefa
@router.post("/tarefas", response_model=TarefasResponse)
async def criar_tarefa(tarefa_model: TarefaCreate, session: AsyncSession = Depends(get_session)):
    repository = CriarTarefaRepository(session)
    usecase = CriarTarefaUsecase(repository)
    tarefa = await usecase.execute(tarefa_model)
    return tarefa
                                       
                                       
# Atualizar uma tarefa existente
@router.put("/tarefas/{id}", response_model=TarefasResponse)
async def atualizar_tarefa_id(id: int, tarefa_data: TarefaUpdate, session: AsyncSession = Depends(get_session)):
    repository = AtualizarTarefaRepository(session)
    usecase = AtualizarTarefaUsecase(repository) 
    tarefa = await usecase.execute(id, tarefa_data)
    return tarefa
  

# Excluir uma tarefa
@router.delete("/tarefas/{id}", status_code=200)
async def excluir_tarefa_id(id: int, session: AsyncSession = Depends(get_session)):
    repository = DeletarTarefaRepository(session)
    usecase = DeletarTarefaUsecase(repository)
    await usecase.execute(id)
    return {"detail": "Tarefa excluída com sucesso."}