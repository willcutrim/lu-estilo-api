from sqlalchemy import Column, Integer, String
from app.db.base import Base

class WhatsappConfig(Base):
    __tablename__ = "whatsapp_configs"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, nullable=False, unique=True)
    token = Column(String, nullable=False)
    phone_number_id = Column(String, nullable=False)
    nome_empresa = Column(String, nullable=True)
