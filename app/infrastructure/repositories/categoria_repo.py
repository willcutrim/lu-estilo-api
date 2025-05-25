from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate

class CategoriaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: CategoriaCreate) -> Categoria:
        categoria = Categoria(**data.dict())
        self.db.add(categoria)
        self.db.commit()
        self.db.refresh(categoria)
        return categoria

    def get_all(self) -> List[Categoria]:
        return self.db.query(Categoria).all()

    def get_by_id(self, id: int) -> Optional[Categoria]:
        return self.db.query(Categoria).filter_by(id=id).first()

    def delete(self, id: int) -> None:
        categoria = self.get_by_id(id)
        if categoria:
            self.db.delete(categoria)
            self.db.commit()
