from abc import ABC, abstractmethod
from typing import Optional
from app.models.orcamento import Orcamento
from app.schemas.orcamento import OrcamentoCreate


class IOrcamentoRepository(ABC):
    @abstractmethod
    def create(self, data: OrcamentoCreate) -> Orcamento:
        pass

    @abstractmethod
    def get_by_id(self, orcamento_id: int) -> Optional[Orcamento]:
        pass
