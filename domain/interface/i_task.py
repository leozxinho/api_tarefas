from abc import ABC, abstractmethod
from domain.entities.dto.request.task_request import Task

class ITaskRepository(ABC):

    @abstractmethod
    def create(self, tarefa: Task) -> Task: ...

    @abstractmethod
    def list(self) -> list[Task]: ...

    @abstractmethod
    def search_by_id(self, id: int) -> Task: ...

    @abstractmethod
    def update(self, id: int, tarefa: Task) -> Task: ...

    @abstractmethod
    def delete(self, id: int) -> None: ...
    
    @abstractmethod
    def filter_task(self, data_inicio: str, data_fim: str) -> Task: ...