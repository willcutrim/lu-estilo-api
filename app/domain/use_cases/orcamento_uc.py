from app.services.mixins.sentry_mixin import HandleExceptionMixin


class CreateOrcamentoUseCase(HandleExceptionMixin):
    def __init__(self, repo, client_repo, whatsapp_repo, whatsapp_service_class):
        self.repo = repo
        self.client_repo = client_repo
        self.whatsapp_repo = whatsapp_repo
        self.WhatsappService = whatsapp_service_class

    def execute(self, data):
        orcamento = self.repo.create(data)

        cliente = self.client_repo.get_by_id(data.client_id)
        config = self.whatsapp_repo.get_by_empresa_id(cliente.empresa_id)

        if not config or not cliente or not cliente.telefone:
            return orcamento

        try:
            service = self.WhatsappService(config.token, config.phone_number_id)
            service.send_message(
                to=cliente.telefone,
                template_name="orcamento_disponivel",
                variables=[cliente.name, str(orcamento.id)]
            )
        except Exception as e:
            self.handle_exception(e, "mensagem via WhatsApp")

        return orcamento
