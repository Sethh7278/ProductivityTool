from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped 

# Creating the engine updated for psycopg3
engine = create_engine("postgresql+psycopg://postgres:postgres@db:5432/productivity_db")

# Creating a base class using declarativeBase class
class Base(DeclarativeBase):
    pass

class Task(Base):
    # Setting Table name
    __tablename__ = "tasks"
    # Creating ID primary key with 'Mapped' being the typehint telling SQLAlchemy what data type it is. The mapped_column is used to describe any additional information that we want
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(75))
    complete: Mapped[bool] = mapped_column(default=False)

# This Creates everything
Base.metadata.create_all(bind=engine)



with Session(engine) as session:
    eat = Task(task="Get Food", complete = False)
    session.add(eat)
    session.commit()



