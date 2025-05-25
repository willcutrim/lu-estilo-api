from typing import Optional, List
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate


class CreateCategoriaUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data: CategoriaCreate) -> Categoria:
        return self.repo.create(data)


class ListCategoriasUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self) -> List[Categoria]:
        return self.repo.get_all()


class GetCategoriaByIdUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id: int) -> Optional[Categoria]:
        return self.repo.get_by_id(id)


class DeleteCategoriaUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, id: int) -> None:
        self.repo.delete(id)
