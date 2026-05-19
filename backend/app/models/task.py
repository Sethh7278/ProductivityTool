
from fastapi import FastAPI
# Importing BaseModel from pydantic
from pydantic import BaseModel

# Declaring a data model that inherits from BaseModel 
class Task(BaseModel):
    # Using standard Python types
    name: str
    complete: bool

app = FastAPI()

app.post("/tasks/")
async def create_task(task : Task):
    return task

