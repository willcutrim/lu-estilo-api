from abc import ABC, abstractmethod
from app.models.client import Client

class IClientRepository(ABC):
    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def get_by_id(self, client_id: int): pass

    @abstractmethod
    def get_by_email_or_cpf(self, email: str, cpf: str): pass

    @abstractmethod
    def create(self, client: Client): pass

    @abstractmethod
    def update(self, db_client: Client, update_data: dict): pass

    @abstractmethod
    def delete(self, db_client: Client): pass
