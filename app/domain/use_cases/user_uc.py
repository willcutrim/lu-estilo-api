from app.domain.interfaces.user_interface import IUserRepository
from app.schemas.user import UserCreate, UserLogin
from app.core.security import get_password_hash, verify_password, create_access_token
from app.models.user import User


class CreateUserUseCase:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, user: UserCreate):
        hashed_pw = get_password_hash(user.password)
        db_user = User(email=user.email, hashed_password=hashed_pw)
        return self.repository.create_user(db_user)

class AuthenticateUserUseCase:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, user: UserLogin):
        db_user = self.repository.get_user_by_email(user.email)
        if not db_user or not verify_password(user.password, db_user.hashed_password):
            return None
        return create_access_token(data={"sub": db_user.email})
