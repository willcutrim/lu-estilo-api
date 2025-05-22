from app.schemas.client import ClientCreate, ClientUpdate
from app.models.client import Client

class CreateClientUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data: ClientCreate):
        if self.repo.get_by_email_or_cpf(data.email, data.cpf):
            raise ValueError("E-mail ou CPF já cadastrados.")
        new_client = Client(**data.dict())
        return self.repo.create(new_client)


class GetAllClientsUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip=0, limit=10, name=None, email=None):
        return self.repo.get_filtered(skip=skip, limit=limit, name=name, email=email)


class GetClientByIdUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id):
        return self.repo.get_by_id(client_id)


class UpdateClientUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id, data: ClientUpdate):
        db_client = self.repo.get_by_id(client_id)
        if not db_client:
            return None
        return self.repo.update(db_client, data.dict())


class DeleteClientUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id):
        db_client = self.repo.get_by_id(client_id)
        if not db_client:
            return None
        self.repo.delete(db_client)
        return True
