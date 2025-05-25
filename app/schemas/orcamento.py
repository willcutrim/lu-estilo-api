from pydantic import BaseModel

from app.choices import choices_orcamento


class OrcamentoCreate(BaseModel):
    client_id: int


class OrcamentoOut(BaseModel):
    id: int
    client_id: int
    status: int
    status_display: str

    @staticmethod
    def from_orm_with_display(orcamento):
        return OrcamentoOut(
            id=orcamento.id,
            client_id=orcamento.client_id,
            status=orcamento.status,
            status_display=choices_orcamento.CHOICES_ORCAMENTO.get(orcamento.status, "desconhecido")
        )

    class Config:
        orm_mode = True
