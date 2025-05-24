from typing import Optional
from sqlalchemy.orm import Session
from app.models.whatsapp_config import WhatsappConfig
from app.schemas.whatsapp import WhatsappConfigCreate


class WhatsappConfigRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_empresa_id(self, empresa_id: int) -> Optional[WhatsappConfig]:
        return self.db.query(WhatsappConfig).filter(WhatsappConfig.empresa_id == empresa_id).first()

    def create_or_update(self, data: WhatsappConfigCreate) -> WhatsappConfig:
        config = self.get_by_empresa_id(data.empresa_id)
        if config:
            config.token = data.token
            config.phone_number_id = data.phone_number_id
            config.nome_empresa = data.nome_empresa
        else:
            config = WhatsappConfig(**data.dict())
            self.db.add(config)
        self.db.commit()
        self.db.refresh(config)
        return config
