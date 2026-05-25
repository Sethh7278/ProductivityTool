from fastapi import FastAPI, APIRouter, HTTPException
from app.schema.task import TaskCreate, TaskResponse, TaskUpdate
from app.models.task import Task
from app.database import SessionLocal
from sqlalchemy import select



router = APIRouter(prefix="", tags=["tasks"])



# Simple FastAPI route that Creates a Task and uses response model and Task create  
@router.post("/Create-Task", response_model=TaskResponse)
# Setting required parameters and datatypes
def create_task(task: TaskCreate):
    new_task = Task(name=task.name, complete=task.complete)
    with SessionLocal() as session:
        session.add(new_task)
        session.commit()
        session.refresh(new_task)

    return new_task

# Using my response model as a list for multiple responses
@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    # Creating a query for all tasks that are not completed
    T = select(Task).where(Task.complete == False)
    with SessionLocal() as session:
        tasks = session.scalars(T).all()
        return tasks

@router.delete("/tasks/{task_id}")
# Deleting task and ensuring task_id is an int
def delete_task(task_id: int):
    # Querying to find the instance that has the ID
    D = select(Task).where(Task.id == task_id)
    with SessionLocal() as session:
        task = session.scalars(D).first()
        # Raising an error if the task with that ID is not there
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        #Commiting the changes
        session.commit()
    return "Task Deleted"


# Creating a put route that is used to update existing rows
@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    # Creating a query to find the task 
    U = select(Task).where(Task.id == task_id)
    with SessionLocal() as session:
        # Using the query to check in the database to find the instance
        task = session.scalars(U).first()
        if task is None:
           raise HTTPException(status_code=404, detail="Task not found")
        # Setting the complete value to true
        task.complete = task_update.complete
        session.commit()
        return task