
# 📝 FastAPI Todo App

A simple and clean backend application for managing todos, built with **FastAPI** and **SQLAlchemy**.

## 🚀 Features

- 🔐 JWT-based user authentication (Login / Register)
- ✅ Create, read, update, and delete todo items
- 🧠 SQLite database (easily replaceable with PostgreSQL or MySQL)
- 📦 Modular structure (routers, models, schemas, database)
- ⚡️ Fast and async-friendly

## 📂 Project Structure

```
FastAPI_TodoApp/
├── main.py             # App entry point
├── database.py         # DB engine and session
├── models.py           # SQLAlchemy models
├── schemas.py          # Pydantic schemas
├── auth.py             # JWT auth & user verification
├── routers/
│   ├── todo.py         # Todo CRUD routes
│   └── user.py         # User auth routes
```

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/Erfan-Alishahi/FastAPI_TodoApp.git
cd FastAPI_TodoApp
```

### 2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, install manually:
```bash
pip install fastapi uvicorn sqlalchemy pydantic passlib[bcrypt] python-jose
```

## ▶️ Run the application

```bash
uvicorn main:app --reload
```

API docs will be available at:  
👉 http://127.0.0.1:8000/docs

## 📌 Endpoints Overview

| Method | Endpoint        | Description             | Auth Required |
|--------|------------------|-------------------------|---------------|
| POST   | /user/register   | Register new user       | ❌            |
| POST   | /user/login      | Login & get JWT token   | ❌            |
| GET    | /todos           | List all todos          | ✅            |
| POST   | /todos           | Create a todo           | ✅            |
| PUT    | /todos/{id}      | Update a todo           | ✅            |
| DELETE | /todos/{id}      | Delete a todo           | ✅            |

## 📦 Future Ideas (TODO)

- Add unit tests with Pytest
- Use PostgreSQL with Docker
- Add user roles and permissions
- Create frontend (React/Vue or mobile app)

## 🤝 Contributing

Pull requests are welcome! If you have suggestions for improvements, feel free to open an issue or fork the project.

## 📄 License

This project is open-source and available under the MIT License.

## ✨ Author

Built by [Erfan Alishahi](https://github.com/Erfan-Alishahi) with 💻 and ☕
