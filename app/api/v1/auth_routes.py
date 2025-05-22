from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.infrastructure.repositories.user_repo import UserRepository
from app.domain.use_cases.user_uc import CreateUserUseCase, AuthenticateUserUseCase
from app.db.session import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    use_case = CreateUserUseCase(repo)
    return use_case.execute(user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    use_case = AuthenticateUserUseCase(repo)
    token = use_case.execute(user)

    if not token:
        raise HTTPException(status_code=400, detail="Credenciais inválidas. Verifique seu e-mail e senha.")
    
    return {"access_token": token}
