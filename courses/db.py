
from sqlalchemy import Column, Integer, String, Table, create_engine
from sqlalchemy.orm import registry, sessionmaker
from student import Student

DATABASE_URL = "sqlite:///local.db"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)

mapper_registry = registry()


students = Table(
    "students",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
)

def start_mappers():
    mapper_registry.map_imperatively(Student, students)

def create_tables():
    mapper_registry.metadata.create_all(bind=engine)

def drop_tables():
    mapper_registry.metadata.drop_all(bind=engine)


def add_contact(session: Session, name: str, ...)

    contact = Contact(...)

    session.add(contact)
    session.commit()
