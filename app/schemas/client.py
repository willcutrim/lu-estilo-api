from typing import Optional
from pydantic import BaseModel, EmailStr

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    telefone: str


class ClientCreate(ClientBase):
    empresa_id: int


class ClientUpdate(ClientBase):
    name: str
    email: EmailStr
    cpf: str
    telefone: str
    empresa_id: Optional[int] = None


class ClientOut(ClientBase):
    id: int

    class Config:
        orm_mode = True
