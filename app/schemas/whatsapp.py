from typing import Optional
from pydantic import BaseModel

class WhatsappConfigCreate(BaseModel):
    empresa_id: int
    token: str
    phone_number_id: str
    nome_empresa: Optional[str] = None

class WhatsappConfigOut(WhatsappConfigCreate):
    id: int

    class Config:
        orm_mode = True
