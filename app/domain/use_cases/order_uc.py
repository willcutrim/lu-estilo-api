class CreateOrderUseCase:
    def __init__(self, repo, client_repo, whatsapp_config_repo, whatsapp_service_class):
        self.repo = repo
        self.client_repo = client_repo
        self.whatsapp_config_repo = whatsapp_config_repo
        self.WhatsappService = whatsapp_service_class

    def execute(self, client_id, items):
        order = self.repo.create_order(client_id, items)

        client = self.client_repo.get_by_id(client_id)
        if not client or not client.telefone:
            return order

        config = self.whatsapp_config_repo.get_by_empresa_id(client.empresa_id)
        if not config:
            return order

        try:
            service = self.WhatsappService(token=config.token, phone_number_id=config.phone_number_id)
            service.send_message(
                to=client.telefone,
                template_name="teste",
                variables=[client.name, str(order.id)]
            )
        except Exception as e:
            print(f"[WHATSAPP] Erro ao enviar mensagem: {e}")

        return order



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
