# app/interface/i_tarefa_repository.py
from abc import ABC, abstractmethod
from app.entities.dto.request.tarefa_request import Tarefa

class ITarefaRepository(ABC):

    @abstractmethod
    def criar(self, tarefa: Tarefa) -> Tarefa: ...

    @abstractmethod
    def listar(self) -> list[Tarefa]: ...

    @abstractmethod
    def buscar_por_id(self, id: int) -> Tarefa: ...

    @abstractmethod
    def atualizar(self, id: int, tarefa: Tarefa) -> Tarefa: ...

    @abstractmethod
    def deletar(self, id: int) -> None: ...
    
    @abstractmethod
    def filtrar_tarefa(self, data_inicio: str, data_fim: str) -> Tarefa: ...