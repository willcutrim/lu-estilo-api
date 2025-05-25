from app.schemas.client import ClientCreate, ClientUpdate
from app.models.client import Client
from app.services.mixins.sentry_mixin import HandleExceptionMixin

class CreateClientUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data: ClientCreate):
        try:
            if self.repo.get_by_email_or_cpf(data.email, data.cpf):
                raise ValueError("E-mail ou CPF já cadastrados.")
            new_client = Client(**data.dict())
            return self.repo.create(new_client)
        except Exception as e:
            self.handle_exception(e, "Erro ao criar cliente.")


class GetAllClientsUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip=0, limit=10, name=None, email=None):
        try:
            return self.repo.get_filtered(skip=skip, limit=limit, name=name, email=email)
        except Exception as e:
            self.handle_exception(e, "listar clientes")
            return []


class GetClientByIdUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id):
        try:
            return self.repo.get_by_id(client_id)
        except Exception as e:
            self.handle_exception(e, "obter cliente por ID")
            return None


class UpdateClientUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id, data: ClientUpdate):
        try:
            db_client = self.repo.get_by_id(client_id)

            if not db_client:
                return None
            
            return self.repo.update(db_client, data.dict())
        except Exception as e:
            self.handle_exception(e, "atualizar cliente")


class DeleteClientUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id):
        try:
            db_client = self.repo.get_by_id(client_id)

            if not db_client:
                return None

            self.repo.delete(db_client)
            return True
        except Exception as e:
            self.handle_exception(e, "deletar cliente")
