from app.domain.interfaces.product_interface import IProductRepository
from app.models.product import Product


class ProductRepository(IProductRepository):
    def __init__(self, db):
        self.db = db

    def get_filtered(
        self, skip=0, limit=10, section=None,
        min_price=None, max_price=None, available=None, categoria_id=None
    ):
        query = self.db.query(Product)
        if section:
            query = query.filter(Product.section.ilike(f"%{section}%"))

        if min_price is not None:
            query = query.filter(Product.price >= min_price)

        if max_price is not None:
            query = query.filter(Product.price <= max_price)

        if available is not None:
            query = query.filter(Product.available == available)

        if categoria_id is not None:
            query = query.filter(Product.categoria_id == categoria_id)
            
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, product_id):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create(self, product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, db_product, update_data):
        for field, value in update_data.items():
            setattr(db_product, field, value)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete(self, db_product):
        self.db.delete(db_product)
        self.db.commit()
