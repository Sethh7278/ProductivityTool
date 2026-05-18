
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Task():
    # Setting Table name
    __tablename__ = "tasks"
    # Creating ID primary key with 'Mapped' being the typehint telling SQLAlchemy what data type it is. The mapped_column is used to describe any additional information that we want
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(75))
    complete: Mapped[bool] = mapped_column(default=False)
