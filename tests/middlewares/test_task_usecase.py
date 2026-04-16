import pytest
from unittest.mock import AsyncMock, MagicMock
from fastapi import HTTPException

from app.usecase.task_usecase import (
    CreateTaskUsecase,
    DeleteTaskUsecase,
    SearchTaskIDUsecase,
    UpdateTaskUsecase,
    ListTaskUsecase,
    FilterTaskDataUsecase,
)


@pytest.fixture
def repository():
    mock = MagicMock()
    mock.create = AsyncMock()
    mock.delete = AsyncMock()
    mock.search_by_id = AsyncMock()
    mock.update = AsyncMock()
    mock.list = AsyncMock()
    mock.filter_task = AsyncMock()
    return mock


@pytest.fixture
def tarefa_mock():
    tarefa = MagicMock()
    tarefa.id = 1
    tarefa.titulo = "Estudar Clean Architecture"
    tarefa.descricao = "Implementar com FastAPI"
    return tarefa


@pytest.fixture
def filtro_mock():
    filtro = MagicMock()
    filtro.data_inicio = "2026-01-01"
    filtro.data_fim = "2026-01-31"
    return filtro


@pytest.mark.asyncio
async def test_create_chama_repository(repository, tarefa_mock):
    repository.create.return_value = tarefa_mock
    usecase = CreateTaskUsecase(repository)
    result = await usecase.execute(tarefa_mock)
    repository.create.assert_called_once_with(tarefa_mock)
    assert result == tarefa_mock


@pytest.mark.asyncio
async def test_delete_chama_repository_com_id(repository):
    repository.delete.return_value = True
    usecase = DeleteTaskUsecase(repository)
    result = await usecase.execute(1)
    repository.delete.assert_called_once_with(1)
    assert result is True


@pytest.mark.asyncio
async def test_search_retorna_tarefa_existente(repository, tarefa_mock):
    repository.search_by_id.return_value = tarefa_mock
    usecase = SearchTaskIDUsecase(repository)
    result = await usecase.execute(1)
    repository.search_by_id.assert_called_once_with(1)
    assert result == tarefa_mock


@pytest.mark.asyncio
async def test_search_lanca_404_quando_nao_encontrada(repository):
    repository.search_by_id.return_value = None
    usecase = SearchTaskIDUsecase(repository)
    with pytest.raises(HTTPException) as exc:
        await usecase.execute(99)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Tarefa não encontrada"


@pytest.mark.asyncio
async def test_update_chama_repository_com_id_e_dados(repository, tarefa_mock):
    repository.update.return_value = tarefa_mock
    usecase = UpdateTaskUsecase(repository)
    result = await usecase.execute(1, tarefa_mock)
    repository.update.assert_called_once_with(1, tarefa_mock)
    assert result == tarefa_mock


@pytest.mark.asyncio
async def test_list_retorna_lista_de_tarefas(repository, tarefa_mock):
    repository.list.return_value = [tarefa_mock, tarefa_mock]
    usecase = ListTaskUsecase(repository)
    result = await usecase.execute()
    repository.list.assert_called_once()
    assert len(result) == 2


@pytest.mark.asyncio
async def test_list_retorna_lista_vazia(repository):
    repository.list.return_value = []
    usecase = ListTaskUsecase(repository)
    result = await usecase.execute()
    assert result == []


@pytest.mark.asyncio
async def test_filter_chama_repository_com_filtro(repository, tarefa_mock, filtro_mock):
    repository.filter_task.return_value = [tarefa_mock]
    usecase = FilterTaskDataUsecase(repository)
    result = await usecase.execute(filtro_mock)
    repository.filter_task.assert_called_once_with(filtro_mock)
    assert result == [tarefa_mock]


@pytest.mark.asyncio
async def test_filter_retorna_vazio_sem_resultados(repository, filtro_mock):
    repository.filter_task.return_value = []
    usecase = FilterTaskDataUsecase(repository)
    result = await usecase.execute(filtro_mock)
    assert result == []