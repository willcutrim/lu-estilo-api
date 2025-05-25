from typing import Optional, List
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate
from app.services.mixins.sentry_mixin import HandleExceptionMixin


class CreateCategoriaUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data: CategoriaCreate) -> List[Categoria]:
        try:
            return self.repo.create(data)
        except Exception as e:
            self.handle_exception(e, "criar categoria")


class ListCategoriasUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self) -> List[Categoria]:
        try:
            return self.repo.get_all()
        except Exception as e:
            self.handle_exception(e, "listar categorias")


class GetCategoriaByIdUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id: int) -> Optional[Categoria]:
        try:
            return self.repo.get_by_id(id)
        except Exception as e:
            self.handle_exception(e, "obter categoria por ID")
            return None


class DeleteCategoriaUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id: int) -> None:
        try:
            self.repo.delete(id)
        except Exception as e:
            self.handle_exception(e, "deletar categoria")
