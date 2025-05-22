from abc import ABC, abstractmethod
from app.models.product import Product

class IProductRepository(ABC):
    @abstractmethod
    def get_filtered(self, skip: int, limit: int, section: str, min_price: float, max_price: float, available: bool): pass

    @abstractmethod
    def get_by_id(self, product_id: int): pass

    @abstractmethod
    def create(self, product: Product): pass

    @abstractmethod
    def update(self, db_product: Product, update_data: dict): pass

    @abstractmethod
    def delete(self, db_product: Product): pass
