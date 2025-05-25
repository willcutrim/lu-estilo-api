from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.choices import choices_orcamento
from app.db.session import get_db
from app.schemas.orcamento import OrcamentoCreate, OrcamentoOut
from app.infrastructure.repositories.orcamento_repo import OrcamentoRepository
from app.infrastructure.repositories.client_repo import ClientRepository
from app.infrastructure.repositories.whatsapp_config_repo import WhatsappConfigRepository
from app.services.whatsapp_service import WhatsappService
from app.domain.use_cases.orcamento_uc import CreateOrcamentoUseCase

router = APIRouter()


@router.post("/", response_model=OrcamentoOut)
def criar_orcamento(data: OrcamentoCreate, db: Session = Depends(get_db)):
    repo = OrcamentoRepository(db)
    client_repo = ClientRepository(db)
    whatsapp_repo = WhatsappConfigRepository(db)

    use_case = CreateOrcamentoUseCase(
        repo,
        client_repo,
        whatsapp_repo,
        WhatsappService
    )

    try:
        orcamento = use_case.execute(data)
        return OrcamentoOut.from_orm_with_display(orcamento)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar orçamento: {e}")

@router.patch("/{id}/enviar")
def enviar_orcamento(id: int, db: Session = Depends(get_db)):
    repo = OrcamentoRepository(db)
    orcamento = repo.get_by_id(id)
    if not orcamento:
        raise HTTPException(status_code=404, detail="Orçamento não encontrado")

    orcamento.status = choices_orcamento.CHOICE_ENVIADO
    db.commit()
    db.refresh(orcamento)
    return OrcamentoOut.from_orm_with_display(orcamento)
