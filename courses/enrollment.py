from .course import Course
from .student import Student


class Enrollment:
    
    def __init__(self, course: Course, student: Student):
        self.course = course 
        self.student = student 

    def __str__(self) -> str:
        return f"{self.student} has enrolled to {self.course}"


def enroll(course: Course, student: Student) -> Enrollment:
    enrollment = Enrollment(
        course=course, 
        student=student
    )
    print(enrollment)
    return enrollment
