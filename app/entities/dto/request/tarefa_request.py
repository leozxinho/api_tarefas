from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluido: bool = False
    
class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str
    concluido: bool
    
class TarefaDelete(BaseModel):
    id: int

class FiltroTarefaData(BaseModel):
    data_inicio: Optional[datetime] = None
    data_fim: Optional[datetime] = None