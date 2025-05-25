from pydantic import BaseModel
from typing import Optional
from datetime import date

from app.schemas.categoria import CategoriaOut

class ProductBase(BaseModel):
    description: str
    price: float
    barcode: str
    section: str
    stock: int
    expiration_date: Optional[date]
    available: Optional[bool] = True
    image_url: Optional[str]
    categoria_id: Optional[int] = None 


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int
    categoria: Optional[CategoriaOut] = None  

    class Config:
        orm_mode = True
