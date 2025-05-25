from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base

from app.choices import choices_orcamento


class Orcamento(Base):
    __tablename__ = "orcamentos"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    status = Column(Integer, default=choices_orcamento.CHOICE_PENDENTE)

    @property
    def status_display(self):
        return choices_orcamento.CHOICES_ORCAMENTO.get(self.status, "desconhecido")