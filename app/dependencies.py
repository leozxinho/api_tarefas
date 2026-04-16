# app/dependencies.py
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database_mysql.mysql_connection import AsyncSessionLocal
from infrastructure.database_mysql.repositories.task.task_repository import get_repository

def get_repository(session: AsyncSession) -> get_repository:
    return get_repository(session)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session