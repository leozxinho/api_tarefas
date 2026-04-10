# 📌 API de Tarefas

API para gerenciamento de tarefas utilizando arquitetura em camadas (Router → UseCase → Repository).

---

## 🔗 Endpoints

### 📄 Listar todas as tarefas

**GET** `/tarefas`

Retorna todas as tarefas cadastradas.

**Response:**

```json
[
  {
    "id": 1,
    "titulo": "Estudar",
    "descricao": "Revisar FastAPI",
    "concluido": true,
    "created_at": "2026-04-10",
    "update_at": "2026-04-10"
  }
]
```

---

### 📅 Filtrar tarefas por data

**GET** `/tarefas/data`

Filtra tarefas com base em critérios de data.

**Query Params (via Depends):**

* `data_inicio` (opcional)
* `data_fim` (opcional)

**Exemplo:**

```
/tarefas/data?data_inicio=2026-04-01&data_fim=2026-04-10
```

---

### 🔍 Buscar tarefa por ID

**GET** `/tarefas/{id}`

Retorna uma tarefa específica.

**Parâmetros:**

* `id` (int)

**Response:**

```json
  {
    "id": 1,
    "titulo": "Estudar",
    "descricao": "Revisar FastAPI",
    "concluido": true,
    "created_at": "2026-04-10",
    "update_at": "2026-04-10"
  }
```

---

### ➕ Criar nova tarefa

**POST** `/tarefas`

Cria uma nova tarefa.

**Body:**

```json
{
  "titulo": "Nova tarefa",
  "descricao": "Descrição da tarefa",
}
```

**Response:**

```json
{
  "id": 1,
  "titulo": "Nova",
  "descricao": "Tarefa",
  "concluido": true,
  "created_at": "2026-04-10T14:35:16",
  "update_at": "2026-04-10T14:35:16"
}
```

---

### ✏️ Atualizar tarefa

**PUT** `/tarefas/{id}`

Atualiza uma tarefa existente.

**Parâmetros:**

* `id` (int)

**Body:**

```json
{
  "titulo": "Nova",
  "descricao": "Tarefa",
  "concluido": true
}
```

---

### ❌ Excluir tarefa

**DELETE** `/tarefas/{id}`

Remove uma tarefa do sistema.

**Parâmetros:**

* `id` (int)

**Response:**

```json
{
  "detail": "Tarefa excluída com sucesso."
}
```

---

## 🧠 Arquitetura

A API segue uma separação clara de responsabilidades:

* **Router** → Define os endpoints
* **UseCase** → Contém as regras de negócio
* **Repository** → Responsável pelo acesso ao banco
* **Session (AsyncSession)** → Gerencia a conexão com o banco de dados

---

## ⚙️ Tecnologias

* FastAPI
* SQLAlchemy (Async)
* Python 3.10+

---

## 🚀 Observações

* Todas as operações são assíncronas
* Uso de `Depends` para injeção de dependências
* Código organizado para fácil manutenção e escalabilidade

---

