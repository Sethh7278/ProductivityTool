
from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
# Declaring a data model that inherits from BaseModel 



# Creating a base class using declarativeBase class


# Creating an ORM class to build a table in the database
class Task(Base):
    # Setting Table name
    __tablename__ = "tasks"
    # Creating ID primary key with 'Mapped' being the typehint telling SQLAlchemy what data type it is. The mapped_column is used to describe any additional information that we want
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(75))
    complete: Mapped[bool] = mapped_column(default=False)