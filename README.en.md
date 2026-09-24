# 💰 Finance Dashboard — API

*[Leia em Português](README.md)*

A REST API for personal finance management, featuring JWT authentication, transaction/category/user management. Built as part of my portfolio, with a focus on backend architecture best practices in Python.

## 🚀 Tech Stack

- **Python 3.14**
- **FastAPI** — async web framework
- **SQLAlchemy** — ORM for data modeling and database access
- **SQLite** — database (easily portable to PostgreSQL)
- **Pydantic** — data validation
- **JWT (python-jose)** — token-based authentication
- **Passlib + bcrypt** — secure password hashing
- **Poetry** — dependency management

## 📐 Architecture
src/finance_dashboard/
├── api/ # API routes (endpoints)
├── core/ # Security: password hashing, JWT, authentication
├── db/ # Database configuration and sessions
├── models/ # SQLAlchemy models (database tables)
├── schemas/ # Pydantic schemas (input/output validation)
└── main.py # Application entry point
## ✨ Features

- **JWT Authentication** — user registration and login, passwords hashed with bcrypt
- **Per-user data isolation** — each user can only access their own transactions
- **Full CRUD** for Transactions, Categories and Users
- **Entity relationships** via foreign keys (Transaction → Category, Transaction → User)
- **Auto-generated docs** via Swagger (`/docs`)

## 🔧 Running locally

```bash
# Clone the repository
git clone https://github.com/DaviCarreiro/finance-dashboard.git
cd finance-dashboard

# Install dependencies
poetry install

# Create .env file with your secret key
echo "SECRET_KEY=your-secret-key-here" > .env

# Create database tables
poetry run python src/finance_dashboard/criar_tabelas.py

# Run the server
poetry run uvicorn finance_dashboard.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## 📌 Main endpoints

| Method | Route | Description |
|--------|------|-----------|
| POST | `/auth/registrar` | Creates a new user |
| POST | `/auth/login` | Authenticates and returns a JWT token |
| GET | `/transacoes` | Lists the authenticated user's transactions |
| POST | `/transacoes` | Creates a new transaction |
| PUT | `/transacoes/{id}` | Updates a transaction |
| DELETE | `/transacoes/{id}` | Deletes a transaction |
| GET/POST/PUT/DELETE | `/categorias` | Categories CRUD |

## 🎯 About the project

This project was built from scratch as part of my backend development learning journey, with a special focus on: data modeling, layered architecture, security (password hashing, JWT, data isolation) and Python ecosystem best practices (type hints, Pydantic, virtual environment management with Poetry).

The React frontend that consumes this API is available at: [finance-dashboard-frontend](https://github.com/DaviCarreiro/finance-dashboard-frontend)

## 👤 Author

**Davi Carreiro**
Computer Science Student | Fortaleza, Brazil

---

Built with 🐍 Python