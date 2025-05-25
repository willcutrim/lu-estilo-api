from datetime import timedelta
import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi import Body

from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.infrastructure.repositories.user_repo import UserRepository
from app.domain.use_cases.user_uc import CreateUserUseCase, AuthenticateUserUseCase
from app.db.session import get_db
from app.core.security import create_access_token, create_refresh_token, verify_refresh_token


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
    db_user = use_case.execute(user)

    if not db_user:
        raise HTTPException(status_code=400, detail="Credenciais inválidas. Verifique seu e-mail e senha.")
    
    access_token = create_access_token(
        data={"sub": db_user.email},
        expires_delta=timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))
    )
    refresh_token = create_refresh_token(
        data={"sub": db_user.email},
        expires_delta=timedelta(days=int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7)))
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh-token")
def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = verify_refresh_token(refresh_token)
        email = payload.get("sub")

        if not email:
            raise HTTPException(status_code=401, detail="Token inválido")

        new_token = create_access_token(
            data={"sub": email},
            expires_delta=timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))
        )
        return {"access_token": new_token, "token_type": "bearer"}

    except Exception:
        raise HTTPException(status_code=401, detail="Refresh token inválido ou expirado")
