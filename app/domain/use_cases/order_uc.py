class CreateOrderUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, client_id, items):
        return self.repo.create_order(client_id, items)

class GetOrderByIdUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, order_id):
        return self.repo.get_by_id(order_id)

class ListOrdersUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, skip=0, limit=10):
        return self.repo.list_orders(skip, limit)

class UpdateOrderStatusUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, order_id, status):
        return self.repo.update_order_status(order_id, status)

class DeleteOrderUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, order_id):
        return self.repo.delete_order(order_id)
