class Student:
    "Class representing domain Student entity."

    def __init__(self, name: str):
        self.name = name
        self.created_at = None 

    def __str__(self) -> str:
        return f"Student: {self.name}"
