from .models import Student
from .repositories import StudentRepository


def create_student(repo: StudentRepository, name: str) -> Student:
    """
    Service function creating a student object
    and saving it in database.
    """

    student = Student(name=name)

    repo.add(student)

    return student 
