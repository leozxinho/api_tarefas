# 📌 API de Tarefas

API REST para gerenciamento de tarefas construída com FastAPI, seguindo os princípios da **Clean Architecture**.

---

## 🔗 Endpoints

Base URL: `/api/v1`

### 📄 Listar todas as tarefas

**GET** `/tarefas`

**Response:**
```json
[
  {
    "id": 1,
    "titulo": "Estudar",
    "descricao": "Clean Architecture",
    "concluido": true,
    "created_at": "2026-04-10",
    "update_at": "2026-04-10"
  }
]
```

---

### 📅 Filtrar tarefas por data

**GET** `/tarefas/data`

**Query Params:**

| Param | Tipo | Obrigatório |
|---|---|---|
| `data_inicio` | string (YYYY-MM-DD) | Não |
| `data_fim` | string (YYYY-MM-DD) | Não |

**Exemplo:**
```
GET /api/v1/tarefas/data?data_inicio=2026-04-01&data_fim=2026-04-10
```

---

### 🔍 Buscar tarefa por ID

**GET** `/tarefas/{id}`

**Response:**
```json
{
  "id": 1,
  "titulo": "Estudar",
  "descricao": "Clean Architecture",
  "concluido": true,
  "created_at": "2026-04-10",
  "update_at": "2026-04-10"
}
```

> Retorna `404` se a tarefa não for encontrada.

---

### ➕ Criar nova tarefa

**POST** `/tarefas`

**Body:**
```json
{
  "titulo": "Nova tarefa",
  "descricao": "Descrição da tarefa"
}
```

**Response:** `200`
```json
{
  "id": 1,
  "titulo": "Nova tarefa",
  "descricao": "Descrição da tarefa",
  "concluido": false,
  "created_at": "2026-04-10T14:35:16",
  "update_at": "2026-04-10T14:35:16"
}
```

---

### ✏️ Atualizar tarefa

**PUT** `/tarefas/{id}`

**Body:**
```json
{
  "titulo": "Título atualizado",
  "descricao": "Nova descrição",
  "concluido": true
}
```

---

### ❌ Excluir tarefa

**DELETE** `/tarefas/{id}`

**Response:** `200`
```json
{
  "detail": "Tarefa excluída com sucesso."
}
```

---

## ⚙️ Tecnologias

| Tecnologia | Uso |
|---|---|
| FastAPI | Framework web |
| SQLAlchemy Async | ORM assíncrono |
| MySQL | Banco de dados |
| Alembic | Migrations |
| Pytest | Testes automatizados |
| Python 3.10+ | Linguagem |

---

## 🚀 Como rodar

**1. Clone o repositório e instale as dependências:**
```bash
git clone <repo>
cd api_tarefas
pip install -r requirements.txt
```

**2. Configure o `.env`:**
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=api_tarefas
```

**3. Rode as migrations:**
```bash
alembic upgrade head
```

**4. Inicie a aplicação:**
```bash
uvicorn main:app --reload
```

---

## 🧪 Testes

```bash
# Todos os testes
pytest tests/ -v

# Apenas middlewares
pytest tests/middlewares/ -v

# Apenas use cases
pytest tests/usecase/ -v
```

---

## 📁 Estrutura do projeto

```
api_tarefas/
├── domain/
│   ├── entities/
│   ├── dto/
│   │   ├── request/
│   │   └── response/
│   └── interface/
├── app/
│   ├── controllers/
│   ├── middlewares/
│   ├── usecase/
│   └── dependencies.py
├── infrastructure/
│   └── database_mysql/
│       ├── repositories/
│       │   └── task/
│       ├── task_model.py
│       ├── base.py
│       └── mysql_connection.py
├── tests/
│   ├── middlewares/
│   └── usecase/
├── main.py
└── requirements.txt
```