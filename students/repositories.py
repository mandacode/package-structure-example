"""Data Access Layer"""
import abc

from .database import Session
from .models import Student


class StudentRepository(abc.ABC):
    """Abstract repository class for managing student data."""
    
    def add(self, student: Student):
        raise NotImplementedError

    def get(self, student_id: int) -> Student:
        raise NotImplementedError


class SQLAlchemyStudentRepository(StudentRepository):
    """SQLAlchemy repository class for managing student data."""

    def __init__(self, session: Session):
        self.session = session 
    
    def add(self, student: Student):
        self.session.add(student)
        self.session.commit()
    
    def get(self, student_id: int) -> Student:
        student = (
            self.session
            .query(Student)
            .where(Student.id == student_id)
            .first()
        )
        return student 
