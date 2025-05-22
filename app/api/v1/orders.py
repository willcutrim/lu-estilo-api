from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.order import OrderCreate, OrderOut
from app.infrastructure.repositories.order_repo import OrderRepository
from app.domain.use_cases.order_uc import (
    CreateOrderUseCase, GetOrderByIdUseCase, ListOrdersUseCase,
    UpdateOrderStatusUseCase, DeleteOrderUseCase
)
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=OrderOut)
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    repo = OrderRepository(db)
    use_case = CreateOrderUseCase(repo)
    try:
        return use_case.execute(data.client_id, data.items)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[OrderOut])
def list_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    repo = OrderRepository(db)
    use_case = ListOrdersUseCase(repo)
    return use_case.execute(skip, limit)

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    repo = OrderRepository(db)
    use_case = GetOrderByIdUseCase(repo)
    order = use_case.execute(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    return order

@router.put("/{order_id}")
def update_status(order_id: int, status: str, db: Session = Depends(get_db)):
    repo = OrderRepository(db)
    use_case = UpdateOrderStatusUseCase(repo)
    order = use_case.execute(order_id, status)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    return {"detail": "Status atualizado com sucesso."}

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    repo = OrderRepository(db)
    use_case = DeleteOrderUseCase(repo)
    deleted = use_case.execute(order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")
    return {"detail": "Pedido excluído com sucesso."}
