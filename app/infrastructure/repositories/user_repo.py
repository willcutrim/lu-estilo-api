from app.domain.interfaces.user_interface import IUserRepository
from app.models.user import User

class UserRepository(IUserRepository):
    def __init__(self, db):
        self.db = db

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
