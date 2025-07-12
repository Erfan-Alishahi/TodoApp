
# 📝 Todo App

A simple and clean backend application for managing todos, built with **FastAPI** and **SQLAlchemy**.

## 🚀 Features

- 🔐 JWT-based user authentication (Login / Register)
- ✅ Create, read, update, and delete todo items
- 🧠 SQLite database (easily replaceable with PostgreSQL or MySQL)
- 📦 Modular structure (routers, models, schemas, database)
- ⚡️ Fast and async-friendly

## 📂 Project Structure

```
TodoApp/
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── testdb.db
├── todosapp.db
├── alembic.ini
├── README.md
├── routers/
│   ├── todos.py
│   ├── auth.py
│   ├── admin.py
│   └── users.py
├── static/
│   ├── css/
│       ├── base.css
│       └── bootstrap.css
│   └── js/
│       ├── base.js
│       ├── bootstrap.js
│       ├── bootstrap.js.map
│       ├── jquery-slim.js
│       ├── popper.js
│       └── popper.min.js.map
├── templates/
│   ├── add-todo.html
│   ├── edit-todo.html
│   ├── home.html
│   ├── layout.html
│   ├── login.html
│   ├── navbar.html
│   ├── register.html
│   └── todo.html
└── test/
    ├── test_admin.py
    ├── test_auth.py
    ├── test_example.py
    ├── test_main.py
    ├── test_todos.py
    ├── test_users.py
    └── utils.py
```

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/Erfan-Alishahi/TodoApp.git
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
