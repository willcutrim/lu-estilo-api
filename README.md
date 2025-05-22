# 🧵 Lu Estilo API

API RESTful para gerenciamento comercial da empresa Lu Estilo, desenvolvida com FastAPI, PostgreSQL, SQLAlchemy e Alembic, seguindo princípios de Clean Architecture.

---

## 🚀 Requisitos

- Python 3.8+
- PostgreSQL 13+
- pip

---

## ⚙️ Passo a passo para rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/lu-estilo-api.git
cd lu-estilo-api
``` 

### 2. Crie e ative um ambiente virtual

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```
pip install -r requirements.txt
```

## 🛠️ Configurar o banco de dados
### 4. Crie o banco no PostgreSQL (se ainda não tiver)
```
CREATE DATABASE lu_db;
CREATE USER lu_user WITH PASSWORD 'lu_pass';
GRANT ALL PRIVILEGES ON DATABASE lu_db TO lu_user;
```

🗂️ Configuração do Alembic

### 5. Configure alembic.ini:
No arquivo alembic.ini, edite:

```
sqlalchemy.url = postgresql://lu_user:lu_pass@localhost:5432/lu_db
```

Ou use variável em env.py com .env:

```
DATABASE_URL=postgresql://lu_user:lu_pass@localhost:5432/lu_db
```
## 📦 Rodar as migrações
### 6. Gere e aplique as migrações com Alembic

```
# Se já tiver as versões geradas:
alembic upgrade head
```

### 7. Se mudar os models, gere nova versão:

```
alembic revision --autogenerate -m "alterações em models"
alembic upgrade head
```

## ▶️ Rodar a API
### 8. Execute a aplicação

```
python run.py
```

#### Acesse:

 - API: http://localhost:8000

 - Docs Swagger: http://localhost:8000/docs

## 📁 Estrutura do Projeto

```
app/
├── api/                # Rotas FastAPI
├── domain/             # Casos de uso e interfaces (Clean Architecture)
├── infrastructure/     # Repositórios com SQLAlchemy
├── models/             # Tabelas do banco
├── schemas/            # Schemas Pydantic
├── db/                 # Base e sessão do banco
├── core/               # Segurança, JWT etc.
alembic/                # Migrações
```

## 🧪 Comandos úteis

```
# Criar nova versão da migração
alembic revision --autogenerate -m "mensagem"

# Rodar todas as migrações pendentes
alembic upgrade head
```

## 📦 Tecnologias
- FastAPI

- SQLAlchemy

- Alembic

- Pydantic

- PostgreSQL

## 👨‍💻 Autor
Willyam Cutrim
GitHub: @willcutrim

Deus seja louvado.
