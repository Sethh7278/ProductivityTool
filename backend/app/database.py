from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, sessionmaker

class Base(DeclarativeBase):
    pass


engine = create_engine("postgresql+psycopg://postgres:postgres@db:5432/productivity_db")

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
# This Creates everything
