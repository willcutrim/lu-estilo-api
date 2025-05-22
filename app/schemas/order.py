from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemOut(OrderItemBase):
    unit_price: float

class OrderCreate(BaseModel):
    client_id: int
    items: List[OrderItemCreate]

class OrderOut(BaseModel):
    id: int
    client_id: int
    status: str
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        orm_mode = True
