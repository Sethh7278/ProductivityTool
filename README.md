# AI Productivity Assistant

A full-stack productivity web application being built to improve software engineering, backend development, database design, and AI integration skills.

The long-term goal is to create an AI-powered productivity assistant with features such as task management, journaling, habit tracking, analytics, and AI-generated productivity insights.

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker
- React (planned)
- OpenAI API (planned)

---

# Features Implemented

Current backend functionality:

- Create tasks
- Retrieve tasks
- Update task completion
- Delete tasks
- PostgreSQL database persistence
- Swagger API testing

---

# Project Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── routes/
│   └── schema/
│
├── Dockerfile
└── requirements.txt
```

---

# Running The Project

From the project root:

```powershell
docker compose up --build
```

Backend:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

# PostgreSQL Access

Open PostgreSQL:

```powershell
docker compose exec db psql -U postgres -d productivity_db
```

Useful commands:

```sql
\dt
\d tasks
SELECT * FROM tasks;
```

Exit PostgreSQL:

```sql
\q
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks` | Create task |
| GET | `/tasks` | Get tasks |
| PATCH | `/tasks/{task_id}` | Update task |
| DELETE | `/tasks/{task_id}` | Delete task |

---

# Sprint 1

Focused on project setup and Docker.

Completed:
- FastAPI backend setup
- Docker setup
- PostgreSQL container setup
- Swagger working

---

# Sprint 2

Focused on database integration.

Completed:
- SQLAlchemy setup
- PostgreSQL connection
- ORM task model
- Database persistence

---

# Sprint 3

Focused on CRUD API development.

Completed:
- Create tasks
- Read tasks
- Update tasks
- Delete tasks
- Request validation
- Error handling
- Swagger testing

---

# Current Backend Flow

```text
Request
↓
FastAPI Route
↓
Pydantic Validation
↓
SQLAlchemy ORM
↓
PostgreSQL
↓
JSON Response
```

---

# Next Steps

Sprint 4:
- React frontend setup
- Connect frontend to backend
- Display tasks in UI
- Create/update/delete tasks from frontend

---

# Future Plans

- User authentication
- Goal tracking
- Habit tracking
- Journaling
- Dashboard analytics
- AI productivity coaching
- AI-generated reflections