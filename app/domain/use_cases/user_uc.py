from app.domain.interfaces.user_interface import IUserRepository
from app.schemas.user import UserCreate, UserLogin
from app.core.security import get_password_hash, verify_password, create_access_token
from app.models.user import User
from app.services.mixins.sentry_mixin import HandleExceptionMixin


class CreateUserUseCase(HandleExceptionMixin):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, user: UserCreate):
        try:
            hashed_pw = get_password_hash(user.password)
            db_user = User(email=user.email, hashed_password=hashed_pw)
            return self.repository.create_user(db_user)
        except Exception as e:
            self.handle_exception(e, "Erro ao criar usuário.")


class AuthenticateUserUseCase(HandleExceptionMixin):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, user: UserLogin):
        try:
            db_user = self.repository.get_user_by_email(user.email)
            if not db_user or not verify_password(user.password, db_user.hashed_password):
                return None

            return db_user

        except Exception as e:
            self.handle_exception(e, "Erro ao autenticar usuário.")
