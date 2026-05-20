from fastapi import FastAPI

from .database import Base, engine
from .models.task import Task
from app.routes.task import router as tasks_router


app = FastAPI(title="AI Productivity App")


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "AI Productivity App"}


app.include_router(tasks_router)





#