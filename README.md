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
