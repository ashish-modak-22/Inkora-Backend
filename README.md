<div align="center">
 
# 📝 Inkora — Backend
 
### A secure, scalable REST API for a modern note-taking application

Built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication** — designed with clean architecture, database migrations, and production-ready patterns from day one.
 
<br/>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge&logo=python&logoColor=white)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-Migrations-6BA81E?style=for-the-badge)](https://alembic.sqlalchemy.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-000000.svg?style=for-the-badge)](https://peps.python.org/pep-0008/)

[Features](#-features) •
[Tech Stack](#-tech-stack) •
[Architecture](#-project-architecture) •
[Getting Started](#-getting-started) •
[API Reference](#-api-reference) •
[Roadmap](#-roadmap) •
[Contributing](#-contributing)
 
</div>

---

## 📖 Overview
 
**Inkora** is the backend service powering a full-featured notes application. It exposes a clean, versionable REST API that handles **user registration and authentication**, **JWT-based session management**, and full **CRUD operations on notes**, complete with **pagination, search, and sorting**.

The project is intentionally structured the way a production FastAPI service should be — routers, schemas, models, and business logic (`crud`) are cleanly separated, database schema evolution is handled through **Alembic migrations** rather than ad-hoc changes, and secrets/configuration are isolated via environment variables.

> This repository contains the **backend/API only**. It is designed to be consumed by any client — a web frontend, a mobile app, or a third-party integration — via standard HTTP/JSON.
 
---

## ✨ Features
 
- 🔐 **Secure Authentication** — User registration and login with `bcrypt`-hashed passwords and stateless **JWT** access tokens
- 🗒️ **Full Notes CRUD** — Create, read, update, and delete notes scoped to the authenticated user
- 🔎 **Search, Sort & Paginate** — Query notes by keyword (title/content), sort by `created_at` or `title`, and paginate results
- 🧾 **Ownership-Scoped Access** — Every note operation is strictly scoped to the requesting user; no cross-user data leakage
- 🗃️ **Relational Data Modeling** — One-to-many `User → Notes` relationship enforced at the database level via SQLAlchemy ORM
- 🧬 **Versioned Database Migrations** — Schema changes tracked and reproducible with Alembic
- 📑 **Auto-Generated API Docs** — Interactive Swagger UI and ReDoc out of the box, courtesy of FastAPI
- 🌍 **Environment-Based Configuration** — Twelve-factor style config via `.env`, kept out of version control
- ⚡ **Async-Ready & Type-Safe** — Built on modern Python typing and Pydantic v2 schema validation
  
---
 
## 🧰 Tech Stack
 
| Layer                  | Technology                                                                 | Purpose                                              |
|-------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------|
| **Language**            | [Python 3.11+](https://www.python.org/)                                    | Core application language                              |
| **Web Framework**       | [FastAPI](https://fastapi.tiangolo.com/)                                   | High-performance async API framework                   |
| **ASGI Server**         | [Uvicorn](https://www.uvicorn.org/)                                        | Lightning-fast ASGI server for running the app          |
| **ORM**                 | [SQLAlchemy 2.0](https://www.sqlalchemy.org/)                              | Database modeling & query layer                        |
| **Database**            | [PostgreSQL](https://www.postgresql.org/)                                  | Primary relational data store                           |
| **DB Driver**           | [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)               | PostgreSQL adapter for Python                            |
| **Migrations**          | [Alembic](https://alembic.sqlalchemy.org/)                                 | Version-controlled schema migrations                    |
| **Validation**          | [Pydantic v2](https://docs.pydantic.dev/)                                  | Request/response schema validation                       |
| **Auth**                | [python-jose](https://python-jose.readthedocs.io/) + [passlib](https://passlib.readthedocs.io/) / [bcrypt](https://pypi.org/project/bcrypt/) | JWT encoding/decoding & password hashing |
| **Config Management**   | [python-dotenv](https://pypi.org/project/python-dotenv/)                   | Loading environment variables from `.env`                |
| **Email Validation**    | [email-validator](https://pypi.org/project/email-validator/)               | RFC-compliant email field validation                     |
 
<details>
<summary><strong>📦 Full dependency list</strong> (from <code>requirements.txt</code>)</summary>


```
alembic==1.18.5
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.2
bcrypt==5.0.0
cffi==2.1.0
click==8.4.2
colorama==0.4.6
cryptography==49.0.0
dnspython==2.8.0
ecdsa==0.19.2
email-validator==2.3.0
fastapi==0.139.2
greenlet==3.5.3
h11==0.16.0
idna==3.18
Mako==1.3.12
MarkupSafe==3.0.3
passlib==1.7.4
psycopg2-binary==2.9.12
pyasn1==0.6.4
pycparser==3.0
pydantic==2.13.4
pydantic_core==2.46.4
python-dotenv==1.2.2
python-jose==3.5.0
python-multipart==0.0.32
rsa==4.9.1
six==1.17.0
SQLAlchemy==2.0.51
typing-inspection==0.4.2
typing_extensions==4.16.0
uvicorn==0.51.0
```
 
</details>

---

## 🏗️ Project Architecture
 
The codebase follows a **layered architecture**, separating HTTP concerns (routers) from validation (schemas), persistence (models/crud), and cross-cutting logic (core/security):

```
Inkora-Backend/
├── app/
│   ├── main.py                # FastAPI app entrypoint & router registration
│   ├── database.py            # Engine, session factory & Base declarative model
│   │
│   ├── core/
│   │   └── security.py        # Password hashing, JWT creation/validation, current-user dependency
│   │
│   ├── models/                # SQLAlchemy ORM models
│   │   ├── user.py            # User table definition
│   │   └── note.py            # Note table definition (FK -> User)
│   │
│   ├── schemas/                # Pydantic request/response models
│   │   ├── user.py            # UserRegister, UserLogin, UserResponse, Token
│   │   └── note.py            # NoteCreate, NoteUpdate, NoteResponse
│   │
│   ├── crud/                   # Database access / business logic layer
│   │   └── notes.py            # Create, read (paginated/search/sort), update, delete
│   │
│   ├── routers/                 # API route definitions
│   │   ├── auth.py             # /auth/register, /auth/login, /auth/me
│   │   └── notes.py            # /notes CRUD endpoints
│   │
│   └── dependencies/            # Shared FastAPI dependencies
│
├── alembic/
│   ├── env.py                   # Alembic runtime configuration
│   ├── script.py.mako           # Migration file template
│   └── versions/                 # Individual migration scripts
│       ├── 2bdc23e770d6_create_users_table.py
│       └── 1de07b0c8402_create_notes_table.py
│
├── alembic.ini                   # Alembic configuration
├── requirements.txt               # Python dependencies
└── .gitignore
```

 
### Request lifecycle
 
```
Client Request
      │
      ▼
 FastAPI Router  ──▶  Pydantic Schema (validation)
      │
      ▼
 Auth Dependency (JWT decode via core/security.py)
      │
      ▼
   CRUD Layer  ──▶  SQLAlchemy ORM  ──▶  PostgreSQL
      │
      ▼
 Pydantic Response Schema  ──▶  JSON Response
```

### Data model
 
```
┌───────────────────┐        1        N     ┌───────────────────┐
│       User         │───────────────────────│        Note        │
├───────────────────┤                        ├───────────────────┤
│ id (PK)             │                        │ id (PK)             │
│ name                │                        │ title               │
│ email (unique)      │                        │ content             │
│ password_hash       │                        │ created_at          │
└───────────────────┘                        │ updated_at          │
                                                │ user_id (FK → User) │
                                                └───────────────────┘
```
 
---
 
## 🚀 Getting Started
 
### Prerequisites
 
Make sure you have the following installed:
 
| Requirement | Version | Notes |
|---|---|---|
| Python | 3.11 or higher | [Download](https://www.python.org/downloads/) |
| PostgreSQL | 14+ | Locally installed, or a hosted instance (Supabase, Railway, Neon, etc.) |
| pip | latest | Bundled with Python |
| Git | any recent | For cloning the repository |
