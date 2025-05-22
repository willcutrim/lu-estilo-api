from abc import ABC, abstractmethod
from app.models.user import User

class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_user_by_email(self, email: str):
        pass
