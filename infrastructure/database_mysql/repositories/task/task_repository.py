# infrastructure/database_mysql/repositories/task_repository.py
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.entities.dto.request.task_request import FilterTaskData, Task
from app.entities.dto.response.task_response import TaskResponse
from app.interface.i_task import ITaskRepository
from infrastructure.database_mysql.task_model import TaskModel


class TaskRepository(ITaskRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, tarefa_model: TaskResponse):
        new = TaskModel(
            titulo=tarefa_model.titulo,
            descricao=tarefa_model.descricao,
        )
        self.session.add(new)
        await self.session.commit()
        await self.session.refresh(new)
        return new

    async def delete(self, tarefa: int):
        stmt = delete(TaskModel).where(TaskModel.id == tarefa)
        await self.session.execute(stmt)
        await self.session.commit()
        return True

    async def filter_task(self, filtro: FilterTaskData):
        query = select(TaskModel)
        filtros = {
            "data_inicio": (TaskModel.data_tarefa, ">="),
            "data_fim": (TaskModel.data_tarefa, "<="),
        }
        for campo, (coluna, operador) in filtros.items():
            valor = getattr(filtro, campo)
            if valor:
                if operador == ">=":
                    query = query.where(coluna >= valor)
                elif operador == "<=":
                    query = query.where(coluna <= valor)

        result = await self.session.execute(query)
        return result.scalars().all()

    async def list(self):
        result = await self.session.execute(select(TaskModel))
        return result.scalars().all()

    async def search_by_id(self, id: int):
        result = await self.session.execute(
            select(TaskModel).filter_by(id=id)
        )
        return result.scalar_one_or_none()

    async def update(self, id: int, tarefa: Task):
        stmt = (
            update(TaskModel)
            .where(TaskModel.id == id)
            .values(
                titulo=tarefa.titulo,
                descricao=tarefa.descricao,
                concluido=tarefa.concluido,
            )
        )
        await self.session.execute(stmt)
        await self.session.commit()

        result = await self.session.execute(select(TaskModel).where(TaskModel.id == id))
        return result.scalar_one_or_none()