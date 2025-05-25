from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.promocao import PromocaoRequest
from app.infrastructure.repositories.client_repo import ClientRepository
from app.infrastructure.repositories.whatsapp_config_repo import WhatsappConfigRepository
from app.services.whatsapp_service import WhatsappService
from app.domain.use_cases.promocao_uc import EnviarPromocaoUseCase
from app.db.session import get_db

router = APIRouter()

@router.post("/enviar")
def enviar_promocao(data: PromocaoRequest, db: Session = Depends(get_db)):
    client_repo = ClientRepository(db)
    whatsapp_repo = WhatsappConfigRepository(db)
    use_case = EnviarPromocaoUseCase(client_repo, whatsapp_repo, WhatsappService)

    use_case.execute(data.empresa_id, data.mensagem)
    return {"detail": "Promoção enviada com sucesso"}
