import asyncio
from urllib.parse import quote_plus
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

password = quote_plus("T@refa_2026#Segura")

DATABASE_URL = f"mysql+aiomysql://tarefa:{password}@localhost:3306/tarefas_crud"

async def test_connection():
    engine = create_async_engine(DATABASE_URL)
    async with engine.connect() as conn:
        print("Conectado com sucesso!")
    await engine.dispose()
asyncio.run(test_connection())