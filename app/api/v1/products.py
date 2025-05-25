from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.dependencies import get_current_user, only_admin
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.infrastructure.repositories.product_repo import ProductRepository
from app.domain.use_cases.product_uc import (
    CreateProductUseCase, GetFilteredProductsUseCase, GetProductByIdUseCase,
    UpdateProductUseCase, DeleteProductUseCase
)
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=ProductOut, dependencies=[Depends(only_admin)])
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    use_case = CreateProductUseCase(repo)
    return use_case.execute(data)


@router.get("/", response_model=List[ProductOut], dependencies=[Depends(get_current_user)])
def get_products(
    skip: int = 0,
    limit: int = 10,
    section: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    available: Optional[bool] = None,
    categoria_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    repo = ProductRepository(db)
    use_case = GetFilteredProductsUseCase(repo)
    return use_case.execute(skip, limit, section, min_price, max_price, available, categoria_id)

@router.get("/{product_id}", response_model=ProductOut, dependencies=[Depends(get_current_user)])
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    use_case = GetProductByIdUseCase(repo)
    product = use_case.execute(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return product

@router.put("/{product_id}", response_model=ProductOut, dependencies=[Depends(only_admin)])
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    use_case = UpdateProductUseCase(repo)
    product = use_case.execute(product_id, data)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return product

@router.delete("/{id}", dependencies=[Depends(only_admin)])
def delete_product(id: int, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    use_case = DeleteProductUseCase(repo)
    success = use_case.execute(id)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return {"detail": "Produto excluído com sucesso."}
