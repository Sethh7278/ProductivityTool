# Sprint 3 Manual Test Cases - Task CRUD API

## Test Environment

- Backend: FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Testing tool: Swagger UI
- Swagger URL: http://localhost:8000/docs

---

# 1. Create Task

## Test: Create valid task

Endpoint:
POST /tasks

Request Body:

{
  "name": "Study FastAPI",
  "complete": false
}

Expected Result:
- Status code: 200
- Response includes:
  - id
  - name
  - complete

Result: Passed
Passed

---

## Test: Empty task name

Endpoint:
POST /tasks

Request Body:

{
  "name": "",
  "complete": false
}

Expected Result:
- Validation error
- Task should not be created

Result: Code 422 Erro: Unprocessable Entity, "msg": "String should have at least 1 character"
Passed

---

# 2. Get Tasks

## Test: Retrieve tasks

Endpoint:
GET /tasks

Expected Result:
- Returns list of tasks
- Each task includes:
  - id
  - name
  - complete

Result: Success, Response body:
  {
    "id": 43,
    "name": "Study FastAPI",
    "complete": false
  }
Passed

---

# 3. Update Task

## Test: Mark task as complete

Endpoint:
PATCH /tasks/{task_id}

Request Body:

{
  "complete": true
}

Expected Result:
- Status code: 200
- Returned task has "complete": true

Result:
curl -X 'PATCH' \
  'http://localhost:8000/tasks/43' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "complete": true
}'
Passed

---

## Test: Update missing task

Endpoint:
PATCH /tasks/999

Request Body:

{
  "complete": true
}

Expected Result:
- Status code: 404
- Response says task not found

Result:"PATCH /tasks/999 HTTP/1.1" 404 Not Found
Passed

---

# 4. Delete Task

## Test: Delete existing task

Endpoint:
DELETE /tasks/{task_id}

Expected Result:
- Status code: 200
- Task is removed from database

Result: "DELETE /tasks/43 HTTP/1.1" 200 OK
Passed

---

## Test: Delete missing task

Endpoint:
DELETE /tasks/999

Expected Result:
- Status code: 404
- Response says task not found

Result:"DELETE /tasks/999 HTTP/1.1" 404 Not Found
Passed

---

# PostgreSQL Verification

Open PostgreSQL:

docker compose exec db psql -U postgres -d productivity_db

Run:

SELECT * FROM tasks ORDER BY id;

Expected Result:
- Created tasks appear
- Updated tasks reflect correct completion status
- Deleted tasks are removed

Results:
productivity_db=# SELECT * FROM tasks ORDER BY id;
 id |  name  | complete 
----+--------+----------
  1 | string | f
  2 | Go gym | t
 34 | string | t
 36 | Go gym | t
 41 | Test   | t
 42 | Test   | t
(6 rows)