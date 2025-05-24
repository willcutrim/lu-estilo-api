from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.whatsapp import WhatsappConfigCreate
from app.infrastructure.repositories.whatsapp_config_repo import WhatsappConfigRepository
from app.services.whatsapp_service import WhatsappService
from app.db.session import get_db

router = APIRouter()

@router.post("/whatsapp/config")
def salvar_config(data: WhatsappConfigCreate, db: Session = Depends(get_db)):
    repo = WhatsappConfigRepository(db)
    config = repo.create_or_update(data)
    return {"detail": "Configuração salva com sucesso", "empresa_id": config.empresa_id}

@router.post("/whatsapp/send")
def enviar_mensagem(empresa_id: int, telefone: str, mensagem: str, db: Session = Depends(get_db)):
    repo = WhatsappConfigRepository(db)
    config = repo.get_by_empresa_id(empresa_id)

    if not config:
        raise HTTPException(status_code=404, detail="Empresa não possui configuração de WhatsApp")

    service = WhatsappService(token=config.token, phone_number_id=config.phone_number_id)

    try:
        result = service.send_message(telefone, mensagem)
        return {"detail": "Mensagem enviada com sucesso", "meta": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar mensagem: {e}")
