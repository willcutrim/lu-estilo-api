from pydantic import BaseModel

class PromocaoRequest(BaseModel):
    empresa_id: int
    mensagem: str
