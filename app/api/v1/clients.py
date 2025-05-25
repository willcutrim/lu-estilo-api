from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user, only_admin
from app.schemas.client import ClientCreate, ClientUpdate, ClientOut
from app.infrastructure.repositories.client_repo import ClientRepository
from app.domain.use_cases.client_uc import (
    CreateClientUseCase, GetAllClientsUseCase, GetClientByIdUseCase,
    UpdateClientUseCase, DeleteClientUseCase
)
from app.db.session import get_db

router = APIRouter()

@router.post("/create", response_model=ClientOut, dependencies=[Depends(only_admin)])
def create_client(data: ClientCreate, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = CreateClientUseCase(repo)
    try:
        return use_case.execute(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[ClientOut], dependencies=[Depends(get_current_user)])
def get_clients(
    skip: int = 0,
    limit: int = 10,
    name: str = None,
    email: str = None,
    db: Session = Depends(get_db)
):
    repo = ClientRepository(db)
    use_case = GetAllClientsUseCase(repo)
    return use_case.execute(skip=skip, limit=limit, name=name, email=email)


@router.get("/{client_id}", response_model=ClientOut, dependencies=[Depends(get_current_user)])
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = GetClientByIdUseCase(repo)
    client = use_case.execute(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return client

@router.put("/{client_id}", response_model=ClientOut, dependencies=[Depends(only_admin)])
def update_client(client_id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = UpdateClientUseCase(repo)
    client = use_case.execute(client_id, data)

    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    return client

@router.delete("/{client_id}", dependencies=[Depends(only_admin)])
def delete_client(client_id: int, db: Session = Depends(get_db)):
    repo = ClientRepository(db)
    use_case = DeleteClientUseCase(repo)
    success = use_case.execute(client_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    return {"detail": "Cliente excluído com sucesso."}
