from fastapi import FastAPI
# Importing BaseModel from pydantic
from pydantic import BaseModel
from pydantic import BaseModel, Field, ConfigDict


# Using Pydantic to validate the data ensuring it can be parsed into the database
class TaskCreate(BaseModel):
    name: str = Field(min_length=1, max_length=75)
    complete: bool = False


class TaskUpdate(BaseModel):

    complete: bool
    
#This class is created for all parameters the client does not provide
class TaskResponse(BaseModel):
    id: int
    name: str
    complete: bool
    # This tells pydantic it can read data from Objects with attributes, not just database
    model_config = ConfigDict(from_attributes=True)



