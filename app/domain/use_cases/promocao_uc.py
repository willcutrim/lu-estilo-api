class EnviarPromocaoUseCase:
    def __init__(self, client_repo, whatsapp_repo, whatsapp_service_class):
        self.client_repo = client_repo
        self.whatsapp_repo = whatsapp_repo
        self.WhatsappService = whatsapp_service_class

    def execute(self, empresa_id: int, mensagem: str):
        clientes = self.client_repo.get_all_by_empresa(empresa_id)
        config = self.whatsapp_repo.get_by_empresa_id(empresa_id)

        if not config:
            raise ValueError("Empresa sem configuração de WhatsApp")

        service = self.WhatsappService(config.token, config.phone_number_id)

        for cliente in clientes:
            if not cliente.telefone:
                continue

            try:
                """
                Aqui você cria a mensagem pela nossa api, porém pode adaptar para no painel do WhatsApp a mensagem
                em si e apenas colocar a variável com o nome do cliente.
                No meu caso optei por criar a mensagem na api, mas você pode fazer como preferir.
                """
                service.send_message(
                    to=cliente.telefone,
                    template_name="promocao_disponivel",
                    variables=[mensagem]
                )
            except Exception as e:
                print(f"[WHATSAPP] Erro com cliente {cliente.name}: {e}")
