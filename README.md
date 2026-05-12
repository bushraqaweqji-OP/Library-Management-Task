## Overview

This project is a Library Management System built using FastAPI and PostgreSQL.

The system allows managing:
- Books
- Members
- Borrowing and returning books

The project follows Domain Driven Design (DDD) principles and uses:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic

Features include:
- CRUD operations
- Borrow/return functionality
- Pagination
- Search
- Validation
- Centralized exception handling

## Tech Stack

- Python 3.14
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn

## Project Structure

```bash
app/
│
├── main.py
│
├── core/
│   ├── database.py
│   └── exceptions.py
│
├── books/
│   ├── models.py
│   ├── schemas.py
│   ├── repository.py
│   ├── service.py
│   └── routes.py
│
├── members/
│   ├── models.py
│   ├── schemas.py
│   ├── repository.py
│   ├── service.py
│   └── routes.py
│
└── migrations/
```

## Architecture

The project follows a layered architecture inspired by Domain Driven Design (DDD).

### Layers

- Routes Layer
  - Handles HTTP requests and responses.

- Service Layer
  - Contains business logic.

- Repository Layer
  - Handles database operations.

- Models
  - SQLAlchemy ORM models.

- Schemas
  - Pydantic request/response validation.


## Installation

### Clone the repository

```bash
git clone <repo_url>
cd library-management-system
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE library_db;
```

Update your database URL inside:

```text
app/core/database.py
```

Example:

```python
DATABASE_URL = "postgresql://postgres:password@localhost/library_db"
```

## Database Migrations

Create migration:

```bash
alembic revision --autogenerate -m "initial migration"
```

Apply migration:

```bash
alembic upgrade head
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```