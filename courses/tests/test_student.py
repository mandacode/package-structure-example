from ..student import Student


def test_student_init():
    name = "John"

    student = Student(name)

    assert student.name == name

def test_student_str():
    name = "John"

    student = Student(name)

    assert str(student) == f"Student: {name}"
