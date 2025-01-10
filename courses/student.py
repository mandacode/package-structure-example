class Student:

    def __init__(self, name: str):
        self.name = name 

    def __str__(self) -> str:
        return f"Student: {self.name}"
    

if __name__ == "__main__":
    student = Student("Krystian")
    print(student)
