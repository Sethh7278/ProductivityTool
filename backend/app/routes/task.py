from fastapi import FastAPI, APIRouter
from app.schema.task import TaskCreate, TaskResponse
from app.models.task import Task
from app.database import SessionLocal


router = APIRouter(prefix="/tasks", tags=["tasks"])



# Simple FastAPI route that Creates a Task and uses response model and Task create  
@router.post("/", response_model=TaskResponse)
# Setting required parameters and datatypes
def create_task(task: TaskCreate):
    new_task = Task(name=task.name, complete=task.complete)
    with SessionLocal() as session:
        session.add(new_task)
        session.commit()
        session.refresh(new_task)

    return new_task

