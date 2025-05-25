# 💬 Integração com WhatsApp

A API possui integração com WhatsApp para envio automático de mensagens em eventos comerciais, como criação de pedidos, orçamentos e envio de promoções.

---

## ⚙️ Configuração necessária

Para utilizar a integração, é necessário cadastrar as credenciais de envio da empresa:

### 🔐 Rota para cadastrar credenciais

```
POST /whatsapp/config
```

### 📥 Payload esperado

```json
{
  "empresa_id": 1,
  "token": "SEU_TOKEN_WHATSAPP",
  "phone_number_id": "ID_DO_NUMERO",
  "nome_empresa": "Nome Fantasia"
}
```

Esses dados são utilizados internamente para autenticar os envios de mensagens.

---

## 📩 Eventos com envio automático de mensagem

### ✅ Pedido criado

```
POST /orders/
```

Ao criar um novo pedido, o sistema envia uma mensagem automática para o cliente confirmando a criação. A mensagem é baseada em um template e pode conter variáveis como o nome do cliente e número do pedido.

---

### ✅ Orçamento criado

```
POST /orcamentos/
```

O envio da mensagem ocorre de forma automática, informando que o orçamento foi gerado.

---

### ✅ Promoção para clientes da empresa

```
POST /whatsapp/promocao
```

Permite enviar uma mensagem para todos os clientes da empresa com um template previamente configurado.

#### 📥 Exemplo de payload:

```json
{
  "empresa_id": 1,
  "template": "modelo_teste",
  "variaveis": ["Olá, {{1}}, aproveite nossa promoção!"],
  "titulo": "Promoção ativa!"
}
```

---

## 📤 Envio manual de mensagem

```
POST /whatsapp/send
```

Utilize essa rota para enviar uma mensagem manual para um número específico.

#### 📥 Exemplo de payload:

```json
{
  "empresa_id": 1,
  "numero": "559999999999",
  "template": "modelo_teste",
  "variaveis": ["Willyam", "#45"]
}
```

---

## 🧱 Templates e Variáveis

As mensagens são baseadas em templates com variáveis dinâmicas (`{{1}}`, `{{2}}`...). O sistema preenche essas variáveis com os dados enviados na chamada.

---

## 🛑 Tratamento de erros

- Erros de autenticação com token inválido retornam 401
- Templates incorretos retornam erro 400
- As exceções são tratadas e logadas com integração opcional com Sentry

---

## 🧪 Testes

Para testar o envio, basta cadastrar a configuração da empresa e acionar qualquer um dos endpoints de criação (pedido, orçamento, envio manual ou promoção).