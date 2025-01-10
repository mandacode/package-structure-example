from courses.course import Course
from courses.enrollment import enroll
from courses.lesson import Lesson
from courses.student import Student


def main():
    # client code

    # create a student
    student = Student("John Doe") 
    # create a course
    course = Course("Javascript course")
    # create a lesson
    lesson1 = Lesson(
        title="Introduction to Javascript", 
        content="JavaScript is a versatile programming language primarily used"
        "for creating interactive and dynamic web pages. "
        "It runs in the browser, allowing developers to manipulate HTML and CSS, "
        "as well as handle user events in real time. As one of the core technologies "
        "of web development alongside HTML and CSS, JavaScript enables features like " 
        "animations, form validation, and interactive maps."
    )
    # add the lesson to the course
    course.add_lesson(lesson1)
    # student enrolls the course
    enroll(course, student)


if __name__ == "__main__":
    main()
