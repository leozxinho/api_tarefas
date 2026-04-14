from urllib.parse import quote_plus
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import  DeclarativeBase
from infrastructure.config import get_environment_variables
import urllib.parse

env = get_environment_variables()


DATABASE_URL = "{driver}://{user}:{password}@{host}:{port}/{db}".format(
    driver="mysql+aiomysql",
    user=env.DB_LOGIN,
    password=urllib.parse.quote_plus(env.DB_PASSWORD),
    host=env.DB_HOST,
    port=env.DB_PORT,
    db=env.DB_NAME
)
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

class Base(DeclarativeBase):
    pass