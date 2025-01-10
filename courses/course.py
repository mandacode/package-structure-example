from .lesson import Lesson


class Course:

    def __init__(self, title: str):
        self.title = title
        self.lessons = [] 
    
    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)

    def __str__(self) -> str:
        return f"Course: {self.title} | Lessons: {len(self.lessons)}"
