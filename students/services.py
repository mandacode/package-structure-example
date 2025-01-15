from .models import Student
from .repositories import StudentRepository


def create_student(repo: StudentRepository, name: str) -> Student:
    """Service function responsible for creating a student."""
    student = Student(name=name)

    repo.add(student)

    return student 


def get_student(repo: StudentRepository, student_id: int) -> Student:
    """Service function responsible for retrieving a student."""
    student = repo.get(student_id=student_id)
    
    return student
