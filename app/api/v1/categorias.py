from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.categoria import CategoriaCreate, CategoriaOut
from app.infrastructure.repositories.categoria_repo import CategoriaRepository
from app.domain.use_cases.categoria_uc import (
    CreateCategoriaUseCase,
    ListCategoriasUseCase,
    GetCategoriaByIdUseCase,
    DeleteCategoriaUseCase
)

router = APIRouter()

@router.post("/", response_model=CategoriaOut)
def criar_categoria(data: CategoriaCreate, db: Session = Depends(get_db)):
    repo = CategoriaRepository(db)
    use_case = CreateCategoriaUseCase(repo)
    return use_case.execute(data)


@router.get("/", response_model=List[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    repo = CategoriaRepository(db)
    use_case = ListCategoriasUseCase(repo)
    return use_case.execute()


@router.get("/{id}", response_model=CategoriaOut)
def buscar_categoria(id: int, db: Session = Depends(get_db)):
    repo = CategoriaRepository(db)
    use_case = GetCategoriaByIdUseCase(repo)
    categoria = use_case.execute(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria


@router.delete("/{id}", status_code=204)
def deletar_categoria(id: int, db: Session = Depends(get_db)):
    repo = CategoriaRepository(db)
    use_case = DeleteCategoriaUseCase(repo)
    use_case.execute(id)
