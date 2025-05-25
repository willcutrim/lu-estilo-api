from sqlalchemy.orm import Session
from typing import Optional

from app.models.orcamento import Orcamento
from app.schemas.orcamento import OrcamentoCreate


class OrcamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: OrcamentoCreate) -> Optional[Orcamento]:
        orcamento = Orcamento(**data.dict())
        self.db.add(orcamento)
        self.db.commit()
        self.db.refresh(orcamento)
        return orcamento

    def get_by_id(self, orcamento_id: int) -> Optional[Orcamento]:
        return self.db.query(Orcamento).filter_by(id=orcamento_id).first()
