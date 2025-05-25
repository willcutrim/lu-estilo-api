# 💬 Integração com WhatsApp Business API

Este sistema está integrado com a API do WhatsApp Cloud para envio automático de mensagens em eventos comerciais, como criação de pedidos, envio de orçamentos e promoções.

---

## 📦 Pré-requisitos

- Conta no Facebook Business
- Número registrado na API do WhatsApp (via [https://developers.facebook.com/](https://developers.facebook.com/))
- Configuração de token, número e templates aprovados

---

## ⚙️ Como funciona

A integração está encapsulada no serviço:

```
app/services/whatsapp_service.py
```

Os dados de autenticação são armazenados por **empresa**, no modelo:

```
app/models/whatsapp_config.py
```

---

## 🔐 Variáveis de ambiente necessárias

No `.env`:

```
WHATSAPP_TOKEN=seu_token_facebook_api
WHATSAPP_PHONE_NUMBER_ID=seu_phone_number_id
```

> Ou configuráveis via banco de dados, por empresa.

---

## 📩 Eventos que disparam mensagens

### ✅ Pedido criado

Ao criar um pedido com:

```
POST /orders/
```

O sistema envia automaticamente uma mensagem de confirmação ao cliente com os dados do pedido (ex: nome e número).

---

### ✅ Orçamento criado

```
POST /orcamentos/
```

Também dispara uma mensagem confirmando o envio do orçamento.

---

### ✅ Promoção manual

```
POST /whatsapp/promocao
```

Envia uma mensagem promocional para **todos os clientes da empresa**.

**Payload exemplo:**

```json
{
  "empresa_id": 1,
  "template": "modelo_teste",
  "variaveis": ["Olá, {{1}}, aproveite a promoção exclusiva!"],
  "titulo": "Nova promoção disponível!"
}
```

---

## 📤 Envio de mensagem direto (manual)

```
POST /whatsapp/send
```

Envio direto usando dados da empresa e template aprovado.

**Payload exemplo:**

```json
{
  "empresa_id": 1,
  "numero": "559999999999",
  "template": "modelo_teste",
  "variaveis": ["Willyam", "pedido #45"]
}
```

---

## ✅ Templates

As mensagens usam **templates do tipo `template`** cadastrados e aprovados via painel da Meta.

Você pode enviar variáveis do tipo `{{1}}`, `{{2}}`, etc., e configurar `language.code = pt_BR`.

---

## 🛑 Tratamento de erros

- Se o token for inválido ou expirado, retorna erro 401
- Se o template não existir ou tiver erro de preenchimento, retorna erro 400
- Todas as exceções são tratadas com logs e envio opcional para o Sentry

---

## 🧪 Testes

Para testar, use o número cadastrado no painel de sandbox e envie templates de exemplo com:

```
POST /whatsapp/send
```

Ou crie um pedido real (`/orders/`) para disparar automaticamente.

---

## 📞 Suporte Meta API

- Documentação oficial: https://developers.facebook.com/docs/whatsapp