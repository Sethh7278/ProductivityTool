from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, sessionmaker 

# Setting up the server with FastAPI and the DB with the engine
app = FastAPI(title= "AI Productivity App")
engine = create_engine("postgresql+psycopg://postgres:postgres@db:5432/productivity_db")
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

@app.get("/")
def root():
    return {"message": "AI Productivity App"}

# Creating a base class using declarativeBase class
class Base(DeclarativeBase):
    pass

# Creating an ORM class to build a table in the database
class Task(Base):
    # Setting Table name
    __tablename__ = "tasks"
    # Creating ID primary key with 'Mapped' being the typehint telling SQLAlchemy what data type it is. The mapped_column is used to describe any additional information that we want
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(75))
    complete: Mapped[bool] = mapped_column(default=False)


# Using Pydantic to validate the data ensuring it can be parsed into the database
class TaskCreate(BaseModel):
    name: str = Field(min_length=1, max_length=75)
    complete: bool = False

#This class is created for all parameters the client does not provide
class TaskResponse(TaskCreate):
    # This tells pydantic it can read data from Objects with attributes, not just database
    model_config = ConfigDict(from_attributes=True)

    id: int = 1


# This Creates everything
Base.metadata.create_all(bind=engine)


# Simple FastAPI route that Creates a Task and uses response model and Task create  
@app.post("/task", response_model=TaskResponse)
# Setting required parameters and datatypes
def create_task(task: TaskCreate):
    new_task = Task(name=task.name, complete=task.complete)
    with SessionLocal() as session:
        session.add(new_task)
        session.commit()
        session.refresh(new_task)

    return new_task



#