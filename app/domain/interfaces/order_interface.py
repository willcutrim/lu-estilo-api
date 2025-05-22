from abc import ABC, abstractmethod

class IOrderRepository(ABC):
    @abstractmethod
    def create_order(self, order_data): pass

    @abstractmethod
    def get_by_id(self, order_id: int): pass

    @abstractmethod
    def list_orders(self, **filters): pass

    @abstractmethod
    def update_order_status(self, order_id: int, status: str): pass

    @abstractmethod
    def delete_order(self, order_id: int): pass
