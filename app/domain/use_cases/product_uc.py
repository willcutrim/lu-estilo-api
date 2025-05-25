from app.schemas.product import ProductCreate, ProductUpdate
from app.models.product import Product


class CreateProductUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data: ProductCreate):
        new_product = Product(**data.dict())
        return self.repo.create(new_product)


class GetFilteredProductsUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip=0, limit=10, section=None, min_price=None, max_price=None, available=None, categoria_id=None):
        return self.repo.get_filtered(skip, limit, section, min_price, max_price, available, categoria_id)


class GetProductByIdUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, product_id):
        return self.repo.get_by_id(product_id)


class UpdateProductUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, product_id, data: ProductUpdate):
        db_product = self.repo.get_by_id(product_id)
        if not db_product:
            return None
        return self.repo.update(db_product, data.dict())


class DeleteProductUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, product_id):
        db_product = self.repo.get_by_id(product_id)
        if not db_product:
            return None
        self.repo.delete(db_product)
        return True
