from app.models.order import Order, OrderItem
from app.models.product import Product
from sqlalchemy.orm import Session

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, client_id, items):
        db_items = []
        for item in items:
            product = self.db.query(Product).filter(Product.id == item.product_id).first()
            if not product or product.stock < item.quantity:
                raise ValueError(f"Produto {item.product_id} sem estoque suficiente.")
            product.stock -= item.quantity
            db_item = OrderItem(
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=product.price
            )
            db_items.append(db_item)

        order = Order(client_id=client_id, items=db_items)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_by_id(self, order_id):
        return self.db.query(Order).filter(Order.id == order_id).first()

    def list_orders(self, skip=0, limit=10):
        return self.db.query(Order).offset(skip).limit(limit).all()

    def update_order_status(self, order_id, status):
        order = self.get_by_id(order_id)
        if order:
            order.status = status
            self.db.commit()
            self.db.refresh(order)
        return order

    def delete_order(self, order_id):
        order = self.get_by_id(order_id)
        if order:
            self.db.delete(order)
            self.db.commit()
        return order
