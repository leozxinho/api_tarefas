from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    concluido: bool = False
    
class TaskUpdate(BaseModel):
    titulo: str
    descricao: str
    concluido: bool
    
class TaskDelete(BaseModel):
    id: int

class FilterTaskData(BaseModel):
    data_inicio: Optional[datetime] = None
    data_fim: Optional[datetime] = None