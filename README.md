# 🧵 Lu Estilo API

API RESTful para gerenciamento comercial da empresa Lu Estilo, desenvolvida com FastAPI, PostgreSQL, SQLAlchemy e Alembic, seguindo princípios de Clean Architecture.

---

## 🚀 Requisitos

- Python 3.8+
- PostgreSQL 13+
- pip
- Docker (opcional para execução com container)

---

## ⚙️ Passo a passo para rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/lu-estilo-api.git
cd lu-estilo-api
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuração do Banco de Dados

### 4. Criar banco no PostgreSQL

```sql
CREATE DATABASE lu_db;
CREATE USER lu_user WITH PASSWORD 'lu_pass';
GRANT ALL PRIVILEGES ON DATABASE lu_db TO lu_user;
```

### 5. Configurar variável de ambiente

Crie um arquivo `.env` com:

```
DATABASE_URL=postgresql://lu_user:lu_pass@localhost:5432/lu_db
SECRET_KEY=sua_chave_jwt
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
SENTRY_DSN=https://seu_dsn@sentry.io/xxxxxx
```

---

## 📦 Migrations com Alembic

### 6. Rodar as migrações

```bash
alembic upgrade head
```

### 7. Se mudar os models:

```bash
alembic revision --autogenerate -m "alterações em models"
alembic upgrade head
```

---

## ▶️ Executar a aplicação

### 8. Rodar localmente com Uvicorn

```bash
uvicorn app.main:app --reload
```

### Ou execute:

```bash
python run.py
```

---

## 🐳 Executar com Docker

```bash
docker build -t lu-api .
docker run -d -p 8000:8000 --env-file .env lu-api
```

---

## 🌐 Deploy com Railway

1. Suba para um repositório GitHub
2. Acesse [railway.app](https://railway.app/)
3. Crie um projeto e selecione “Deploy from GitHub”
4. Railway detecta o Dockerfile automaticamente
5. Configure as variáveis de ambiente no painel

---

## 🔐 Autenticação & Permissões

- JWT com `access_token` e `refresh_token`
- Endpoint de login: `POST /auth/login`
- Endpoint de refresh: `POST /auth/refresh-token`
- Use o botão "Authorize" no Swagger com seu token
- Níveis de acesso: **usuário comum** e **admin**
- Rotas de criação/edição/deleção são protegidas com `only_admin`

---

## 📡 Monitoramento de Erros

Sentry integrado para capturar exceções automaticamente.

---

## 📁 Estrutura do Projeto

```
app/
├── api/                # Rotas FastAPI
├── domain/             # Casos de uso e interfaces
├── infrastructure/     # Repositórios (SQLAlchemy)
├── models/             # Models do banco
├── schemas/            # Pydantic Schemas
├── db/                 # Base e sessão SQLAlchemy
├── core/               # JWT, segurança, configurações
├── services/           # Integrações (ex: WhatsApp)
├── utils/              # Mixin e handlers genéricos
alembic/                # Migrations
```

---

## 🧪 Comandos úteis

```bash
# Criar nova versão da migração
alembic revision --autogenerate -m "mensagem"

# Rodar todas as migrações pendentes
alembic upgrade head
```

---

## 📦 Tecnologias

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- PostgreSQL
- Docker
- Sentry

---

## 👨‍💻 Autor

Willyam Cutrim  
GitHub: [@willcutrim](https://github.com/willcutrim)

> 🙌 Deus seja louvado.