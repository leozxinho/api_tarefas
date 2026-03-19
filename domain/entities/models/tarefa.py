from datetime import datetime
from sqlalchemy import Index, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from infrastructure.database_mysql.mysql_connection import Base

class TarefaModel(Base):
    __tablename__ = "tarefas"
    __table_args__ = (
        Index('idx_tarefas_titulo', "titulo"),
        
        #Indice composto
        Index('idx_tarefas_concluida_created', "concluido", "created_at"),
    )
    
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(250), nullable=False)
    concluido: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now)
    
    def __repr__(self) -> str:
        return f"TarefaModel(id={self.id}, titulo='{self.titulo}')"