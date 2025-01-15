"""Database Layer"""
from sqlalchemy import (Column, DateTime, Integer, String, Table,
                        create_engine, func)
from sqlalchemy.orm import registry, sessionmaker

from .models import Student

DATABASE_URL = "sqlite:///local.db"

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

mapper_registry = registry()


students = Table(
    "students",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("created_at", DateTime, default=func.now())
)

def get_session() -> Session:
    session = Session()

    try:
        yield session

    finally:
        session.close()

def start_mappers():
    mapper_registry.map_imperatively(Student, students)

def create_tables():
    mapper_registry.metadata.create_all(bind=engine)

def drop_tables():
    mapper_registry.metadata.drop_all(bind=engine)
