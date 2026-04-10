from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict



class TarefasResponse(BaseModel):
    id: int
    titulo: str | None
    descricao: str | None
    concluido: bool = False
    created_at: datetime
    update_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
        
        
    
class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
