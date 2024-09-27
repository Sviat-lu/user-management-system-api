[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![FastAPI](https://img.shields.io/badge/framework-FastAPI-green)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/database-PostgreSQL-blue)](https://www.postgresql.org/)
[![orm](https://img.shields.io/badge/orm-SQLAlchemy-red)](https://www.sqlalchemy.org/)
[![Black](https://img.shields.io/badge/codestyle-black-black)](https://github.com/psf/black)

# User Management System with PostgreSQL and SQLAlchemy

This project is a user management system built with FastAPI and PostgreSQL, utilizing SQLAlchemy for ORM (Object-Relational Mapping).

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Features](#features)
- [Installation](#installation)
  - [Using Docker](#using-docker)
  - [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Overview

This is a backend service for processing user data efficiently, allowing for CRUD (Create, Read, Update, Delete) operations while ensuring unique user identifiers. The system supports importing user data from a CSV file into the PostgreSQL database using Docker for containerization.

## Technologies

- **Language**: Python 3.12
- **Framework**: FastAPI 0.115.0
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker

## Features

1. **User Management**:
   - Create users with a name, email, phone number and notes fields.
   - Retrieve user details by ID.
   - Update user information.
   - List all users with their  name, email, phone number and notes.
   - Delete user by ID.

2. **API Documentation**:
   - Integrated Swagger UI for easy API exploration.

3. **Data Import**:
   - Import user data from a CSV file into the PostgreSQL database during the initial setup.

4. **Email validation**:
   - Validating user email before saving to DB.

## Installation

To run the project locally, follow the steps below.

### Using Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/Sviat-lu/user-management-system-api
   cd user-management-system-api
   ```

2. Set up environment variables in `.env.template`:

   ```bash
   POSTGRES_DB="your_db_name_here"
   POSTGRES_USER="your_db_user_here"
   POSTGRES_PASSWORD="your_password_here"

   JWT_SECRET_KEY="your_secret_key_here"
   ```

3. Start the application using script:

   ```bash
   source scripts/start.sh
   ```

This will start the FastAPI server and the PostgreSQL database.

4. Access the application:

   **FastAPI docs**: http://localhost:8000/docs

   **OpenAPI schema**: http://localhost:8000/openapi.json


### Setup Instructions:

> **Prerequisites:**
> - **Python 3.12+**
> - **PostgreSQL 15.8+**
> - **Poetry** (for dependency management)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sviat-lu/user-management-system-api
   cd user-management-system-api
   ```
2. **Set Up the Virtual Environment:**

   ```bash
   poetry install

3. **Create a `.env` file in the root directory and add the following variables:**

    ```bash
    PYTHONPATH=./src

    APP_HOST="0.0.0.0"
    APP_PORT=8000

    POSTGRES_HOST="127.0.0.1"
    POSTGRES_PORT=5432
    POSTGRES_DB="your_db_name_here"
    POSTGRES_USER="your_db_user_here"
    POSTGRES_PASSWORD="your_password_here"
    ```

4. **Create new db table using command:**
    ```bash
    psql -U %your_db_user_here% -d %your_password_here% -f ./docker/initdb/init.sql
    ```

5. **Run server:**
    ```bash
    python3 main.py
    ```

6. **Access the application:**

   **FastAPI docs**: http://localhost:8000/docs

   **OpenAPI schema**: http://localhost:8000/openapi.json


## API Endpoints

### The following API endpoints are available:

- **Create User**:
   ```bash
   curl -X 'POST' \
   'http://127.0.0.1:8000/v1/users/' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{
      "name": "string",
      "email": "user@example.com",
      "phone": "(832) 576-1114",
      "note": "string"
   }'
   ```

  **Response**:
  ```json
   {
      "name": "string",
      "email": "user@example.com",
      "phone": "string",
      "note": "(832) 576-1114",
      "id": 5001
   }
   ```

- **Get User by ID**:
   ```bash
   curl -X 'GET' \
   'http://127.0.0.1:8000/v1/users/5001/' \
   -H 'accept: application/json'
   ```
  **Response**:
  ```json
   {
      "name": "string",
      "email": "user@example.com",
      "phone": "string",
      "note": "(832) 576-1114",
      "id": 5001
   }
   ```

- **Update User**:
   ```bash
   curl -X 'PATCH' \
   'http://127.0.0.1:8000/v1/users/5001/' \
   -H 'accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{
      "name": "updated_name",
      "email": "updated@email.com",
      "phone": "(111) 111-1111",
      "note": "updated_note"
   }
   ```

  **Response**:
  ```json
   {
      "name": "updated_name",
      "email": "updated@email.com",
      "phone": "(111) 111-1111",
      "note": "updated_note",
      "id": 5001
   }
   ```

- **List of 2 Users**:
   ```bash
   curl -X 'GET' \
   'http://127.0.0.1:8000/v1/users/?limit=2&offset=0' \
   -H 'accept: application/json'
   ```

  **Response**:
  ```json
   [
      {
         "name": "Corey Powell",
         "email": "dujeen@aturadka.tn",
         "phone": "(962) 886-1969",
         "note": "g0D6kM66XS)8nVFOb$",
         "id": 1
      },
      {
         "name": "Chad Rodgers",
         "email": "in@os.vn",
         "phone": "(435) 519-4751",
         "note": "oJkOAX4!3SK",
         "id": 2
      }
   ]
   ```

- **Remove User**:
   ```bash
   curl -X 'DELETE' \
   'http://127.0.0.1:8000/v1/users/5001/' \
   -H 'accept: */*'
   ```
   Remove user from the database by its ID.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
