# 💰 Finance Dashboard — API

*[Read this in English](README.en.md)*

API REST para controle financeiro pessoal, com autenticação JWT, gerenciamento de transações, categorias e usuários. Projeto desenvolvido como parte do meu portfólio, com foco em boas práticas de arquitetura backend em Python.

## 🚀 Tecnologias

- **Python 3.14**
- **FastAPI** — framework web assíncrono
- **SQLAlchemy** — ORM para modelagem e acesso ao banco de dados
- **SQLite** — banco de dados (facilmente portável para PostgreSQL)
- **Pydantic** — validação de dados
- **JWT (python-jose)** — autenticação via tokens
- **Passlib + bcrypt** — hash seguro de senhas
- **Poetry** — gerenciamento de dependências

## 📐 Arquitetura

O projeto segue uma separação clara de responsabilidades:
src/finance_dashboard/
├── api/ # Rotas da API (endpoints)
├── core/ # Segurança: hash de senha, JWT, autenticação
├── db/ # Configuração de banco de dados e sessões
├── models/ # Modelos SQLAlchemy (tabelas do banco)
├── schemas/ # Schemas Pydantic (validação de entrada/saída)
└── main.py # Ponto de entrada da aplicação

## ✨ Funcionalidades

- **Autenticação JWT** — registro e login de usuários, com senhas armazenadas via hash bcrypt
- **Isolamento de dados por usuário** — cada usuário só acessa suas próprias transações
- **CRUD completo** de Transações, Categorias e Usuários
- **Relacionamentos entre entidades** via chaves estrangeiras (Transação → Categoria, Transação → Usuário)
- **Documentação automática** via Swagger (`/docs`)

## 🔧 Como rodar localmente

```bash
# Clonar o repositório
git clone https://github.com/DaviCarreiro/finance-dashboard.git
cd finance-dashboard

# Instalar dependências
poetry install

# Criar arquivo .env com a chave secreta
echo "SECRET_KEY=sua-chave-secreta-aqui" > .env

# Criar as tabelas do banco
poetry run python src/finance_dashboard/criar_tabelas.py

# Rodar o servidor
poetry run uvicorn finance_dashboard.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`, com a documentação interativa em `http://127.0.0.1:8000/docs`.

## 📌 Endpoints principais

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/auth/registrar` | Cria um novo usuário |
| POST | `/auth/login` | Autentica e retorna um token JWT |
| GET | `/transacoes` | Lista as transações do usuário autenticado |
| POST | `/transacoes` | Cria uma nova transação |
| PUT | `/transacoes/{id}` | Atualiza uma transação |
| DELETE | `/transacoes/{id}` | Remove uma transação |
| GET/POST/PUT/DELETE | `/categorias` | CRUD de categorias |

## 🎯 Sobre o projeto

Este projeto foi construído do zero como parte do meu aprendizado em desenvolvimento backend, com foco especial em: modelagem de dados, arquitetura em camadas, segurança (hash de senha, JWT, isolamento de dados) e boas práticas do ecossistema Python (type hints, Pydantic, ambiente virtual gerenciado via Poetry).

O frontend (React) que consome esta API está disponível em: [finance-dashboard-frontend](https://github.com/DaviCarreiro/finance-dashboard-frontend)

## 👤 Autor

**Davi Carreiro**
Estudante de Ciência da Computação | Fortaleza, CE

---

Feito com 🐍 Python