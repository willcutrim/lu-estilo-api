from app.schemas.product import ProductCreate, ProductUpdate
from app.models.product import Product
from app.services.mixins.sentry_mixin import HandleExceptionMixin


class CreateProductUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, data: ProductCreate):
        new_product = Product(**data.dict())
        return self.repo.create(new_product)


class GetFilteredProductsUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip=0, limit=10, section=None, min_price=None, max_price=None, available=None, categoria_id=None):
        try:
            return self.repo.get_filtered(skip, limit, section, min_price, max_price, available, categoria_id)
        except Exception as e:
            self.handle_exception(e, "filtrar produtos")
            return []


class GetProductByIdUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, product_id):
        try:
            return self.repo.get_by_id(product_id)
        except Exception as e:
            self.handle_exception(e, "obter produto por ID")
            return None


class UpdateProductUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, product_id, data: ProductUpdate):
        try:
            db_product = self.repo.get_by_id(product_id)
            if not db_product:
                return None
            return self.repo.update(db_product, data.dict())
        except Exception as e:
            self.handle_exception(e, "atualizar produto")


class DeleteProductUseCase(HandleExceptionMixin):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, product_id):
        try:
            db_product = self.repo.get_by_id(product_id)
            if not db_product:
                return None
            self.repo.delete(db_product)
            return True
    
        except Exception as e:
            self.handle_exception(e, "deletar produto")
